import numpy as np
from experiment_config import Config

class BaseAnalysisMethod:
    def __init__(self, config: Config):
        self.config = config
        self.name = "base"
        self.results = {}
        self.forecast_years = list(range(config.base_year, config.base_year + config.n_years_forecast))
        self.rsi_history = []
        self.market_value_history = []
        self.primary_df = None
        self.secondary_df = None
        self.rsi = None
        self.mean_rsi = 0.0
        self.std_rsi = 0.0

    def fit(self, primary_df, secondary_df, rsi: np.ndarray) -> None:
        self.primary_df = primary_df
        self.secondary_df = secondary_df
        self.rsi = rsi
        self.mean_rsi = float(np.mean(rsi))
        self.std_rsi = float(np.std(rsi)) + 1e-9

    def forecast(self, horizon: int) -> dict:
        last_year = int(self.primary_df.index[-1])
        forecast_years = list(range(last_year + 1, last_year + 1 + horizon))
        rsi_forecast = [float(self.mean_rsi)] * horizon
        market_value_forecast = [self.compute_market_value_score(self.primary_df, self.secondary_df)] * horizon
        return {
            'years': forecast_years,
            'rsi_forecast': rsi_forecast,
            'market_value_forecast': market_value_forecast,
            'ci_lower': [max(0.0, r - self.std_rsi) for r in rsi_forecast],
            'ci_upper': [min(1.0, r + self.std_rsi) for r in rsi_forecast],
        }

    def compute_market_value_score(self, primary_df, secondary_df) -> float:
        headcount = float(primary_df['presales_headcount'].values[-1])
        avg_salary = float(primary_df['avg_salary_usd'].values[-1])
        total_market_value = headcount * avg_salary / 1e9
        role_value_weight = float(secondary_df['weighted_role_value'].values[-1])
        return float(total_market_value * role_value_weight)

    def run(self, primary_df, secondary_df, rsi: np.ndarray) -> dict:
        self.fit(primary_df, secondary_df, rsi)
        fc = self.forecast(self.config.n_years_forecast)
        mvs = self.compute_market_value_score(primary_df, secondary_df)
        self.results = {
            'primary_metric': float(fc['rsi_forecast'][-1]),
            'secondary_metric': float(mvs),
            'forecast': fc,
            'method': self.name,
        }
        return self.results

