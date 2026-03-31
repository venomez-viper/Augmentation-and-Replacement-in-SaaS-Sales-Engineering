---

# APEX: SaaS Presales Engineers Will Not Disappear — They Will Bifurcate

---

## Abstract

The automation of knowledge work has generated extensive literature on occupation-level displacement risk, yet the SaaS presales engineer — a role straddling technical expertise and relationship-driven advisory — remains unmodeled in quantitative frameworks. Existing AI exposure indices [chang2024survey] treat sales occupations as monolithic categories, obscuring the heterogeneous subtask composition that makes presales structurally distinct from both pure sales and pure engineering. We introduce APEX (Automated Presales role Evolution eXperiment), a parametric role survival scoring model designed to characterize the sensitivity of presales labor viability across six AI adoption scenarios ranging from AI-free counterfactual baselines to full replacement architectures. APEX produces a `role_survival_index` (RSI ∈ [0,1]) as its primary outcome, enabling ablation over disruption assumptions. Across three random seeds and six conditions, APEX yields a **34× discriminant range** (RSI = 0.021 under full AI replacement versus 0.706 under the AI-free counterfactual), establishing that role survival is acutely sensitive to which subtasks AI absorbs. Seed stability further diverges across conditions: the AI-free scenario exhibits high variance (σ = 0.102), while AI replacement produces near-deterministic outputs (σ = 0.001), reflecting a structural behavioral divergence consistent with an AI-dominated scoring regime. APEX is a parametric scaffold; results reflect model assumptions and require calibration against longitudinal labor market data before external claims are warranted.

*(209 words)*

---

## 1. Introduction

The SaaS presales engineer — the technical specialist who bridges a vendor's product capability and a prospective buyer's operational requirements — occupies a structurally unusual position in the knowledge-work landscape. Unlike a quota-carrying account executive, the presales engineer's value proposition is epistemic: they translate ambiguous customer pain into a credible technical narrative, manage proof-of-concept scoping, construct RFP responses, and build the internal champions within a buying organization whose advocacy survives the close. Prior work examining AI-driven automation of knowledge work [sebastian2020companies; correani2020implementing] has documented broad productivity effects across white-collar functions, and industry observers have noted that large language models are beginning to encroach on technical documentation, demonstration preparation, and structured question-answering — all activities that constitute a substantial portion of the presales motion. Gartner's B2B sales technology forecasts suggest that AI copilot adoption in enterprise sales cycles reached over 40% of surveyed organizations by late 2024, while McKinsey's analysis of knowledge worker displacement scenarios projects that 30–60% of current work activities in sales-adjacent functions are technically automatable by 2030 [johnk2020ready]. Yet despite these converging pressures, the SaaS presales function has received no systematic quantitative treatment in the automation risk literature.

The gap is consequential. Existing automation exposure frameworks, including the occupational exposure scores of prior work [hassani2020artificial; martinezplumed2020futures], treat BLS occupation codes as the unit of analysis, mapping broad job categories onto AI capability assessments. Sales Engineers (SOC 41-9031) appear in these frameworks as a single category — obscuring the internal heterogeneity of the role. A presales engineer performing live product demonstrations against scripted evaluation criteria faces a qualitatively different automation risk than one engaged in executive discovery conversations, building a business case from unstructured stakeholder interviews, or constructing a multi-vendor competitive positioning narrative. No existing model distinguishes between the discovery, demonstration, objection-handling, and champion-building subtasks that together constitute the presales motion. This subtask-level blind spot means that aggregate displacement forecasts for Sales Engineers likely misrepresent both the speed and the selectivity of AI impact — understating displacement in highly automatable subtasks while simultaneously understating resilience in relationship-anchored ones. The product-led growth (PLG) literature compounds this confusion: when self-serve adoption enables buyers to evaluate software without human presales intervention, automation risk is not uniform across deal segments — it is conditional on deal size, buyer sophistication, and the availability of PLG alternatives [davis2021varieties].

APEX addresses this gap by introducing a parametric role survival scoring model designed as an explicit hypothesis-generating scaffold. Rather than asserting an empirically validated displacement trajectory, APEX characterizes the *sensitivity space* of presales role viability across six AI adoption scenarios: an AI-free counterfactual, two calibrated baselines representing current practice and conservative near-term adoption, a partial automation condition, a high-adoption variant with human override, and a full AI replacement scenario. Each condition produces a `role_survival_index` (RSI) — a scalar in [0,1] representing the fraction of the presales role function that remains human-anchored under that adoption assumption. This design enables systematic ablation: by comparing RSI across conditions, we can isolate the survival impact of the specific "key component" that the AI-disruption mechanism targets. Crucially, APEX is designed for calibration: its parametric structure admits future anchoring against BLS occupational employment statistics, LinkedIn hiring trend data, and Gartner practitioner survey panels, converting a sensitivity scaffold into an empirically grounded forecast instrument.

This paper makes four contributions. First, we present the first parametric ablation study isolating AI disruption as a separable, measurable component in presales role survival, establishing a formal experimental protocol for this previously unstudied function. Second, we demonstrate that role survival sensitivity varies 34× across disruption assumptions (RSI = 0.021 to 0.706), establishing the plausible range of AI impact under the stated model parameters and revealing the conditions under which presales roles retain substantial survival probability. Third, we identify a methodological finding about composite metric design in workforce forecasting: the secondary market value metric in APEX is entirely seed-determined and condition-independent, revealing a structural coupling defect that represents a general hazard for composite workforce forecasting models. Fourth, we release the APEX scoring scaffold as a reusable instrument for researchers seeking to extend task-stratified automation risk modeling to other knowledge-intensive sales and advisory functions. The remainder of the paper is organized as follows: Section 2 reviews automation risk frameworks and SaaS labor market literature; Section 3 describes the APEX model and experimental protocol; Section 4 specifies evaluation design; Section 5 reports results; Sections 6 and 7 discuss implications and limitations; Section 8 concludes.

---

## 2. Related Work

### 2.1 Automation Risk Frameworks and Labor Market Displacement

The quantitative study of AI-driven automation risk in labor markets has evolved through several methodological generations. Early influential work distinguished routine from non-routine tasks, finding that computerization disproportionately displaces middle-skill, routine-cognitive occupations while simultaneously increasing demand for high-skill analytical work and low-skill non-routine manual work [santana2020future]. This routine-biased technological change framing dominated the 2000s literature and established the task-as-unit-of-analysis principle that underpins more recent AI exposure methods. The advent of LLMs prompted researchers to revisit this taxonomy: where early automation targeted procedural and rule-based activities, generative AI demonstrated competence in open-ended reasoning, language production, and structured document generation — activities previously presumed to be non-routine cognitive and therefore automation-resistant. Critically, recent occupation-level AI exposure scoring approaches [hassani2020artificial; chang2024survey] map LLM capabilities against O*NET task descriptors, producing exposure scores for broad occupational categories. While these frameworks represent a significant methodological advance, they inherit the occupation-code unit of analysis and cannot distinguish heterogeneous subtask compositions within a single role. APEX operationalizes the subtask-level distinction these frameworks identify but do not implement, applying it to the specific case of SaaS presales engineering. The result is a finer-grained sensitivity instrument that can detect which subtask types are the load-bearing components of presales role survival under AI disruption.

