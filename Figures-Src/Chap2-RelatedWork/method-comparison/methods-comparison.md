# 表2-1 现有方法对比总结表

## 表格内容

| 方法类别 | 代表工作 | 核心思想 | 数据类型 | 优势 | 局限性 |
|---------|---------|---------|---------|------|--------|
| **基于因果推断** | MicroCause, CIRCA, CausalRCA | 构建因果图，基于因果关系推理根因 | 指标、日志 | 可解释性强，符合人类推理逻辑 | 依赖准确的因果发现，对噪声敏感 |
| **基于特征表示** | DiagFusion, Nezha, DeepHunt, ART | 多模态融合，深度学习提取特征 | 指标、日志、追踪 | 自动特征提取，端到端训练 | 缺乏可解释性，泛化性差，需大量标注数据 |
| **被动式AIOps** | RCACopilot | LLM辅助分析，人工主导诊断 | 告警、日志 | 利用LLM知识，降低门槛 | 效率低，依赖人工经验 |
| **工具增强智能体** | D-Bot, RCAgent | LLM主导诊断，调用外部工具 | 多模态 | 自主诊断能力，灵活性强 | 缺乏经验积累，诊断过程不可控 |
| **多智能体协作** | mABC, COLA | 多智能体分工协作 | 多模态 | 复杂任务处理能力强 | 协调开销大，仍缺乏经验积累 |
| **本文方法** | - | SOP驱动+双域闭环+故障指纹 | 多模态 | 经验复用，持续演进，可控可解释 | - |

## LaTeX代码

```latex
\begin{table}[htbp]
    \centering
    \caption{现有微服务故障诊断方法对比总结}
    \label{tab:methods-comparison}
    \renewcommand{\arraystretch}{1.3}
    \footnotesize
    \begin{tabular}{|p{2cm}|p{2.5cm}|p{3cm}|p{2.5cm}|p{3cm}|}
        \hline
        \rowcolor{lightgray!30}
        \textbf{方法类别} & \textbf{代表工作} & \textbf{核心思想} & \textbf{优势} & \textbf{局限性} \\
        \hline
        基于因果推断 & MicroCause, CIRCA & 构建因果图，推理根因 & 可解释性强 & 依赖准确的因果发现 \\
        \hline
        基于特征表示 & DiagFusion, Nezha, ART & 多模态融合，深度学习 & 自动特征提取 & 缺乏可解释性，泛化性差 \\
        \hline
        被动式AIOps & RCACopilot & LLM辅助分析 & 利用LLM知识 & 效率低，依赖人工 \\
        \hline
        工具增强智能体 & D-Bot, RCAgent & LLM+工具调用 & 自主诊断能力 & 缺乏经验积累 \\
        \hline
        多智能体协作 & mABC, COLA & 多智能体分工 & 复杂任务处理 & 协调开销大 \\
        \hline
        \rowcolor{blue!10}
        \textbf{本文方法} & - & SOP驱动+双域闭环 & 经验复用，持续演进 & - \\
        \hline
    \end{tabular}
\end{table}
```

## 引用方式

```latex
表\ref{tab:methods-comparison}总结了现有微服务故障诊断方法的主要特点。
从表中可以看出，传统方法在可解释性或自动化方面各有优势，但都缺乏
经验积累与持续演进的能力。基于大模型的方法虽然提升了诊断的自主性，
但仍未解决经验复用的问题。本文方法通过SOP知识库和双域闭环架构，
实现了诊断经验的结构化沉淀与持续演进。
```
