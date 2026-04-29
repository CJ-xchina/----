#!/usr/bin/env python3
"""生成故障指纹检索实验的 MRR 柱状图（面板版）。"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mrr_panel_chart import render_mrr_panel_chart


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


render_mrr_panel_chart(
    section="fingerprint",
    method_order=[
        "TF-IDF",
        "MS-Rank",
        "BWGNN",
        "AnoFusion",
        "ART",
        "DiagFusion",
        "PMF（本文方法）",
    ],
    method_labels={
        "AnoFusion": "AnoFusion",
        "ART": "ART",
        "BWGNN": "BWGNN",
        "TF-IDF": "TF-IDF",
        "MS-Rank": "MS-Rank",
        "DiagFusion": "DiagFusion",
        "PMF（本文方法）": "PMF（本文方法）",
    },
    group_map={
        "AnoFusion": "baseline",
        "ART": "baseline",
        "BWGNN": "baseline",
        "TF-IDF": "baseline",
        "MS-Rank": "baseline",
        "DiagFusion": "baseline",
        "PMF（本文方法）": "ours",
    },
    separators=[],
    highlight_method="PMF（本文方法）",
    xlim=(0, 70),
    xticks=[0, 20, 40, 60],
    figsize=(15.2, 5.6),
    output_base=os.path.join(SCRIPT_DIR, "fig5-fingerprint-mrr-bar"),
)
print("故障指纹检索 MRR 柱状图生成完成！")