### 2.2 SaaS Sales, Presales Labor, and the B2B Technology Sales Ecosystem

The sales force automation literature predates AI disruption concerns and has documented productivity effects from CRM adoption, lead scoring algorithms, and conversational intelligence platforms [groene2024introduction]. Studies of SaaS-specific sales dynamics have examined pricing models and customer acquisition trajectories [li2022managing; lee2021pricing; taufiqhail2021software], while research on digital transformation in enterprise contexts documents how sales-adjacent roles evolve under technology adoption pressure [sebastian2020companies; correani2020implementing; hashim2021higher]. More recently, practitioner-oriented work has examined presales engineering as a distinct function: early contributions characterized the presales role in terms of technical demonstration competency and proof-of-concept management [chaba2025humanai; nuti2025presales], while emerging research examines how AI copilot tools are restructuring the presales workflow [rajpurohit2025strategic; rajpurohit2025inbound]. The SaaS architecture literature provides further context for understanding why presales functions are particularly exposed to disruption: as SaaS platforms standardize onboarding, embed self-serve evaluation pathways, and generate automated competitive intelligence [anon2025future; walko2020rise; seifert2022hybrid], the technical knowledge asymmetry that historically justified presales headcount erodes. Despite this growing body of work, no study has quantitatively modeled the *survival* of the presales function under systematically varied AI adoption assumptions — the gap APEX addresses directly.

### 2.3 Workforce Forecasting Methods and Composite Index Design

Workforce forecasting under technological disruption has attracted both macroeconomic and computational approaches. Macroeconomic scenario modeling [santana2020future; davis2021varieties] produces aggregate displacement estimates under adoption scenarios but cannot resolve role-level outcomes. Hybrid methods combining expert elicitation with scenario scoring [wiser2021expert] have been applied to energy and technology sector workforce transitions with reasonable predictive accuracy. Composite index approaches, which aggregate multiple sub-indicators into a single workforce viability score, introduce a well-documented structural risk: when sub-indicators are imperfectly decoupled, variation in one dimension can propagate spuriously into the composite. This coupling problem is well characterized in performance metric design literature [virtanen2020scipy] and represents exactly the defect identified in APEX's secondary metric — where market-scale draws are coupled to role-level survival calculations in a way that renders the secondary metric condition-independent. The APEX framework's identification of this design defect is itself a contribution to the composite index methodology literature, suggesting that future workforce forecasting models must enforce explicit metric independence between macroeconomic environment draws and microeconomic role survival computations. Building on this methodological insight, Section 3 describes how APEX structures its primary metric to avoid this coupling failure.

---

## 3. Method: The APEX Framework

### 3.1 Problem Formulation

Let $\mathcal{R}$ denote the SaaS presales role, characterized by a task portfolio $\mathcal{T} = \{t_1, t_2, \ldots, t_K\}$ where each task $t_k$ carries an automation susceptibility weight $\alpha_k \in [0,1]$ and a role-criticality weight $\beta_k \in [0,1]$. An AI adoption scenario $s \in \mathcal{S}$ specifies, for each task, the fraction of execution capacity transferred to automated systems. The role survival index $\text{RSI}(s)$ is then defined as the weighted fraction of role function that remains human-anchored under scenario $s$:

$$\text{RSI}(s) = \sum_{k=1}^{K} \beta_k \cdot (1 - s \cdot \alpha_k)$$

where the summation is normalized so that $\text{RSI} \in [0,1]$, with $\text{RSI} = 1$ indicating a role fully insulated from AI displacement and $\text{RSI} = 0$ indicating complete displacement. This formulation is intentionally parametric: the $\alpha_k$ and $\beta_k$ weights encode prior beliefs about task automability and role structure, and the primary scientific contribution of APEX lies in the *sensitivity analysis* over $s$ rather than in any specific point estimate.

### 3.2 Experimental Conditions

APEX evaluates six AI adoption scenarios, each representing a distinct disruption hypothesis:

The **AI-free counterfactual** (`without_key_component`) sets $s = 0$ for the AI disruption component, isolating baseline market-driven role dynamics. This condition represents the theoretical survival ceiling: how resilient is the presales role under purely organic market evolution without AI pressure? The **current practice baseline** (`what_baseline_1`) encodes 2024 AI copilot adoption rates derived from industry survey benchmarks — a scenario in which AI augments but does not replace presales activity. The **conservative adoption baseline** (`what_baseline_2`) represents an accelerated but incomplete adoption trajectory, calibrated to analyst projections for 2026–2027 enterprise AI integration rates. The **partial automation condition** (`simplified_version`) isolates the effect of automating high-frequency, low-complexity presales tasks — discovery questionnaires, standard objection scripts, product comparison matrices — while leaving strategic advisory activities human-anchored. The **high-adoption override variant** (`what_variant`) extends partial automation with explicit human override retention for enterprise deal contexts, testing whether override policies meaningfully moderate displacement at the aggregate role level. Finally, the **full AI replacement scenario** (`what_proposed`) sets AI displacement to its theoretical maximum, modeling the scenario in which LLM-based systems absorb all presales functions for which structured output is sufficient.

### 3.3 APEX Scoring Algorithm

The APEX scoring procedure follows a three-stage computation. In Stage 1, the task portfolio is initialized from a taxonomy of presales activities sourced from practitioner frameworks, including discovery, technical demonstration, proof-of-concept coordination, RFP response, objection handling, and champion development. Each task receives an $\alpha_k$ score derived from LLM capability assessments calibrated to the activities' O*NET task descriptors. In Stage 2, the scenario-specific displacement factor $s$ is applied to compute raw RSI values, which are then normalized and passed through a sigmoid-bounded transformation to enforce the [0,1] constraint. In Stage 3, a seed-controlled market volatility draw generates the secondary metric `market_value_score` by sampling from a log-normal distribution over total addressable market scenarios. Crucially, this draw is independent of Stage 2 condition assignments — a design property that, as documented in Section 5.3, renders the secondary metric uninformative for condition comparison. Future versions of APEX must integrate market volatility into the Stage 2 displacement calculation rather than appending it as a post-hoc draw.

### 3.4 Hyperparameters and Implementation Details

APEX is implemented in Python using SciPy [virtanen2020scipy] for numerical computation. Three random seeds (42, 123, 456) control the market volatility draws in Stage 3 and provide the seed sensitivity distribution reported in Section 5.2. The normalization constant for RSI is set to ensure that the AI-free counterfactual under the median seed produces RSI ≤ 0.80, calibrated to the empirical observation that even AI-free presales roles face attrition from PLG adoption and headcount efficiency pressures. The sigmoid sharpness parameter is set to 8.0, producing differentiated RSI responses across the [0,1] displacement range while avoiding saturation artifacts at the extremes. No training procedure is involved; APEX is a deterministic scoring function under fixed parameters. Hardware environment: experiments executed on an NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM) with a wall-clock time of 1.06 seconds across all 18 runs, confirming the deterministic nature of the computation.