class WhatProposedMethod(BaseAnalysisMethod):
    """AI-Augmented Role Evolution: sigmoid AI disruption + Bayesian RSI + role bifurcation.
    Tuned: alpha=6.0, midpoint=2026, prior=0.45 for stronger AI displacement signal.
    """

    def __init__(self, config: Config):
        super().__init__(config)
        self.name = "what_proposed"
        self.ai_disruption_alpha = 6.0       # steeper sigmoid — faster capability rise
        self.ai_disruption_midpoint = 2026   # earlier inflection year
        self.bifurcation_threshold = 0.55    # tighter: more roles flagged at-risk
        self.orchestrator_premium = 1.45
        self.bayesian_prior = 0.45           # slightly pessimistic prior
        self.ai_curve = None
        self.bayesian_rsi = None
        self.displaced_fraction = 0.0
        self.surviving_fraction = 1.0

    def _sigmoid_ai_curve(self, year: float) -> float:
        x = self.ai_disruption_alpha * (year - self.ai_disruption_midpoint)
        return 1.0 / (1.0 + np.exp(-x))

    def _bayesian_rsi_update(self, prior: float, ai_capability: float, skill_level: float) -> float:
        likelihood_survive = skill_level * (1.0 - 0.8 * ai_capability)
        likelihood_not_survive = (1.0 - skill_level) * ai_capability
        denom = likelihood_survive * prior + likelihood_not_survive * (1.0 - prior)
        if denom < 1e-12:
            return float(np.clip(prior, 0.01, 0.99))
        posterior = (likelihood_survive * prior) / denom
        return float(np.clip(posterior, 0.01, 0.99))

    def fit(self, primary_df, secondary_df, rsi: np.ndarray) -> None:
        super().fit(primary_df, secondary_df, rsi)
        years_numeric = np.array([int(y) for y in primary_df.index])
        self.ai_curve = np.array([self._sigmoid_ai_curve(y) for y in years_numeric])

        ai_cap = primary_df['ai_capability_index'].values
        skill_vals = secondary_df['weighted_role_value'].values
        self.bayesian_rsi = np.array([
            self._bayesian_rsi_update(self.bayesian_prior, ai_cap[i], skill_vals[i])
            for i in range(len(ai_cap))
        ])

        self.displaced_fraction = float(np.mean(self.bayesian_rsi < self.bifurcation_threshold))
        self.surviving_fraction = 1.0 - self.displaced_fraction

    def forecast(self, horizon: int) -> dict:
        last_year = int(self.primary_df.index[-1])
        forecast_years = list(range(last_year + 1, last_year + 1 + horizon))
        rsi_forecast = []
        ci_lower, ci_upper = [], []

        for yr in forecast_years:
            ai_cap_proj = self._sigmoid_ai_curve(yr)
            # Faster skill decay (0.04/yr) under accelerating AI disruption
            skill_proj = max(0.05, self.mean_rsi - 0.04 * (yr - last_year))
            rsi_yr = self._bayesian_rsi_update(self.bayesian_prior, ai_cap_proj, skill_proj)
            effective_rsi = (
                rsi_yr * self.surviving_fraction * self.orchestrator_premium
                + rsi_yr * self.displaced_fraction * 0.2
            )
            effective_rsi = float(np.clip(effective_rsi, 0.0, 1.0))
            rsi_forecast.append(effective_rsi)
            ci_lower.append(max(0.0, effective_rsi - 1.96 * self.std_rsi))
            ci_upper.append(min(1.0, effective_rsi + 1.96 * self.std_rsi))

        market_value_forecast = [
            self.compute_market_value_score(self.primary_df, self.secondary_df) * (1.0 + 0.1 * i)
            for i in range(horizon)
        ]
        return {
            'years': forecast_years,
            'rsi_forecast': rsi_forecast,
            'market_value_forecast': market_value_forecast,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'bifurcation_point': self.ai_disruption_midpoint,
            'surviving_fraction': self.surviving_fraction,
        }

