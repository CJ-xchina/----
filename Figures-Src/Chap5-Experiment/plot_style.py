#!/usr/bin/env python3
"""统一的图表样式配置 - 第五章实验图表"""

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# ============================================
# 字体配置
# ============================================

# 设置中文字体（优先使用系统中文字体）
def setup_chinese_font():
    """配置中文字体支持"""
    # 尝试多个中文字体
    chinese_fonts = [
        'Source Han Sans SC',   # 思源黑体
        'Noto Sans CJK SC',     # 思源黑体
        'SimHei',           # 黑体
        'Microsoft YaHei',  # 微软雅黑
        'STSong',           # 华文宋体
        'STHeiti',          # 华文黑体
        'WenQuanYi Micro Hei',  # 文泉驿微米黑
    ]

    available_fonts = [f.name for f in font_manager.fontManager.ttflist]

    # 尝试找到可用的中文字体
    font_found = False
    for font in chinese_fonts:
        if font in available_fonts:
            matplotlib.rcParams['font.sans-serif'] = [font, 'DejaVu Sans']
            print(f"使用中文字体: {font}")
            font_found = True
            break

    # 如果没找到，尝试直接使用字体文件
    if not font_found:
        try:
            # 尝试加载用户目录下的字体
            font_path = '/home/yangcx24/.fonts/NotoSansSC-Regular.otf'
            if os.path.exists(font_path):
                from matplotlib.font_manager import FontProperties
                font_manager.fontManager.addfont(font_path)
                matplotlib.rcParams['font.sans-serif'] = ['Source Han Sans SC', 'DejaVu Sans']
                print(f"使用中文字体文件: {font_path}")
                font_found = True
        except Exception as e:
            print(f"加载字体文件失败: {e}")

    if not font_found:
        print("警告: 未找到中文字体，使用默认字体")
        matplotlib.rcParams['font.sans-serif'] = ['DejaVu Sans']

    # 解决负号显示问题
    matplotlib.rcParams['axes.unicode_minus'] = False

# ============================================
# 全局样式配置
# ============================================

def setup_plot_style():
    """设置统一的绘图样式"""
    setup_chinese_font()

    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42

    # 统一为白底学术风格
    matplotlib.rcParams['figure.facecolor'] = 'white'
    matplotlib.rcParams['axes.facecolor'] = 'white'
    matplotlib.rcParams['axes.edgecolor'] = '#6B7280'
    matplotlib.rcParams['text.color'] = '#111827'
    matplotlib.rcParams['axes.labelcolor'] = '#111827'
    matplotlib.rcParams['xtick.color'] = '#374151'
    matplotlib.rcParams['ytick.color'] = '#374151'

    # 字体大小配置
    matplotlib.rcParams['font.size'] = 12.5
    matplotlib.rcParams['axes.titlesize'] = 14.5
    matplotlib.rcParams['axes.labelsize'] = 12.5
    matplotlib.rcParams['xtick.labelsize'] = 11.5
    matplotlib.rcParams['ytick.labelsize'] = 11.5
    matplotlib.rcParams['legend.fontsize'] = 11.5

    # 线条和标记配置
    matplotlib.rcParams['lines.linewidth'] = 2.1
    matplotlib.rcParams['lines.markersize'] = 6.5

    # 图表边框和网格
    matplotlib.rcParams['axes.linewidth'] = 1.0
    matplotlib.rcParams['grid.linewidth'] = 0.85
    matplotlib.rcParams['grid.alpha'] = 1.0
    matplotlib.rcParams['grid.color'] = '#E5E7EB'

    # 刻度配置
    matplotlib.rcParams['xtick.major.width'] = 1.0
    matplotlib.rcParams['ytick.major.width'] = 1.0
    matplotlib.rcParams['xtick.major.size'] = 4.5
    matplotlib.rcParams['ytick.major.size'] = 4.5

    # 图例配置
    matplotlib.rcParams['legend.frameon'] = False
    matplotlib.rcParams['legend.framealpha'] = 1.0
    matplotlib.rcParams['legend.edgecolor'] = '#D1D5DB'
    matplotlib.rcParams['legend.facecolor'] = 'white'

    # 保存配置
    matplotlib.rcParams['savefig.dpi'] = 300
    matplotlib.rcParams['savefig.bbox'] = 'tight'
    matplotlib.rcParams['savefig.pad_inches'] = 0.1

# ============================================
# 颜色方案
# ============================================

# 主色调（用于不同数据集）
DATASET_COLORS = {
    'AIOps-25': '#4E79A7',
    'Bank': '#E15759',
    'Market': '#59A14F',
}

# 方法类型颜色
METHOD_COLORS = {
    'traditional': '#A0A4A8',
    'llm': '#4E79A7',
    'ours': '#D1495B',
}

