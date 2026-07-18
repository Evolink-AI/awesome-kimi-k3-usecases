#!/usr/bin/env python3
"""Restore source-backed case media and prepare it for the repository R2 namespace."""

from __future__ import annotations

import argparse
import json
import mimetypes
import re
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
R2_ROOT = (
    "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/"
    "github-repo-media/awesome-kimi-k3-usecases"
)
LEGACY_VIDEO_CASES = set(range(1, 7))


def source_items(payload: object) -> list[dict]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("items", "posts", "results"):
            value = payload.get(key)
            if isinstance(value, list):
                return value
    raise ValueError("source payload does not contain an item list")


def source_link(item: dict) -> str:
    for key in ("link", "url", "source_url"):
        value = item.get(key)
        if isinstance(value, str) and value:
            return value.split("?", 1)[0].rstrip("/")
    raise ValueError("source item has no link")


def unique_urls(urls: list[str]) -> list[str]:
    return list(dict.fromkeys(url for url in urls if isinstance(url, str) and url.startswith("http")))


def extension(url: str, content_type: str = "") -> str:
    parsed = urlparse(url)
    suffix = Path(parsed.path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
        return ".jpg" if suffix == ".jpeg" else suffix
    query_format = parse_qs(parsed.query).get("format", [""])[0].lower()
    if query_format in {"jpg", "jpeg", "png", "webp", "gif"}:
        return ".jpg" if query_format == "jpeg" else f".{query_format}"
    guessed = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
    return ".jpg" if guessed in {None, ".jpe", ".jpeg"} else guessed


def image_signature_is_valid(path: Path) -> bool:
    payload = path.read_bytes()[:16]
    return (
        payload.startswith(b"\xff\xd8\xff")
        or payload.startswith(b"\x89PNG\r\n\x1a\n")
        or payload.startswith((b"GIF87a", b"GIF89a"))
        or (payload.startswith(b"RIFF") and payload[8:12] == b"WEBP")
    )


def video_signature_is_valid(path: Path) -> bool:
    payload = path.read_bytes()[:32]
    return len(payload) >= 12 and payload[4:8] == b"ftyp"


def download_image(url: str, target_stem: Path) -> Path:
    target = target_stem.with_suffix(extension(url))
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_file() and target.stat().st_size >= 1_000 and image_signature_is_valid(target):
        return target
    partial = target.with_suffix(target.suffix + ".part")
    result = subprocess.run(
        [
            "curl", "--location", "--fail", "--silent", "--show-error",
            "--retry", "5", "--retry-all-errors", "--retry-delay", "1",
            "--output", str(partial), url,
        ],
        check=False,
    )
    if result.returncode != 0:
        partial.unlink(missing_ok=True)
        raise ValueError(f"curl failed to download image: {url}")
    if partial.stat().st_size < 1_000 or not image_signature_is_valid(partial):
        partial.unlink(missing_ok=True)
        raise ValueError(f"downloaded file is not a valid source image: {url}")
    partial.replace(target)
    return target


def video_resolution(url: str) -> tuple[int, int]:
    match = re.search(r"/(\d+)x(\d+)/", url)
    if not match:
        return (0, 0)
    return (int(match.group(1)), int(match.group(2)))


def select_video_variant(urls: list[str]) -> str:
    variants = [url for url in urls if "video.twimg.com/" in url and ".mp4" in url]
    if not variants:
        raise ValueError("source item has no direct MP4 variant")
    preferred = [url for url in variants if max(video_resolution(url)) <= 1280]
    candidates = preferred or variants
    return max(candidates, key=lambda url: video_resolution(url)[0] * video_resolution(url)[1])


def download_video(url: str, target: Path) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_file() and target.stat().st_size >= 10_000 and video_signature_is_valid(target):
        return target
    partial = target.with_suffix(target.suffix + ".part")
    result = subprocess.run(
        [
            "curl", "--location", "--fail", "--silent", "--show-error",
            "--retry", "5", "--retry-all-errors", "--retry-delay", "1",
            "--output", str(partial), url,
        ],
        check=False,
    )
    if result.returncode != 0:
        partial.unlink(missing_ok=True)
        raise ValueError(f"curl failed to download video: {url}")
    if partial.stat().st_size < 10_000 or not video_signature_is_valid(partial):
        partial.unlink(missing_ok=True)
        raise ValueError(f"downloaded file is not a valid MP4: {url}")
    partial.replace(target)
    return target


def r2_url(path: Path) -> str:
    return f"{R2_ROOT}/{path.relative_to(ROOT).as_posix()}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--download-dir", type=Path, default=ROOT / "media/source-cases")
    parser.add_argument("--apply-data", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = source_items(json.loads(args.source.read_text(encoding="utf-8")))
    source_by_link = {source_link(item): item for item in source}
    data_path = ROOT / "data/use-cases.json"
    curated = json.loads(data_path.read_text(encoding="utf-8"))
    items = curated["items"]
    downloaded: list[Path] = []

    for item in items:
        number = item["public_number"]
        nn = f"{number:02d}"
        link = item["source_url"].split("?", 1)[0].rstrip("/")
        raw = source_by_link.get(link)
        if raw is None:
            raise ValueError(f"case {number} is missing from source artifact: {link}")
        urls = unique_urls(raw.get("media") or [])
        posters = [url for url in urls if "pbs.twimg.com/" in url and "video_thumb" in url]
        images = [url for url in urls if "pbs.twimg.com/media/" in url]
        videos = [url for url in urls if "video.twimg.com/" in url and ".mp4" in url]
        assets: list[dict] = []
        selected_source_urls: list[str] = []

        if posters or videos:
            video_source_url = select_video_variant(videos)
            if number in LEGACY_VIDEO_CASES:
                assets.append({
                    "kind": "video",
                    "url": f"{R2_ROOT}/media/cases/case-{nn}.mp4",
                    "poster_url": f"{R2_ROOT}/media/cases/case-{nn}-poster.jpg",
                    "play_label": f"Play case {number} demo video",
                })
                item["poster_path"] = f"media/cases/case-{nn}-poster.jpg"
                item["playable_video_path"] = f"media/cases/case-{nn}.mp4"
            else:
                if not posters:
                    raise ValueError(f"case {number} has video media but no source poster")
                poster_path = download_image(posters[0], args.download_dir / f"case-{nn}-poster")
                video_path = download_video(video_source_url, args.download_dir / f"case-{nn}.mp4")
                downloaded.extend((poster_path, video_path))
                assets.append({
                    "kind": "video",
                    "url": r2_url(video_path),
                    "poster_url": r2_url(poster_path),
                    "play_label": f"Play case {number} demo video",
                })
                item["poster_path"] = poster_path.relative_to(ROOT).as_posix()
                item["playable_video_path"] = video_path.relative_to(ROOT).as_posix()
            selected_source_urls.append(video_source_url)
        elif not images:
            raise ValueError(f"case {number} has no usable source media")

        for index, url in enumerate(images, start=1):
            image_path = download_image(url, args.download_dir / f"case-{nn}-{index:02d}")
            downloaded.append(image_path)
            assets.append({
                "kind": "image",
                "url": r2_url(image_path),
            })
            selected_source_urls.append(url)

        item["media_type"] = "video" if any(asset["kind"] == "video" for asset in assets) else "image"
        item["media_assets"] = assets
        item["media_source_urls"] = selected_source_urls

    if args.apply_data:
        data_path.write_text(json.dumps(curated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    videos = sum(item["media_type"] == "video" for item in items)
    images = sum(item["media_type"] == "image" for item in items)
    assets = sum(len(item["media_assets"]) for item in items)
    print(f"cases={len(items)}")
    print(f"video_cases={videos}")
    print(f"image_cases={images}")
    print(f"media_assets={assets}")
    print(f"downloaded_files={len(downloaded)}")
    print(f"download_dir={args.download_dir}")
    print(f"data_updated={args.apply_data}")


if __name__ == "__main__":
    main()
