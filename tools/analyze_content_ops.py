#!/usr/bin/env python3
"""Build bounded content-operations strategy memory from local records."""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import re
from pathlib import Path


PLATFORM_ALIASES = {
    "x": "X",
    "twitter": "X",
    "dev.to": "Dev.to",
    "devto": "Dev.to",
    "hashnode": "Hashnode",
    "quora": "Quora",
    "medium": "Medium",
    "youtube": "YouTube",
    "youtube community": "YouTube",
    "youtube shorts": "YouTube",
    "github": "GitHub",
    "github docs": "GitHub",
    "seo": "SEO / Owned",
    "seo / 官网": "SEO / Owned",
    "seo / 官网繁中": "SEO / Owned",
    "reddit": "Reddit",
    "hackernoon": "HackerNoon",
    "hacker news": "Hacker News",
    "product hunt": "Product Hunt",
}


def normalize_platform(raw: str) -> str:
    value = re.sub(r"（.*?）|\(.*?\)", "", raw).strip()
    value = re.sub(r"\s+(主帖|首条回复|投票|Community|Shorts)$", "", value).strip()
    lowered = value.lower()
    for prefix, canonical in PLATFORM_ALIASES.items():
        if lowered == prefix or lowered.startswith(prefix + " "):
            return canonical
    return value


def date_from_path(path: Path) -> str:
    match = re.search(r"(20\d{2}-\d{2}-\d{2})", path.name)
    return match.group(1) if match else "unknown"


def empty_ops() -> dict:
    return {
        "published_records": 0,
        "submitted_not_public": 0,
        "blocked_records": 0,
        "moderation_events": 0,
        "technical_failures": 0,
        "latest_date": None,
        "latest_status": None,
        "recent_reasons": [],
    }


def parse_record(path: Path, aggregate: dict) -> None:
    section = None
    record_date = date_from_path(path)
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## 已公开") or line.startswith("## 已发布"):
            section = "published"
            continue
        if line.startswith("## 已提交"):
            section = "submitted"
            continue
        if line.startswith("## 未发布"):
            section = "blocked"
            continue
        if line.startswith("## "):
            section = None
            continue
        if section is None or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in {"平台", "---"} or set(cells[0]) == {"-"}:
            continue
        platform = normalize_platform(cells[0])
        status = cells[1]
        details = " | ".join(cells[1:])
        ops = aggregate.setdefault(platform, empty_ops())
        ops["latest_date"] = max(filter(None, [ops["latest_date"], record_date]))
        ops["latest_status"] = status
        if section == "published" and "已发布" in status:
            ops["published_records"] += 1
        elif section == "submitted":
            ops["submitted_not_public"] += 1
        elif section == "blocked":
            ops["blocked_records"] += 1
        if re.search(r"AutoMod|自动归档|审核归档|moderation", details, re.I):
            ops["moderation_events"] += 1
        if re.search(r"编辑器|保存失败|空白|未登录|无.*权限|无发布入口|技术阻断", details):
            ops["technical_failures"] += 1
        if section != "published" and details not in ops["recent_reasons"]:
            ops["recent_reasons"].append(details[:300])
            ops["recent_reasons"] = ops["recent_reasons"][-5:]


def load_metric_snapshots(paths: list[Path]) -> tuple[list[dict], dict]:
    snapshots = []
    latest_by_platform = {}
    for path in sorted(paths):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SystemExit(f"Invalid metrics snapshot {path}: {exc}") from exc
        as_of = data.get("as_of", path.stem)
        snapshots.append({"path": str(path), "as_of": as_of})
        for platform, payload in data.get("platforms", {}).items():
            current = latest_by_platform.get(platform)
            if current is None or str(as_of) >= str(current["as_of"]):
                latest_by_platform[platform] = {"as_of": as_of, **payload}
    return snapshots, latest_by_platform


def metric_value(payload: dict, name: str, default=None):
    return payload.get("metrics", {}).get(name, default)


