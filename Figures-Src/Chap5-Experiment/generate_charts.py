#!/usr/bin/env python3
"""Legacy wrapper for Chapter 5 chart generation.

This file previously contained hard-coded historical numbers.
To avoid reintroducing stale simulated results, keep this entrypoint as a thin
shim that redirects users to the maintained generators driven by
`simulated_experiment_results.json`.
"""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    print("This legacy script is deprecated.")
    print("Use the maintained generators below instead:")
    print(f"  python {root / 'fig5-2-fingerprint-mrr' / 'source.py'}")
    print(f"  python {root / 'fig5-5-e2e-mrr' / 'source.py'}")
    print(f"  python {root / 'mrr-chart' / 'generate_mrr_chart.py'}")
    print(f"  python {root / 'mrr-chart' / 'generate_e2e_mrr_chart.py'}")


if __name__ == "__main__":
    main()
