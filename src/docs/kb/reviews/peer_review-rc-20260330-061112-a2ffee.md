---
created: '2026-03-30T23:31:44+00:00'
evidence:
- stage-18/reviews.md
id: peer_review-rc-20260330-061112-a2ffee
run_id: rc-20260330-061112-a2ffee
stage: 18-peer_review
tags:
- peer_review
- stage-18
- run-rc-20260
title: 'Stage 18: Peer Review'
---

# Stage 18: Peer Review

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

2. **"Bifurcation" claim is overstated.** The title asserts presales engineers "will bifurcate," implying a prediction about the labor market. The paper consisten

... (truncated, see full artifact)
