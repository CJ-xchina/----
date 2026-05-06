#!/usr/bin/env python3
"""Generate diagnosis cost analysis chart for Chapter 5."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.size'] = 10

output_dir = os.path.dirname(os.path.abspath(__file__))
cost_dir = os.path.join(output_dir, 'diagnosis-cost')
os.makedirs(cost_dir, exist_ok=True)

datasets = ['AIOps-25', 'Bank', 'Market']

# Time breakdown in seconds
# Fingerprint | SOP Recall | LLM Reasoning & Tool Calls
time_data = {
    'AIOps-25': [12.8, 0.87, 277.33],
    'Bank':      [11.4, 0.73, 254.87],
    'Market':    [14.6, 0.94, 302.46],
}

fig, ax = plt.subplots(figsize=(8, 5))

x = np.arange(len(datasets))
width = 0.5
bottoms = np.zeros(len(datasets))
colors = ['#2E75B6', '#ED7D31', '#FFC000']
stage_labels = ['Fingerprint Construction', 'SOP Recall', 'LLM Reasoning & Tool Calls']

for i, (label, color) in enumerate(zip(stage_labels, colors)):
    values = [time_data[ds][i] for ds in datasets]
    bars = ax.bar(x, values, width, bottom=bottoms, color=color, label=label, edgecolor='white', linewidth=0.5)
    # Annotate fingerprint and total values
    if i == 0:
        for j, (bar, ds) in enumerate(zip(bars, datasets)):
            total = sum(time_data[ds])
            ax.text(bar.get_x() + bar.get_width()/2., total + 8,
                    f'{total:.0f}s', ha='center', va='bottom', fontsize=9, fontweight='bold')
    bottoms += np.array(values)

ax.set_ylabel('Time (s)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(datasets, fontsize=11)
ax.set_title('End-to-End Diagnosis Time Breakdown', fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(cost_dir, 'chart.pdf'), dpi=150, bbox_inches='tight')
plt.close()
print(f'Saved: {cost_dir}/chart.pdf')
