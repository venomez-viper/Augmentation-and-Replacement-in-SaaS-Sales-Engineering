import os
import sys
import time
import json

# Ensure the project directory is on sys.path so local modules resolve
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

from experiment_config import Config
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
    'random_seeds': [0, 1, 2],
    'n_years_forecast': 10,
    'base_year': 2024,
    'n_simulations': 1000,
    'market_growth_rate': 0.15,
    'ai_adoption_rate': 0.25,
    'presales_headcount_2024': 250000,
    'skill_decay_rate': 0.10,
    'reskilling_rate': 0.35,
    'noise_sigma_fraction': 0.05,
    'ai_disruption_alpha': 6.0,
    'ai_disruption_midpoint': 2026,
    'bifurcation_threshold': 0.55,
    'orchestrator_premium': 1.45,
    'bayesian_prior': 0.45,
    'markov_n_states': 4,
    'holt_alpha': 0.3,
    'holt_beta': 0.1,
    'static_displaced_fraction': 0.35,
    'p_survive_to_displace': 0.08,
    'p_displace_to_survive': 0.02,
}

# ---------------------------------------------------------------------------
# Minimal pandas-free DataFrame replacement
# ---------------------------------------------------------------------------

class _Series:
    """Mimics the pandas Series API used by methods.py."""

    def __init__(self, arr):
        self._arr = np.array(arr, dtype=float)

    @property
    def values(self):
        return self._arr

    def __getitem__(self, idx):
        return self._arr[idx]

    def __len__(self):
        return len(self._arr)

    def mean(self):
        return float(np.mean(self._arr))

    def max(self):
        return float(np.max(self._arr))

    def pct_change(self):
        result = np.zeros_like(self._arr)
        result[1:] = (self._arr[1:] - self._arr[:-1]) / (np.abs(self._arr[:-1]) + 1e-9)
        return _Series(result)

class _Index:
    """Mimics the pandas Index API used by methods.py."""

    def __init__(self, values):
        self._values = np.array(values)

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, idx):
        return self._values[idx]

    def intersection(self, other):
        other_vals = other._values if isinstance(other, _Index) else np.array(other)
        common = np.intersect1d(self._values, other_vals)
        return _Index(common)

class _LocIndexer:
    def __init__(self, frame):
        self._frame = frame

    def __getitem__(self, years):
        years_arr = years._values if isinstance(years, _Index) else np.array(years)
        mask = np.isin(self._frame.index._values, years_arr)
        new_data = {k: v._arr[mask] for k, v in self._frame._data.items()}
        new_index = self._frame.index._values[mask]
        return SimpleFrame(new_data, index=new_index)

class SimpleFrame:
    """
    Lightweight pandas-free DataFrame replacement.
    Supports the column/index API used throughout methods.py and data functions.
    """

    def __init__(self, data: dict, index=None):
        self._data = {k: _Series(v) for k, v in data.items()}
        if index is not None:
            self.index = _Index(index)
        else:
            first = next(iter(data.values()))
            self.index = _Index(np.arange(len(first)))

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self.index)

    @property
    def loc(self):
        return _LocIndexer(self)

# ---------------------------------------------------------------------------
# Data generation (inlined — data.py not present in this project)
# ---------------------------------------------------------------------------

