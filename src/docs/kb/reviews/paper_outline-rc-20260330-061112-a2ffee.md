---
created: '2026-03-30T23:18:44+00:00'
evidence:
- stage-16/outline.md
id: paper_outline-rc-20260330-061112-a2ffee
run_id: rc-20260330-061112-a2ffee
stage: 16-paper_outline
tags:
- paper_outline
- stage-16
- run-rc-20260
title: 'Stage 16: Paper Outline'
---

# Stage 16: Paper Outline

## Paper Outline: SaaS Presales Engineer Evolution Under AI Disruption

---

### Method Name

**APEX** — *Automated Presales EXtinction model* (Automated Presales role Evolution eXperiment)

---

### Candidate Titles

| # | Title | Memorability | Specificity | Novelty Signal |
|---|---|---|---|---|
| 1 | **APEX: Quantifying AI-Driven Role Survival in SaaS Presales Markets** | 4/5 | 5/5 | 4/5 |
| 2 | **APEX: Task-Stratified Automation Risk Forecasting for Technical Sales Roles** | 3/5 | 5/5 | 5/5 |
| 3 **APEX: SaaS Presales Engineers Will Not Disappear — They Will Bifurcate** | 5/5 | 4/5 | 5/5 |

**Recommended:** Title 3 — declarative surprise format, strongest recall, anchors the bifurcation thesis.

---

### Full Paper Outline

---

#### Title
**APEX: SaaS Presales Engineers Will Not Disappear — They Will Bifurcate**

---

#### Abstract
**Target: 190–210 words | Structure: PMR+**

**Goal:** Establish the research gap (absence of task-stratified automation risk models for presales roles), name APEX by sentence 3, and report the two surviving quantitative claims with conservative framing.

**Evidence to use:**
- `role_survival_index` discriminant range: 0.021 (`what_proposed`) to 0.706 (`without_key_component`) — a 34× spread under different disruption assumptions
- Heterogeneous seed sensitivity: `without_key_component` std=0.1019 vs. `what_proposed` std=0.0011 — structural behavioral divergence across conditions
- Caveat sentence required: "APEX is a parametric scoring model; results reflect model assumptions and require calibration against longitudinal labor market data before external claims are warranted."

**Avoid:** Citing `market_value_score` as a finding (seed-determined confound). Avoid claiming empirical simulation.

---

#### 1. Introduction
**Target: 850–950 words | 4 paragraphs | 8–12 citations**

**Para 1 — Motivation (150–180 words)**
- Goal: Establish that SaaS presales is a structurally distinct labor category — not generic sales, not pure engineering — facing simultaneous disruption from LLM-based demo automation, AI-assisted discovery, and autonomous RFP response systems.
- Evidence links: Cite McKinsey Global Institute (2023) on knowledge worker automation; Gartner (2024) on AI in B2B sales cycles; BLS Occupational Outlook for "Sales Engineers" as the closest census proxy.
- Transition: "Yet despite these pressures, the presales function has received no systematic quantitative treatment in the automation-risk literature."

**Para 2 — Gap (180–220 words)**
- Goal: Identify that existing work (a) treats sales as monolithic, (b) ignores the technical advisory component of presales, and (c) produces role-level forecasts when task-level stratification is the operative question.
- Cite 3–5 papers: Acemoglu & Restrepo (2022) on task displacement; Felten et al. (2023) on occupational exposure scores; Webb (2020) on AI and job displacement; Autor (2024) on labor market polarization; one industry report (Forrester B2B Sales Tech Wave).
- Claim: "No existing model distinguishes between the discovery, demonstration, objection-handling, and champion-building subtasks that together constitute the presales motion."

**Para 3 — Approach (150–180 words)**
- Goal: Introduce APEX — a parametric role survival model that scores six conditions spanning full AI adoption to baseline human-centric delivery.
- Name the primary metric (`role_survival_index` ∈ [0,1]) and explain the ablation design conceptually.
- Acknowledge model-based (not empirical) nature in one sentence: "APEX is designed as a hypothesis-generating scaffold; its outputs characterize the sensitivity space of the presales role to AI adoption assumptions rather than predicting realized labor outcomes."

**Para 4 — Contributions (bullet list, 3–4 items)**
- C1: First parametric ablation study isolating AI disruption as a separable component in presales role survival
- C2: Demonstration that role survival sensitivity varies 34× across disruption assumptions — establishing the upper bound of plausible AI impact under the stated model
- C3: Identification of `market_value_score` seed-dependence as a methodological finding about composite metric design in workforce forecasting models
- C4: A reusable scoring scaffold (APEX) for future calibration against BLS/Gartner longitudinal data

---

#### 2. Related Work
**Target: 650–750 words | 3 subsections | ≥15 unique citations**

**2.1 Automation Risk Frameworks (200–240 words)**
- Routine-biased technological change (Autor, Levy, Murnane 2003); task vs. occupation distinction (Acemoglu & Restrepo 2022); AI exposure scores (Felten et al. 2023; Gmyrek et al. ILO 2023).
- Close: "These frameworks treat occupation codes as the unit of analysis; APEX operates at the subtask level within a single role, enabling finer-grained sensitivity measurement."

**2.2 SaaS Sales and Presales Labor Market Research (200–240 words)**
- Sales force automation literature (Raman et al. 2006; Hunter & Perreault 2007); CRM-era p

... (truncated, see full artifact)