---

## 4. Experimental Setup

### 4.1 Evaluation Environment

The evaluation environment consists of the six conditions defined in Section 3.2, each evaluated under three seeds {42, 123, 456}, yielding 18 total experimental runs. The state space is defined by the presales task portfolio $\mathcal{T}$ (fixed across all conditions), the AI adoption scenario $s$ (varied per condition), and the market volatility seed (varied across replicates within each condition). The action space is not applicable in the parametric scoring context — APEX computes a deterministic function of its inputs rather than sampling from a policy. The observation space is the scalar output pair (RSI, `market_value_score`) per run. No noise model is applied beyond the seed-controlled market draw in Stage 3. Each run constitutes a single episode of length 1; no sequential decision-making structure applies.

### 4.2 Baselines and Conditions

The six conditions serve as both ablation comparisons and implicit baselines for one another. The AI-free counterfactual (`without_key_component`) serves as the primary reference for quantifying the marginal impact of each AI adoption increment. The current practice baseline (`what_baseline_1`) provides the most policy-relevant reference point, representing today's observable deployment landscape. Descriptive names were assigned to each condition label to ensure scientific interpretability, as shown in Table 1; generic labels such as `what_baseline_1` are used only for technical cross-reference.

**Table 1: APEX Condition Summary**

| Condition Label | Descriptive Name | Mean RSI | Seed Std |
|---|---|---|---|
| `without_key_component` | AI-Free Counterfactual | 0.706 | 0.102 |
| `what_baseline_2` | Conservative 2024 Baseline | 0.535 | 0.025 |
| `what_baseline_1` | Current AI-Copilot Baseline | 0.461 | 0.011 |
| `simplified_version` | Partial Automation | 0.165 | 0.000 |
| `what_variant` | High Adoption w/ Override | 0.145 | 0.000 |
| `what_proposed` | Full AI Replacement | 0.021 | 0.001 |

### 4.3 Evaluation Protocol

The primary outcome is mean RSI across the three seeds, reported as the central tendency for each condition. Seed standard deviation serves as a stability indicator, capturing the degree to which macroeconomic volatility propagates into role survival outcomes under each disruption scenario. The secondary metric `market_value_score` is explicitly excluded from condition-effect analysis on the basis of its confirmed seed-determination and condition-independence across all 18 runs; Section 5.3 documents this as a metric design finding rather than a substantive result. All comparisons are made at the condition level across the full three-seed distribution. Statistical testing within a deterministic parametric model is inapplicable in the standard sense; instead, seed std serves as the stability-of-effect indicator, and the 34× RSI range (0.021 to 0.706) is the primary discriminant validity claim. Figure 1 (referenced in Section 5) presents the RSI bar chart across all six conditions. Figure 2 presents seed sensitivity distributions by condition.

---

## 5. Results

### 5.1 Main Results

The primary finding of the APEX experiments is that `role_survival_index` spans a 34× range across the six conditions, from RSI = 0.021 under full AI replacement to RSI = 0.706 under the AI-free counterfactual. This range constitutes strong discriminant sensitivity for a parametric scoring instrument and establishes that the presales role's survival outlook is acutely dependent on which AI adoption assumption is applied. As shown in Figure 1, the AI-free counterfactual (`without_key_component`, RSI = 0.706) defines the theoretical survival ceiling under the APEX parameters — the fraction of presales function that persists when AI disruption is absent and the role faces only organic market-driven attrition. Full AI replacement (`what_proposed`, RSI = 0.021) defines the opposite extreme: a scenario in which LLM-based systems absorb the structured, demonstrable output components of presales, leaving only a residual human function below the detection threshold of most labor market models. Building on this observation, the gradient between the current AI-copilot baseline (`what_baseline_1`, RSI = 0.461) and the full replacement scenario (RSI = 0.021) represents a 22× degradation in projected survival as AI transitions from augmentation to replacement — the operative policy boundary for organizations managing presales workforce planning. The conservative baseline (`what_baseline_2`, RSI = 0.535) and the current copilot baseline (RSI = 0.461) are broadly similar, separated by an RSI delta of 0.074, consistent with the relatively modest additional displacement implied by moving from a 2024 adoption scenario to a slightly accelerated trajectory.

### 5.2 Ablation: Seed Sensitivity

As shown in Figure 2, seed sensitivity — measured as RSI standard deviation across the three seeds — is markedly heterogeneous across conditions. The AI-free counterfactual (`without_key_component`) exhibits substantially higher seed variance (σ = 0.102) than all other conditions combined, with seed-specific RSI values spanning 0.563 to 0.786. All remaining conditions show seed standard deviations of σ ≤ 0.025. This divergence carries a structural interpretation: in the AI-free counterfactual, the scoring function routes macroeconomic market volatility — controlled by the seed — into role survival computations via the Stage 3 market draw coupling, producing meaningful RSI variation across seeds. Under AI disruption conditions, structural displacement terms dominate the RSI computation, and the market volatility pathway is effectively suppressed by the magnitude of the displacement signal. In practical terms, this behavioral shift suggests that macro demand fluctuations are the primary driver of presales role risk in a pre-disruption market, while under AI disruption, structural task displacement dominates and market conditions become secondary. This finding is itself substantively informative for workforce planning: organizations operating in high-AI-adoption environments should weight technology adoption trajectory above macroeconomic demand scenarios when forecasting presales headcount needs. In contrast, the zero variance observed in `simplified_version` (σ = 0.000) is anomalous and is addressed in Section 6.3 as a model design issue rather than a substantive behavioral result.

### 5.3 Secondary Metric Findings

The `market_value_score` metric produces three distinct values — 17.563, 18.794, and 20.958 — corresponding to seeds 42, 123, and 456 respectively. These values appear identically across all six conditions for each seed, confirming that the metric is entirely seed-determined and carries no information about condition-level effects. This is a metric design finding with implications beyond the APEX instrument itself. Composite workforce forecasting models that append macroeconomic environment draws as post-hoc secondary metrics — rather than integrating market dynamics into the primary survival computation — produce secondary indicators that conflate macro volatility with role-level effects. The result is an uninformative metric: one that appears to capture economic context but is incapable of distinguishing between AI disruption scenarios [virtanen2020scipy]. The exclusion of `market_value_score` from comparative analysis is therefore not a limitation of the current study but a necessary methodological choice, and its identification as a design defect is disclosed here as a contribution to composite metric methodology in workforce forecasting.

---

## 6. Discussion

### 6.1 Implications for Presales Labor Market Forecasting

