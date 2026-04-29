# 基于假设驱动验证的诊断轨迹生成流程

## 基本信息

- **图表编号**：第3章方法论插图
- **图表类型**：流程图
- **工具**：drawio MCP
- **创建时间**：2026-03-02

## 用途

展示离线进化域中诊断轨迹的生成流程，核心流程为：

1. **输入**：故障注入场景 + 故障类型标签（先验知识）
2. **探索智能体**：接收先验知识，采用假设驱动验证模式
3. **六维度验证框架**：目标组件自检、上游影响分析、下游影响分析、同节点关联分析、K8s资源检查、排他性验证
4. **多轮Rollout推演**：生成多条诊断轨迹
5. **关键路径标记**：从完整轨迹精炼为关键步骤
6. **轨迹质量分类**：NE+S, E+S, NE+F, E+F, 错误
7. **输出**：带关键路径标记的高质量诊断轨迹

## 引用位置

第3章 基于大语言模型的微服务故障诊断方法 - SOP自动化构建 - 轨迹生成阶段

## 文件清单

| 文件 | 说明 |
|------|------|
| `trajectory-generation.drawio` | drawio 源文件 |
| `chart.pdf` | PDF 导出（矢量格式，用于 LaTeX 引用） |
| `chart.png` | PNG 导出（预览用） |
| `README.md` | 本文件 |

## LaTeX 引用示例

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.85\textwidth]{Figures-Src/Chap3-Methodology/trajectory-generation/chart.pdf}
  \caption{基于假设驱动验证的诊断轨迹生成流程}
  \label{fig:trajectory-generation}
\end{figure}
```

## 配色方案

- 主色：#3d5a80 / #5e81ac（蓝色系）
- 强调色：#e07a5f（橙红色，用于输入和失败类别）
- 成功色：#81b29a（绿色，用于成功类别和输出）
- 容器背景：#f0f4f8（浅灰蓝）
- 错误/灰色：#999999
