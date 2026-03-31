class Config:
    def __init__(self):
        self.random_seeds = [0, 1, 2]
        self.n_years_forecast = 10
        self.base_year = 2024
        self.n_simulations = 1000
        self.market_growth_rate = 0.15
        self.ai_adoption_rate = 0.25
        self.presales_headcount_2024 = 250000
        self.skill_decay_rate = 0.10
        self.reskilling_rate = 0.35
        self.primary_metric = "role_survival_index"
        self.secondary_metric = "market_value_score"
        self.output_dir = "results"
        self.results_file = "results.json"
        self.time_budget_hours = 4
        self.conditions = [
            "what_proposed",
            "what_variant",
            "what_baseline_1",
            "what_baseline_2",
            "without_key_component",
            "simplified_version",
        ]
        self.topic = (
            "what is the future of SAAS presales engineers "
            "what will they evolve and market patterns analysis "
            "and forecast also impact by AI"
        )
        self.saas_market_size_2024_billions = 250.0
        self.saas_market_size_2034_billions = 1000.0
        self.avg_salary_min_usd = 80000
        self.avg_salary_max_usd = 180000
        self.noise_sigma_fraction = 0.05
        self.ai_capability_midpoint_year = 2025
        self.ai_capability_steepness = 0.8
        self.headcount_peak_year = 2027
        self.headcount_decline_rate = 0.04
        self.skill_demand_shift_start = 2020
        self.orchestrator_weight = 1.0
        self.hybrid_weight = 0.6
        self.traditional_weight = 0.3
        self.displaced_weight = 0.0