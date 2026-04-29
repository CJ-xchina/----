#!/usr/bin/env python3
"""Deprecated Chapter 5 chart script.

The old version embedded obsolete simulated values directly in code.
Keep this file as an explicit redirect so future updates only use the JSON-based
pipeline under the maintained chart generators.
"""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    print("generate_charts_v2.py is deprecated and no longer stores chart data.")
    print("Regenerate Chapter 5 figures with the maintained scripts:")
    print(f"  python {root / 'fig5-2-fingerprint-mrr' / 'source.py'}")
    print(f"  python {root / 'fig5-5-e2e-mrr' / 'source.py'}")
    print(f"  python {root / 'mrr-chart' / 'generate_mrr_chart.py'}")
    print(f"  python {root / 'mrr-chart' / 'generate_e2e_mrr_chart.py'}")


if __name__ == "__main__":
    main()
