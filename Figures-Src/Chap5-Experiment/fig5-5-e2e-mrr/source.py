#!/usr/bin/env python3
"""生成图5-5：端到端诊断任务的 MRR 对比图。"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mrr_panel_chart import render_mrr_panel_chart


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


render_mrr_panel_chart(
    section="e2e",
    method_order=[
        "TF-IDF",
        "MS-Rank",
        "BWGNN",
        "AnoFusion",
        "ART",
        "DiagFusion",
        "OpenRCA",
        "ReAct",
        "RCAgent",
        "mABC",
        "Flow-of-Action",
        "本文方法",
    ],
    method_labels={
        "AnoFusion": "AnoFusion",
        "ART": "ART",
        "OpenRCA": "OpenRCA\n(RCA-agent)",
        "TF-IDF": "TF-IDF",
        "BWGNN": "BWGNN",
        "MS-Rank": "MS-Rank",
        "DiagFusion": "DiagFusion",
        "ReAct": "ReAct",
        "RCAgent": "RCAgent",
        "mABC": "mABC",
        "Flow-of-Action": "Flow-of-Action",
        "本文方法": "本文方法",
    },
    group_map={
        "AnoFusion": "traditional",
        "ART": "traditional",
        "TF-IDF": "traditional",
        "BWGNN": "traditional",
        "MS-Rank": "traditional",
        "DiagFusion": "traditional",
        "OpenRCA": "llm",
        "ReAct": "llm",
        "RCAgent": "llm",
        "mABC": "llm",
        "Flow-of-Action": "llm",
        "本文方法": "ours",
    },
    separators=[5.5, 10.5],
    highlight_method="本文方法",
    xlim=(0, 80),
    xticks=[0, 20, 40, 60, 80],
    figsize=(16.4, 7.1),
    output_base=os.path.join(SCRIPT_DIR, "chart"),
)
print("图5-5已生成。")
