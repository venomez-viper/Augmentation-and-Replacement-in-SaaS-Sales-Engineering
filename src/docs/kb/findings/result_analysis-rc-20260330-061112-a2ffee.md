---
created: '2026-03-30T23:16:15+00:00'
evidence:
- stage-14/analysis.md
- stage-14/experiment_summary.json
- stage-14/results_table.tex
id: result_analysis-rc-20260330-061112-a2ffee
run_id: rc-20260330-061112-a2ffee
stage: 14-result_analysis
tags:
- result_analysis
- stage-14
- run-rc-20260
title: 'Stage 14: Result Analysis'
---

# Stage 14: Result Analysis

## Unified Research Assessment: SaaS Presales Engineers Under AI Disruption

**Research Director Synthesis — Three-Perspective Integration**

---

## Metrics Summary

| Condition | Primary (role_survival_index) | Seed Std | Secondary (market_value_score) |
|---|---|---|---|
| `without_key_component` | 0.706 | 0.1019 | ~17.5–21B (seed-determined) |
| `what_baseline_2` | 0.535 | 0.025 | ~17.5–21B (seed-determined) |
| `what_baseline_1` | 0.461 | 0.0109 | ~17.5–21B (seed-determined) |
| `simplified_version` | 0.1647 | 0.000 | ~17.5–21B (seed-determined) |
| `what_variant` | 0.1447 | 0.0002 | ~17.5–21B (seed-determined) |
| `what_proposed` | 0.0207 | 0.0011 | ~17.5–21B (seed-determined) |

**Critical observation confirmed by all three perspectives:** The secondary metric (`market_value_score`) is entirely seed-determined and condition-independent. It carries no information about condition effects and should be set aside in any interpretation.

---

## Consensus Findings

All three perspectives agree on the following, with no meaningful dissent:

**1. The experiment is a deterministic formula evaluation, not an empirical simulation.**
The 1.06-second elapsed time across 18 runs is conclusive. The outputs encode the assumptions of whoever wrote the scoring function. No real-world data was consumed. This is not a criticism that invalidates the work — parametric models can be useful — but it means all results are downstream of assumptions, not observations. The optimist's framing of findings as "empirically quantified" is therefore premature.

**2. The secondary metric is uninformative as a condition effect.**
The three seed-specific values (17.563, 18.794, 20.958) appear identically across every condition. This is not a finding about market stability under disruption; it is a structural artifact of how the seed influences the market value computation. The optimist's inference that "economic activity is preserved and redistributing" is not supported — the metric cannot distinguish between conditions.

**3. Condition definitions are absent, making numerical comparisons uninterpretable in isolation.**
The gap between `what_proposed` (0.021) and `without_key_component` (0.706) is the experiment's most prominent result. All three perspectives identify that this comparison is currently uninterpretable without knowing what each condition models. The skeptic and methodologist identify this as a P0 failure; even the optimist's analysis implicitly assumes a specific interpretation (AI disruption mechanism = key component) that is not confirmed in the data.

**4. `simplified_version`'s zero variance across seeds is anomalous.**
No perspective disputes this. Either the condition has a coding defect (seed not consumed) or it has a closed-form output that must be explicitly documented. The condition as reported cannot be used as evidence either way.

---

## Contested Points

**Contested: Is the `without_key_component` result interpretable at all?**

- *Optimist position:* The ablation is informative because it reveals that removing AI disruption dramatically improves survival — this is a "known lever."
- *Skeptic/methodologist position:* The inverted ablation logic (removing a "key component" should degrade performance, not improve it) means the naming is either misleading or the condition hierarchy is undisclosed. The result cannot be directionally interpreted without knowing what the component is.

**Judgment:** The skeptic/methodologist position prevails here. The optimist's interpretation requires assuming that "key component" = "AI disruption mechanism," which may be correct but is not stated. Until condition definitions are published, the 34x gap cannot be characterized as a finding about a "known lever." It could equally be an artifact of a misconfigured condition ordering.

**Contested: Does seed-to-seed variation within `without_key_component` (range 0.224) undermine the result?**

- *Skeptic position:* The spread is alarming — the aggregate mean of 0.706 is not robust.
- *Optimist position:* The variation at least confirms the metric is sensitive to inputs, which is better than a flat metric.

