#!/usr/bin/env python3
"""Build a full-set source-fidelity manifest and verifier package."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OWNER_PRESENTATION = {
    "menu_layout": "centralized-single-table",
    "acknowledge_layout": "inline-comma",
    "quick_start_position": "pre-case-section",
    "media_policy": "all-source-media",
    "video_playback_policy": "r2-playable",
    "localization_fallback": "english",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument(
        "--supplemental-git-ref",
        help="Immutable git commit containing additional reviewed public cases",
    )
    parser.add_argument(
        "--combined-source",
        type=Path,
        help="Generated source package that binds the primary artifact and supplemental commit",
    )
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument(
        "--public-manifest",
        type=Path,
        default=ROOT / "data/source-fidelity-manifest.json",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    primary_source = args.source.expanduser().resolve()
    curated_path = ROOT / "data/use-cases.json"
    curated = json.loads(curated_path.read_text(encoding="utf-8"))
    items = curated["items"]
    source = primary_source
    source_inputs = [
        {
            "kind": "primary-file",
            "path": str(primary_source),
            "sha256": sha256_file(primary_source),
        }
    ]

    if args.supplemental_git_ref:
        if not args.combined_source:
            raise ValueError("--combined-source is required with --supplemental-git-ref")
        commit = subprocess.check_output(
            ["git", "rev-parse", f"{args.supplemental_git_ref}^{{commit}}"],
            cwd=ROOT,
            text=True,
        ).strip()
        supplemental_payload = subprocess.check_output(
            ["git", "show", f"{commit}:data/use-cases.json"],
            cwd=ROOT,
            text=True,
        )
        supplemental_data = json.loads(supplemental_payload)
        primary_data = json.loads(primary_source.read_text(encoding="utf-8"))
        primary_items = primary_data.get("items", [])
        primary_urls = {item.get("url") or item.get("source_url") for item in primary_items}
        supplemental_items = [
            item
            for item in supplemental_data.get("items", [])
            if item.get("source_url") not in primary_urls
        ]
        curated_by_url = {item["source_url"]: item for item in items}
        for item in supplemental_items:
            current = curated_by_url.get(item.get("source_url"))
            if not current:
                raise ValueError(f"supplemental source missing from curated data: {item.get('source_url')}")
            for field in ("title", "decision", "quality_tier", "media_assets"):
                if current.get(field) != item.get(field):
                    raise ValueError(
                        f"supplemental source differs from curated data for {item.get('source_url')}: {field}"
                    )
        combined = {
            "schema_version": 1,
            "primary_source": source_inputs[0],
            "supplemental_source": {
                "kind": "git-commit",
                "commit": commit,
                "path": "data/use-cases.json",
            },
            "items": [*primary_items, *supplemental_items],
        }
        source = args.combined_source.expanduser().resolve()
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        source_inputs.append(combined["supplemental_source"])

    source_urls = {item.get("url") or item.get("source_url") for item in json.loads(source.read_text(encoding="utf-8")).get("items", [])}
    curated_urls = {item["source_url"] for item in items}
    if source_urls != curated_urls:
        raise ValueError(
            f"source package differs from curated public set: source={len(source_urls)}, curated={len(curated_urls)}"
        )
    source_sha = sha256_file(source)
    cases: list[dict] = []
    public_cases: list[dict] = []
    expected_media_count = 0

    for item in items:
        assets = item["media_assets"]
        source_media_urls = item["media_source_urls"]
        if not source_media_urls:
            raise ValueError(f"case {item['public_number']} has no source media URLs")
        if item["media_type"] == "video":
            videos = [asset for asset in assets if asset.get("kind") == "video"]
            supplementary = [asset for asset in assets if asset.get("kind") == "image"]
            if len(videos) != 1 or len(videos) + len(supplementary) != len(assets):
                raise ValueError(f"case {item['public_number']} has invalid video assets")
            video = videos[0]
            supplementary_urls = [asset["url"] for asset in supplementary]
            expected_urls = [video["poster_url"], *supplementary_urls]
            media_fields = {
                "poster_url": video["poster_url"],
                "playable_video_url": video["url"],
                "r2_media_urls": supplementary_urls,
            }
            disposition = "r2-video"
        elif item["media_type"] == "image":
            expected_urls = [asset["url"] for asset in assets]
            media_fields = {"r2_media_urls": expected_urls}
            disposition = "r2-image"
        else:
            raise ValueError(f"case {item['public_number']} has unsupported media type")

        if len(source_media_urls) != len(expected_urls):
            raise ValueError(
                f"case {item['public_number']} source/expected media mismatch: "
                f"{len(source_media_urls)} != {len(expected_urls)}"
            )
        expected_media_count += len(expected_urls)
        case = {
            "source_url": item["source_url"],
            "author_handle": item["author_handle"],
            "author_url": item["author_url"],
            "title": item["title"],
            "takeaway": item["takeaway"],
            "body_notes": item["body_notes"],
            "type": item["type"],
            "date": item["date"],
            "category": item["category"],
            "decision": item["decision"],
            "decision_reason": item["decision_reason"],
            "dedup_key": item["dedup_key"],
            "prompt_boundary": item["prompt_boundary"],
            "media_type": item["media_type"],
            "source_media_urls": source_media_urls,
            "source_media_count": len(source_media_urls),
            "public_media_disposition": disposition,
            "expected_public_visual_count": len(expected_urls),
            "public_number": item["public_number"],
            **media_fields,
        }
        cases.append(case)
        public_cases.append({
            "public_number": item["public_number"],
            "source_url": item["source_url"],
            "source_media_urls": source_media_urls,
            "public_media_disposition": disposition,
            "expected_public_media_urls": expected_urls,
            **({"playable_video_url": video["url"]} if item["media_type"] == "video" else {}),
        })

    manifest = {
        "schema_version": 1,
        "source_artifact": source.name,
        "source_manifest_sha256": source_sha,
        "source_inputs": source_inputs,
        "selected_case_count": len(cases),
        "cases_with_source_media": len(cases),
        "expected_public_visual_count": expected_media_count,
        "media_policy": "all-source-media",
        "owner_presentation": OWNER_PRESENTATION,
        "cases": public_cases,
    }
    package = {
        "run_id": "kimi-k3-full-set-remediation-2026-07-18",
        "run_mode": "first-publication",
        "existing_public_set_audit": True,
        "repo": str(ROOT),
        "source_package": str(source),
        "source_inputs": source_inputs,
        "source_index_policy": "data/use-cases.json is the canonical public index",
        "case_namespace": {
            "name": "Kimi K3 public use cases",
            "heading_prefix": "Case",
            "anchor_prefix": "case",
            "numbering_policy": "global-contiguous",
            "existing_count": 0,
            "intended_count": len(cases),
        },
        "counts": {
            "within_24_hours": len(cases),
            "high_confidence_update": len(cases),
            "deferred": 0,
            "unsure": 0,
            "drop": 0,
        },
        "source_fidelity_manifest": {
            "source_manifest_sha256": source_sha,
            "selected_case_count": len(cases),
            "cases_with_source_media": len(cases),
            "expected_public_visual_count": expected_media_count,
            "media_policy": "all-source-media",
        },
        "owner_presentation": OWNER_PRESENTATION,
        "selected_cases": cases,
    }

    args.package.parent.mkdir(parents=True, exist_ok=True)
    args.package.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.public_manifest.parent.mkdir(parents=True, exist_ok=True)
    args.public_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"selected_cases={len(cases)}")
    print(f"expected_public_media={expected_media_count}")
    print(f"source_manifest_sha256={source_sha}")
    print(f"package={args.package}")
    print(f"public_manifest={args.public_manifest}")


if __name__ == "__main__":
    main()
