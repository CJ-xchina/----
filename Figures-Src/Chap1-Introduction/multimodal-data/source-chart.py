import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'cpu-chart.png'

rng = np.random.default_rng(20260312)
x = np.arange(0, 101)
base = 46 + 6 * np.sin(x / 3.8) + rng.normal(0, 6.5, size=len(x))
trend = np.piecewise(
    x,
    [x < 18, (x >= 18) & (x < 40), (x >= 40) & (x < 54), (x >= 54) & (x < 67), x >= 67],
    [lambda t: -2 + 0.10 * t,
     lambda t: 1.5 + 0.22 * (t - 18),
     lambda t: 5.0 - 0.15 * (t - 40),
     lambda t: 28 - 0.85 * (t - 54),
     lambda t: -4 + 0.08 * (t - 67)]
)
y = base + trend

# 设计一个更平滑的异常模式：先缓慢抬升，再进入高压平台，随后回落
anomaly_mask = (x >= 47) & (x <= 66)
y[anomaly_mask] += np.array([4, 6, 8, 12, 16, 20, 24, 30, 34, 36, 34, 32, 28, 24, 18, 12, 6, 0, -4, -6])
y = np.clip(y, 18, 96)

font_cn = FontProperties(fname='/home/yangcx24/.fonts/NotoSansSC-Regular.otf')
font_en = FontProperties(fname='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf')

fig = plt.figure(figsize=(5.77, 2.62), dpi=100, facecolor='#ffffff')
ax = fig.add_axes([0.085, 0.12, 0.83, 0.78])
ax.set_facecolor('#ffffff')
ax.plot(x, y, color='blue', lw=1.1, label='CPU 利用率')
ax.axvspan(47, 66, color='#e88d8d', alpha=0.72, label='异常区段')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title('CPU 利用率', fontproperties=font_cn, fontsize=5.0, pad=2)
ax.set_xlabel('时间', fontproperties=font_cn, fontsize=4.2, labelpad=1)
ax.set_ylabel('CPU 利用率 (%)', fontproperties=font_cn, fontsize=4.2, labelpad=1)
ax.tick_params(axis='both', labelsize=4.1, colors='#555555', length=2)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(font_en)
ax.grid(True, color='#9e9e9e', alpha=0.42, linewidth=0.5)
for spine in ax.spines.values():
    spine.set_color('#8c8c8c')
    spine.set_linewidth(0.8)
leg = ax.legend(loc='upper right', fontsize=4.5, frameon=True, borderpad=0.25, handlelength=1.5, prop=font_cn)
leg.get_frame().set_facecolor('#ffffff')
leg.get_frame().set_edgecolor('#c7c7c7')
leg.get_frame().set_linewidth(0.8)

fig.savefig(OUT, facecolor=fig.get_facecolor(), dpi=100)
print(OUT)
print(OUT.stat().st_size)