**Judgment:** Both are partly right. High seed sensitivity in one condition but near-zero sensitivity in others (especially `what_proposed` std=0.0011) suggests the conditions are operating under structurally different variance regimes. This is neither pure good news nor pure bad news — it is an uncharacterized heterogeneity that requires a broader seed sweep before the `without_key_component` mean can be reported with any confidence.

**Contested: Does the optimist's inference that "market value is redistributing, not disappearing" have any evidential basis?**

**Judgment:** No. The secondary metric is seed-determined. The optimist's framing reads genuine meaning into a confound. This inference should be retracted until `market_value_score` is decoupled from seed initialization.

---

## Statistical Checks

| Check | Status | 

... (truncated, see full artifact)


{
  "metrics_summary": {
    "primary_metric": {
      "min": 0.1647,
      "max": 0.1647,
      "mean": 0.1647,
      "count": 1
    },
    "primary_metric_mean": {
      "min": 0.1647,
      "max": 0.1647,
      "mean": 0.1647,
      "count": 1
    },
    "primary_metric_std": {
      "min": 0.0,
      "max": 0.0,
      "mean": 0.0,
      "count": 1
    },
    "secondary_metric": {
      "min": 20.9579,
      "max": 20.9579,
      "mean": 20.9579,
      "count": 1
    },
    "simplified_version/123/primary_metric": {
      "min": 0.1647,
      "max": 0.1647,
      "mean": 0.1647,
      "count": 1
    },
    "simplified_version/123/secondary_metric": {
      "min": 18.7938,
      "max": 18.7938,
      "mean": 18.7938,
      "count": 1
    },
    "simplified_version/42/primary_metric": {
      "min": 0.1647,
      "max": 0.1647,
      "mean": 0.1647,
      "count": 1
    },
    "simplified_version/42/secondary_metric": {
      "min": 17.563,
      "max": 17.563,
      "mean": 17.563,
      "count": 1
    },
    "simplified_version/456/primary_metric": {
      "min": 0.1647,
      "max": 0.1647,
      "mean": 0.1647,
      "count": 1
    },
    "simplified_version/456/secondary_metric": {
      "min": 20.9579,
      "max": 20.9579,
      "mean": 20.9579,
      "count": 1
    },
    "simplified_version/primary_metric": {
      "min": 0.1647,
      "max": 0.1647,
      "mean": 0.1647,
      "count": 1
    },
    "simplified_version/primary_metric_mean": {
      "min": 0.1647,
      "max": 0.1647,
      "mean": 0.1647,
      "count": 1
    },
    "simplified_version/primary_metric_std": {
      "min": 0.0,
      "max": 0.0,
      "mean": 0.0,
      "count": 1
    },
    "simplified_version/secondary_metric": {
      "min": 20.9579,
      "max": 20.9579,
      "mean": 20.9579,
      "count": 1
    },
    "what_baseline_1/123/primary_metric": {
      "min": 0.4734,
      "max": 0.4734,
      "mean": 0.4734,
      "count": 1
    },
    "what_baseline_1/123/secondary_metric": {
      "min": 18.7938,
      "max": 18.7938,
      "mean": 18.7938,
      "count": 1
    },
    "what_baseline_1/42/primary_metric": {
      "min": 0.4469,
      "max": 0.4469,
      "mean": 0.4469,
      "count": 1
    },
    "what_baseline_1/42/secondary_metric": {
      "min": 17.563,
      "max": 17.563,
      "mean": 17.563,
      "count": 1
    },
    "what_baseline_1/456/primary_metric": {
      "min": 0.4623,
      "max": 0.4623,
      "mean": 0.4623,
      "count": 1
    },
    "what_baseline_1/456/secondary_metric": {
      "min": 20.9579,
      "max": 20.9579,
      "mean": 20.9579,
      "count": 1
    },
    "what_baseline_1/primary_metric": {
      "min": 0.4623,
      "max": 0.4623,
      "mean": 0.4623,
      "count": 1
    },
    "what_baseline_1/primary_metric_mean": {
      "min": 0.4609,
      "max": 0.4609,
      "mean": 0.4609,
      "count": 1
    },
    "what_baseline_1/primary_metric_std": {
      "min": 0.0109,
      "max": 0.0109,
      "mean": 0.0109,
      "count": 1
    },
    "what_baseline_1/secondary_metric": {
      "min": 20.9579,
      "max": 20.9579,
      "mean": 20.9579,
      "count": 1
    },
    "what_baseline_2/123/primary_metric": {
      "min": 0.5511,
      "max": 0.5511,
      "mean": 0.5511,
      "count": 1
    },
    "what_baseline_2/123/secondary_metric": {
      "min": 18.7938,
      "max": 18.7938,
      "mean": 18.7938,
      "count": 1
    },
    "what_baseline_2/42/primary_metric": {
      "min": 0.4992,
      "max": 0.4992,
      "mean": 0.4992,
      "count": 1
    },
    "what_baseline_2/42/secondary_metric": {
      "min": 17.563,
      "max": 17.563,
      "mean": 17.563,
      "count": 1
    },
    "what_baseline_2/456/primary_metric": {
      "min": 0.5534,
      "max": 0.5534,
      "mean": 0.5534,
      "count": 1
    },
    "what_baseline_2/456/secondary_metric": {
      "min": 20.9579,
      "max": 20.9579,
      "mean": 20.9579,
      "count": 1
    },
    "what_baseline_2/primary_metric": {
      "min": 0.5534,
      "max": 0.5534,
      "mean": 0.5534,
      "count": 1
    },
    "what_baseline_2/primary_metric_mean": {
      "min": 0.5346,
      "max": 0.5346,
      "mean": 0.5346,
      "count": 1
    },
    "what_baseline_2/primary_metric_std": {
      "min": 0.025,
      "max": 0.025,
      "mean": 0.025,
      "count": 1
    },
    "what_baseline_2/secondary_metric": {
      "min": 20.9579,
      "max": 20.9579,
      "mean": 20.9579,
      "count": 1
    },
    "what_proposed/123/primary_metric": {
      "min": 0.0193,
      "max": 0.0193,
      "mean": 0.0193,
      "count": 1
    },
    "what_proposed/123/secondary_metric": {
      "min": 18.7938,
      "max": 18.7938,
      "mean": 18.7938,
      "count": 1
    },
    "what_proposed/42/primary_metric": {
      "min": 0.0207,
      "max": 0.0207,
      "mean": 0.0207,
      "count": 1
    },
    "what_proposed/42/secondary_metric": {
      "min": 17.563,
      "max": 17.563,
      "mean": 17.563,
      "count": 1
  

... (truncated, see full artifact)


\begin{table}[h]
\centering
\caption{Experiment Results}
\begin{tabular}{lrrrr}
\hline
Metric & Min & Max & Mean & N \\
\hline
primary_metric & 0.1647 & 0.1647 & 0.1647 & 1 \\
primary_metric_mean & 0.1647 & 0.1647 & 0.1647 & 1 \\
primary_metric_std & 0.0000 & 0.0000 & 0.0000 & 1 \\
secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
simplified_version/123/primary_metric & 0.1647 & 0.1647 & 0.1647 & 1 \\
simplified_version/123/secondary_metric & 18.7938 & 18.7938 & 18.7938 & 1 \\
simplified_version/42/primary_metric & 0.1647 & 0.1647 & 0.1647 & 1 \\
simplified_version/42/secondary_metric & 17.5630 & 17.5630 & 17.5630 & 1 \\
simplified_version/456/primary_metric & 0.1647 & 0.1647 & 0.1647 & 1 \\
simplified_version/456/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
simplified_version/primary_metric & 0.1647 & 0.1647 & 0.1647 & 1 \\
simplified_version/primary_metric_mean & 0.1647 & 0.1647 & 0.1647 & 1 \\
simplified_version/primary_metric_std & 0.0000 & 0.0000 & 0.0000 & 1 \\
simplified_version/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_baseline_1/123/primary_metric & 0.4734 & 0.4734 & 0.4734 & 1 \\
what_baseline_1/123/secondary_metric & 18.7938 & 18.7938 & 18.7938 & 1 \\
what_baseline_1/42/primary_metric & 0.4469 & 0.4469 & 0.4469 & 1 \\
what_baseline_1/42/secondary_metric & 17.5630 & 17.5630 & 17.5630 & 1 \\
what_baseline_1/456/primary_metric & 0.4623 & 0.4623 & 0.4623 & 1 \\
what_baseline_1/456/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_baseline_1/primary_metric & 0.4623 & 0.4623 & 0.4623 & 1 \\
what_baseline_1/primary_metric_mean & 0.4609 & 0.4609 & 0.4609 & 1 \\
what_baseline_1/primary_metric_std & 0.0109 & 0.0109 & 0.0109 & 1 \\
what_baseline_1/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_baseline_2/123/primary_metric & 0.5511 & 0.5511 & 0.5511 & 1 \\
what_baseline_2/123/secondary_metric & 18.7938 & 18.7938 & 18.7938 & 1 \\
what_baseline_2/42/primary_metric & 0.4992 & 0.4992 & 0.4992 & 1 \\
what_baseline_2/42/secondary_metric & 17.5630 & 17.5630 & 17.5630 & 1 \\
what_baseline_2/456/primary_metric & 0.5534 & 0.5534 & 0.5534 & 1 \\
what_baseline_2/456/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_baseline_2/primary_metric & 0.5534 & 0.5534 & 0.5534 & 1 \\
what_baseline_2/primary_metric_mean & 0.5346 & 0.5346 & 0.5346 & 1 \\
what_baseline_2/primary_metric_std & 0.0250 & 0.0250 & 0.0250 & 1 \\
what_baseline_2/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_proposed/123/primary_metric & 0.0193 & 0.0193 & 0.0193 & 1 \\
what_proposed/123/secondary_metric & 18.7938 & 18.7938 & 18.7938 & 1 \\
what_proposed/42/primary_metric & 0.0207 & 0.0207 & 0.0207 & 1 \\
what_proposed/42/secondary_metric & 17.5630 & 17.5630 & 17.5630 & 1 \\
what_proposed/456/primary_metric & 0.0220 & 0.0220 & 0.0220 & 1 \\
what_proposed/456/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_proposed/primary_metric & 0.0220 & 0.0220 & 0.0220 & 1 \\
what_proposed/primary_metric_mean & 0.0207 & 0.0207 & 0.0207 & 1 \\
what_proposed/primary_metric_std & 0.0011 & 0.0011 & 0.0011 & 1 \\
what_proposed/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_variant/123/primary_metric & 0.1445 & 0.1445 & 0.1445 & 1 \\
what_variant/123/secondary_metric & 18.7938 & 18.7938 & 18.7938 & 1 \\
what_variant/42/primary_metric & 0.1446 & 0.1446 & 0.1446 & 1 \\
what_variant/42/secondary_metric & 17.5630 & 17.5630 & 17.5630 & 1 \\
what_variant/456/primary_metric & 0.1450 & 0.1450 & 0.1450 & 1 \\
what_variant/456/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
what_variant/primary_metric & 0.1450 & 0.1450 & 0.1450 & 1 \\
what_variant/primary_metric_mean & 0.1447 & 0.1447 & 0.1447 & 1 \\
what_variant/primary_metric_std & 0.0002 & 0.0002 & 0.0002 & 1 \\
what_variant/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
without_key_component/123/primary_metric & 0.7862 & 0.7862 & 0.7862 & 1 \\
without_key_component/123/secondary_metric & 18.7938 & 18.7938 & 18.7938 & 1 \\
without_key_component/42/primary_metric & 0.5625 & 0.5625 & 0.5625 & 1 \\
without_key_component/42/secondary_metric & 17.5630 & 17.5630 & 17.5630 & 1 \\
without_key_component/456/primary_metric & 0.7701 & 0.7701 & 0.7701 & 1 \\
without_key_component/456/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
without_key_component/primary_metric & 0.7701 & 0.7701 & 0.7701 & 1 \\
without_key_component/primary_metric_mean & 0.7063 & 0.7063 & 0.7063 & 1 \\
without_key_component/primary_metric_std & 0.1019 & 0.1019 & 0.1019 & 1 \\
without_key_component/secondary_metric & 20.9579 & 20.9579 & 20.9579 & 1 \\
\hline
\end{tabular}
\end{table}