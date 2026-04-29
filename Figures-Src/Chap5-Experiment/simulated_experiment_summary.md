# Chapter 5 Simulated Results Summary

## 5.3 Fault Fingerprint Retrieval

| Method | AIOps-25 Hit@1 | AIOps-25 MRR | Bank Hit@1 | Bank MRR | Market Hit@1 | Market MRR |
|---|---:|---:|---:|---:|---:|---:|
| TF-IDF | 23.74 | 39.74 | 22.40 | 37.79 | 19.89 | 35.70 |
| MS-Rank | 26.88 | 43.05 | 25.03 | 40.74 | 22.92 | 38.88 |
| ART | 35.11 | 51.20 | 33.04 | 49.09 | 29.99 | 46.29 |
| DiagFusion | 36.75 | 52.50 | 34.90 | 50.79 | 31.97 | 47.94 |
| AnoFusion | 33.25 | 49.50 | 30.45 | 47.12 | 27.94 | 44.13 |
| BWGNN | 29.89 | 45.75 | 27.93 | 43.61 | 26.22 | 41.89 |
| PMF（本文方法） | 53.26 | 66.33 | 49.95 | 63.61 | 46.79 | 60.85 |

## 5.4 Fault Fingerprint Clusters for SOP Experiments

| Dataset | Cluster Count | Avg Fingerprints / Cluster | Min Fingerprints | Max Fingerprints | Selected Clusters (Top 50%) |
|---|---:|---:|---:|---:|---:|
| AIOps-25 | 34 | 11.76 | 3 | 29 | 17 |
| Bank | 16 | 8.50 | 2 | 16 | 8 |
| Market | 20 | 7.40 | 2 | 14 | 10 |

## 5.5 End-to-End Diagnosis

| Method | AIOps-25 Hit@1 | AIOps-25 MRR | Bank Hit@1 | Bank MRR | Market Hit@1 | Market MRR |
|---|---:|---:|---:|---:|---:|---:|
| TF-IDF | 7.76 | 19.03 | 6.59 | 17.94 | 5.27 | 16.28 |
| MS-Rank | 8.89 | 21.08 | 8.17 | 19.96 | 6.77 | 18.11 |
| ART | 13.33 | 27.65 | 12.26 | 25.73 | 10.57 | 23.55 |
| DiagFusion | 14.44 | 28.66 | 13.07 | 26.64 | 12.02 | 24.94 |
| AnoFusion | 12.50 | 26.38 | 11.44 | 24.80 | 9.80 | 22.22 |
| BWGNN | 11.67 | 24.27 | 9.84 | 22.46 | 8.27 | 20.84 |
| ReAct | 18.88 | 34.48 | 17.20 | 32.03 | 15.05 | 29.82 |
| RCAgent | 31.42 | 46.83 | 27.89 | 43.24 | 24.87 | 40.13 |
| mABC | 40.84 | 55.57 | 37.70 | 52.66 | 35.37 | 49.70 |
| OpenRCA (RCA-agent) | 18.06 | 33.39 | 16.40 | 30.93 | 14.26 | 28.19 |
| Flow-of-Action | 46.11 | 60.33 | 41.85 | 56.38 | 39.11 | 52.82 |
| 本文方法 | 58.03 | 70.49 | 54.15 | 66.99 | 49.61 | 63.53 |

## 5.6 Ablation

| Variant | Hit@1 | Hit@3 | Hit@5 | MRR |
|---|---:|---:|---:|---:|
| 本文方法 | 58.04 | 79.45 | 88.05 | 70.78 |
| w/o SOP 引导 | 19.19 | 39.46 | 54.46 | 34.57 |
| w/o 逃逸机制 | 43.05 | 64.43 | 77.75 | 57.60 |
| w/o 焦点与感知域约束 | 50.01 | 71.12 | 81.94 | 63.32 |