def decide_mode(ops: dict, payload: dict) -> tuple[str, list[str]]:
    reasons = []
    moderation = max(ops["moderation_events"], metric_value(payload, "moderation_archives", 0) or 0)
    technical_streak = metric_value(payload, "consecutive_technical_failures", 0) or 0
    zero_reader_streak = metric_value(payload, "consecutive_zero_reader_posts", 0) or 0
    mismatch = metric_value(payload, "audience_mismatch_ratio", 0) or 0
    sample = metric_value(payload, "sample_size", metric_value(payload, "sample_posts", 0)) or 0
    organic = metric_value(payload, "organic_engagements", None)

    if moderation:
        reasons.append(f"{moderation} moderation/archive signal(s)")
        return "pause", reasons
    if technical_streak >= 3:
        reasons.append(f"{technical_streak} consecutive technical failures")
        return "blocked", reasons
    if ops["technical_failures"] >= 3 and ops["blocked_records"] >= 3:
        reasons.append(f"{ops['technical_failures']} recorded technical/access failures")
        return "blocked", reasons
    if zero_reader_streak >= 3:
        reasons.append(f"{zero_reader_streak} consecutive zero-reader posts")
        return "reduce", reasons
    if mismatch >= 0.5:
        reasons.append(f"audience mismatch ratio {mismatch:.1%}")
        return "test", reasons
    if sample >= 3 and organic == 0:
        reasons.append(f"zero organic engagements across {sample} comparable samples")
        return "test", reasons
    if ops["published_records"] >= 3 and not payload:
        reasons.append("publishing volume exists without a current metric snapshot")
        return "measure", reasons
    if ops["blocked_records"] >= 3 and ops["published_records"] == 0:
        reasons.append("repeated blockers with no successful publication")
        return "blocked", reasons
    if ops["published_records"]:
        reasons.append("published evidence exists but downstream conversion is unproven")
        return "test", reasons
    reasons.append("insufficient executable evidence")
    return "blocked", reasons


def confidence(ops: dict, payload: dict) -> str:
    sample = metric_value(payload, "sample_size", metric_value(payload, "sample_posts", 0)) or 0
    attempts = ops["published_records"] + ops["submitted_not_public"] + ops["blocked_records"]
    if sample >= 5 or attempts >= 6:
        return "high"
    if sample >= 3 or attempts >= 3:
        return "medium"
    return "low"


def next_action(mode: str) -> str:
    return {
        "scale": "Repeat only the validated format and preserve attribution.",
        "test": "Run one named experiment with a measurable stop condition.",
        "maintain": "Keep low frequency and reuse only strong source material.",
        "reduce": "Require materially new evidence before the next post.",
        "pause": "Stop routine submissions until the recovery condition is met.",
        "blocked": "Resolve access, tooling, rules, or measurement first.",
        "measure": "Collect comparable outcome data before adding volume.",
    }[mode]


def write_markdown(memory: dict, path: Path) -> None:
    lines = [
        "# Strategy Memory",
        "",
        f"- Generated: {memory['generated_at']}",
        f"- Rule version: {memory['rule_version']}",
        "",
        "| Platform | Mode | Confidence | Published units | Blocked records | Primary reason |",
        "|---|---|---:|---:|---:|---|",
    ]
    for platform, data in memory["platforms"].items():
        ops = data["operations"]
        reason = "; ".join(data["reasons"]).replace("|", "/")
        lines.append(
            f"| {platform} | {data['mode']} | {data['confidence']} | "
            f"{ops['published_records']} | {ops['blocked_records']} | {reason} |"
        )
    lines.extend(["", "## Guardrails", ""])
    lines.extend(f"- {item}" for item in memory["guardrails"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--records-glob", default="05-执行与记录/*海外平台发布结果.md")
    parser.add_argument("--metrics-glob", default="05-执行与记录/运营学习/*platform-metrics.json")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument("--now", help="ISO date/time for deterministic runs")
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    records = [Path(p) for p in sorted(glob.glob(str(workspace / args.records_glob)))]
    metric_paths = [Path(p) for p in sorted(glob.glob(str(workspace / args.metrics_glob)))]
    operations = {}
    for record in records:
        parse_record(record, operations)
    snapshots, latest_metrics = load_metric_snapshots(metric_paths)

    platforms = {}
    for platform in sorted(set(operations) | set(latest_metrics)):
        ops = operations.get(platform, empty_ops())
        payload = latest_metrics.get(platform, {})
        mode, reasons = decide_mode(ops, payload)
        platforms[platform] = {
            "mode": mode,
            "confidence": confidence(ops, payload),
            "reasons": reasons,
            "next_action": next_action(mode),
            "operations": ops,
            "latest_metrics": payload,
        }

    generated_at = args.now or dt.datetime.now(dt.timezone.utc).isoformat()
    memory = {
        "schema_version": 1,
        "rule_version": "content-ops-v1",
        "generated_at": generated_at,
        "workspace": str(workspace),
        "sources": {
            "publication_records": [str(path) for path in records],
            "metric_snapshots": snapshots,
        },
        "platforms": platforms,
        "guardrails": [
            "Performance data must not modify product facts or approved claims.",
            "One outlier creates a hypothesis, not a scaling rule.",
            "Moderation, account, privacy, and factual-integrity signals can pause a channel immediately.",
            "External publishing and account changes still require explicit authorization.",
        ],
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(memory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown_output:
        write_markdown(memory, args.markdown_output)


if __name__ == "__main__":
    main()
