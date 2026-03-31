---

## Peer Review: APEX: SaaS Presales Engineers Will Not Disappear — They Will Bifurcate

---

### Reviewer A — Methodology Expert

**Summary:** APEX is a parametric ablation scaffold for characterizing AI-driven displacement sensitivity across six adoption scenarios for SaaS presales engineers. The central output is a Role Survival Index (RSI ∈ [0,1]) evaluated at 3 random seeds × 6 conditions = 18 runs.

**Strengths:**

- The ablation design (six conditions spanning an AI-free counterfactual to full replacement) is logically structured and the RSI formulation is analytically transparent: the linear functional $\text{RSI}(s) = \sum_k \beta_k(1 - s\alpha_k)$ makes sensitivity behavior directly interpretable.
- The paper commendably self-discloses the `market_value_score` coupling defect (Section 5.3/6.3) rather than burying it, which reflects scientific integrity.
- Tables 1–5 are consistently formatted and the condition abbreviations are used coherently throughout.

**Weaknesses:**

1. **Structural duplication — Section 3 appears twice.** The paper contains two full versions of "3. Method: The APEX Framework" (one shorter version ending around line 84 of the draft, and a longer expanded version later). This is a clear editorial error that must be resolved before submission. Only one version of Section 3 should appear.

2. **`what_proposed` is the worst-performing condition.** In ML paper conventions, the "proposed" method should represent the contribution being advocated. Here, `what_proposed` = Full AI Replacement (RSI = 0.021) is the floor, not the claimed contribution. This labeling creates interpretive confusion and should be redesigned. The actual methodological contribution is APEX itself, not any one condition.

3. **The $\alpha_k$ and $\beta_k$ vectors are never published.** Section 3.3 describes how they are derived but the actual numerical values are absent from both the paper and the provided results.json. Without these, the model is not reproducible despite the claim in Section 3.4 that "complete experimental code, parameter files, and seed configurations will be released upon publication." Reviewers cannot assess calibration quality.

4. **Sigmoid normalization distorts the linear RSI.** The paper derives $\text{RSI}(s)$ as a linear function of $s$ in Section 3.1 (allowing analytical sensitivity computation), but then applies a sigmoid transformation in Stage 2 that breaks this linearity. The reported RSI values are post-sigmoid, so the "analytically transparent" claim in Section 3.4 applies only to the pre-transformation raw RSI, not the reported metric.

**Actionable Revisions:**

- Remove the duplicate Section 3 before resubmission.
- Publish the full $\alpha_k$, $\beta_k$ weight table as either a numbered table or supplementary material.
- Rename `what_proposed` to a label that does not imply it is the advocated method (e.g., `full_replacement` or `FAR` consistently).
- Clarify in the abstract and Section 3.1 that the reported RSI is sigmoid-transformed and thus non-linear in $s$, or explain why the linearity claim still holds post-transformation.

---

### Reviewer B — Domain Expert (SaaS Labor Markets / Future of Work)

**Summary:** The paper makes a topical and currently underserved argument: that the SaaS presales function should be modeled at the subtask level rather than the occupation-code level for AI displacement analysis. The bifurcation thesis (augmentation vs. replacement regime) is directionally consistent with emerging practitioner observations.

**Strengths:**

- The identification of the presales function as a gap in automation-risk literature is well-motivated. The critique of BLS SOC 41-9031 (Sales Engineers) as obscuring internal task heterogeneity is accurate and relevant.
- The paper's framing of deal-size and PLG conditionality (Section 1, paragraph 2) reflects genuine nuance in how enterprise vs. self-serve SaaS markets differ in presales headcount dynamics.
- The bimodal augmentation/replacement regime finding (Table 4, between-regime RSI gap = 0.456) is the paper's most substantively interesting result for workforce planners, and Section 6's discussion of why override policies provide negligible survival benefit (PAR vs. HAO delta = 0.020) is a non-obvious and well-argued finding.

**Weaknesses:**

1. **Topic drift: market patterns analysis is absent.** The stated topic includes "market patterns analysis and forecast." The secondary metric (`market_value_score`) was intended to capture TAM dynamics but is explicitly confirmed to be condition-invariant and uninformative (Sections 5.3, 7). The paper therefore delivers a role survival sensitivity model but not a market forecast. The title and framing should either drop the market forecast claim or APEX must be revised to actually model market trajectory.

2. **"Bifurcation" claim is overstated.** The title asserts presales engineers "will bifurcate," implying a prediction about the labor market. The paper consistently clarifies that APEX produces a sensitivity probe, not an empirical forecast. The title sets an expectation the paper explicitly declines to fulfill. A more accurate title would reflect the conditional and parametric nature of the results.

3. **No treatment of deal-size heterogeneity despite being raised.** The introduction mentions that PLG alternatives make automation risk "conditional on deal size, buyer sophistication" (Section 1), but the APEX task portfolio ($K=6$) does not stratify by deal size. Enterprise discovery vs. SMB discovery likely have different $\alpha_k$ values, but these are collapsed into single weights. The paper raises this as a theoretical distinction but does not operationalize it.

4. **The "30–60% technically automatable by 2030" McKinsey claim in the introduction cites [johnk2020ready], which appears to be a 2020 readiness paper — not a McKinsey automation forecast.** This citation should be verified or replaced with the correct source (McKinsey Global Institute 2023 generative AI report or equivalent).

**Actionable Revisions:**

