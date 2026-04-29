# 微服务故障诊断多模态数据示意

## 用途
- 对应第1章引言中的插图：微服务故障诊断多模态数据示意。
- LaTeX 引用路径：`Figures-Src/Chap1-Introduction/多模态数据/chart.pdf`。

## 文件说明
- `source.drawio`：主图的 draw.io 可编辑源文件。
- `source-chart.py`：生成左下角 CPU 指标子图的 Python 脚本。
- `source-diagram.py`：生成 draw.io 源文件的 Python 脚本。
- `cpu-chart.png`：由 Python 代码生成的 CPU 指标子图，不是从参考图直接裁剪。
- `chart.png` / `chart.pdf`：导出的最终图。

## 说明
- 除左下角 CPU 指标子图外，其余元素均为 draw.io 原生可编辑组件重绘。
- CPU 指标子图由 Python 代码生成后嵌入 draw.io。
- 当前版本已将 CPU 异常模式、调用链示例、日志示例和 Trace 时间线示例替换为新的合成内容，避免照搬参考图中的具体案例。
