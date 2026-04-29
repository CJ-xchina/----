#!/usr/bin/env python3
"""生成图5-4：SOP 构建迭代指标与结构变化图"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# 添加父目录到路径以导入样式配置
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style import setup_plot_style, METRIC_COLORS, save_figure, style_axes
from simulated_results_loader import load_sop_iteration

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 设置统一样式
setup_plot_style()

sop_data = load_sop_iteration()
turns = sop_data["turns"]
escape_rate = sop_data["escape_rate"]
exploration_success_rate = sop_data["exploration_success_rate"]
diagnosis_success_rate = sop_data["diagnosis_success_rate"]
completion_rate = sop_data["completion_rate"]
sop_nodes = sop_data["sop_nodes"]
sop_edges = sop_data["sop_edges"]

# 创建1x2子图
fig, axes = plt.subplots(1, 2, figsize=(15.6, 5.9))

# ========== 子图(a): 指标变化 ==========
ax1 = axes[0]
ax1.plot(turns, escape_rate, 'o-', label='逃逸率',
         color=METRIC_COLORS['escape_rate'], linewidth=2.5, markersize=7)
ax1.plot(turns, exploration_success_rate, 's-', label='探索成功率',
         color=METRIC_COLORS['success_rate'], linewidth=2.5, markersize=7)
ax1.plot(turns, diagnosis_success_rate, '^-', label='诊断成功率',
         color=METRIC_COLORS['diagnosis_rate'], linewidth=2.5, markersize=7)
ax1.plot(turns, completion_rate, 'd-', label='任务完成率',
         color=METRIC_COLORS['completion_rate'], linewidth=2.5, markersize=7)

ax1.set_xlabel('迭代轮次')
ax1.set_ylabel('比率 (%)')
ax1.set_title('(a) 关键指标变化', fontsize=15, fontweight='bold', pad=8)
ax1.set_xticks(turns)
ax1.set_xticklabels([str(t) if t % 2 == 1 else '' for t in turns], fontsize=11)
ax1.legend(loc='center right', fontsize=10.5)
ax1.set_ylim(0, 100)
style_axes(ax1, grid_axis='y')

# ========== 子图(b): SOP结构变化 ==========
ax2 = axes[1]
ax2.plot(turns, sop_nodes, 'o-', label='平均SOP节点数',
         color=METRIC_COLORS['nodes'], linewidth=2.5, markersize=7)
ax2.plot(turns, sop_edges, 's-', label='平均SOP边数',
         color=METRIC_COLORS['edges'], linewidth=2.5, markersize=7)

ax2.set_xlabel('迭代轮次')
ax2.set_ylabel('数量')
ax2.set_title('(b) SOP 结构变化', fontsize=15, fontweight='bold', pad=8)
ax2.set_xticks(turns)
ax2.set_xticklabels([str(t) if t % 2 == 1 else '' for t in turns], fontsize=11)
ax2.legend(loc='upper left', fontsize=11)
style_axes(ax2, grid_axis='y')

plt.tight_layout()
save_figure(os.path.join(SCRIPT_DIR, 'chart'))
print("图5-4已生成。")
