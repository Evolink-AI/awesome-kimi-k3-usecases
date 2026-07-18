#!/usr/bin/env python3
"""Audit every expected R2 visual and playable video from the source manifest."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]


def current_head() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unavailable"


def fetch_prefix(url: str) -> tuple[str, int, str, bytes, str]:
    result = subprocess.run(
        [
            "curl", "-L", "-sS", "--retry", "5", "--retry-all-errors",
            "--retry-delay", "1", "--connect-timeout", "10", "--max-time", "60",
            "--user-agent", "awesome-kimi-k3-usecases-r2-audit/1.0",
            "--range", "0-31", "--dump-header", "-", url,
        ],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return url, 0, "", b"", result.stderr.decode("utf-8", errors="replace").strip()
    sections = result.stdout.split(b"\r\n\r\n")
    if len(sections) < 2:
        return url, 0, "", b"", "curl response did not contain a header block"
    headers = sections[-2].decode("iso-8859-1", errors="replace").splitlines()
    body = sections[-1][:32]
    status_parts = headers[0].split() if headers else []
    status = int(status_parts[1]) if len(status_parts) > 1 and status_parts[1].isdigit() else 0
    content_type = ""
    for header in headers[1:]:
        if header.lower().startswith("content-type:"):
            content_type = header.split(":", 1)[1].strip().split(";", 1)[0].lower()
            break
    return url, status, content_type, body, ""


def image_signature(payload: bytes) -> bool:
    return (
        payload.startswith(b"\xff\xd8\xff")
        or payload.startswith(b"\x89PNG\r\n\x1a\n")
        or payload.startswith((b"GIF87a", b"GIF89a"))
        or (payload.startswith(b"RIFF") and payload[8:12] == b"WEBP")
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "data/source-fidelity-manifest.json")
    parser.add_argument("--report", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    visual_urls = [
        url
        for case in manifest["cases"]
        for url in case["expected_public_media_urls"]
    ]
    playable_urls = [
        case["playable_video_url"]
        for case in manifest["cases"]
        if case.get("playable_video_url")
    ]
    all_urls = list(dict.fromkeys([*visual_urls, *playable_urls]))
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = {row[0]: row[1:] for row in pool.map(fetch_prefix, all_urls)}

    failures: list[str] = []
    for url in visual_urls:
        status, content_type, payload, error = results[url]
        if status not in {200, 206} or not content_type.startswith("image/") or not image_signature(payload):
            failures.append(
                f"visual {url}: status={status} content_type={content_type or '<missing>'} error={error or '<none>'}"
            )
    for url in playable_urls:
        status, content_type, payload, error = results[url]
        if status not in {200, 206} or content_type != "video/mp4" or len(payload) < 12 or payload[4:8] != b"ftyp":
            failures.append(
                f"video {url}: status={status} content_type={content_type or '<missing>'} error={error or '<none>'}"
            )

    passed = (
        not failures
        and len(visual_urls) == manifest["expected_public_visual_count"]
        and len(set(visual_urls)) == len(visual_urls)
        and len(playable_urls) == len(set(playable_urls))
    )
    lines = [
        "# R2 Source Media Audit v1",
        "",
        f"- Status: `{'passed' if passed else 'failed'}`",
        f"- Target commit: `{current_head()}`",
        f"- Source manifest SHA256: `{manifest['source_manifest_sha256']}`",
        f"- Expected visual media: {len(visual_urls)}",
        f"- Checked visual media: {sum(results[url][0] in {200, 206} for url in visual_urls)}",
        f"- Expected playable videos: {len(playable_urls)}",
        f"- Checked playable videos: {sum(results[url][0] in {200, 206} for url in playable_urls)}",
        f"- Failures: {len(failures)}",
        f"- Command exit code: {0 if passed else 1}",
        f"- Result: {'pass' if passed else 'fail'}",
    ]
    if failures:
        lines.extend(["", "## Failures", "", *[f"- {failure}" for failure in failures]])
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("PASS" if passed else "FAIL")
    print(f"expected_visual_media={len(visual_urls)}")
    print(f"checked_visual_media={sum(results[url][0] in {200, 206} for url in visual_urls)}")
    print(f"expected_playable_videos={len(playable_urls)}")
    print(f"checked_playable_videos={sum(results[url][0] in {200, 206} for url in playable_urls)}")
    print(f"failures={len(failures)}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