# 指标颜色（用于多指标对比）
METRIC_COLORS = {
    'escape_rate': '#D1495B',
    'success_rate': '#2E8B57',
    'diagnosis_rate': '#4E79A7',
    'completion_rate': '#8E6BBE',
    'nodes': '#D08C3F',
    'edges': '#4FA3A5',
}

PIE_COLORS = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2',
              '#59A14F', '#EDC948', '#B07AA1', '#9C755F']

RANK_METRIC_COLORS = {
    'P@1': '#4E79A7',
    'P@3': '#F28E2B',
}

HIGHLIGHT_BG = '#F6F2E8'

# ============================================
# 辅助函数
# ============================================

def add_value_labels(ax, bars, rotation=0, fontsize=11):
    """在柱状图上添加数值标签"""
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.annotate(f'{height:.1f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom',
                       fontsize=fontsize,
                       rotation=rotation,
                       color='#111827',
                       fontweight='semibold')

def highlight_bar(bar, color='#334155', linewidth=1.8):
    """高亮显示特定柱子"""
    bar.set_edgecolor(color)
    bar.set_linewidth(linewidth)

def save_figure(filename_base):
    """保存图表为PDF和PNG格式"""
    plt.savefig(f'{filename_base}.pdf', dpi=300, bbox_inches='tight')
    plt.savefig(f'{filename_base}.png', dpi=300, bbox_inches='tight', facecolor='white')
    print(f"图表已保存: {filename_base}.pdf 和 {filename_base}.png")


def style_axes(ax, grid_axis='y'):
    """统一坐标轴样式"""
    ax.set_axisbelow(True)
    ax.grid(axis=grid_axis, linestyle='-', linewidth=0.85, color='#E5E7EB')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#6B7280')
    ax.spines['bottom'].set_color('#6B7280')
    ax.spines['left'].set_linewidth(1.0)
    ax.spines['bottom'].set_linewidth(1.0)


def style_bottom_legend(fig, handles, labels, ncol=4, y=0.01, fontsize=13):
    """统一底部图例样式"""
    return fig.legend(
        handles, labels,
        loc='lower center',
        bbox_to_anchor=(0.5, y),
        ncol=ncol,
        frameon=False,
        fontsize=fontsize,
        labelspacing=1.0,
        handlelength=1.2,
        handletextpad=0.6,
        borderpad=0.0,
        columnspacing=1.6
    )


def style_top_legend(fig, handles, labels, ncol=3, y=1.02, fontsize=12):
    """统一顶部图例样式"""
    return fig.legend(
        handles, labels,
        loc='upper center',
        bbox_to_anchor=(0.5, y),
        ncol=ncol,
        frameon=False,
        fontsize=fontsize,
        labelspacing=0.8,
        handlelength=1.2,
        handletextpad=0.6,
        borderpad=0.0,
        columnspacing=1.6
    )

# ============================================
# 中文标签映射
# ============================================

# 方法名称中英文映射
METHOD_NAMES_CN = {
    'TF-IDF': 'TF-IDF',
    'Metric': 'Metric',
    'ART': 'ART',
    'DiagFusion': 'DiagFusion',
    'BWGNN': 'BWGNN',
    'Random': '随机',
    'MAG': 'MAG',
    'PMF': 'PMF（本文）',
    'CHASE': 'CHASE',
    'CIRCA': 'CIRCA',
    'PageRank': 'PageRank',
    'Flow-of-Action': 'Flow-of-Action',
    'ReAct': 'ReAct',
    'RCAgent': 'RCAgent',
    'mABC': 'mABC',
    'OpenRCA': 'OpenRCA (RCA-agent)',
    'Ours': '本文方法',
}

# 数据集名称
DATASET_NAMES_CN = {
    'AIOps-25': 'AIOps-25',
    'Bank': 'Bank',
    'Market': 'Market',
}

# 指标名称
METRIC_NAMES_CN = {
    'P@1': 'P@1 (%)',
    'P@3': 'P@3 (%)',
    'P@5': 'P@5 (%)',
    'MRR': 'MRR (%)',
    'Escape Rate': '逃逸率 (%)',
    'Success Rate': '成功率 (%)',
    'Diagnosis Rate': '诊断成功率 (%)',
    'Completion Rate': '任务完成率 (%)',
    'Tool Calls': '工具调用次数',
    'Nodes': '节点数',
    'Edges': '边数',
    'Iteration Turn': '迭代轮次',
    'Methods': '方法',
    'Rate': '比率 (%)',
    'Count': '数量',
}

if __name__ == '__main__':
    # 测试样式配置
    setup_plot_style()

    # 创建测试图表
    fig, ax = plt.subplots(figsize=(10, 6))
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 30]
    ax.plot(x, y, 'o-', label='测试数据')
    ax.set_xlabel('X轴标签')
    ax.set_ylabel('Y轴标签')
    ax.set_title('样式测试图表')
    ax.legend()
    ax.grid(True)

    save_figure('test_style')
    print("样式配置测试完成！")
