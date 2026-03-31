[thinking] Let me read the file as requested.


## Final Research Proposal: SaaS Presales Engineers Under AI Disruption

**Synthesized from Innovator, Pragmatist, and Contrarian Perspectives**

---

## Synthesis Strategy

The three perspectives do not converge on a shared optimistic or pessimistic view — and that disagreement is the most important signal. The innovator projects skill elevation and role transformation. The pragmatist offers concrete measurement tools to test those claims. The contrarian argues the transformation narrative is structurally unfounded and the likely outcome is net role shrinkage. The final hypotheses below take the innovator's most falsifiable structural claims, ground them in the pragmatist's executable methodology, and build in the contrarian's displacement mechanisms as explicit alternative outcomes — rather than dismissing them.

**One unresolved disagreement is preserved explicitly:** Whether buyer sophistication increases or decreases demand for presales engineers is genuinely contested, with valid evidence on both sides. This is not flattened into a compromise.

---

## Final Hypothesis 1 — Presales Automation Risk Is Stratified by Task Type, Not Role Level: A Measurable Taxonomy Exists and Differs from Current Industry Forecasts

**Rationale:**

The innovator's hourglass model and the contrarian's shrinkage model both rest on an unmeasured empirical foundation: which presales tasks are actually automatable, at what rate, and for which buyer contexts. The pragmatist correctly identifies this as Gap 1 and proposes an LLM-based classification methodology to fill it. This hypothesis is the necessary foundation for all downstream workforce predictions — without it, both the bifurcation narrative and the shrinkage narrative are speculative.

The contrarian raises a critical refinement: the unit of analysis should not be skill level (Tier 1 vs. Tier 2) but deal segment (SMB/mid-market vs. enterprise). The PLG evidence suggests that automation risk is not uniform across presales tasks in the abstract — it is conditional on deal size, buyer sophistication, and the availability of self-serve alternatives. This conditionality is absent from both the innovator's and pragmatist's framings and must be built into the classification rubric.

**Methodology (Incorporating Pragmatist's Design):**

1. Construct a canonical presales task taxonomy (~80–100 tasks) from 300+ job postings (LinkedIn/Indeed), stratified by deal segment (SMB ACV <$50K; mid-market $50K–$250K; enterprise >$250K).
2. Rate each task on a structured rubric: automation feasibility, buyer-context dependency, judgment intensity, deal-segment conditionality.
3. Run LLM classification (3 prompt variants, GPT-4o or Claude Sonnet) against the rubric; aggregate scores.
4. Recruit 8–10 senior presales practitioners across deal segments for human baseline ratings (Pavilion/SalesHacker community).
5. Compute Cohen's Kappa stratified by deal segment — not just overall — to detect whether automation risk profiles differ materially by segment (the contrarian's core prediction).

**Measurable Prediction:**

- Cohen's Kappa ≥ 0.70 overall (pragmatist's threshold).
- Automation risk scores for SMB/mid-market tasks will be ≥25% higher on average than enterprise task scores, confirming the contrarian's deal-segment bifurcation hypothesis over the innovator's skill-tier bifurcation hypothesis.
- At least 3 task categories (e.g., basic objection handling, sandbox setup, feature walkthroughs) will score ≥4.0/5.0 on automation feasibility across all deal segments — establishing a concrete automation floor.

**Failure Condition:**

- Rejected if Kappa < 0.50 (LLM not viable as classification proxy).
- Rejected if automation risk scores are not significantly different across deal segments (p > 0.05), which would falsify the contrarian's segmentation hypothesis and support the skill-tier bifurcation model instead.
- Rejected if no task category scores ≥3.5/5.0 on automation feasibility, which would indicate presales tasks are broadly non-automatable and undermine all displacement narratives.

**Resource Requirements:** ~$30 API spend, no GPU, 2 weeks elapsed time, 1 ML engineer + 8–10 presales practitioner volunteers.

