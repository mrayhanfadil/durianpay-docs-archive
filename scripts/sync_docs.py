#!/usr/bin/env python3
"""Download the public Durianpay docs Markdown pages into a private archive."""
from __future__ import annotations

import concurrent.futures
import hashlib
import html
import ipaddress
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urljoin, urlparse
from urllib.request import Request, urlopen

BASE = "https://docs.durianpay.id"
LLMS_URL = f"{BASE}/llms.txt"
USER_AGENT = "Mozilla/5.0 (compatible; DurianpayDocsPersonalArchive/1.0)"
ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
ASSET_DIR = ROOT / "assets"
MAX_ASSET_BYTES = 50 * 1024 * 1024
MAX_ASSETS = 1500
WORKERS = 4


def request_bytes(url: str, *, accept: str = "text/markdown,text/plain,*/*") -> tuple[int, str, bytes]:
    last_error: Exception | None = None
    for attempt in range(3):
        req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
        try:
            with urlopen(req, timeout=45) as response:
                body = response.read(MAX_ASSET_BYTES + 1)
                if len(body) > MAX_ASSET_BYTES:
                    raise ValueError(f"response exceeds {MAX_ASSET_BYTES} bytes")
                return response.status, response.headers.get("Content-Type", ""), body
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                return exc.code, exc.headers.get("Content-Type", ""), exc.read(4096)
            last_error = exc
        except (URLError, TimeoutError, OSError, ValueError) as exc:
            last_error = exc
            if attempt == 2:
                break
        time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url}: {last_error}")


def sitemap_urls(sitemap: str) -> list[str]:
    # llms.txt links page Markdown endpoints; retain only same-origin .md pages.
    candidates = re.findall(r"\((https?://[^)\s]+)\)", sitemap)
    urls: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        candidate = html.unescape(candidate)
        parsed = urlparse(candidate)
        if parsed.scheme != "https" or parsed.netloc.lower() != "docs.durianpay.id":
            continue
        if not parsed.path.endswith(".md"):
            continue
        canonical = candidate.rstrip(".,")
        if canonical not in seen:
            seen.add(canonical)
            urls.append(canonical)
    return urls


def page_path(url: str) -> Path:
    parsed = urlparse(url)
    relative = unquote(parsed.path).lstrip("/")
    if not relative or ".." in Path(relative).parts:
        raise ValueError(f"unsafe page path: {url}")
    target = CONTENT_DIR / relative
    if parsed.query:
        suffix = hashlib.sha256(parsed.query.encode()).hexdigest()[:10]
        target = target.with_name(f"{target.stem}-{suffix}{target.suffix}")
    return target


def fetch_page(url: str) -> dict:
    status, content_type, body = request_bytes(url)
    result = {"url": url, "status": status, "content_type": content_type, "bytes": len(body)}
    if status != 200:
        result["error"] = body.decode("utf-8", errors="replace")[:500]
        return result
    stripped = body.lstrip().lower()
    if stripped.startswith((b"<!doctype html", b"<html")):
        result["error"] = "Got HTML instead of the Markdown endpoint"
        return result
    if not body.strip():
        result["error"] = "Empty response"
        return result
    target = page_path(url)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_bytes(body)
    os.replace(temporary, target)
    result["path"] = str(target.relative_to(ROOT))
    result["sha256"] = hashlib.sha256(body).hexdigest()
    return result


def safe_asset_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        return False
    hostname = parsed.hostname.lower().rstrip(".")
    if hostname in {"localhost", "localhost.localdomain"} or hostname.endswith(".local"):
        return False
    try:
        ip = ipaddress.ip_address(hostname)
        if not ip.is_global:
            return False
    except ValueError:
        pass
    return True


