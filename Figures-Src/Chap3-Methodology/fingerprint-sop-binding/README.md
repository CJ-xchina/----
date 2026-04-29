# 故障指纹聚类与SOP绑定机制

## 基本信息

- **图表编号**: 第3章方法论插图
- **图表类型**: 流程图 / 机制示意图
- **所属章节**: 第3章 基于大语言模型的微服务故障诊断方法
- **用途**: 展示故障指纹在向量空间中的聚类过程，以及每个聚类簇与SOP的绑定关系；同时展示在线诊断时如何通过余弦相似度匹配召回对应SOP

## 图表说明

本图分为左右两部分：

### 左半部分 -- 离线进化域
1. 故障注入实验产生故障事件流
2. 故障指纹编码模型将事件编码为向量
3. 向量空间中形成多个聚类簇（簇A/B/C，分别用红/蓝/绿色表示不同故障类型）
4. 每个聚类簇绑定一个对应的SOP（SOP-1/2/3）
5. 所有SOP汇入SOP知识库

### 右半部分 -- 在线诊断域
1. 新故障告警触发故障指纹编码
2. 通过余弦相似度匹配找到最近的聚类簇
3. 召回对应的SOP
4. 交给双智能体协同诊断

### 跨域连接
- 指纹库查询：在线域的余弦相似度匹配查询离线域的故障指纹向量空间
- SOP检索：在线域从离线域的SOP知识库中检索对应SOP

## 文件列表

| 文件 | 说明 |
|------|------|
| `README.md` | 本文件 |
| `fingerprint-sop-binding.drawio` | drawio 源文件 |
| `chart.pdf` | PDF 导出文件（用于 LaTeX 引用） |
| `chart.png` | PNG 导出文件（用于预览） |

## 设计规范

- **配色**: 离线域背景 #fef9ef，在线域背景 #e8f4f8，主色 #3d5a80/#5e81ac
- **聚类簇颜色**: 红色系(#f4cccc/#cc4444)、蓝色系(#c9daf8/#4472c4)、绿色系(#d9ead3/#44aa44)
- **字体**: Noto Sans SC
- **语言**: 所有文字标注使用中文
- **工具**: drawio MCP 绘制

## LaTeX 引用

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.85\textwidth]{Figures-Src/Chap3-Methodology/fingerprint-sop-binding/chart.pdf}
  \caption{故障指纹聚类与SOP绑定机制}
  \label{fig:fingerprint-sop-binding}
\end{figure}
```

## 数据来源

- 基于论文第3章方法论中关于故障表示学习与SOP构建的描述
- 参考知识库 `/root/autodl-tmp/knowledge-base/knowledge/Method/` 中的相关文档