**Unresolved Disagreement Preserved:** This study measures automation *potential* — it cannot resolve whether vendors will actually invest in automation or cut headcount instead (the contrarian's vendor incentive argument). Automation feasibility and automation deployment are distinct questions; this hypothesis addresses only the former.

---

## Final Hypothesis 2 — Adversarial POC Design Produces Measurably Higher Win Rates in Enterprise Accounts But Not in SMB/Mid-Market

**Rationale:**

The innovator's "Evaluation Architect Inversion" hypothesis is the most structurally novel claim in the set — and it has a real analogue in AI safety red-teaming practice. However, the contrarian's segmentation critique applies directly: the mechanism (trust-through-adversarial-disclosure) is plausible in enterprise accounts where procurement involves legal, security, and risk committees that reward rigor, but is implausible in SMB/mid-market where buyer psychology favors speed-to-value and adversarial framing may register as product weakness rather than trust signal.

The pragmatist's RAG methodology provides a directly applicable evaluation framework: the same blind-rating approach used to assess AI-generated objection responses can be applied to adversarially-designed vs. standard POC decks, with presales managers and procurement representatives as raters.

**Methodology:**

1. Construct paired POC materials for 10–15 representative deal scenarios: one standard (feature-forward, benefit-emphasizing) and one adversarial (explicitly surfacing 3 known product limitations with mitigation framing).
2. Recruit enterprise procurement professionals (n=20) and SMB/mid-market buyers (n=20) to evaluate the paired materials blind.
3. Rate each POC on: perceived vendor credibility, likelihood to advance to contract, trust signal strength (3-point scale).
4. Compare credibility and advancement likelihood scores between adversarial and standard POC across segments.
5. If access to live deal data exists: A/B test adversarial POC methodology on 30+ deals via Gong/Clari tracking over 90 days, stratified by deal segment.

**Measurable Prediction:**

- Enterprise segment: Adversarial POC rated ≥15% higher on perceived vendor credibility and ≥10% higher on advancement likelihood vs. standard POC.
- SMB/mid-market segment: No significant credibility advantage for adversarial POC (difference <5%), or adversarial POC rated lower on advancement likelihood.
- This segmented outcome would simultaneously validate the innovator's mechanism and confirm the contrarian's scope limitation — producing a more precise and actionable result than either perspective alone.

**Failure Condition:**

- Rejected if adversarial POC produces credibility advantages in SMB/mid-market at the same magnitude as enterprise (falsifies segmentation hypothesis, supports uniform applicability).
- Rejected if adversarial POC produces no credibility advantage in enterprise either (falsifies the innovator's core mechanism entirely — buyers do not reward adversarial transparency in any segment).
- Rejected if inter-rater reliability among procurement evaluators falls below Kappa 0.50 (evaluation criteria too ambiguous).

**Unresolved Disagreement Preserved:** The contrarian argues that sophisticated enterprise buyers will specifically exclude vendor-guided evaluation design as biased — meaning even a well-designed adversarial POC may be structurally distrusted because it originates from the vendor. This hypothesis cannot resolve whether adversarial POC design is sustainable as a practice if enterprise procurement committees begin requiring third-party evaluation validation regardless of POC quality.

---

## Final Hypothesis 3 — Presales Headcount Will Bifurcate by Deal Segment Before It Bifurcates by Skill Level: The Contrarian and Innovator Are Both Partially Right on Different Timescales

**Rationale:**

This hypothesis resolves the central tension between the innovator and contrarian by placing their predictions on different timescales and at different deal segments — rather than treating them as mutually exclusive. The contrarian is likely correct about the near-term (2025–2027): headcount will decline in SMB/mid-market driven by PLG infrastructure and AI automation, before any XAI reskilling market materializes. The innovator is likely correct about the medium-term (2027–2030) in enterprise accounts: a small, high-compensation tier of XAI-fluent presales engineers will emerge — but only after the shrinkage at lower market segments has already occurred. The hourglass shape the innovator predicts is real, but it sits on top of a smaller total workforce than current projections assume.

**Methodology:**

Longitudinal observational study using publicly available data:
1. Track LinkedIn headcount for "Solutions Engineer," "Sales Engineer," "Presales Engineer" titles quarterly from Q1 2025 to Q4 2027, stratified by employer size (SMB/mid-market vs. enterprise) using company employee count as proxy.
2. Track job posting skill requirements (Indeed/LinkedIn job postings) for XAI/AI explainability skills in presales roles, quarterly.
3. Track PLG-related role postings ("Product-Led Growth," "Self-Serve," "Developer Experience") at SaaS companies with presales headcount declines, to detect substitution patterns.
4. Correlate headcount trends with ACV tier data where available (public revenue/headcount disclosures from SaaS companies).

**Measurable Prediction:**

- By Q4 2026: SMB/mid-market SaaS presales headcount shows net negative YoY growth (contrarian's prediction confirmed at segment level).
- By Q4 2026: Enterprise presales headcount holds flat or grows (contrarian's total-shrinkage prediction partially falsified for enterprise).
- By Q4 2027: XAI/AI explainability skill requirements appear in >15% of enterprise presales postings but <10% of mid-market presales postings (innovator's bifurcation confirmed at enterprise level, not uniformly).

**Failure Condition:**

- Rejected if enterprise and SMB/mid-market presales headcount trends are indistinguishable through 2027 (segment-based bifurcation hypothesis falsified; either uniform growth or uniform shrinkage).
- Rejected if XAI skill requirements remain below 10% across all presales postings by Q4 2027 (innovator's skill-tier model falsified; shrinkage occurs without replacement by higher-value tier).
- Rejected if XAI skill requirements exceed 25% across all presales postings by Q4 2026 (contrarian's reskilling skepticism falsified; market is moving faster toward upgrade path than predicted).

---

## Unresolved Disagreements (Not Flattened)

| Disagreement | Innovator Position | Contrarian Position | Resolution Status |
|---|---|---|---|
| Will XAI fluency be a trainable presales skill? | Yes — reachable via structured upskilling programs | No — requires ML depth incompatible with presales backgrounds | **Unresolved.** Hypothesis 1 taxonomy will reveal skill-gap magnitude but not trainability. Requires separate reskilling study. |
| Does buyer sophistication help or hurt presales? | Sophisticated buyers need more expert guidance | Sophisticated buyers exclude vendor-side evaluation as biased | **Unresolved.** Hypothesis 2 tests this directly — result will determine which mechanism dominates in which segment. |
| Is PLG a substitute for presales or a complement? | PLG handles Tier 1; presales focuses on Tier 2 | PLG eliminates presales need in SMB/mid-market entirely | **Partially resolvable** via Hypothesis 3 headcount tracking — if PLG role postings rise as presales postings fall at the same companies, substitution is confirmed. |
| What is the vendor incentive equilibrium? | Vendors invest in reskilling high-value presales | Vendors cut headcount before funding reskilling | **Not addressed by any hypothesis above.** Requires primary research: interviews with VP Sales/CROs at SaaS companies about 2025–2027 workforce planning decisions. |

---

## Research Priority Ranking

| Hypothesis | Feasibility | Time to Result | Strategic Value | Priority |
|---|---|---|---|---|
| H1: Automation Risk Taxonomy | Very High (~$30, 2 weeks) | 2–3 weeks | Foundational — enables all downstream predictions | **P1** |
| H2: Adversarial POC Win Rate | Medium (requires buyer recruitment) | 90 days | High — directly actionable for presales teams | **P2** |
| H3: Segment-Based Headcount Bifurcation | High (public data) | 12–24 months | High — resolves innovator/contrarian core dispute | **P3 (start immediately, long horizon)** |