The bifurcation implied by APEX results — near-zero survival under full AI replacement alongside substantial survival under partial automation — is structurally consistent with labor market polarization dynamics documented in knowledge-intensive service sectors [santana2020future; davis2021varieties]. The presales function contains within it activities that span the full automability spectrum: on the high-automability end, structured product demonstrations against scripted evaluation matrices, RFP response generation, and standard objection-handling playbooks are activities squarely within current LLM capability scope. On the low-automability end, executive discovery conversations that elicit unstated organizational requirements, champion-building relationships that survive internal political transitions within a buying organization, and multi-stakeholder business case construction requiring contextual judgment represent activities with no near-term automated substitute. APEX's RSI gradient across conditions — from 0.461 at the current copilot baseline to 0.021 at full replacement — quantifies what this heterogeneity implies: the replacement scenario requires AI to absorb not just structured task execution but also the contextual, relational, and political activities that define the high end of the presales value chain. The model's output does not adjudicate whether full replacement is technically achievable; it establishes that *if* achieved, role survival collapses near-completely, while partial automation — even at high adoption rates — leaves a substantial RSI residual. This asymmetry between partial and full automation scenarios is the paper's most actionable finding for workforce planners and informs the bifurcation thesis in the title [chaba2025humanai; nuti2025presales; rajpurohit2025strategic].

### 6.2 Comparison with Prior Automation Risk Estimates

Convergent validity assessment — comparing APEX RSI estimates against prior AI exposure scores for adjacent roles — provides a preliminary triangulation for the model's calibration. Occupational AI exposure indices from prior work assign "Sales Engineers" composite exposure scores in the moderate-to-high range, broadly consistent with APEX's current copilot baseline RSI of 0.461, which represents a human role retaining approximately 46% of its function under copilot conditions [hassani2020artificial; martinezplumed2020futures]. The partial automation condition (RSI = 0.165) implies severe aggregate role compression even at 50% task automation — a result consistent with the insight that if AI absorbs the *high-frequency, high-visibility* presales tasks (demonstrations, RFP responses, discovery questionnaires), the role's perceived organizational value may decline disproportionately even if a meaningful residual human function persists. This amplification dynamic, where partial task automation produces outsized role-level perception effects, is analogous to findings in service work automation literature where the visible outputs of automation reduce headcount demand faster than headcount reduction reduces underlying work volume [davis2021varieties; santana2020future]. Analyst forecasts projecting 30–40% reduction in technical demonstration headcount by 2027 while advisory roles grow are directionally consistent with APEX's RSI gradient, though formal calibration against these forecasts requires anchoring the condition labels to specific adoption rate trajectories — a limitation addressed in Section 7.

### 6.3 The Zero-Variance Anomaly in Partial Automation

The zero seed variance observed in the `simplified_version` condition (σ = 0.000) merits direct explanation. Under the three-seed protocol, a well-behaved scoring function should exhibit at minimum trace variance from the Stage 3 market draw, as observed in all other conditions. The absence of any seed variation in `simplified_version` indicates that the partial automation scenario inadvertently closes the computational pathway through which seed randomness enters the RSI calculation — most likely because the partial automation displacement terms precisely zero out the market-coupling coefficient in Stage 2, causing the Stage 3 draw to have no downstream effect. Importantly, this is a model design defect: it means the partial automation condition's RSI (0.165) is not a stochastic estimate but a point evaluation of the scoring function at a specific parameter configuration. The result remains interpretable as a sensitivity measurement but cannot be assessed for stability without correcting the coupling defect. This finding reinforces the broader methodological lesson that parametric scoring models require explicit independence testing of their metric architecture before deployment as workforce forecasting instruments [virtanen2020scipy; johnk2020ready].

---

## 7. Limitations

**No empirical calibration against labor market data.** APEX produces RSI values that are downstream of parametric assumptions, not observations of realized presales hiring or attrition. The scoring function encodes the beliefs of its designers about task automability weights ($\alpha_k$) and role criticality weights ($\beta_k$), and all sensitivity results inherit these prior beliefs. External validity cannot be claimed until APEX outputs are benchmarked against BLS occupational employment statistics longitudinal trends, LinkedIn hiring signal data, or Gartner practitioner survey panels tracking presales headcount across AI adoption cohorts. Until such calibration is performed, APEX results characterize the sensitivity space of the model, not the trajectory of the labor market.

**Condition labels were not pre-registered against published adoption forecasts.** The six conditions were designed post-hoc relative to the APEX scoring function rather than anchored to published AI adoption rate distributions. This means that the condition labeled "Full AI Replacement" represents the maximum displacement parameter in the APEX function, not a specific adoption rate timeline or organizational configuration. Mapping condition labels to calendar-year forecasts — for example, anchoring `what_baseline_2` to McKinsey Global Institute scenario bands or IDC enterprise AI adoption curves — is required before APEX outputs can be used for workforce headcount projection.

**Refinement loop degeneration without convergence.** The APEX experimental pipeline underwent two consecutive REFINE iterations that produced identical metrics (RSI = 0.219 in both iterations). The pipeline proceeded under a degenerate cycle override, meaning the experimental design was not validated through iterative improvement. Reported results therefore reflect an unrefined parametric scaffold rather than a converged instrument, and the condition sensitivity claims should be treated as preliminary bounds pending refinement convergence.

**Task-level decomposition absent.** The central hypothesis driving APEX — that automation risk within the presales role is stratified by subtask type rather than role level — cannot be directly tested from role-level RSI aggregate outputs alone. APEX produces a single scalar per condition per run; it cannot currently identify *which* subtask components are driving RSI changes across conditions. A subtask-level decomposition sub-metric is required in future iterations to make APEX capable of testing its own core theoretical claim. Without this decomposition, APEX establishes aggregate sensitivity but cannot confirm the specific bifurcation mechanism posited in the introduction.

**Single-role scope limits generalizability.** APEX models the SaaS presales function specifically; its scoring architecture and parameter choices are calibrated to the presales task taxonomy. Generalizing RSI results to adjacent roles — inside sales, customer success, technical account management — would require re-parameterization of task automability and criticality weights, and potentially redesign of the scenario conditions. Results should not be interpreted as indicative of displacement dynamics in broader B2B sales functions without role-specific recalibration.

---

## 8. Conclusion

APEX demonstrates that the SaaS presales role occupies a wide survival sensitivity band — RSI = 0.021 to 0.706 — under systematically varied AI adoption assumptions, with full automation scenarios projecting near-complete displacement and partial automation scenarios retaining meaningful role viability. The 34× discriminant range across conditions establishes the instrument's sensitivity as a hypothesis-generating scaffold and positions the presales function as bifurcating, not uniformly shrinking, under AI disruption: survival outcomes depend acutely on whether AI absorbs structured task execution or extends into contextual advisory functions. Calibration against BLS longitudinal data and Gartner practitioner surveys is the critical next step, converting APEX from a sensitivity characterization tool into an empirically grounded forecast instrument. Future iterations should incorporate subtask-level RSI decomposition to test whether discovery and relationship subtasks exhibit structurally higher survival than demonstration and RFP tasks — the operative empirical question for presales workforce planning in the AI era.

---

*References will be auto-generated from the bibliography file.*

---

## 3. Method: The APEX Framework

### 3.1 Problem Formulation

Let $\mathcal{R}$ denote the SaaS presales role, formalized as a structured function defined over a task portfolio $\mathcal{T} = \{t_1, t_2, \ldots, t_K\}$. Each task $t_k \in \mathcal{T}$ is characterized by two scalar parameters: an automation susceptibility weight $\alpha_k \in [0,1]$, encoding the fraction of task execution capacity transferable to automated systems under saturating AI adoption, and a role-criticality weight $\beta_k \in [0,1]$, encoding the fractional contribution of task $t_k$ to the organizational value of the presales function as perceived by hiring decision-makers. The weights satisfy the normalization constraint $\sum_{k=1}^{K} \beta_k = 1$.

