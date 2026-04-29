#!/usr/bin/env python3
"""
生成超参数敏感性分析柱状图
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
import matplotlib
matplotlib.use('Agg')
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style import (
    HIGHLIGHT_BG,
    RANK_METRIC_COLORS,
    add_value_labels,
    highlight_bar,
    setup_plot_style,
    style_axes,
    style_top_legend,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 设置中文字体 - 使用绝对路径
font_path = '/home/yangcx24/.fonts/NotoSansSC-Regular.otf'
font_manager.fontManager.addfont(font_path)

setup_plot_style()

# 数据
k_values = [50, 100, 150, 200, 250, 300]
k_p1 = [52.17, 58.70, 61.59, 64.88, 63.04, 60.87]
k_p3 = [71.74, 76.81, 79.35, 82.76, 81.52, 78.26]

alpha_values = [0.10, 0.15, 0.20, 0.25, 0.30]
alpha_p1 = [58.70, 61.59, 64.88, 62.32, 59.78]
alpha_p3 = [77.17, 79.35, 82.76, 80.43, 78.26]

l_values = [3, 5, 10, 15, 20]
l_p1 = [56.52, 60.87, 64.88, 62.32, 59.78]
l_p3 = [75.00, 78.26, 82.76, 80.43, 78.26]

fig, axes = plt.subplots(1, 3, figsize=(15.8, 4.9), sharey=True)
bar_w = 0.34


def draw_grouped_bars(ax, x_labels, p1, p3, title, xlabel, best_idx):
    x = np.arange(len(x_labels))
    ax.axvspan(best_idx - 0.52, best_idx + 0.52, color=HIGHLIGHT_BG, zorder=0)
    bars_p1 = ax.bar(
        x - bar_w / 2, p1, width=bar_w,
        color=RANK_METRIC_COLORS['P@1'], label='P@1',
        edgecolor='none', zorder=2
    )
    bars_p3 = ax.bar(
        x + bar_w / 2, p3, width=bar_w,
        color=RANK_METRIC_COLORS['P@3'], label='P@3',
        edgecolor='none', zorder=2
    )
    highlight_bar(bars_p1[best_idx], linewidth=1.4)
    highlight_bar(bars_p3[best_idx], linewidth=1.4)
    add_value_labels(ax, [bars_p1[best_idx]], fontsize=10)
    add_value_labels(ax, [bars_p3[best_idx]], fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.set_xlabel(xlabel, fontsize=11.5)
    ax.set_title(title, fontsize=13, fontweight='semibold')
    style_axes(ax, grid_axis='y')
    ax.set_ylim([50, 90])
    ax.set_yticks([50, 60, 70, 80, 90])
    return bars_p1, bars_p3


bars1, bars2 = draw_grouped_bars(
    axes[0], k_values, k_p1, k_p3,
    '(a) 特征维度 K', 'K', k_values.index(200)
)
draw_grouped_bars(
    axes[1], alpha_values, alpha_p1, alpha_p3,
    '(b) 阻尼系数 $\\alpha$', r'$\alpha$', alpha_values.index(0.20)
)
draw_grouped_bars(
    axes[2], l_values, l_p1, l_p3,
    '(c) 滞后窗口 L', 'L', l_values.index(10)
)

axes[1].tick_params(labelleft=False)
axes[2].tick_params(labelleft=False)

fig.supylabel('Precision (%)', x=0.015, fontsize=12.5)
style_top_legend(fig, [bars1[0], bars2[0]], ['P@1', 'P@3'], ncol=2, y=1.02, fontsize=12)
plt.subplots_adjust(left=0.055, right=0.995, top=0.82, bottom=0.19, wspace=0.14)

# 保存
output_path = os.path.join(SCRIPT_DIR, 'chart.pdf')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved to: {output_path}")

# 保存PNG
output_png = os.path.join(SCRIPT_DIR, 'chart.png')
plt.savefig(output_png, dpi=180, bbox_inches='tight')
print(f"Saved to: {output_png}")
