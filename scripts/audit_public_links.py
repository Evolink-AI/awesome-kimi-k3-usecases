#!/usr/bin/env python3
"""Check public URLs referenced by README files without mutating the repo."""

from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r'https://[^\s)>"]+')


def check(url: str) -> tuple[str, int | str]:
    headers = {"User-Agent": "awesome-kimi-k3-usecases-link-audit/1.0", "Range": "bytes=0-0"}
    last_error: str = "UnknownError"
    for attempt in range(5):
        request = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return url, response.status
        except urllib.error.HTTPError as error:
            if error.code < 500:
                return url, error.code
            last_error = str(error.code)
        except Exception as error:  # noqa: BLE001
            last_error = type(error).__name__
        time.sleep(1.0 * (attempt + 1))
    return url, last_error


def main() -> int:
    urls: set[str] = set()
    for path in [ROOT / "README.md", *sorted(ROOT.glob("README_*.md"))]:
        urls.update(URL_RE.findall(path.read_text(encoding="utf-8")))
    urls = {url.rstrip(".,") for url in urls if "img.shields.io" not in url}
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = sorted(pool.map(check, urls))
    failures = []
    for url, status in results:
        ok = isinstance(status, int) and status in {200, 206, 301, 302, 303, 307, 308}
        print(f"{'PASS' if ok else 'FAIL'} {status} {url}")
        if not ok:
            failures.append((url, status))
    print(f"checked={len(results)} failures={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