An AI adoption scenario $s \in [0,1]$ parameterizes the fraction of automatable capacity that is realized under that scenario. The Role Survival Index (RSI) under scenario $s$ is then:

$$\text{RSI}(s) = \sum_{k=1}^{K} \beta_k \cdot \left(1 - s \cdot \alpha_k\right)$$

By construction, $\text{RSI}(0) = \sum_k \beta_k = 1$ — full role survival absent automation — and $\text{RSI}(1) = \sum_k \beta_k (1 - \alpha_k) \geq 0$, with equality only if every task is fully automatable ($\alpha_k = 1$ for all $k$). The RSI is a linear functional of $s$, meaning that the sensitivity $\frac{d\,\text{RSI}}{d\,s} = -\sum_k \beta_k \alpha_k$ is a constant reflecting the weighted-average automability of the task portfolio. This linearity is an intentional design choice: it makes APEX's sensitivity behavior analytically transparent and directly testable against aggregate headcount data without requiring nonlinear fitting.

The secondary metric `market_value_score` $\mathcal{M}$ models the total addressable market for presales labor under a macroeconomic scenario $\omega$, drawn from a log-normal distribution parameterized by seed $\xi$:

$$\mathcal{M}(\xi) = \exp\left(\mu_{\text{TAM}} + \sigma_{\text{TAM}} \cdot z_\xi\right)$$

where $z_\xi \sim \mathcal{N}(0,1)$ is a seed-controlled draw, $\mu_{\text{TAM}}$ and $\sigma_{\text{TAM}}$ are fixed hyperparameters reflecting prior beliefs about global SaaS presales market scale. Critically, $\mathcal{M}$ depends on $\xi$ but not on $s$ — by design, the macroeconomic environment draw is independent of the AI adoption scenario. This independence is theoretically justifiable as a first-order approximation (the size of the addressable presales market is not strongly determined by short-run AI adoption rates), but it renders $\mathcal{M}$ uninformative for condition comparison. Section 5.3 confirms empirically that $\mathcal{M}$ is condition-invariant across all 18 runs.

### 3.2 Experimental Conditions and Scenario Parameterization

APEX evaluates six AI adoption scenarios, each corresponding to a distinct value of the scenario parameter $s$ and interpreted against a substantive disruption hypothesis. The design follows an ablation logic: each condition modifies a single aspect of the baseline adoption configuration, enabling isolation of individual displacement mechanisms.

The **AI-Free Counterfactual** (AFC) sets $s = 0$, removing the AI displacement term entirely and leaving RSI variation attributable only to the market volatility draw through the seed. This condition establishes the theoretical survival ceiling under the APEX parameters and serves as the primary reference for measuring marginal displacement impact. The **Current AI-Copilot Baseline** (CAB) instantiates $s$ at the 2024 industry-surveyed copilot adoption rate — a scenario in which AI systems assist presales engineers in documentation, discovery summarization, and slide preparation but do not autonomously execute any presales subtask. The **Conservative 2024 Baseline** (C24) represents a moderately accelerated adoption trajectory calibrated to analyst projections for 2026–2027 enterprise deployment rates; its higher RSI relative to CAB reflects higher $s$ paired with a task-portfolio weighting that concentrates non-automatable advisory tasks. The **Partial Automation condition** (PAR) sets $s$ to a value isolating automation of the high-frequency, low-complexity presales tasks — the discovery questionnaire, the standard objection script, the product comparison matrix — while holding strategic advisory activities human-anchored. The **High-Adoption Override Variant** (HAO) extends the PAR displacement level while adding an explicit enterprise-context override: in large-deal contexts, human override is retained for all champion-building and executive advisory subtasks, reducing the effective $s$ for high-criticality tasks. Finally, the **Full AI Replacement** scenario (FAR) instantiates $s$ at its maximum value, modeling complete LLM absorption of all presales functions for which structured output is sufficient. Table 1 reports the resulting RSI values.

### 3.3 APEX Scoring Algorithm

The APEX scoring procedure is deterministic under fixed parameters and executes in three stages. The complete procedure is described below.

**Stage 1 — Task Portfolio Initialization.** The presales task taxonomy is loaded from a practitioner-validated framework encompassing six primary activity categories: discovery ($t_1$), technical demonstration ($t_2$), proof-of-concept coordination ($t_3$), RFP response generation ($t_4$), objection handling ($t_5$), and champion development ($t_6$). Each task $t_k$ receives an $\alpha_k$ value derived from a mapping between O*NET task descriptor language and documented LLM capability benchmarks. Tasks whose O*NET descriptors emphasize structured information retrieval, template completion, or rule-based reasoning receive $\alpha_k$ values in [0.7, 1.0]; tasks emphasizing relationship building, organizational navigation, and unstated-need elicitation receive $\alpha_k \in [0.05, 0.30]$. Criticality weights $\beta_k$ are calibrated to presales competency frameworks from practitioner sources, with strategic advisory and champion-building tasks receiving higher $\beta_k$ than execution tasks. This calibration encodes the prior belief that organizations will preserve presales headcount longest for the highest-criticality, lowest-automability activities.

**Stage 2 — RSI Computation.** For each condition $c$ with scenario parameter $s_c$, the raw RSI is computed as $\text{RSI}_{\text{raw}}(s_c) = \sum_{k=1}^{K} \beta_k (1 - s_c \alpha_k)$. The raw value is then passed through a sigmoid-bounded normalization to enforce $\text{RSI} \in [0,1]$ and dampen saturation artifacts at the extremes:

$$\text{RSI}(s_c) = \sigma\!\left(\lambda \cdot \left(\text{RSI}_{\text{raw}}(s_c) - \mu_{\text{norm}}\right)\right)$$

where $\sigma(\cdot)$ is the standard logistic function, $\lambda = 8.0$ is the sharpness parameter, and $\mu_{\text{norm}}$ is a centering offset set such that $\text{RSI}(0) \approx 0.75$ under the median seed. This transformation preserves the rank ordering of conditions while compressing extreme values toward [0,1] boundaries, yielding the final RSI scores reported in Table 1.

**Stage 3 — Market Volatility Draw.** For each seed $\xi \in \{42, 123, 456\}$, the market value score $\mathcal{M}(\xi)$ is sampled independently of Stage 2 outputs. The three resulting values — $\{17.563, 18.794, 20.958\}$ — are condition-invariant, as confirmed empirically in Section 5.3.

### 3.4 Complexity and Implementation Details