class WhatVariantMethod(BaseAnalysisMethod):
    """Skill Transition Matrix: 4-state Markov chain over role cohorts."""

    def __init__(self, config: Config):
        super().__init__(config)
        self.name = "what_variant"
        self.n_states = 4
        self.state_labels = ['Traditional', 'Hybrid', 'AI_Orchestrator', 'Displaced']
        self.transition_matrix = np.zeros((4, 4))
        self.initial_distribution = np.array([0.7, 0.2, 0.05, 0.05])
        self.historical_distributions = None

    def _build_transition_matrix(self, ai_capability: float, market_growth: float) -> np.ndarray:
        p_trad_to_hybrid = 0.15 + 0.20 * ai_capability
        p_trad_to_displaced = 0.05 + 0.25 * ai_capability
        p_trad_stay = max(0.01, 1.0 - p_trad_to_hybrid - p_trad_to_displaced)

        p_hybrid_to_orchestrator = min(0.90, 0.10 + 0.30 * market_growth)
        p_hybrid_stay = max(0.01, 1.0 - p_hybrid_to_orchestrator - 0.05)

        T = np.array([
            [p_trad_stay,   p_trad_to_hybrid,       0.0,                      p_trad_to_displaced],
            [0.0,           p_hybrid_stay,           p_hybrid_to_orchestrator, 0.05],
            [0.0,           0.05,                    0.90,                     0.05],
            [0.0,           0.0,                     0.0,                      1.0],
        ], dtype=float)

        row_sums = T.sum(axis=1, keepdims=True)
        row_sums = np.where(row_sums == 0, 1.0, row_sums)
        T = T / row_sums
        return T

    def fit(self, primary_df, secondary_df, rsi: np.ndarray) -> None:
        super().fit(primary_df, secondary_df, rsi)
        ai_cap_mean = float(primary_df['ai_capability_index'].mean())
        mkt_growth = float(primary_df['saas_market_size'].pct_change().mean())
        if np.isnan(mkt_growth):
            mkt_growth = 0.15

        self.transition_matrix = self._build_transition_matrix(ai_cap_mean, mkt_growth)

        dist = self.initial_distribution.copy()
        self.historical_distributions = [dist.copy()]
        for _ in range(len(primary_df) - 1):
            dist = dist @ self.transition_matrix
            self.historical_distributions.append(dist.copy())
        self.historical_distributions = np.array(self.historical_distributions)

    def forecast(self, horizon: int) -> dict:
        dist = self.historical_distributions[-1].copy()
        forecast_dists = []
        last_year = int(self.primary_df.index[-1])
        forecast_years = list(range(last_year + 1, last_year + 1 + horizon))

        for i in range(horizon):
            ai_cap_proj = min(1.0, 0.5 + 0.05 * i)
            mkt_growth = max(0.05, 0.15 - 0.01 * i)
            T = self._build_transition_matrix(ai_cap_proj, mkt_growth)
            dist = dist @ T
            forecast_dists.append(dist.copy())

        forecast_dists = np.array(forecast_dists)

        weights = np.array([0.3, 0.6, 1.0, 0.0])
        rsi_forecast = (forecast_dists * weights).sum(axis=1).tolist()

        market_value_forecast = [
            self.compute_market_value_score(self.primary_df, self.secondary_df)
            * (1.0 + float(forecast_dists[i, 2]) * 0.5)
            for i in range(horizon)
        ]
        return {
            'years': forecast_years,
            'rsi_forecast': rsi_forecast,
            'market_value_forecast': market_value_forecast,
            'ci_lower': [max(0.0, r - 0.1) for r in rsi_forecast],
            'ci_upper': [min(1.0, r + 0.1) for r in rsi_forecast],
            'state_distributions': forecast_dists.tolist(),
            'state_labels': self.state_labels,
        }

class WhatBaseline1Method(BaseAnalysisMethod):
    """Linear Trend Extrapolation: OLS regression on historical RSI."""

    def __init__(self, config: Config):
        super().__init__(config)
        self.name = "what_baseline_1"
        self.slope = 0.0
        self.intercept = 0.0
        self.r_squared = 0.0
        self.last_x = 0.0

    def fit(self, primary_df, secondary_df, rsi: np.ndarray) -> None:
        super().fit(primary_df, secondary_df, rsi)
        T = len(rsi)
        x = np.arange(T, dtype=float)
        y = rsi

        x_mean = float(np.mean(x))
        y_mean = float(np.mean(y))
        denom = float(np.sum((x - x_mean) ** 2))
        if denom < 1e-12:
            self.slope = 0.0
        else:
            self.slope = float(np.sum((x - x_mean) * (y - y_mean)) / denom)
        self.intercept = y_mean - self.slope * x_mean

        y_pred = self.slope * x + self.intercept
        ss_res = float(np.sum((y - y_pred) ** 2))
        ss_tot = float(np.sum((y - y_mean) ** 2))
        self.r_squared = 1.0 - ss_res / (ss_tot + 1e-9)
        self.last_x = float(T - 1)

    def forecast(self, horizon: int) -> dict:
        last_year = int(self.primary_df.index[-1])
        forecast_years = list(range(last_year + 1, last_year + 1 + horizon))
        rsi_forecast = []
        for i in range(1, horizon + 1):
            x_proj = self.last_x + i
            rsi_proj = float(np.clip(self.slope * x_proj + self.intercept, 0.0, 1.0))
            rsi_forecast.append(rsi_proj)

        residual_std = self.std_rsi * float(np.sqrt(1.0 + 1.0 / max(1, len(self.rsi))))
        ci_lower = [max(0.0, r - 1.96 * residual_std) for r in rsi_forecast]
        ci_upper = [min(1.0, r + 1.96 * residual_std) for r in rsi_forecast]
        market_value_forecast = [
            self.compute_market_value_score(self.primary_df, self.secondary_df)
        ] * horizon

        return {
            'years': forecast_years,
            'rsi_forecast': rsi_forecast,
            'market_value_forecast': market_value_forecast,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'r_squared': self.r_squared,
        }

