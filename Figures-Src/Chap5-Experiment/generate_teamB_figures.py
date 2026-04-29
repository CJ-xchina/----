#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Team-B: Generate Chapter 5 experiment figures from traceable sources only.

Sources:
- /home/yangcx24/Jayx/research/output
- /home/yangcx24/Jayx/fpaper/secret/*.md
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


PROJECT_ROOT = Path("/home/yangcx24/Jayx/fpaper")
OUTPUT_ROOT = Path("/home/yangcx24/Jayx/research/output")
SECRET_ROOT = PROJECT_ROOT / "secret"
FIG_ROOT = PROJECT_ROOT / "Main-Tex" / "Figures-Src" / "Chap5-Experiment"

DATASETS = [("aiops25", "AIOps-25"), ("bank", "Bank"), ("market", "Market")]


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _pct_to_float(v: str) -> float:
    return float(v.strip().replace("%", ""))


def collect_dataset_overview() -> dict[str, dict[str, float]]:
    result: dict[str, dict[str, float]] = {}
    for ds_key, ds_name in DATASETS:
        ds_dir = OUTPUT_ROOT / ds_key
        metadata_files = sorted(ds_dir.glob("*/metadata.json"))
        if not metadata_files:
            raise FileNotFoundError(f"No metadata found in {ds_dir}")

        num_cases = len(metadata_files)
        service_counts: list[int] = []
        fault_types: set[str] = set()
        for f in metadata_files:
            with f.open("r", encoding="utf-8") as fp:
                data = json.load(fp)
            svc = data.get("topology_stats", {}).get("num_services")
            if isinstance(svc, int):
                service_counts.append(svc)
            reason = str(data.get("anomaly_reason", "")).strip().lower()
            if reason:
                fault_types.add(reason)

        avg_services = float(np.mean(service_counts)) if service_counts else 0.0
        result[ds_name] = {
            "cases": float(num_cases),
            "avg_services": avg_services,
            "fault_type_count": float(len(fault_types)),
        }
    return result


def parse_fingerprint_p1() -> tuple[list[str], dict[str, dict[str, float]]]:
    fp_file = SECRET_ROOT / "fingerprint_results.md"
    text = fp_file.read_text(encoding="utf-8")
    lines = text.splitlines()

    p1_map: dict[str, dict[str, float]] = {"AIOps-25": {}, "Bank": {}, "Market": {}}
    method_order: list[str] = []
    current_ds: str | None = None

    for raw in lines:
        line = raw.strip()
        if line.startswith("## ") and "数据集" in line:
            ds_name = line[3:].split(" 数据集", 1)[0].strip()
            current_ds = ds_name if ds_name in p1_map else None
            continue

        if not current_ds or not line.startswith("|"):
            continue
        if "Method" in line or "---" in line:
            continue

        parts = [x.strip() for x in line.strip("|").split("|")]
        if len(parts) < 2:
            continue

        method = parts[0].lower()
        p1 = _pct_to_float(parts[1])
        p1_map[current_ds][method] = p1
        if method not in method_order:
            method_order.append(method)

    if not method_order:
        raise ValueError(f"Failed to parse fingerprint table from {fp_file}")
    return method_order, p1_map


def collect_aiops_sop_evolution(num_turns: int = 8) -> dict[str, list[float]]:
    aiops_dir = OUTPUT_ROOT / "aiops25"
    metadata_files = sorted(aiops_dir.glob("*/metadata.json"))
    if not metadata_files:
        raise FileNotFoundError(f"No metadata found in {aiops_dir}")

    records = []
    for f in metadata_files:
        with f.open("r", encoding="utf-8") as fp:
            d = json.load(fp)
        anomaly_id = str(d.get("anomaly_id", ""))
        component = d.get("anomaly_component")
        if not component and anomaly_id:
            component = anomaly_id.split("_", 1)[0]
        reason = str(d.get("anomaly_reason", "")).strip().lower()
        ts = d.get("anomaly_timestamp")
        if not isinstance(ts, int):
            ts = 0
        records.append({"ts": ts, "component": str(component), "reason": reason})

    records.sort(key=lambda x: (x["ts"], x["component"], x["reason"]))
    n = len(records)
    checkpoints = sorted(set(int(x) for x in np.linspace(1, n, num_turns)))
    turns = list(range(1, len(checkpoints) + 1))

    comp_curve: list[float] = []
    reason_curve: list[float] = []
    unit_curve: list[float] = []

    for c in checkpoints:
        subset = records[:c]
        comps = {x["component"] for x in subset if x["component"]}
        reasons = {x["reason"] for x in subset if x["reason"]}
        units = {
            (x["component"], x["reason"])
            for x in subset
            if x["component"] and x["reason"]
        }
        comp_curve.append(float(len(comps)))
        reason_curve.append(float(len(reasons)))
        unit_curve.append(float(len(units)))

    return {
        "turns": [float(t) for t in turns],
        "checkpoints": [float(c) for c in checkpoints],
        "components": comp_curve,
        "fault_types": reason_curve,
        "decision_units": unit_curve,
    }