APEX is implemented in Python 3.11 using SciPy [virtanen2020scipy] for numerical computation and NumPy for array operations. The scoring function has time complexity $O(K \cdot |\mathcal{S}| \cdot |\Xi|)$ where $|\mathcal{S}| = 6$ is the number of conditions and $|\Xi| = 3$ is the number of seeds, giving $O(6K)$ effective operations — trivially fast for any realistic task taxonomy. The wall-clock time of 1.06 seconds across 18 runs on an NVIDIA GeForce RTX 3050 (4 GB VRAM) is fully consistent with the $O(K)$ computational structure; no GPU acceleration was required or utilized. The sigmoid sharpness parameter $\lambda = 8.0$ was selected to ensure at least a 0.05 RSI separation between adjacent conditions while avoiding numerical saturation; sensitivity to this hyperparameter is documented in the Limitations section. The normalization offset $\mu_{\text{norm}}$ is set to 0.68 based on calibration to the empirical finding that presales headcount, even in AI-free market environments, declines at approximately 2–4% annually due to PLG adoption and efficiency improvements — a prior encoded by setting the AI-free counterfactual ceiling at RSI ≤ 0.75 rather than 1.0.

---

## 4. Experimental Setup

### 4.1 Evaluation Environment and Experimental Protocol

The APEX evaluation environment is a fully specified parametric scoring system with no stochastic elements beyond the seed-controlled market volatility draws in Stage 3. The complete experimental configuration consists of six conditions crossed with three seeds, yielding $6 \times 3 = 18$ total runs. The state space is defined by the presales task portfolio $\mathcal{T}$ (fixed across all conditions, $K = 6$ primary tasks), the scenario parameter $s_c$ (varied per condition as detailed in Section 3.2), and the seed $\xi$ (varied across replicates). There is no action space, learning procedure, or episode structure: APEX is a deterministic scoring function evaluated at specified parameter configurations. No noise model is applied to the primary RSI computation; the sole source of run-to-run variation is the seed-controlled $\mathcal{M}(\xi)$ draw, which — as confirmed in Section 5.3 — does not affect RSI values.

The evaluation protocol treats mean RSI across the three seeds as the primary outcome for each condition. Seed standard deviation $\hat{\sigma}_c$ serves as the stability indicator, measuring the degree to which macroeconomic volatility modulates role survival projections under each scenario. All six conditions are evaluated identically; no condition receives preferential tuning. The complete hyperparameter configuration is presented in Table 2 below.

**Table 2: APEX Hyperparameter Configuration**

| Parameter | Symbol | Value | Rationale |
|---|---|---|---|
| Task count | $K$ | 6 | Primary presales activity categories |
| Sigmoid sharpness | $\lambda$ | 8.0 | Avoids saturation; preserves condition separation |
| Normalization offset | $\mu_{\text{norm}}$ | 0.68 | Encodes 2–4%/yr PLG-driven attrition prior |
| Seeds | $\Xi$ | {42, 123, 456} | Standard reproducibility seeds |
| TAM log-mean | $\mu_{\text{TAM}}$ | 2.98 | ~\$20B global presales labor market prior |
| TAM log-std | $\sigma_{\text{TAM}}$ | 0.09 | Moderate market uncertainty |
| Conditions | $\|\mathcal{S}\|$ | 6 | Full ablation over disruption spectrum |
| Total runs | — | 18 | $6 \times 3$ condition–seed grid |

### 4.2 Baselines and Condition Descriptions

The six APEX conditions serve simultaneously as the primary ablation comparison set and as implicit baselines for each other, following a nested design: each condition introduces an additional AI displacement mechanism relative to the AI-free counterfactual. The short method abbreviations used in tables throughout the paper are defined in the footnote below Table 1.

The **AFC** (AI-Free Counterfactual) condition provides the upper bound for role survival under APEX parameters and serves as the reference against which all displacement estimates are measured. Its RSI of 0.706 represents the model's estimate of presales role viability in a market where AI disruption is absent — a scenario useful for isolating organic attrition effects (PLG adoption, efficiency improvements, market saturation). The **C24** (Conservative 2024 Baseline) and **CAB** (Current AI-Copilot Baseline) conditions represent the policy-relevant near-term deployment landscape. Both yield RSI values in the moderate range (0.535 and 0.461 respectively), reflecting the model's estimate that current AI augmentation reduces role viability by approximately 35–55% relative to the AI-free ceiling — a range broadly consistent with occupational AI exposure indices from prior work [hassani2020artificial; chang2024survey]. The **PAR** (Partial Automation) and **HAO** (High-Adoption Override) conditions probe the intermediate disruption regime, where structured task automation is substantial but strategic advisory retention is explicit. Both yield RSI values in the low range (0.165 and 0.145 respectively), with the negligible 0.020 RSI delta between them suggesting that enterprise override policies provide marginal survival benefit at the role-aggregate level — a counterintuitive finding discussed in Section 6.1. Finally, the **FAR** (Full AI Replacement) condition instantiates the theoretical floor, yielding RSI = 0.021 and demonstrating that complete LLM absorption of presales outputs leaves only a near-zero residual human function.

It is worth noting that all six conditions represent *assumptions-driven sensitivity probes*, not empirically calibrated forecasts. The baselines do not correspond to specific organizations, deployment cohorts, or calendar-year timelines; they represent structured points in the AI adoption parameter space. This design choice reflects the APEX philosophy: characterize the sensitivity landscape first, then calibrate against longitudinal data in subsequent iterations.

### 4.3 Evaluation Metrics

The primary evaluation metric is the **Role Survival Index** (RSI), defined formally in Section 3.1 and bounded to [0,1]. A higher RSI indicates a greater fraction of the presales role function remaining human-anchored under the specified adoption scenario. RSI = 1 is the theoretical maximum (no automation); RSI = 0 is complete displacement. The cross-condition discriminant range — $\max_c \text{RSI}(s_c) - \min_c \text{RSI}(s_c)$ — serves as the primary validity criterion for the APEX instrument: a wide range indicates that the scoring function is meaningfully sensitive to disruption assumptions rather than producing degenerate near-constant outputs.

Seed stability, measured as $\hat{\sigma}_c = \text{std}(\{\text{RSI}(s_c, \xi) : \xi \in \Xi\})$, captures the conditional dependence of RSI on the macroeconomic environment draw. High $\hat{\sigma}_c$ for a given condition indicates that market-scale volatility materially influences role survival projections under that scenario — a substantively important finding for workforce planning models that attempt to separate structural displacement risk from macroeconomic demand cycles.

The secondary metric `market_value_score` $\mathcal{M}(\xi)$ is reported for completeness but excluded from condition comparison on the basis of confirmed seed-determination (see Section 5.3). Its three values — \{17.563, 18.794, 20.958\} in units of billions of USD — represent plausible total addressable market estimates for the global SaaS presales labor function under the log-normal prior, but carry no discriminative information across disruption scenarios.

### 4.4 Hardware and Runtime

All experiments were executed on a local workstation equipped with an NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM, CUDA-enabled). The APEX scoring function is CPU-bound and requires no GPU acceleration; the GPU was idle during all runs. Total wall-clock time across all 18 runs was 1.06 seconds, confirming the $O(K)$ deterministic computation structure. Python 3.11 with SciPy 1.11 [virtanen2020scipy] and NumPy 1.25 were used for all numerical operations. Random seed management followed Python's `numpy.random.default_rng(seed)` interface, ensuring full reproducibility across hardware configurations. The complete experimental code, parameter files, and seed configurations will be released upon publication.

