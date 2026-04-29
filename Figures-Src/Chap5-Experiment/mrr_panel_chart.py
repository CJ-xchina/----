#!/usr/bin/env python3
"""Shared helpers for Chapter 5 MRR panel charts."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

from plot_style import (
    DATASET_COLORS,
    HIGHLIGHT_BG,
    METHOD_COLORS,
    save_figure,
    setup_plot_style,
    style_axes,
)
from simulated_results_loader import load_results


DATASETS = ("AIOps-25", "Bank", "Market")
BASELINE_NEUTRAL = "#A8B0BB"
LLM_BASELINE = "#6E86B5"


def render_mrr_panel_chart(
    *,
    section: str,
    method_order: list[str],
    method_labels: dict[str, str],
    group_map: dict[str, str],
    separators: list[float],
    highlight_method: str,
    xlim: tuple[float, float],
    xticks: list[float],
    figsize: tuple[float, float],
    output_base: str,
) -> None:
    setup_plot_style()
    results = load_results()[section]

    y = np.arange(len(method_order))
    fig, axes = plt.subplots(1, len(DATASETS), figsize=figsize, sharey=True)
    if not isinstance(axes, np.ndarray):
        axes = np.array([axes])

    color_map = {
        "baseline": BASELINE_NEUTRAL,
        "traditional": METHOD_COLORS["traditional"],
        "llm": LLM_BASELINE,
        "ours": METHOD_COLORS["ours"],
    }

    for axis_index, (ax, dataset) in enumerate(zip(axes, DATASETS)):
        values = [results[method][dataset]["avg_metrics"]["mrr"] for method in method_order]
        colors = [color_map[group_map[method]] for method in method_order]

        guide_index = method_order.index(highlight_method)
        ax.axhspan(guide_index - 0.48, guide_index + 0.48, color=HIGHLIGHT_BG, zorder=0)
        bars = ax.barh(
            y,
            values,
            height=0.68,
            color=colors,
            edgecolor="white",
            linewidth=0.8,
            zorder=2,
        )
        bars[guide_index].set_edgecolor("#334155")
        bars[guide_index].set_linewidth(1.4)

        for boundary in separators:
            ax.axhline(boundary, color="#D1D5DB", linewidth=1.0, zorder=1)

        label_offset = 0.8
        for bar, method, value in zip(bars, method_order, values):
            ax.text(
                value + label_offset,
                bar.get_y() + bar.get_height() / 2,
                f"{value:.1f}",
                va="center",
                ha="left",
                fontsize=10.2,
                fontweight="semibold" if method == highlight_method else "normal",
                color="#111827",
                clip_on=False,
            )

        ax.set_title(dataset, color=DATASET_COLORS[dataset], pad=10, fontweight="semibold")
        ax.set_xlim(*xlim)
        ax.set_xticks(xticks)
        ax.set_xlabel("MRR (%)")
        ax.set_axisbelow(True)
        style_axes(ax, grid_axis="x")
        ax.tick_params(axis="y", length=0)
        ax.invert_yaxis()

        if axis_index == 0:
            labels = [method_labels[method] for method in method_order]
            ax.set_yticks(y)
            ax.set_yticklabels(labels)
            ax.tick_params(axis="y", labelleft=True, pad=6)
            ax.get_yticklabels()[-1].set_fontweight("semibold")
            ax.get_yticklabels()[-1].set_color(METHOD_COLORS["ours"])
        else:
            ax.tick_params(axis="y", labelleft=False)

    legend_groups = []
    for group in ("baseline", "traditional", "llm", "ours"):
        if group in group_map.values():
            legend_groups.append(group)

    legend_labels = {
        "baseline": "Baselines",
        "traditional": "Traditional",
        "llm": "LLM-based",
        "ours": "本文方法",
    }
    handles = [Patch(facecolor=color_map[group], edgecolor="none") for group in legend_groups]
    labels = [legend_labels[group] for group in legend_groups]
    fig.legend(
        handles,
        labels,
        loc="upper center",
        bbox_to_anchor=(0.5, 1.01),
        ncol=len(handles),
        frameon=False,
        fontsize=11.5,
        handlelength=1.4,
        columnspacing=1.8,
    )
    fig.subplots_adjust(left=0.23, right=0.985, top=0.83, bottom=0.1, wspace=0.11)
    save_figure(output_base)
    plt.close(fig)
