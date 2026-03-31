import json
import os

import numpy as np

from experiment_config import Config

def compute_forecast_accuracy(rsi_true: np.ndarray, rsi_pred: list) -> dict:
    n = min(len(rsi_true), len(rsi_pred))
    true_arr = np.array(rsi_true[:n], dtype=float)   # shape [n]
    pred_arr = np.array(rsi_pred[:n], dtype=float)   # shape [n]

    mae = float(np.mean(np.abs(true_arr - pred_arr)))
    rmse = float(np.sqrt(np.mean((true_arr - pred_arr) ** 2)))

    # AUC of RSI curve using trapezoid rule (numpy 2.x compatible)
    try:
        auc_true = float(np.trapezoid(true_arr))
        auc_pred = float(np.trapezoid(pred_arr))
    except AttributeError:
        # Fallback for numpy < 2.0
        auc_true = float(np.trapz(true_arr))
        auc_pred = float(np.trapz(pred_arr))

    auc_diff = abs(auc_true - auc_pred) / (abs(auc_true) + 1e-9)

    return {
        'mae': mae,
        'rmse': rmse,
        'auc_relative_diff': auc_diff,
        'auc_true': auc_true,
        'auc_pred': auc_pred,
        'n_points': n,
    }

def aggregate_seed_results(seed_results: list) -> dict:
    primary_vals = [float(r['primary_metric']) for r in seed_results]
    secondary_vals = [float(r['secondary_metric']) for r in seed_results]

    return {
        'primary_metric_mean': float(np.mean(primary_vals)),
        'primary_metric_std': float(np.std(primary_vals)),
        'secondary_metric_mean': float(np.mean(secondary_vals)),
        'secondary_metric_std': float(np.std(secondary_vals)),
        'primary_metric_min': float(np.min(primary_vals)),
        'primary_metric_max': float(np.max(primary_vals)),
        'n_seeds': len(seed_results),
    }

def compare_conditions(all_results: dict) -> dict:
    summary = {}
    for condition_name, agg in all_results.items():
        summary[condition_name] = {
            'primary_metric': float(agg['primary_metric_mean']),
            'primary_std': float(agg['primary_metric_std']),
            'secondary_metric': float(agg['secondary_metric_mean']),
            'rank': None,
        }

    # Metric direction: minimize — lower primary_metric is better (rank=1)
    ranked = sorted(
        summary.keys(),
        key=lambda k: summary[k]['primary_metric'],
        reverse=False,
    )
    for rank_i, cname in enumerate(ranked, 1):
        summary[cname]['rank'] = rank_i

    summary['best_condition'] = ranked[0] if ranked else None
    return summary

def save_results(results: dict, config: Config) -> None:
    os.makedirs(config.output_dir, exist_ok=True)
    out_path = os.path.join(config.output_dir, config.results_file)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Results saved to {out_path}")

def print_condition_report(condition_name: str, agg: dict) -> None:
    print(f"  Condition: {condition_name}")
    print(
        f"    primary_metric (role_survival_index): "
        f"{agg['primary_metric_mean']:.4f} \u00b1 {agg['primary_metric_std']:.4f}"
    )
    print(
        f"    secondary_metric (market_value_score): "
        f"{agg['secondary_metric_mean']:.4f} \u00b1 {agg['secondary_metric_std']:.4f}"
    )