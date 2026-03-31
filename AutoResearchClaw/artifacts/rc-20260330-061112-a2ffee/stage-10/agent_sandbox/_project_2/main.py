import os
import sys
import time
import json

# Ensure the project directory is on sys.path so local modules resolve
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from data import get_datasets
from methods import (
    WhatProposedMethod,
    WhatVariantMethod,
    WhatBaseline1Method,
    WhatBaseline2Method,
    WithoutKeyComponentMethod,
    SimplifiedVersionMethod,
)
from evaluate import (
    aggregate_seed_results,
    compare_conditions,
    save_results,
    print_condition_report,
)

HYPERPARAMETERS = {
    'random_seeds': [42, 123, 456],
    'n_years_forecast': 10,
    'base_year': 2024,
    'n_simulations': 1000,
    'market_growth_rate': 0.15,
    'ai_adoption_rate': 0.25,
    'presales_headcount_2024': 250000,
    'skill_decay_rate': 0.08,
    'reskilling_rate': 0.35,
    'noise_sigma_fraction': 0.05,
    'ai_disruption_alpha': 5.0,
    'ai_disruption_midpoint': 2027,
    'bifurcation_threshold': 0.6,
    'orchestrator_premium': 1.45,
    'bayesian_prior': 0.5,
    'markov_n_states': 4,
    'holt_alpha': 0.3,
    'holt_beta': 0.1,
    'static_displaced_fraction': 0.35,
    'p_survive_to_displace': 0.08,
    'p_displace_to_survive': 0.02,
}


def main():
    config = Config()
    start_time = time.time()
    time_limit_seconds = config.time_budget_hours * 3600

    # --- METRIC DEFINITION ---
    print("METRIC_DEF: primary_metric=role_survival_index | range=[0,1] | higher_is_better=True")
    print("METRIC_DEF: secondary_metric=market_value_score | units=weighted_billions | higher_is_better=True")

    # --- REGISTERED CONDITIONS ---
    conditions = [
        ("what_proposed",         WhatProposedMethod),
        ("what_variant",          WhatVariantMethod),
        ("what_baseline_1",       WhatBaseline1Method),
        ("what_baseline_2",       WhatBaseline2Method),
        ("without_key_component", WithoutKeyComponentMethod),
        ("simplified_version",    SimplifiedVersionMethod),
    ]
    print(f"REGISTERED_CONDITIONS: {[c[0] for c in conditions]}")

    # --- TIME ESTIMATE: pilot run ---
    pilot_start = time.time()
    try:
        pilot_df, pilot_sec_df, pilot_rsi = get_datasets(config, seed=42)
        pilot_method = WhatProposedMethod(config)
        pilot_method.run(pilot_df, pilot_sec_df, pilot_rsi)
    except Exception as e:
        print(f"WARN: pilot run failed ({e}), time estimate unavailable")
    pilot_elapsed = time.time() - pilot_start
    n_total_runs = len(conditions) * len(config.random_seeds)
    estimated_total = pilot_elapsed * n_total_runs
    print(f"TIME_ESTIMATE: {estimated_total:.1f}s (pilot={pilot_elapsed:.3f}s x {n_total_runs} runs)")

    if len(config.random_seeds) > 3:
        print("SEED_WARNING: only 3 seeds used due to time budget")

    all_results = {}

    # --- MAIN LOOP: conditions x seeds ---
    for condition_name, ConditionClass in conditions:
        # TIME BUDGET GUARD (outer)
        elapsed = time.time() - start_time
        if elapsed > time_limit_seconds * 0.8:
            print(f"TIME_BUDGET_EXCEEDED after {elapsed:.1f}s — stopping.")
            break

        print(f"\n{'=' * 60}")
        print(f"Running condition: {condition_name}")
        seed_results = []

        for seed in config.random_seeds:
            # TIME BUDGET GUARD (inner)
            elapsed = time.time() - start_time
            if elapsed > time_limit_seconds * 0.8:
                print(f"  TIME_BUDGET_EXCEEDED (inner) — skipping remaining seeds.")
                break

            try:
                # Per-seed isolation: fresh data and model
                primary_df, secondary_df, rsi = get_datasets(config, seed)
                method = ConditionClass(config)
                result = method.run(primary_df, secondary_df, rsi)

                # NaN / divergence fast-fail guard
                primary_val = result.get('primary_metric', float('nan'))
                secondary_val = result.get('secondary_metric', float('nan'))
                if (primary_val != primary_val or  # NaN check
                        secondary_val != secondary_val or
                        abs(primary_val) > 100 or
                        abs(secondary_val) > 1e12):
                    print(f"FAIL: NaN/divergence detected for condition={condition_name} seed={seed}")
                    continue

                seed_results.append(result)

                # PER-SEED REPORTING
                print(
                    f"  condition={condition_name} seed={seed} "
                    f"primary_metric: {primary_val:.4f} | "
                    f"secondary_metric: {secondary_val:.4f}"
                )

            except Exception as e:
                print(f"  ERROR: condition={condition_name} seed={seed} raised {type(e).__name__}: {e}")
                continue

        if seed_results:
            agg = aggregate_seed_results(seed_results)
            all_results[condition_name] = agg
            print_condition_report(condition_name, agg)
            # Aggregated reporting in standard format
            print(
                f"condition={condition_name} "
                f"primary_metric_mean: {agg['primary_metric_mean']:.4f} "
                f"primary_metric_std: {agg['primary_metric_std']:.4f}"
            )
        else:
            print(f"  WARN: no valid seed results for condition={condition_name}")

    # --- SUMMARY COMPARISON ---
    print(f"\n{'=' * 60}")
    print("SUMMARY — Comparison across all conditions:")
    summary = compare_conditions(all_results)
    for cname in sorted(all_results.keys()):
        r = summary[cname]
        print(
            f"  [{r['rank']}] {cname}: "
            f"primary={r['primary_metric']:.4f}, "
            f"secondary={r['secondary_metric']:.4f}"
        )
    print(f"\nBEST_CONDITION: {summary.get('best_condition', 'N/A')}")

    # --- SAVE RESULTS ---
    final_output = {
        'hyperparameters': HYPERPARAMETERS,
        'config': {
            'topic': config.topic if hasattr(config, 'topic') else 'SaaS presales evolution',
            'seeds': config.random_seeds,
            'n_years_forecast': config.n_years_forecast,
        },
        'conditions': all_results,
        'summary': summary,
    }
    save_results(final_output, config)

    total_elapsed = time.time() - start_time
    print(f"\nTotal elapsed: {total_elapsed:.1f}s")


if __name__ == "__main__":
    main()