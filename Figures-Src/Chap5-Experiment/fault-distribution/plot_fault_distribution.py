#!/usr/bin/env python3
"""生成三个数据集的故障类型分布对比图（三个横向排列的精致学术风格饼状图）"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style import setup_plot_style, PIE_COLORS, style_bottom_legend

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

setup_plot_style()

fault_types_full = [
    'CPU故障', '内存故障', '网络故障', '磁盘I/O故障',
    'JVM故障', '应用故障', '容器故障', '配置故障'
]

aiops25 = [14.5, 14.5, 23.5, 12.0, 8.5, 6.0, 15.0, 6.0]
bank = [26.5, 8.8, 43.4, 17.6, 0.0, 0.0, 0.0, 3.7]
market = [17.6, 10.8, 28.4, 34.5, 0.0, 5.4, 0.0, 3.3]

colors = PIE_COLORS


def filter_zero_data(types, data):
    filtered_items = []
    for t, d, c in zip(types, data, colors):
        if d > 0:
            filtered_items.append((t, d, c))
    filtered_items.sort(key=lambda item: item[1], reverse=True)
    filtered_types = [item[0] for item in filtered_items]
    filtered_data = [item[1] for item in filtered_items]
    filtered_colors = [item[2] for item in filtered_items]
    return filtered_types, filtered_data, filtered_colors


def annotate_pie(ax, wedges, data):
    for wedge, value in zip(wedges, data):
        angle = np.deg2rad((wedge.theta1 + wedge.theta2) / 2.0)
        x = np.cos(angle)
        y = np.sin(angle)
        text = f'{value:.1f}%'
        if value >= 8.0:
            ax.text(
                0.69 * x, 0.69 * y, text,
                ha='center', va='center',
                fontsize=13.2, fontweight='semibold', color='#111827'
            )
        else:
            line_x = [0.96 * x, 1.05 * x]
            line_y = [0.96 * y, 1.05 * y]
            text_x = 1.18 * x
            text_y = 1.14 * y
            ax.plot(line_x, line_y, color='#9CA3AF', linewidth=0.9)
            ax.text(
                text_x, text_y, text,
                ha='left' if x >= 0 else 'right',
                va='center',
                fontsize=12.4, fontweight='semibold', color='#111827'
            )


def draw_pie(ax, title, types, data, cols):
    wedges, _ = ax.pie(
        data,
        labels=None,
        colors=cols,
        startangle=90,
        radius=1.12,
        counterclock=False,
        wedgeprops={'linewidth': 1.3, 'edgecolor': 'white', 'joinstyle': 'round'}
    )
    annotate_pie(ax, wedges, data)
    ax.set_title(title, fontsize=15.5, fontweight='semibold', pad=14, color='#111827')
    ax.set_aspect('equal')
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    return wedges


types1, data1, cols1 = filter_zero_data(fault_types_full, aiops25)
types2, data2, cols2 = filter_zero_data(fault_types_full, bank)
types3, data3, cols3 = filter_zero_data(fault_types_full, market)

# 横向布局，保留统一图例
fig, axes = plt.subplots(1, 3, figsize=(18.2, 7.1))
fig.patch.set_facecolor('white')

wedges1 = draw_pie(axes[0], '(a) AIOps-25', types1, data1, cols1)
wedges2 = draw_pie(axes[1], '(b) Bank', types2, data2, cols2)
wedges3 = draw_pie(axes[2], '(c) Market', types3, data3, cols3)

# 统一图例
legend_handles = [Patch(facecolor=c, edgecolor='none', label=t) for t, c in zip(fault_types_full, colors)]
style_bottom_legend(fig, legend_handles, fault_types_full, ncol=4, y=-0.03, fontsize=12.6)

plt.subplots_adjust(left=0.03, right=0.99, top=0.90, bottom=0.23, wspace=0.14)

output_path = os.path.join(SCRIPT_DIR, 'chart.pdf')
plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0.15)
print(f"Saved to: {output_path}")

output_png = os.path.join(SCRIPT_DIR, 'chart.png')
plt.savefig(output_png, dpi=220, bbox_inches='tight', pad_inches=0.15)
print(f"Saved to: {output_png}")
