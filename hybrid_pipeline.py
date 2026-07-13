import asyncio
import aiohttp
import json
import logging
import gzip
import io
from urllib.parse import urlparse
from datetime import datetime, timezone

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# 공통 설정
CC_INDEX_API = "http://index.commoncrawl.org/CC-MAIN-2024-18-index" # 최신 Index 예시
CC_DATA_BASE_URL = "https://data.commoncrawl.org/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

# Step 1: 학술 Seed URL 확보 (Target Generation) - Cursor Pagination 적용
async def fetch_academic_domains(session, target_limit=10000):
    """
    OpenAlex API를 사용하여 신뢰할 수 있는 학술 출판사/저널의 도메인을 Cursor 기반으로 대규모 추출합니다.
    """
    logger.info(f"Step 1: OpenAlex API에서 학술 도메인 리스트를 추출합니다. (목표: {target_limit}개)")
    domains = set()
    cursor = "*"
    
    while len(domains) < target_limit:
        url = f"https://api.openalex.org/sources?per-page=200&cursor={cursor}"
        try:
            async with session.get(url, timeout=15) as response:
                if response.status == 200:
                    data = await response.json()
                    results = data.get("results", [])
                    if not results:
                        break # 더 이상 데이터가 없음
                        
                    for item in results:
                        homepage = item.get("homepage_url")
                        if homepage:
                            parsed = urlparse(homepage)
                            domain = parsed.netloc.replace("www.", "")
                            if domain:
                                domains.add(domain)
                    
                    # 다음 페이지를 위한 cursor 업데이트
                    meta = data.get("meta", {})
                    cursor = meta.get("next_cursor")
                    if not cursor:
                        break # 마지막 페이지
                else:
                    logger.error(f"OpenAlex API 호출 오류 (status {response.status})")
                    break
        except Exception as e:
            logger.error(f"OpenAlex API 호출 중 오류 발생: {e}")
            break
            
    # set을 list로 변환하며 한도에 맞게 자름
    domain_list = list(domains)[:target_limit]
    logger.info(f"총 {len(domain_list)}개의 순수 도메인이 수집 큐에 추가되었습니다.")
    return domain_list

# Step 2 & 3: CDX 탐색 및 분기 처리
async def process_domain(session, domain, semaphore):
    """
    개별 도메인에 대해 Query-then-Fetch (WARC or Live) 의사결정 파이프라인을 실행합니다.
    """
    target_url = f"https://{domain}/robots.txt"
    cdx_query_url = f"{CC_INDEX_API}?url={target_url}&output=json&limit=1"
    
    async with semaphore:
        try:
            # Step 2: 아카이브 CDX Index API 선행 탐색
            logger.info(f"[{domain}] CDX Index 탐색 시작: {target_url}")
            async with session.get(cdx_query_url, timeout=10) as response:
                if response.status == 200:
                    text = await response.text()
                    if text.strip():
                        record = json.loads(text.splitlines()[0])
                        http_status = record.get("status")
                        
                        if http_status == "200":
                            # Case A: 아카이브 정상 기록
                            logger.info(f"[{domain}] Case A (status 200): 아카이브 데이터 추출 진행")
                            return await fetch_warc_payload(session, domain, record)
                        else:
                            # Case B: 아카이브 기록 있으나 차단(403 등)
                            logger.warning(f"[{domain}] Case B (status {http_status}): CCBot 차단 기록됨. Fallback 진행")
                            return await fetch_live(session, domain, target_url)
                    else:
                        # Case C: 데이터 없음
                        return await fetch_live(session, domain, target_url)
                elif response.status == 404:
                    return await fetch_live(session, domain, target_url)
                else:
                    return await fetch_live(session, domain, target_url)
                    
        except asyncio.TimeoutError:
            return await fetch_live(session, domain, target_url)
        except Exception as e:
            return await fetch_live(session, domain, target_url)