- Revise the title to eliminate the forward-looking "will bifurcate" framing or explicitly scope it as "under APEX-parameterized assumptions."
- Either add a market trajectory model to the secondary metric or remove the market forecast claim from the abstract and introduction.
- Add a paragraph in Section 3 (or Limitations) acknowledging that deal-size stratification is absent from the current APEX parameterization, with a concrete proposal for how $\alpha_k$ would differ across SMB vs. enterprise deal segments.
- Verify the McKinsey citation in Section 1.

---

### Reviewer C — Statistics / Rigor Expert

**Summary:** APEX uses n=3 seeds and reports pairwise paired t-tests with df=2. Statistical power is severely limited. Several claims require qualification.

**Strengths:**

- The paper correctly identifies that n=3 limits within-regime statistical power (Limitations, Section 7) and avoids overclaiming significance for the AFC vs. C24 and AFC vs. CAB comparisons (t=3.05–3.89, p=0.060–0.093).
- Seed standard deviation as a stability indicator is a reasonable proxy for sensitivity analysis in a deterministic model, and the seed sensitivity asymmetry finding (AFC σ=0.102 vs. replacement conditions σ≤0.001) is correctly interpreted as a structural behavioral difference, not random noise.
- The explicit exclusion of `market_value_score` from comparative analysis on the basis of confirmed condition-invariance is statistically correct and transparently disclosed.

**Weaknesses:**

1. **n=3 is insufficient for the t-tests reported.** With df=2, the critical t-value at p=0.05 is 4.303, which the paper notes. However, the paper still reports t=54.3 (p<0.001) for CAB vs. FAR and t=22.7 (p=0.002) for C24 vs. FAR, presenting these as "statistically significant" without noting that APEX is a deterministic function — the three "replicates" differ only in the seed-controlled Stage 3 market draw, which does not affect RSI. Therefore for the FAR and PAR conditions (near-zero seed variance), the three observations are essentially identical, making the paired t-test inapplicable. A t-statistic of 54.3 with n=3 is an artifact of near-zero within-condition variance, not evidence of statistical robustness.

2. **No confidence intervals reported anywhere.** The abstract reports "RSI = 0.021" and "RSI = 0.706" as point estimates; Table 3 reports ± std, but no confidence intervals appear for any primary claim. At minimum, 95% CIs around the mean RSI for each condition should be provided.

3. **The PAR vs. HAO comparison is reported as "Yes* (significant)" but is flagged as a model defect.** Including this comparison in Table 5 at all is misleading — a footnote demotion is insufficient. A result that achieves "significance" purely because one condition has zero variance by design should be excluded from the statistical comparison table, not asterisked.

4. **The 34× range is the headline discriminant claim, but it conflates two different sources of variation.** The 34× range (0.021 to 0.706) reflects the designed span of the $s$ parameter across conditions — it is an input property of the ablation design, not an emergent finding. Calling this a "methodological contribution" (Introduction, Contribution 2) overstates what is demonstrated: any scoring function with a sufficiently wide parameter range will show large output sensitivity. The meaningful discriminant finding is the bimodal regime structure, not the total range.

5. **The paper claims "three random seeds" provide a "seed sensitivity distribution" (Section 3.4), but three points do not constitute a distribution in any meaningful statistical sense.** The Limitations acknowledge needing 10–15 seeds; this should be moved to a caveat in the abstract.

**Actionable Revisions:**

- Remove the near-zero-variance conditions (FAR, PAR, HAO) from the paired t-test table entirely, or add a clear statement that the t-test is inapplicable when within-condition variance is seed-determined and RSI is condition-invariant under those seeds.
- Add 95% confidence intervals to Table 3 (even with n=3: $\bar{x} \pm t_{0.025,2} \cdot s/\sqrt{3}$).
- Reframe the "34× range" claim: clarify that the range is a property of the parameter space design, and the emergent finding is the between-regime discontinuity (RSI gap = 0.456, Table 4).
- Add to the abstract a one-sentence caveat that "statistical comparisons are conducted with n=3 seeds and should be treated as preliminary."
- Move the 10–15 seed requirement from Limitations to Section 4.3 as a prospective power analysis.

---

### Cross-Cutting Issues (All Reviewers)

| Issue | Severity | Section |
|---|---|---|
| Duplicate Section 3 in submitted draft | **Major — reject risk** | §3 (both versions) |
| $\alpha_k$, $\beta_k$ vectors unpublished | **Major** | §3.3 |
| `what_proposed` label maps to worst condition | **Moderate** | §3.2, Tables |
| Market forecast claim unfulfilled | **Moderate** | Abstract, §1 |
| Title overclaims a forward prediction | **Moderate** | Title |
| n=3 t-tests with near-zero within-condition variance are inapplicable | **Moderate** | §5.3, Table 5 |
| No confidence intervals | **Minor** | Tables 3–5 |
| McKinsey citation via [johnk2020ready] requires verification | **Minor** | §1 |
| Limitations section uses bullet/bold-header format rather than prose | **Minor — style** | §7 |
| No citations in §4 (Experimental Setup) | **Minor** | §4 |

**Recommendation:** Major revisions required. The core sensitivity analysis is sound and the self-disclosure of metric design defects reflects appropriate scientific transparency. The duplicate Section 3, the missing weight vectors, the inapplicable t-tests for near-deterministic conditions, and the unfulfilled market forecast claim must each be resolved before this work is suitable for publication.