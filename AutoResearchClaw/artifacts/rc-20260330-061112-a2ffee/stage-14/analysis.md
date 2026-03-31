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

| Check | Status | Notes |
|---|---|---|
| Sample size adequacy | **FAIL** | n=1 per condition; 3 seeds ≠ 3 replications if deterministic |
| Confidence intervals | **ABSENT** | No CI reported anywhere |
| Significance testing | **ABSENT** | No p-values, no effect size estimates |
| Multiple comparison correction | **ABSENT** | 6 conditions × 3 seeds × 2 metrics ≈ 50 values; no FDR control |
| Seed sensitivity analysis | **PARTIAL** | 3 seeds run but sweep is too narrow; `without_key_component` std=0.1019 flags instability |
| Internal consistency | **PASS** | Results are deterministically reproducible given same seeds |
| Metric range validity | **UNVERIFIED** | `role_survival_index` [0,1] and `market_value_score` units unvalidated against real data |

The statistical infrastructure for this experiment is insufficient to support any inferential claim. The results can be described as outputs of a model under specific parameterizations — nothing more.

---

## Methodology Audit

**Severity-ranked issues:**

**P0 — Blocks interpretation entirely:**
1. Condition definitions not disclosed — comparisons have no semantic content
2. `role_survival_index` formula and inputs not disclosed — construct validity cannot be assessed
3. No real-world benchmark condition — no calibration to published labor market data

**P1 — Undermines quantitative confidence:**
4. n=1 with 3 seeds is insufficient; minimum 30 samples with CI required
5. Secondary metric is seed-determined; must be decoupled or removed
6. `simplified_version` zero-variance is unexplained
7. Seed sweep too narrow for `without_key_component` (std=0.1019)

**P2 — Limits scope of conclusions:**
8. Single-component ablation; no interaction effects measurable
9. No task-level granularity — cannot test the stated hypothesis (automation risk stratified by task type)
10. Formula-based execution not labeled as such; creates false impression of empirical simulation

---

## Limitations

1. **The experiment cannot test its own primary hypothesis.** Hypothesis 1 posits that automation risk is stratified *by task type*, but `role_survival_index` is an aggregate role-level outcome. No task-level decomposition exists in the results. The experiment's outputs are orthogonal to the claim being tested.

2. **External validity is zero until calibration is demonstrated.** The scoring function encodes assumptions. Until those assumptions are shown to track real presales labor market behavior (headcount data, hiring trends, role evolution surveys), the numerical outputs have no predictive standing for real practitioners or policymakers.

3. **The condition hierarchy is opaque.** The ordering `what_proposed` < `what_variant` ≈ `simplified_version` < `what_baseline_1` < `what_baseline_2` < `without_key_component` implies an interpretive ladder that the experiment never discloses. Without a stated logic for this ordering, neither the bottom (0.021) nor the top (0.706) can be positioned as a policy-relevant bound.

4. **Conflated constructs in the primary metric.** Headcount survival, role redefinition, and compensation trajectory are collapsed into a single index. A presales function that survives but is deskilled scores the same as one that survives and gains influence — opposite real-world outcomes, identical numerical treatment.

---

## Conclusion

**Result Quality Rating: 3/10**

**Justification:** The experiment is internally consistent and technically reproducible — credit for those properties. However, the core deliverable (evidence about presales role survival under AI disruption) is not achievable from the current design. The primary metric is undisclosed and unvalidated, the conditions are unlabeled, the secondary metric is a confound, the ablation logic is inverted without explanation, and the experiment does not measure the hypothesis it states. The optimist correctly identifies that a large effect size exists in the data — but effect size without interpretable conditions and validated metrics is noise that happens to be large.

**Three key findings that survive scrutiny:**
1. The model is sensitive enough to produce a wide range of outcomes (0.021–0.706) — discriminant validity of the instrument is plausible, though unconfirmed
2. Seed sensitivity is highly heterogeneous across conditions — this structural property is real and requires explanation
3. The secondary metric (`market_value_score`) is condition-independent — this is a definite finding about the experiment design, though not about the real world

**Recommendation: REFINE**

Not PROCEED — the current outputs cannot support any claim about the real presales labor market and should not be presented as findings. Not PIVOT — the research question is valid and important, and the scaffold of conditions and metrics is a reasonable starting point.

**Required before any re-run:**
1. Publish condition definitions in plain language — what does each scenario assume about AI adoption rate, buyer behavior, and presales role scope?
2. Publish the `role_survival_index` formula and justify its components against real labor market indicators
3. Add a minimum of one condition anchored to a published forecast (BLS, Gartner, or McKinsey automation risk estimates)
4. Expand seed sweep to ≥20 seeds; report full distributions, not means alone
5. Add a task-level decomposition sub-metric to make the experiment capable of testing Hypothesis 1

Once these five changes are implemented, the experiment would be well-positioned for a meaningful run. The research question — whether presales automation risk is task-stratified rather than role-stratified, and whether the SaaS presales function survives AI disruption in meaningful form — is substantively important and under-studied. The work is worth refining.