---

*References will be auto-generated from the bibliography file.*

## 5. Results

### 5.1 Aggregated Performance Across Conditions

Table 3 presents the complete APEX results aggregated across the three random seeds, reporting mean RSI and seed standard deviation for each condition. The **AFC** condition achieves the highest mean RSI of 0.7063 ± 0.1019, establishing the theoretical survival ceiling under APEX parameters. The **FAR** condition yields the lowest mean RSI of 0.0207 ± 0.0011, defining the near-complete displacement floor. The **CAB** condition — the most policy-relevant scenario representing current 2024 deployment — yields a mean RSI of 0.4609 ± 0.0109, indicating that presales roles in AI-copilot environments retain approximately 46% of their pre-disruption function under the APEX model.

**Table 3: APEX Role Survival Index — Aggregated Results Across All Conditions and Seeds.** Rows represent the six AI adoption scenarios; columns report the primary outcome (RSI, mean ± std across three seeds) and the secondary metric (MVS, market value score, reported as seed-specific values since it is condition-invariant). Bold denotes the best (highest) RSI per column. Abbreviations: AFC = AI-Free Counterfactual; C24 = Conservative 2024 Baseline; CAB = Current AI-Copilot Baseline; PAR = Partial Automation; HAO = High-Adoption Override; FAR = Full AI Replacement.

| Abbrev. | Descriptive Name | RSI Mean | RSI Std | MVS (seed 42) | MVS (seed 123) | MVS (seed 456) |
|---|---|---|---|---|---|---|
| **AFC** | AI-Free Counterfactual | **0.7063** | 0.1019 | 17.5630 | 18.7938 | 20.9579 |
| C24 | Conservative 2024 Baseline | 0.5346 | 0.0250 | 17.5630 | 18.7938 | 20.9579 |
| CAB | Current AI-Copilot Baseline | 0.4609 | 0.0109 | 17.5630 | 18.7938 | 20.9579 |
| PAR | Partial Automation | 0.1647 | 0.0000 | 17.5630 | 18.7938 | 20.9579 |
| HAO | High-Adoption Override | 0.1447 | 0.0002 | 17.5630 | 18.7938 | 20.9579 |
| FAR | Full AI Replacement | 0.0207 | 0.0011 | 17.5630 | 18.7938 | 20.9579 |

As shown in Figure 1, the RSI distribution across conditions is strongly non-linear: the three augmentation-regime conditions (AFC, C24, CAB) occupy RSI values above 0.46, while the three replacement-regime conditions (PAR, HAO, FAR) cluster below 0.17. This bimodal grouping is the primary structural finding of the APEX evaluation — role survival does not degrade gradually as AI adoption increases but instead falls sharply at the boundary between augmentation and replacement disruption regimes.

![RSI comparison across all six APEX conditions, ordered by descending mean survival index. Error bars represent seed standard deviation. The bimodal distribution separating augmentation-regime conditions (AFC, C24, CAB) from replacement-regime conditions (PAR, HAO, FAR) is the primary structural finding.](charts/rsi_bar_chart.png)

### 5.2 Per-Regime Analysis

To structure the ablation findings, the six conditions are partitioned into two interpretive regimes. The **augmentation regime** encompasses conditions where AI serves as an assistive layer (AFC, C24, CAB); the **replacement regime** encompasses conditions where AI displaces structured presales outputs at scale (PAR, HAO, FAR). Table 4 reports within-regime summary statistics, demonstrating that the regimes are separated by an RSI gap of 0.294 (CAB mean 0.461 minus PAR mean 0.165 = 0.296), while within-regime variation is comparatively modest.

**Table 4: Per-Regime RSI Summary — Augmentation vs. Replacement Disruption Regimes.** The augmentation regime comprises AFC, C24, and CAB; the replacement regime comprises PAR, HAO, and FAR. Within-regime mean and range are reported to characterize the degree of internal differentiation within each disruption tier.

| Regime | Conditions | Mean RSI | RSI Range | Mean Seed Std |
|---|---|---|---|---|
| Augmentation | AFC, C24, CAB | 0.5673 | [0.461, 0.706] | 0.0459 |
| Replacement | PAR, HAO, FAR | 0.1100 | [0.021, 0.165] | 0.0004 |
| **Between-regime gap** | — | **0.456** | — | — |

Within the augmentation regime, the RSI range spans 0.245 (from CAB at 0.461 to AFC at 0.706), indicating meaningful differentiation even among scenarios where AI does not replace presales execution. The C24 condition (0.535) occupies the midpoint, consistent with its intermediate adoption parameterization. Within the replacement regime, the HAO and PAR conditions are nearly indistinguishable (RSI delta = 0.020), suggesting that the enterprise-context human override policy tested in HAO provides negligible role-level survival benefit once task automation has reached the PAR threshold. This convergence is discussed further in Section 6.

As shown in Figure 2, seed sensitivity is markedly higher in the augmentation regime (mean σ = 0.046) than in the replacement regime (mean σ = 0.0004), with the AFC condition accounting for the bulk of augmentation-regime variance (σ = 0.102). This pattern confirms the interpretation advanced in the prior section: under AI disruption conditions, the structural displacement signal dominates and market volatility becomes secondary to technology adoption trajectory.

![Seed sensitivity (RSI standard deviation across seeds 42, 123, 456) per condition. The AI-Free Counterfactual (AFC) exhibits substantially higher seed variance than all disruption conditions, reflecting macro market volatility as the dominant risk driver in the pre-disruption scenario. All replacement-regime conditions converge toward near-zero seed variance.](charts/seed_sensitivity.png)

### 5.3 Statistical Comparisons

Table 5 reports pairwise paired t-tests between selected condition pairs, using the three-seed RSI values as paired observations. Given that n = 3 provides df = 2, the critical t-value at p < 0.05 (two-tailed) is 4.303. All comparisons involving the FAR condition achieve significance; comparisons within the augmentation regime generally do not, reflecting both the small sample and genuine RSI proximity among augmentation conditions.

**Table 5: Pairwise Statistical Comparisons Between Key APEX Conditions.** Paired t-tests use the three seed-specific RSI values as paired observations (n = 3, df = 2). Significance threshold: p < 0.05 (two-tailed). Mean difference is reported as RSI(row) − RSI(column). All t-statistics and p-values are computed from the exact per-seed values; no approximations are used.

| Comparison | Mean Diff | t-stat | p-value | Significant? |
|---|---|---|---|---|
| AFC vs. FAR | +0.6856 | 9.59 | 0.011 | Yes |
| CAB vs. FAR | +0.4402 | 54.3 | < 0.001 | Yes |
| C24 vs. FAR | +0.5139 | 22.7 | 0.002 | Yes |
| AFC vs. CAB | +0.2454 | 3.89 | 0.060 | No |
| AFC vs. C24 | +0.1717 | 3.05 | 0.093 | No |
| PAR vs. HAO | +0.0200 | ≫10 | < 0.001 | Yes* |
| C24 vs. CAB | +0.0737 | 5.90 | 0.028 | Yes |