def discover_assets(page_url: str, text: str) -> list[str]:
    found: list[str] = []
    patterns = [
        r"!\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))",
        r"<img\b[^>]*?\bsrc\s*=\s*['\"]([^'\"]+)['\"]",
        r"<source\b[^>]*?\bsrc\s*=\s*['\"]([^'\"]+)['\"]",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            raw = next((group for group in match.groups() if group), "").strip()
            if raw:
                found.append(urljoin(page_url, html.unescape(raw)))
    # Keep file downloads linked from the vendor docs, not arbitrary linked webpages.
    file_exts = {".pdf", ".xlsx", ".xls", ".csv", ".zip", ".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".docx", ".doc", ".pptx"}
    for match in re.finditer(r"\[[^\]]+\]\((https?://[^)\s]+)\)", text):
        candidate = html.unescape(match.group(1))
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
        if Path(parsed.path).suffix.lower() in file_exts and (host.endswith("durianpay.id") or host.endswith("durianpay.readme.io")):
            found.append(candidate)
    return list(dict.fromkeys(url for url in found if safe_asset_url(url)))


def asset_path(url: str) -> Path:
    parsed = urlparse(url)
    name = Path(unquote(parsed.path)).name or "asset"
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name)[:120]
    digest = hashlib.sha256(url.encode()).hexdigest()[:12]
    return ASSET_DIR / (parsed.hostname or "unknown") / f"{digest}-{name}"


def fetch_asset(url: str) -> dict[str, object]:
    result: dict[str, object] = {"url": url}
    try:
        status, content_type, body = request_bytes(url, accept="image/avif,image/webp,image/*,application/pdf,application/octet-stream,*/*")
        result.update({"status": status, "content_type": content_type, "bytes": len(body)})
        if status != 200:
            result["error"] = body.decode("utf-8", errors="replace")[:300]
            return result
        target = asset_path(url)
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_suffix(target.suffix + ".tmp")
        temporary.write_bytes(body)
        os.replace(temporary, target)
        result["path"] = str(target.relative_to(ROOT))
        result["sha256"] = hashlib.sha256(body).hexdigest()
    except Exception as exc:  # Record failures instead of silently dropping referenced files.
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    dry_run = "--dry-run" in sys.argv[1:]
    status, content_type, body = request_bytes(LLMS_URL, accept="text/plain,text/markdown,*/*")
    if status != 200:
        raise SystemExit(f"llms.txt HTTP {status}: {body[:300]!r}")
    sitemap = body.decode("utf-8-sig")
    if "# Durianpay Documentation" not in sitemap:
        raise SystemExit("Unexpected llms.txt body; refusing to crawl")
    urls = sitemap_urls(sitemap)
    if not urls:
        raise SystemExit("No same-origin Markdown pages found in llms.txt")
    print(f"Discovered {len(urls)} unique Markdown pages from {LLMS_URL}")
    if dry_run:
        for url in urls:
            print(url)
        return 0

    source_dir = ROOT / "source"
    source_dir.mkdir(parents=True, exist_ok=True)
    (source_dir / "llms.txt").write_bytes(body)
    timestamp = datetime.now(timezone.utc).isoformat()
    results: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        futures = {executor.submit(fetch_page, url): url for url in urls}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            label = result.get("path", futures[future])
            print(f"{result['status']} {result.get('bytes', 0):>8} {label}")
    results.sort(key=lambda item: item["url"])
    pages_ok = [item for item in results if item.get("status") == 200 and "path" in item]
    page_failures = [item for item in results if "path" not in item]

    asset_sources: list[str] = []
    for result in pages_ok:
        source_url = result["url"]
        page_file = ROOT / result["path"]
        text = page_file.read_text(encoding="utf-8", errors="replace")
        asset_sources.extend(discover_assets(source_url, text))
    asset_sources = list(dict.fromkeys(asset_sources))[:MAX_ASSETS]
    print(f"Discovered {len(asset_sources)} embedded images / linked files")
    asset_results: list[dict] = []
    if asset_sources:
        with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
            futures = {executor.submit(fetch_asset, url): url for url in asset_sources}
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                asset_results.append(result)
                if "error" in result:
                    print(f"ASSET-ERROR {result['url']}: {result['error']}")
                else:
                    print(f"ASSET-OK {result['bytes']:>8} {result['path']}")
    asset_results.sort(key=lambda item: item["url"])

    write_json(ROOT / "manifest.json", {
        "source": BASE,
        "sitemap_url": LLMS_URL,
        "retrieved_at_utc": timestamp,
        "pages_discovered": len(urls),
        "pages_saved": len(pages_ok),
        "page_failures": page_failures,
        "pages": results,
        "assets_discovered": len(asset_sources),
        "assets_saved": sum(1 for item in asset_results if "path" in item),
        "asset_failures": [item for item in asset_results if "error" in item],
        "assets": asset_results,
    })
    total_bytes = sum(item.get("bytes", 0) for item in pages_ok)
    print(f"Summary: {len(pages_ok)}/{len(urls)} pages saved; {total_bytes} page bytes; "
          f"{sum(1 for item in asset_results if 'path' in item)}/{len(asset_sources)} assets saved")
    return 1 if page_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