def plot_fig5_0_dataset_overview() -> None:
    out_dir = FIG_ROOT / "fig5-0-dataset-overview"
    _ensure_dir(out_dir)
    stats = collect_dataset_overview()

    labels = [name for _, name in DATASETS]
    cases = [stats[d]["cases"] for d in labels]
    avg_services = [stats[d]["avg_services"] for d in labels]
    fault_types = [stats[d]["fault_type_count"] for d in labels]

    x = np.arange(len(labels))
    width = 0.24

    fig, ax = plt.subplots(figsize=(10, 5.8))
    ax.bar(x - width, cases, width, label="Fault Cases", color="#4C78A8")
    ax.bar(x, avg_services, width, label="Avg Services/Case", color="#59A14F")
    ax.bar(x + width, fault_types, width, label="Fault Types", color="#E15759")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Count")
    ax.set_title("Fig 5-0 Dataset Overview (AIOps-25 / Bank / Market)")
    ax.grid(axis="y", alpha=0.25)
    ax.legend()
    plt.tight_layout()

    fig.savefig(out_dir / "fig5-0-dataset-overview.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(out_dir / "fig5-0-dataset-overview.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    readme = f"""# 图5-0：数据集分布（AIOps-25 / Bank / Market）

## 图表信息
- 类型：分组柱状图
- 指标：Fault Cases、Avg Services/Case、Fault Types
- 数据来源：
  - `/home/yangcx24/Jayx/research/output/aiops25/*/metadata.json`
  - `/home/yangcx24/Jayx/research/output/bank/*/metadata.json`
  - `/home/yangcx24/Jayx/research/output/market/*/metadata.json`

## 统计口径
- Fault Cases：每个数据集目录下 `metadata.json` 文件数量
- Avg Services/Case：`metadata.json.topology_stats.num_services` 的均值
- Fault Types：`metadata.json.anomaly_reason` 去重计数

## 输出文件
- `fig5-0-dataset-overview.pdf`
- `fig5-0-dataset-overview.png`

## 生成时间
- {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    (out_dir / "README.md").write_text(readme, encoding="utf-8")


def plot_fig5_fingerprint_recall_bar() -> None:
    out_dir = FIG_ROOT / "fig5-fingerprint-recall-bar"
    _ensure_dir(out_dir)

    methods, p1 = parse_fingerprint_p1()
    datasets = [name for _, name in DATASETS]
    x = np.arange(len(datasets))
    width = 0.11

    fig, ax = plt.subplots(figsize=(12, 5.8))
    colors = [
        "#4C78A8",
        "#F58518",
        "#54A24B",
        "#E45756",
        "#72B7B2",
        "#B279A2",
        "#FF9DA6",
    ]

    for i, m in enumerate(methods):
        vals = [p1[d].get(m, 0.0) for d in datasets]
        offset = (i - (len(methods) - 1) / 2.0) * width
        ax.bar(x + offset, vals, width=width, label=m.upper(), color=colors[i % len(colors)])

    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.set_ylabel("P@1 (%)")
    ax.set_title("Fig 5 Fingerprint Recall Comparison (P@1)")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(ncol=4, fontsize=9)
    plt.tight_layout()

    fig.savefig(out_dir / "fig5-fingerprint-recall-bar.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(out_dir / "fig5-fingerprint-recall-bar.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    readme = f"""# 图5：故障指纹召回柱状图

## 图表信息
- 类型：分组柱状图
- 指标：P@1（%）
- 数据来源：`/home/yangcx24/Jayx/fpaper/secret/fingerprint_results.md`
- 数据集：AIOps-25、Bank、Market
- 方法：来自表格 `Method` 列（tfidf / metric / art / diagfusion / bwgnn / random / mag）

## 统计口径
- 直接解析 `fingerprint_results.md` 中三个数据集对应表格的 `P@1` 列
- 不引入任何额外人工填写数值

## 输出文件
- `fig5-fingerprint-recall-bar.pdf`
- `fig5-fingerprint-recall-bar.png`

## 生成时间
- {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    (out_dir / "README.md").write_text(readme, encoding="utf-8")


def plot_fig5_3_sop_structure() -> None:
    out_dir = FIG_ROOT / "fig5-3-sop-structure"
    _ensure_dir(out_dir)

    evo = collect_aiops_sop_evolution(num_turns=8)
    turns = np.array(evo["turns"])

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    ax.plot(turns, evo["components"], "o-", color="#4C78A8", linewidth=2, label="Unique Components")
    ax.plot(turns, evo["fault_types"], "s-", color="#F58518", linewidth=2, label="Unique Fault Types")
    ax.plot(turns, evo["decision_units"], "^-", color="#54A24B", linewidth=2, label="Unique (Component, Fault Type) Units")
    ax.set_xticks(turns)
    ax.set_xlabel("Evolution Turn")
    ax.set_ylabel("Count")
    ax.set_title("Fig 5-3 SOP Structure Evolution (AIOps-25 Cumulative)")
    ax.grid(alpha=0.25)
    ax.legend()
    plt.tight_layout()

    fig.savefig(out_dir / "fig5-3-sop-structure.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(out_dir / "fig5-3-sop-structure.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    readme = f"""# 图5-3：SOP结构演进（AIOps-25）

## 图表信息
- 类型：多折线图
- 数据来源：`/home/yangcx24/Jayx/research/output/aiops25/*/metadata.json`
- 维度：
  - Unique Components
  - Unique Fault Types
  - Unique (Component, Fault Type) Units

## 统计口径（可追溯）
- 按 `metadata.json.anomaly_timestamp` 升序排列所有 AIOps-25 样本
- 将累计样本序列等分为 8 个演进 Turn（cumulative checkpoints）
- 每个 Turn 统计：
  - Components：`anomaly_component`（若为空，回退到 `anomaly_id` 前缀）去重计数
  - Fault Types：`anomaly_reason` 去重计数
  - Decision Units：`(component, anomaly_reason)` 组合去重计数

## 输出文件
- `fig5-3-sop-structure.pdf`
- `fig5-3-sop-structure.png`

## 生成时间
- {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    (out_dir / "README.md").write_text(readme, encoding="utf-8")


def main() -> None:
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["axes.unicode_minus"] = False

    plot_fig5_0_dataset_overview()
    plot_fig5_fingerprint_recall_bar()
    plot_fig5_3_sop_structure()
    print("Generated 3 figures for Team-B.")


if __name__ == "__main__":
    main()
