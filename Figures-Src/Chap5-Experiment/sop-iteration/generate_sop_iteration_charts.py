#!/usr/bin/env python3
"""生成SOP构建迭代过程关键指标变化图（优化版 - 中文标签，大字体）"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# 添加父目录到路径以导入样式配置
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plot_style import setup_plot_style, METRIC_COLORS, save_figure, style_axes

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 设置统一样式
setup_plot_style()

# 实验数据（20轮迭代）
turns = list(range(1, 21))

# 关键指标数据
escape_rate = [87.5, 82.3, 78.1, 65.4, 58.7, 52.3, 45.8, 38.2, 32.5, 28.7,
               22.3, 18.5, 15.2, 12.8, 9.5, 7.2, 6.5, 5.8, 5.2, 5.0]

lasso_success_rate = [18.5, 22.3, 25.8, 32.5, 38.2, 42.8, 48.5, 52.3, 58.7, 62.5,
                      68.2, 72.5, 75.8, 78.2, 80.5, 81.2, 80.8, 81.5, 80.2, 80.8]

diagnosis_success_rate = [0.0, 0.0, 0.0, 12.5, 18.2, 25.8, 32.5, 45.2, 52.8, 58.5,
                         62.5, 68.2, 72.5, 75.8, 72.5, 78.2, 75.5, 78.8, 75.2, 76.5]

exploration_tool_calls = [256, 248, 235, 228, 215, 205, 192, 185, 175, 168,
                          158, 152, 145, 142, 138, 135, 132, 128, 125, 122]

diagnosis_tool_calls = [0, 0, 0, 32, 48, 56, 62, 68, 72, 78,
                       82, 85, 88, 90, 92, 94, 95, 96, 97, 98]

sop_nodes = [1, 3, 6, 10, 15, 21, 28, 35, 42, 48,
             53, 57, 60, 62, 63, 64, 64, 65, 65, 65]

sop_edges = [0, 2, 5, 9, 14, 20, 27, 34, 41, 47,
             52, 56, 59, 61, 62, 63, 63, 64, 64, 64]

completion_rate = [35.2, 42.5, 48.5, 55.2, 62.5, 68.2, 72.5, 78.5, 82.5, 85.2,
                  88.5, 90.2, 92.5, 95.2, 96.5, 98.2, 97.5, 98.5, 98.2, 99.5]

# 创建2x2子图
fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# ========== 子图(a): 成功率指标 ==========
ax1 = axes[0, 0]
ax1.plot(turns, escape_rate, 'o-', label='逃逸率',
         color=METRIC_COLORS['escape_rate'], linewidth=2.5, markersize=7)
ax1.plot(turns, lasso_success_rate, 's-', label='探索成功率',
         color=METRIC_COLORS['success_rate'], linewidth=2.5, markersize=7)
ax1.plot(turns, diagnosis_success_rate, '^-', label='诊断成功率',
         color=METRIC_COLORS['diagnosis_rate'], linewidth=2.5, markersize=7)

ax1.set_xlabel('迭代轮次')
ax1.set_ylabel('比率 (%)')
ax1.set_title('(a) 成功率', fontsize=15, fontweight='bold', pad=8)
ax1.set_xticks(turns)
ax1.set_xticklabels([str(t) if t % 2 == 1 else '' for t in turns], fontsize=11)
ax1.legend(loc='center right', fontsize=11)
ax1.set_ylim(0, 100)
style_axes(ax1, grid_axis='y')

# ========== 子图(b): 工具调用次数 ==========
ax2 = axes[0, 1]
ax2.plot(turns, exploration_tool_calls, 'o-', label='探索工具调用',
         color=METRIC_COLORS['diagnosis_rate'], linewidth=2.5, markersize=7)
ax2.plot(turns, diagnosis_tool_calls, 's-', label='诊断工具调用',
         color=METRIC_COLORS['escape_rate'], linewidth=2.5, markersize=7)

ax2.set_xlabel('迭代轮次')
ax2.set_ylabel('工具调用次数')
ax2.set_title('(b) 工具调用', fontsize=15, fontweight='bold', pad=8)
ax2.set_xticks(turns)
ax2.set_xticklabels([str(t) if t % 2 == 1 else '' for t in turns], fontsize=11)
ax2.legend(loc='upper right', fontsize=11)
style_axes(ax2, grid_axis='y')

# ========== 子图(c): SOP结构演进 ==========
ax3 = axes[1, 0]
ax3.plot(turns, sop_nodes, 'o-', label='SOP节点数',
         color=METRIC_COLORS['nodes'], linewidth=2.5, markersize=7)
ax3.plot(turns, sop_edges, 's-', label='SOP边数',
         color=METRIC_COLORS['edges'], linewidth=2.5, markersize=7)

ax3.set_xlabel('迭代轮次')
ax3.set_ylabel('数量')
ax3.set_title('(c) SOP结构', fontsize=15, fontweight='bold', pad=8)
ax3.set_xticks(turns)
ax3.set_xticklabels([str(t) if t % 2 == 1 else '' for t in turns], fontsize=11)
ax3.legend(loc='upper left', fontsize=11)
style_axes(ax3, grid_axis='y')

# ========== 子图(d): 任务完成率 ==========
ax4 = axes[1, 1]
ax4.plot(turns, completion_rate, 'd-', label='任务完成率',
         color=METRIC_COLORS['completion_rate'], linewidth=2.5, markersize=7)

ax4.set_xlabel('迭代轮次')
ax4.set_ylabel('比率 (%)')
ax4.set_title('(d) 任务完成率', fontsize=15, fontweight='bold', pad=8)
ax4.set_xticks(turns)
ax4.set_xticklabels([str(t) if t % 2 == 1 else '' for t in turns], fontsize=11)
ax4.legend(loc='lower right', fontsize=11)
ax4.set_ylim(0, 110)
style_axes(ax4, grid_axis='y')

plt.tight_layout()
save_figure(os.path.join(SCRIPT_DIR, 'fig5-sop-iteration-metrics'))
print("SOP构建迭代指标图生成完成！")