# Step 3-A: WARC 원문 추출 및 GZIP 해제
async def fetch_warc_payload(session, domain, cdx_record):
    """
    AWS S3에서 Range Request로 가져온 압축 데이터를 해제하고 본문을 파싱합니다.
    """
    filename = cdx_record.get("filename")
    offset = int(cdx_record.get("offset"))
    length = int(cdx_record.get("length"))
    
    # CDX Timestamp를 ISO 8601로 변환 (예: 20240501123045 -> 2024-05-01T12:30:45)
    timestamp_raw = cdx_record.get("timestamp", "")
    try:
        dt = datetime.strptime(timestamp_raw, "%Y%m%d%H%M%S")
        crawl_date = dt.strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        crawl_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    
    headers = {"Range": f"bytes={offset}-{offset + length - 1}"}
    warc_url = f"{CC_DATA_BASE_URL}{filename}"
    
    try:
        async with session.get(warc_url, headers=headers, timeout=15) as response:
            if response.status in (200, 206):
                compressed_data = await response.read()
                
                # 1. 메모리상에서 비동기적(IO)으로 GZIP 압축 해제
                try:
                    with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as gz:
                        warc_data = gz.read()
                except Exception as e:
                    logger.error(f"[{domain}] GZIP 압축 해제 실패: {e}. Fallback 진행")
                    return await fetch_live(session, domain, f"https://{domain}/robots.txt")
                
                # 2. 디코딩 및 헤더 제거 (WARC 헤더 + HTTP 헤더 분리)
                parts = warc_data.split(b"\r\n\r\n", 2)
                if len(parts) >= 3:
                    robots_txt = parts[-1].decode('utf-8', errors='replace')
                else:
                    # 포맷이 예상과 다를 경우 전체 디코딩
                    robots_txt = warc_data.decode('utf-8', errors='replace')
                
                logger.info(f"[{domain}] [SUCCESS] WARC 원문 추출 및 파싱 완료 ({len(robots_txt)} bytes)")
                return {
                    "domain": domain, 
                    "source": "CommonCrawl_WARC", 
                    "status": 200, 
                    "crawl_date": crawl_date,
                    "content": robots_txt[:500] + "..."
                }
            else:
                return await fetch_live(session, domain, f"https://{domain}/robots.txt")
    except Exception as e:
        return await fetch_live(session, domain, f"https://{domain}/robots.txt")

# Step 3-B: 직접 비동기 크롤링 (Fallback)
async def fetch_live(session, domain, url):
    """
    Case B/C의 경우, 타겟 서버에 직접 비동기 요청을 수행합니다. (안전 장치 적용)
    """
    headers = {"User-Agent": USER_AGENT}
    crawl_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    
    try:
        logger.info(f"[{domain}] Live 직접 크롤링 시도")
        async with session.get(url, headers=headers, timeout=10) as response:
            content = await response.text()
            logger.info(f"[{domain}] [SUCCESS] Live 크롤링 완료 (status {response.status})")
            return {
                "domain": domain, 
                "source": "Live_Fetch", 
                "status": response.status, 
                "crawl_date": crawl_date,
                "content": content[:500] + "..."
            }
            
    except asyncio.TimeoutError:
        logger.warning(f"[{domain}] [FAILED] Live 크롤링 타임아웃 (10s)")
        return {"domain": domain, "source": "Live_Fetch", "status": "Timeout", "crawl_date": crawl_date, "content": None}
    except aiohttp.ClientError as e:
        return {"domain": domain, "source": "Live_Fetch", "status": "NetworkError", "crawl_date": crawl_date, "content": None}
    except Exception as e:
        return {"domain": domain, "source": "Live_Fetch", "status": "Error", "crawl_date": crawl_date, "content": None}

# 메인 실행 엔진
async def main():
    async with aiohttp.ClientSession() as session:
        # 1. 시드 URL 추출 (10,000개 목표)
        domains = await fetch_academic_domains(session, target_limit=10000)
        
        logger.info(f"수집 파이프라인 가동. 총 {len(domains)}개 도메인.")
        logger.info("동시성 제어(Semaphore) 적용: 동시에 최대 10개 도메인 접근 허용")
        
        # Politeness 준수: 대규모 수집 시 Semaphore를 적절히 조절 (예: 10)
        semaphore = asyncio.Semaphore(10)
        
        tasks = [process_domain(session, domain, semaphore) for domain in domains]
        
        # 비동기 병렬 실행
        results = await asyncio.gather(*tasks)
        
        logger.info("파이프라인 종료. 최종 결과 저장 중...")
        with open("hybrid_pipeline_results.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        logger.info("완료. 결과 파일: hybrid_pipeline_results.json")

if __name__ == "__main__":
    asyncio.run(main())