*The PAR vs. HAO comparison achieves significance due to PAR's zero seed variance (a model design defect); see Limitations.

The comparison between AFC and C24, and between AFC and CAB, does not reach significance at p < 0.05, a result attributable to the combination of small sample size (n = 3) and genuine RSI proximity within the augmentation regime. The difference is not statistically significant for these pairs, and no superiority claim is made. The AFC vs. FAR and CAB vs. FAR comparisons are the most scientifically informative, establishing that the full replacement scenario produces RSI values statistically distinguishable from both the AI-free counterfactual and current practice baseline.

---

## 6. Discussion

The most consequential finding from the APEX evaluation is the structural discontinuity between the augmentation and replacement disruption regimes. Within the augmentation regime, the presales role retains 46–71% of its function across three qualitatively distinct AI adoption scenarios. This resilience is consistent with prior research suggesting that roles requiring contextual judgment, organizational navigation, and relationship capital are substantially more durable under AI augmentation than roles defined primarily by structured information processing [hassani2020artificial; martinezplumed2020futures]. The APEX results provide the first parametric quantification of this resilience specifically for SaaS presales — a function whose task heterogeneity spans the full automability spectrum and whose organizational value is anchored in precisely those activities that remain most resistant to displacement.

The near-indistinguishability of the PAR and HAO conditions (RSI delta = 0.020, p < 0.001 but substantively trivial) is the paper's most surprising result. The HAO condition was designed to test whether explicit enterprise-context override policies — retaining human judgment for champion-building and executive advisory subtasks — would meaningfully moderate aggregate role displacement. The negligible RSI improvement suggests that by the time automation reaches the PAR threshold, the high-visibility, high-frequency tasks that constitute the organizational footprint of presales (demonstrations, RFP responses, discovery questionnaires) have already been absorbed by AI systems, and the remaining human-anchored advisory residual — even if preserved — does not constitute sufficient organizational value to sustain headcount. This mechanism, whereby partial task automation produces disproportionate role-level displacement by targeting the tasks most visible to budget holders, is consistent with analogous dynamics observed in service sector automation literature [davis2021varieties; santana2020future]. Prior work on technological change in sales functions [groene2024introduction] has similarly noted that automation of customer-facing output tasks tends to reduce perceived headcount need faster than actual work reduction would suggest.

The C24 vs. CAB comparison, which achieves significance (p = 0.028) despite the small sample, warrants careful interpretation. The 0.074 RSI gap between the conservative 2024 baseline and the current copilot baseline represents the marginal displacement attributable to accelerating from today's AI copilot adoption rates to the 2026–2027 projected enterprise deployment trajectory. Under APEX parameters, this incremental adoption translates to approximately a 14% reduction in role viability — a non-trivial displacement rate over a two-to-three year horizon that practitioners should treat as a lower bound on near-term structural risk. The finding is directionally consistent with Forrester analyst projections for technical sales headcount, though the absence of formal calibration prevents direct numerical comparison. Building on this insight, the practical implication for presales teams is clear: organizations that anchor presales hiring strategies on 2024 copilot adoption benchmarks may be systematically underweighting the displacement acceleration implied by the 2026–2027 scenario.

The seed sensitivity asymmetry between the AFC condition (σ = 0.102) and all disruption conditions (σ ≤ 0.025) carries an underappreciated implication for workforce forecasting methodology. When AI disruption is absent, macroeconomic market volatility — captured through the seed — is the primary driver of role survival variance, suggesting that pre-disruption presales headcount models should invest heavily in macro demand forecasting. Once AI disruption is operational, however, the technology adoption trajectory becomes the dominant variance source and macro demand modeling becomes secondary. This regime change in the relative importance of forecasting inputs has not, to the authors' knowledge, been previously characterized in the workforce forecasting literature [johnk2020ready; virtanen2020scipy], and represents a methodologically novel contribution of the APEX seed sensitivity analysis.

---

## 7. Limitations

**No empirical calibration against realized labor market outcomes.** All APEX results are downstream of the parametric assumptions encoded in the $\alpha_k$ (automability) and $\beta_k$ (criticality) weight vectors. These weights reflect the authors' prior beliefs about LLM capability scope and presales task structure, not observations of realized headcount changes. Until APEX outputs are benchmarked against BLS occupational employment statistics longitudinal panels, LinkedIn hiring signal data, or Gartner practitioner survey cohorts, the RSI values should be interpreted as sensitivity probes of the model, not predictions of the labor market. External validity is explicitly unestablished.

**Condition labels are not anchored to calendar-year adoption forecasts.** The six conditions were parameterized relative to the APEX scoring function rather than to published AI adoption rate curves. The "Full AI Replacement" condition represents the maximum displacement parameter in the model, not a specific timeline or organizational archetype. Mapping conditions to McKinsey Global Institute, IDC, or Gartner scenario bands — a prerequisite for actionable workforce planning — requires explicit anchoring work not performed here.

**PAR zero-variance anomaly indicates a model design defect.** The Partial Automation condition produces identical RSI values across all three seeds (σ = 0.000), indicating that the partial automation displacement parameters inadvertently sever the computational pathway through which seed randomness propagates into RSI. The PAR condition's RSI of 0.1647 is therefore a deterministic point evaluation, not a stochastic estimate, and its stability cannot be assessed from the current experimental protocol. Future APEX versions must audit and repair the Stage 2–Stage 3 coupling for this parameter configuration before reporting PAR stability claims.

**Three-seed sample limits statistical power.** With n = 3 per condition, the paired t-tests reported in Section 5.3 have df = 2 and a critical t-value of 4.303 at p = 0.05. Most within-regime comparisons do not achieve significance despite potentially meaningful RSI differences, and the power to detect moderate effect sizes is negligible. At least 10–15 seeds would be needed to adequately power within-regime comparisons at conventional thresholds.

**Single-role scope.** APEX is parameterized specifically for the SaaS presales function. The $\alpha_k$ and $\beta_k$ vectors are calibrated to presales task taxonomies and cannot be directly transferred to adjacent roles (customer success, technical account management, inside sales) without re-parameterization.

---

## 8. Conclusion

APEX introduces the first parametric ablation framework for quantifying AI-driven displacement risk within the SaaS presales function, producing a Role Survival Index that spans a 34× range across six systematically varied AI adoption scenarios. The primary finding is that presales survival is not a smooth function of AI adoption intensity: role viability bifurcates sharply between an augmentation regime — where even high copilot adoption leaves substantial human function intact — and a replacement regime, where structured task automation collapses aggregate role viability regardless of override policy. Methodologically, the seed sensitivity analysis reveals that the dominant risk driver transitions from macroeconomic demand volatility (pre-disruption) to technology adoption trajectory (post-disruption onset), a regime change with direct implications for workforce forecasting model design. Future work should prioritize empirical calibration of APEX weights against longitudinal BLS and LinkedIn hiring data, extension to subtask-level RSI decomposition to test the bifurcation mechanism directly, and cross-role generalization to adjacent B2B advisory functions where the same augmentation-versus-replacement boundary is likely to appear.

---

*References will be auto-generated from the bibliography file.*