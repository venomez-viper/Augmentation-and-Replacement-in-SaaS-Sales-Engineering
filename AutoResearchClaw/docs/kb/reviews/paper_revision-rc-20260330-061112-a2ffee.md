---
created: '2026-03-30T23:46:47+00:00'
evidence:
- stage-19/paper_revised.md
id: paper_revision-rc-20260330-061112-a2ffee
run_id: rc-20260330-061112-a2ffee
stage: 19-paper_revision
tags:
- paper_revision
- stage-19
- run-rc-20260
title: 'Stage 19: Paper Revision'
---

# Stage 19: Paper Revision

---

# APEX: AI Augments or Replaces — Measuring SaaS Presales Role Survival

---

# Abstract

The automation of knowledge work has generated extensive literature on occupation-level displacement risk, yet the SaaS presales engineer — a role straddling technical expertise and relationship-driven advisory — remains unmodeled in quantitative frameworks. Existing AI exposure indices [chang2024survey] treat sales occupations as monolithic categories, obscuring the heterogeneous subtask composition that makes presales structurally distinct from both pure sales and pure engineering. We introduce APEX (Automated Presales role Evolution eXperiment), a parametric role survival scoring model that characterizes the sensitivity of presales labor viability across six AI adoption scenarios ranging from AI-free counterfactual baselines to full replacement architectures. APEX produces a Role Survival Index (RSI ∈ [0,1]) as its primary outcome via a sigmoid-normalized scoring function, enabling ablation over disruption assumptions across three random seeds. Across 18 experimental runs, APEX yields a 56× discriminant range (RSI = 0.0091 under full AI replacement versus RSI = 0.5124 under the conservative 2024 baseline), establishing that role survival is acutely sensitive to which subtasks AI absorbs. Strikingly, the AI-free counterfactual (RSI = 0.2890) falls below both augmentation baselines, providing parametric evidence that AI copilot tools confer a modeled viability benefit that outweighs organic market attrition. These comparisons are conducted with n=3 seeds and should be treated as preliminary pending higher-seed calibration.

*(196 words)*

---

# Introduction

The SaaS presales engineer — the technical specialist who bridges a vendor's product capability and a prospective buyer's operational requirements — occupies a structurally unusual position in the knowledge-work landscape. Unlike a quota-carrying account executive, the presales engineer's value proposition is epistemic: they translate ambiguous customer pain into a credible technical narrative, manage proof-of-concept scoping, construct RFP responses, and build the internal champions within a buying organization whose advocacy survives the close. Prior work examining AI-driven automation of knowledge work [sebastian2020companies; correani2020implementing] has documented broad productivity effects across white-collar functions, and industry observers have noted that large language models are beginning to encroach on technical documentation, demonstration preparation, and structured question-answering — all activities that constitute a substantial portion of the presales motion. Gartner's B2B sales technology forecasts suggest that AI copilot adoption in enterprise sales cycles reached over 40% of surveyed organizations by late 2024, while analysis of knowledge worker displacement scenarios projects that 30–60% of current work activities in sales-adjacent functions are technically automatable by 2030 [johnk2020ready]. Yet despite these converging pressures, the SaaS presales function has received no systematic quantitative treatment in the automation risk literature.

The gap is consequential. Existing automation exposure frameworks, including the occupational exposure scores of prior work [hassani2020artificial; martinezplumed2020futures], treat BLS occupation codes as the unit of analysis, mapping broad job categories onto AI capability assessments. Sales Engineers (SOC 41-9031) appear in these frameworks as a single category — obscuring the internal heterogeneity of the role. A presales engineer performing live product demonstrations against scripted evaluation criteria faces a qualitatively different automation risk than one engaged in executive discovery conversations, building a business case from unstructured stakeholder interviews, or constructing a multi-vendor competitive positioning narrative. No existing model distinguishes between the discovery, demonstration, objection-handling, and champion-building subtasks that together constitute the presales motion. This subtask-level blind spot means that aggregate displacement forecasts for Sales Engineers likely misrepresent both the speed and the selectivity of AI impact — understating displacement in highly automatable subtasks while simultaneously understating resilience in relationship-anchored ones. The product-led growth (PLG) literature compounds this confusion: when self-serve adoption enables buyers to evaluate software without human presales intervention, automation risk is not uniform across deal segments — it is conditional on deal size, buyer sophistication, and the availability of PLG alternatives [davis2021varieties].

APEX addresses this gap by introducing a parametric role survival scoring model designed as an explicit hypothesis-generating scaffold. Rather than asserting an empirically validated displacement trajectory, APEX characterizes the *sensitivity space* of presales role viabilit

... (truncated, see full artifact)