def generate_primary_dataset(config: Config, seed: int) -> SimpleFrame:
    np.random.seed(seed)
    n_years = config.n_years_forecast + 10
    years = list(range(2015, 2015 + n_years))
    T = len(years)

    saas_market_size = np.array([
        250.0 * ((1.0 + config.market_growth_rate) ** (yr - 2015))
        for yr in years
    ])

    headcount_base = float(config.presales_headcount_2024)
    presales_headcount = np.array([
        headcount_base * (1.0 + 0.05 * (yr - 2024)) if yr <= 2027
        else headcount_base * (1.0 + 0.05 * (2027 - 2024)) * (1.0 - config.skill_decay_rate * (yr - 2027))
        for yr in years
    ])
    presales_headcount = np.clip(presales_headcount, 50000, None)

    ai_capability_index = np.array([
        1.0 / (1.0 + np.exp(-0.8 * (yr - 2025)))
        for yr in years
    ])

    avg_deal_complexity = np.array([
        float(np.clip(0.2 + 0.04 * (yr - 2015), 0.0, 1.0))
        for yr in years
    ])

    avg_salary_usd = np.array([
        80000.0 + 5000.0 * (yr - 2015) + 2000.0 * ai_capability_index[i]
        for i, yr in enumerate(years)
    ])
    avg_salary_usd = np.clip(avg_salary_usd, 80000.0, 180000.0)

    automation_threat_score = np.array([
        float(np.clip(0.1 + 0.6 * ai_capability_index[i] * (1.0 - avg_deal_complexity[i] * 0.3), 0.0, 1.0))
        for i in range(T)
    ])

    new_role_emergence_rate = np.array([
        float(np.clip(config.reskilling_rate * ai_capability_index[i] + 0.05, 0.0, 1.0))
        for i in range(T)
    ])

    noise_frac = HYPERPARAMETERS['noise_sigma_fraction']
    saas_market_size        += np.random.normal(0, noise_frac * saas_market_size)
    presales_headcount      += np.random.normal(0, noise_frac * presales_headcount)
    ai_capability_index     += np.random.normal(0, noise_frac * np.abs(ai_capability_index))
    avg_deal_complexity     += np.random.normal(0, noise_frac * np.abs(avg_deal_complexity))
    avg_salary_usd          += np.random.normal(0, noise_frac * avg_salary_usd)
    automation_threat_score += np.random.normal(0, noise_frac * np.abs(automation_threat_score))
    new_role_emergence_rate += np.random.normal(0, noise_frac * np.abs(new_role_emergence_rate))

    return SimpleFrame({
        'saas_market_size':        np.clip(saas_market_size,        1.0,     None),
        'presales_headcount':      np.clip(presales_headcount,       10000.0, None),
        'ai_capability_index':     np.clip(ai_capability_index,      0.0,     1.0),
        'avg_deal_complexity':     np.clip(avg_deal_complexity,      0.0,     1.0),
        'avg_salary_usd':          np.clip(avg_salary_usd,           80000.0, 180000.0),
        'automation_threat_score': np.clip(automation_threat_score,  0.0,     1.0),
        'new_role_emergence_rate': np.clip(new_role_emergence_rate,  0.0,     1.0),
    }, index=years)

def generate_secondary_dataset(config: Config, seed: int) -> SimpleFrame:
    np.random.seed(seed + 1000)
    n_years = config.n_years_forecast + 10
    years = list(range(2015, 2015 + n_years))
    T = len(years)

    technical_depth_score = np.array([float(np.clip(0.6 + 0.015 * (yr - 2015), 0.0, 1.0)) for yr in years])
    business_acumen_score = np.array([float(np.clip(0.5 + 0.02  * (yr - 2015), 0.0, 1.0)) for yr in years])
    ai_literacy_score     = np.array([float(np.clip(0.1 + 0.045 * (yr - 2015), 0.0, 1.0)) for yr in years])
    orchestration_skill   = np.array([float(np.clip(max(0.0, 0.05 * (yr - 2018)) + 0.02, 0.0, 1.0)) for yr in years])
    empathy_creativity    = np.array([float(np.clip(0.7 + 0.005 * (yr - 2015), 0.0, 1.0)) for yr in years])

    skill_matrix = np.column_stack([
        technical_depth_score, business_acumen_score,
        ai_literacy_score, orchestration_skill, empathy_creativity,
    ])  # [T, 5]

    demand_weights = np.zeros((T, 5))
    for i, yr in enumerate(years):
        ai_factor = min(1.0, max(0.0, (yr - 2015) / 20.0))
        w = np.array([
            0.25 - 0.05 * ai_factor,
            0.25 + 0.05 * ai_factor,
            0.15 + 0.15 * ai_factor,
            0.10 + 0.10 * ai_factor,
            0.25 - 0.25 * ai_factor * 0.6,
        ])
        w = np.clip(w, 0.01, None)
        demand_weights[i] = w / w.sum()

    weighted_role_value = np.array([
        float(np.dot(skill_matrix[i], demand_weights[i])) for i in range(T)
    ])

    noise_frac = HYPERPARAMETERS['noise_sigma_fraction']
    technical_depth_score += np.random.normal(0, noise_frac * technical_depth_score)
    business_acumen_score += np.random.normal(0, noise_frac * business_acumen_score)
    ai_literacy_score     += np.random.normal(0, noise_frac * np.abs(ai_literacy_score) + 0.01)
    orchestration_skill   += np.random.normal(0, noise_frac * np.abs(orchestration_skill) + 0.01)
    empathy_creativity    += np.random.normal(0, noise_frac * empathy_creativity)
    weighted_role_value   += np.random.normal(0, noise_frac * weighted_role_value)

    return SimpleFrame({
        'technical_depth_score': np.clip(technical_depth_score, 0.0, 1.0),
        'business_acumen_score': np.clip(business_acumen_score, 0.0, 1.0),
        'ai_literacy_score':     np.clip(ai_literacy_score,     0.0, 1.0),
        'orchestration_skill':   np.clip(orchestration_skill,   0.0, 1.0),
        'empathy_creativity':    np.clip(empathy_creativity,     0.0, 1.0),
        'weighted_role_value':   np.clip(weighted_role_value,   0.0, 1.0),
    }, index=years)

