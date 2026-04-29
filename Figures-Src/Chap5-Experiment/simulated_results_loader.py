#!/usr/bin/env python3
"""Helpers for loading simulated Chapter 5 experiment results."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULTS_PATH = ROOT / "simulated_experiment_results.json"


def load_results() -> dict:
    return json.loads(RESULTS_PATH.read_text(encoding="utf-8"))


def load_mrr_series(section: str) -> tuple[list[str], dict[str, list[float]]]:
    results = load_results()[section]
    methods = list(results.keys())
    datasets = ["AIOps-25", "Bank", "Market"]
    series = {
        dataset: [results[method][dataset]["avg_metrics"]["mrr"] for method in methods]
        for dataset in datasets
    }
    return methods, series


def load_sop_iteration() -> dict[str, list[float]]:
    return load_results()["sop_iteration"]