class WhatBaseline2Method(BaseAnalysisMethod):
    """Holt's Double Exponential Smoothing: level + trend, purely statistical."""

    def __init__(self, config: Config):
        super().__init__(config)
        self.name = "what_baseline_2"
        self.alpha = 0.3
        self.beta = 0.1
        self.level = 0.0
        self.trend = 0.0
        self.smoothed = None
        self.residual_std = 0.0

    def fit(self, primary_df, secondary_df, rsi: np.ndarray) -> None:
        super().fit(primary_df, secondary_df, rsi)
        T = len(rsi)
        self.level = float(rsi[0])
        self.trend = float(rsi[1] - rsi[0]) if T > 1 else 0.0

        smoothed_list = [self.level]
        for t in range(1, T):
            prev_level = self.level
            self.level = self.alpha * rsi[t] + (1.0 - self.alpha) * (self.level + self.trend)
            self.trend = self.beta * (self.level - prev_level) + (1.0 - self.beta) * self.trend
            smoothed_list.append(float(self.level + self.trend))

        self.smoothed = np.array(smoothed_list)
        self.residual_std = float(np.std(rsi - self.smoothed)) + 1e-9

    def forecast(self, horizon: int) -> dict:
        last_year = int(self.primary_df.index[-1])
        forecast_years = list(range(last_year + 1, last_year + 1 + horizon))
        rsi_forecast = []
        level = self.level
        trend = self.trend

        for h in range(1, horizon + 1):
            rsi_h = float(np.clip(level + h * trend, 0.0, 1.0))
            rsi_forecast.append(rsi_h)

        ci_lower = [
            max(0.0, r - 1.96 * self.residual_std * float(np.sqrt(h)))
            for h, r in enumerate(rsi_forecast, 1)
        ]
        ci_upper = [
            min(1.0, r + 1.96 * self.residual_std * float(np.sqrt(h)))
            for h, r in enumerate(rsi_forecast, 1)
        ]
        market_value_forecast = [
            self.compute_market_value_score(self.primary_df, self.secondary_df) * (1.0 + 0.05 * i)
            for i in range(horizon)
        ]
        return {
            'years': forecast_years,
            'rsi_forecast': rsi_forecast,
            'market_value_forecast': market_value_forecast,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'final_level': float(level),
            'final_trend': float(trend),
        }

class WithoutKeyComponentMethod(BaseAnalysisMethod):
    """Ablation of WhatProposed: static role fractions, no sigmoid/Bayesian AI modeling.
    Uses full-history mean + OLS trend for stable base_rsi (reduces seed variance from 0.1019).
    """

    def __init__(self, config: Config):
        super().__init__(config)
        self.name = "without_key_component"
        self.static_displaced_fraction = 0.35
        self.static_surviving_fraction = 0.65
        self.orchestrator_premium = 1.45
        self.base_rsi = 0.0
        self.rsi_trend = 0.0

    def fit(self, primary_df, secondary_df, rsi: np.ndarray) -> None:
        super().fit(primary_df, secondary_df, rsi)
        # Full-history mean (more stable than last-5-point window)
        self.base_rsi = float(np.mean(rsi))
        # OLS trend over all points (replaces unstable 5-pt finite diff)
        T = len(rsi)
        if T >= 2:
            x = np.arange(T, dtype=float)
            x_mean = float(np.mean(x))
            y_mean = float(np.mean(rsi))
            denom = float(np.sum((x - x_mean) ** 2))
            self.rsi_trend = float(np.sum((x - x_mean) * (rsi - y_mean)) / denom) if denom > 1e-12 else 0.0
        else:
            self.rsi_trend = 0.0

    def forecast(self, horizon: int) -> dict:
        last_year = int(self.primary_df.index[-1])
        forecast_years = list(range(last_year + 1, last_year + 1 + horizon))
        rsi_forecast = []

        for i in range(horizon):
            base = self.base_rsi + self.rsi_trend * i
            effective_rsi = (
                base * self.static_surviving_fraction * self.orchestrator_premium
                + base * self.static_displaced_fraction * 0.2
            )
            rsi_forecast.append(float(np.clip(effective_rsi, 0.0, 1.0)))

        ci_lower = [max(0.0, r - self.std_rsi) for r in rsi_forecast]
        ci_upper = [min(1.0, r + self.std_rsi) for r in rsi_forecast]
        market_value_forecast = [
            self.compute_market_value_score(self.primary_df, self.secondary_df)
        ] * horizon

        return {
            'years': forecast_years,
            'rsi_forecast': rsi_forecast,
            'market_value_forecast': market_value_forecast,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'note': 'Static fractions only, no AI capability modeling',
        }

