# 表2-1 现有方法对比总结表

## 基本信息
- **图表编号**: 表2-1
- **中文标题**: 现有微服务故障诊断方法对比总结
- **英文标题**: Comparison of Existing Microservice Fault Diagnosis Methods
- **所属章节**: 第2章 相关技术与研究现状 - 2.5节 本章小结
- **优先级**: P0（必须）

## 表格内容

| 方法类别 | 代表工作 | 核心思想 | 优势 | 局限性 |
|---------|---------|---------|------|--------|
| 基于因果推断 | MicroCause, CIRCA | 构建因果图，推理根因 | 可解释性强 | 依赖准确的因果发现 |
| 基于特征表示 | DiagFusion, Nezha, ART | 多模态融合，深度学习 | 自动特征提取 | 缺乏可解释性，泛化性差 |
| 被动式AIOps | RCACopilot | LLM辅助分析 | 利用LLM知识 | 人工主导，效率低 |
| 工具增强智能体 | D-Bot, RCAgent | LLM+工具调用 | 自主诊断能力 | 缺乏经验积累 |
| 多智能体协作 | mABC, COLA | 多智能体分工协作 | 复杂任务处理 | 协调开销大 |
| **本文方法** | - | SOP驱动+双域闭环 | 经验复用，持续演进 | - |

## 设计要点
- 多列对比，清晰展示各方法特点
- 最后一行突出本文方法的定位
- 可以用颜色区分不同类别

## LaTeX代码模板
```latex
\begin{table}[htbp]
  \centering
  \caption{现有微服务故障诊断方法对比总结}
  \label{tab:methods-comparison}
  \renewcommand{\arraystretch}{1.3}
  \small
  \begin{tabular}{|l|l|p{3cm}|p{2.5cm}|p{3cm}|}
    \hline
    \rowcolor{lightgray!30}
    \textbf{方法类别} & \textbf{代表工作} & \textbf{核心思想} & \textbf{优势} & \textbf{局限性} \\
    \hline
    ... & ... & ... & ... & ... \\
    \hline
  \end{tabular}
\end{table}
```

## 引用方式
```latex
表\ref{tab:methods-comparison}总结了现有微服务故障诊断方法的主要特点...
```

## 文件清单
- [ ] methods-comparison.tex (LaTeX表格代码)
- [ ] methods-comparison.md (表格内容说明)
