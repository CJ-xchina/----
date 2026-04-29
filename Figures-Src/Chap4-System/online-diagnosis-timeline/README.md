# 基于 Claude Code 的代理执行时序图

## 图表信息

| 属性 | 值 |
|------|-----|
| 图表类型 | UML 时序图 |
| 所属章节 | 第4章 系统实现 |
| 引用位置 | 4.3 节 双智能体协同机制的实现 |
| 绘制工具 | drawio |

## 图表描述

展示 Claude Code 在平台中执行代理任务时的核心交互时序，包括：

1. **执行重心**：以 Claude Code 沙箱环境为中心，弱化前端与调度细节
2. **主代理与子代理分工**：主代理负责规划与收敛，子代理负责专门观测、检索与分析
3. **Claude Code Skills 与 MCP 协同**：Claude Code Skills 提供能力定义，MCP 连接平台 API 与外部数据源
4. **统一任务骨架**：无论是根因定位、探索还是其他任务，都遵循同一执行循环
5. **循环执行**：规划 → 委托/直连工具 → 获取结果 → 更新状态 → 判断是否完成

## 文件清单

| 文件 | 说明 |
|------|------|
| `README.md` | 本说明文件 |
| `source.drawio` | drawio 源文件 |
| `chart.pdf` | PDF 矢量图（用于 LaTeX） |
| `chart.png` | PNG 图片（用于预览） |

## LaTeX 引用

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.95\textwidth]{Figures-Src/Chap4-System/在线诊断时序/chart.pdf}
  \caption{基于 Claude Code 的代理执行时序图}
  \label{fig:agent_execution_sequence}
\end{figure}
```