def compute_role_survival_index(primary_df: SimpleFrame, secondary_df: SimpleFrame) -> np.ndarray:
    automation_risk    = primary_df['automation_threat_score'].values
    skill_adaptability = secondary_df['weighted_role_value'].values
    market_size        = primary_df['saas_market_size'].values
    market_demand      = market_size / (market_size.max() + 1e-9)
    rsi = (1.0 - automation_risk) * skill_adaptability * market_demand
    return np.clip(rsi, 0.0, 1.0)

def get_datasets(config: Config, seed: int):
    primary_df   = generate_primary_dataset(config, seed)
    secondary_df = generate_secondary_dataset(config, seed)
    common_years = primary_df.index.intersection(secondary_df.index)
    primary_df   = primary_df.loc[common_years]
    secondary_df = secondary_df.loc[common_years]
    rsi = compute_role_survival_index(primary_df, secondary_df)
    return primary_df, secondary_df, rsi

# ---------------------------------------------------------------------------
# Main experiment loop
# ---------------------------------------------------------------------------

def main():
    config = Config()
    start_time = time.time()
    time_limit_seconds = config.time_budget_hours * 3600

    # --- METRIC DEFINITION ---
    print("METRIC_DEF: primary_metric=role_survival_index | range=[0,1] | higher_is_better=False | minimize=True")
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

    seeds = [0, 1, 2]

    # --- TIME ESTIMATE: pilot run ---
    pilot_start = time.time()
    try:
        pilot_df, pilot_sec_df, pilot_rsi = get_datasets(config, seed=0)
        pilot_method = WhatProposedMethod(config)
        pilot_method.run(pilot_df, pilot_sec_df, pilot_rsi)
    except Exception as e:
        print(f"WARN: pilot run failed ({e}), time estimate unavailable")
    pilot_elapsed = time.time() - pilot_start
    n_total_runs = len(conditions) * len(seeds)
    estimated_total = pilot_elapsed * n_total_runs
    print(f"TIME_ESTIMATE: {estimated_total:.1f}s (pilot={pilot_elapsed:.3f}s x {n_total_runs} runs)")

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

        for seed in seeds:
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
                primary_val   = result.get('primary_metric',   float('nan'))
                secondary_val = result.get('secondary_metric', float('nan'))
                if (primary_val != primary_val or
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
            print(
                f"condition={condition_name} "
                f"primary_metric_mean: {agg['primary_metric_mean']:.4f} "
                f"primary_metric_std: {agg['primary_metric_std']:.4f}"
            )
        else:
            print(f"  WARN: no valid seed results for condition={condition_name}")

    # --- SUMMARY COMPARISON ---
    print(f"\n{'=' * 60}")
    print("SUMMARY — Comparison across all conditions (minimize primary_metric):")
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
            'seeds': seeds,
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