#!/usr/bin/env python3
"""Validate the downloaded source pages and assets against manifest.json."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.json"


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sitemap = (ROOT / "source/llms.txt").read_text(encoding="utf-8")
    sitemap_urls = set(re.findall(r"\((https://docs\.durianpay\.id/[^)\s]+\.md)\)", sitemap))
    pages = data.get("pages", [])
    page_urls = {page["url"] for page in pages}
    problems: list[str] = []
    if len(page_urls) != len(pages):
        problems.append("duplicate source URLs in page manifest")
    if sitemap_urls != page_urls:
        problems.append(f"sitemap/manifest mismatch: {len(sitemap_urls)} sitemap URLs vs {len(page_urls)} manifest URLs")
    for page in pages:
        path = ROOT / page.get("path", "")
        if page.get("status") != 200 or not path.is_file():
            problems.append(f"page missing or not HTTP 200: {page.get('url')}")
            continue
        raw = path.read_bytes()
        if not raw.strip():
            problems.append(f"empty page: {path.relative_to(ROOT)}")
        if hashlib.sha256(raw).hexdigest() != page.get("sha256"):
            problems.append(f"page hash mismatch: {path.relative_to(ROOT)}")
        if raw.lstrip().lower().startswith((b"<!doctype html", b"<html")):
            problems.append(f"HTML error page stored as Markdown: {path.relative_to(ROOT)}")
    assets = data.get("assets", [])
    assets_saved = [asset for asset in assets if asset.get("path")]
    for asset in assets_saved:
        path = ROOT / asset["path"]
        if not path.is_file():
            problems.append(f"asset missing: {asset['url']}")
            continue
        raw = path.read_bytes()
        if len(raw) != asset.get("bytes") or hashlib.sha256(raw).hexdigest() != asset.get("sha256"):
            problems.append(f"asset size/hash mismatch: {asset['url']}")
    if data.get("page_failures"):
        problems.append(f"manifest contains {len(data['page_failures'])} page failures")
    if data.get("asset_failures"):
        problems.append(f"manifest contains {len(data['asset_failures'])} asset failures")
    print(f"Pages: {len(page_urls)}/{len(sitemap_urls)}; assets: {len(assets_saved)}/{data.get('assets_discovered', 0)}")
    print(f"Page bytes: {sum(page.get('bytes', 0) for page in pages)}; asset bytes: {sum(asset.get('bytes', 0) for asset in assets_saved)}")
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1
    print("PASS: every indexed page and captured asset exists and matches its SHA-256; no recorded fetch failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
