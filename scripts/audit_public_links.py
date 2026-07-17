#!/usr/bin/env python3
"""Check public URLs referenced by README files without mutating the repo."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r'https://[^\s)>"]+')
CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)


def check(url: str) -> tuple[str, int | str]:
    command = [
        "curl", "-L", "-sS", "--retry", "8", "--retry-all-errors",
        "--retry-delay", "1", "--connect-timeout", "10", "--max-time", "30",
        "--user-agent", "awesome-kimi-k3-usecases-link-audit/1.0",
    ]
    if url.startswith("https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/"):
        command.extend(["-r", "0-0"])
    command.extend(["-o", "/dev/null", "-w", "%{http_code}", url])
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    status_text = result.stdout[-3:]
    if result.returncode == 0 and status_text.isdigit():
        return url, int(status_text)
    return url, result.stderr.strip() or f"curl-exit-{result.returncode}"


def main() -> int:
    exception_data = json.loads((ROOT / "data/link-audit-exceptions.json").read_text(encoding="utf-8"))
    exceptions = {
        item["url"]: set(item["allowed_statuses"])
        for item in exception_data.get("exceptions", [])
    }
    urls: set[str] = set()
    for path in [ROOT / "README.md", *sorted(ROOT.glob("README_*.md"))]:
        text = CODE_BLOCK_RE.sub("", path.read_text(encoding="utf-8"))
        urls.update(URL_RE.findall(text))
    urls = {url.rstrip(".,") for url in urls if "img.shields.io" not in url}
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = sorted(pool.map(check, urls))
    failures = []
    accepted = []
    for url, status in results:
        ok = isinstance(status, int) and status in {200, 206, 301, 302, 303, 307, 308}
        excepted = isinstance(status, int) and status in exceptions.get(url, set())
        print(f"{'PASS' if ok else 'EXCEPT' if excepted else 'FAIL'} {status} {url}")
        if excepted:
            accepted.append((url, status))
        if not ok and not excepted:
            failures.append((url, status))
    print(f"checked={len(results)} accepted_exceptions={len(accepted)} failures={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
