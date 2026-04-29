# 图5-2 三个数据集的故障类型分布对比

## 图表说明

本图展示三个数据集（AIOps-25、Bank、Market）的故障类型分布情况，采用聚类后的8大类故障类型进行展示。

## 聚类方案

将原始故障类型聚类为以下8大类：

| 聚类类别 | 包含的原始故障类型 |
|---------|------------------|
| **CPU故障** | cpu stress, node cpu stress, jvm cpu, high CPU usage, container CPU load, node CPU load 等 |
| **内存故障** | memory stress, node memory stress, high memory usage, JVM OOM, container memory load 等 |
| **网络故障** | network delay, network loss, network corrupt, dns error, network latency, packet loss 等 |
| **磁盘I/O故障** | io fault, node disk fill, high disk I/O, disk space consumption 等 |
| **JVM故障** | jvm latency, jvm gc, jvm exception |
| **应用故障** | code error |
| **容器故障** | pod failure, pod kill, container process termination |
| **配置故障** | target port misconfig |

## 数据统计

| 数据集 | 主要故障类型 |
|--------|-------------|
| AIOps-25 | 网络故障(23.5%)、容器故障(15.0%)、CPU/内存故障(各14.5%) |
| Bank | 网络故障(43.4%)、CPU故障(26.5%)、磁盘I/O故障(17.6%) |
| Market | 磁盘I/O故障(34.5%)、网络故障(28.4%)、CPU故障(17.6%) |

## 引用位置

第5章 实验设置 - 5.2 实验设置

## 文件列表

- `README.md`: 本文件
- `plot_fault_distribution.py`: 绘图脚本
- `chart.png`: PNG 格式导出
- `chart.pdf`: PDF 矢量格式导出（推荐用于 LaTeX）
