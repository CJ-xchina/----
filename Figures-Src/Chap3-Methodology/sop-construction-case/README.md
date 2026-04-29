# RuleAgent驱动的SOP渐进式组织示意图

## 用途

展示第三章 `3.3.4` 中 RuleAgent 对 SOP 执行渐进式局部修改的代表性过程。该图不是完整执行日志，而是从一次较长组织序列中抽取的四个代表性动作。

## 图表结构

图中自上而下展示四个步骤，每一步均采用“左—中—右”结构：

1. **左侧：参考输入**
   - 上部为轨迹片段
   - 下部为高分决策单元
   - 本步真正被引用的内容采用高亮色显示
2. **中部：思考摘要与工具调用**
   - 概括本步修改意图
   - 展示本步代表性工具调用
3. **右侧：SOP 前后对照**
   - 左框为修改前版本
   - 右框为修改后版本
   - 体现 SOP 的渐进式演化

## 四个代表性动作

1. 补入关键故障特征验证节点
2. 加入竞争候选排除分支
3. 抽象实体与条件表达
4. 收束终止语义并保存

## 设计要点

- 每一步都只展示 **一次代表性局部修改**。
- 第 `n` 步的“修改前 SOP”来自第 `n-1` 步的修改结果。
- 图中突出的是 RuleAgent 的组织与改写过程，而不是实验流程复盘。
- 图中仅保留与渐进式组织直接相关的方法信息。

## LaTeX 引用

```latex
\begin{figure}[tbp]
  \centering
  \includegraphics[width=0.90\textwidth]{Figures-Src/Chap3-Methodology/SOP构建案例/chart.pdf}
  \bicaption{\enspace RuleAgent驱动的SOP渐进式组织示意}{\enspace Progressive SOP Organization Example by RuleAgent}
  \label{fig:sop_construction_case}
\end{figure}
```

## 文件清单

| 文件 | 说明 |
|------|------|
| `sop-construction-case.drawio` | drawio 源文件 |
| `chart.svg` | SVG 导出 |
| `chart.pdf` | PDF 导出 |
| `chart.png` | PNG 预览 |
| `README.md` | 本文件 |