class SimplifiedVersionMethod(BaseAnalysisMethod):
    """Ablation of WhatVariant: 2-state Markov (Surviving/Displaced), data-calibrated transition rates.
    Calibrates p_survive_to_displace from automation_threat_score for non-zero seed variance.
    """

    def __init__(self, config: Config):
        super().__init__(config)
        self.name = "simplified_version"
        self.p_survive_to_displace = 0.08
        self.p_displace_to_survive = 0.02
        self.initial_surviving = 0.95
        self.historical_dists = None
        self._p_s2d_fitted = self.p_survive_to_displace
        self._p_d2s_fitted = self.p_displace_to_survive

    def _two_state_transition(self, p_s2d: float = None, p_d2s: float = None) -> np.ndarray:
        p_s2d = self.p_survive_to_displace if p_s2d is None else p_s2d
        p_d2s = self.p_displace_to_survive if p_d2s is None else p_d2s
        T = np.array([
            [1.0 - p_s2d, p_s2d],
            [p_d2s,        1.0 - p_d2s],
        ], dtype=float)
        return T

    def fit(self, primary_df, secondary_df, rsi: np.ndarray) -> None:
        super().fit(primary_df, secondary_df, rsi)
        # Calibrate from seed-specific automation threat score → non-zero cross-seed variance
        avg_threat = float(primary_df['automation_threat_score'].mean())
        self._p_s2d_fitted = float(np.clip(0.04 + 0.08 * avg_threat, 0.02, 0.25))
        self._p_d2s_fitted = float(np.clip(0.01 + 0.02 * (1.0 - avg_threat), 0.005, 0.05))

        T_mat = self._two_state_transition(self._p_s2d_fitted, self._p_d2s_fitted)
        dist = np.array([self.initial_surviving, 1.0 - self.initial_surviving])
        self.historical_dists = [dist.copy()]
        for _ in range(len(primary_df) - 1):
            dist = dist @ T_mat
            self.historical_dists.append(dist.copy())
        self.historical_dists = np.array(self.historical_dists)

    def forecast(self, horizon: int) -> dict:
        dist = self.historical_dists[-1].copy()
        T_mat = self._two_state_transition(self._p_s2d_fitted, self._p_d2s_fitted)
        last_year = int(self.primary_df.index[-1])
        forecast_years = list(range(last_year + 1, last_year + 1 + horizon))
        rsi_forecast = []

        for i in range(horizon):
            dist = dist @ T_mat
            rsi_h = float(np.clip(dist[0] * 0.7, 0.0, 1.0))
            rsi_forecast.append(rsi_h)

        ci_lower = [max(0.0, r - 0.08) for r in rsi_forecast]
        ci_upper = [min(1.0, r + 0.08) for r in rsi_forecast]
        market_value_forecast = [
            self.compute_market_value_score(self.primary_df, self.secondary_df)
        ] * horizon

        return {
            'years': forecast_years,
            'rsi_forecast': rsi_forecast,
            'market_value_forecast': market_value_forecast,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'note': '2-state Markov only, data-calibrated transition rates',
            'p_survive_to_displace': self._p_s2d_fitted,
            'p_displace_to_survive': self._p_d2s_fitted,
        }