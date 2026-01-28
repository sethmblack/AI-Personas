# Skill Extraction Report: fei-fei-li

**Source:** experts/fei-fei-li/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 5

---

## HIGH Priority

### 1. dataset-quality-audit

**Source Pattern:** The ImageNet Methodology + ImageNet Quality Control Details
**Purpose:** Systematically evaluate dataset quality for ML training using ImageNet-derived principles
**Trigger:** "Review this dataset for quality issues" or "Is this training data good enough?" or "Audit our data pipeline"
**Inputs:** Dataset description, annotation methodology, quality control processes, data sources
**Outputs:** Quality assessment report with scores for taxonomy design, annotation consistency, diversity coverage, and actionable recommendations
**Reasoning:** Meets all 5 criteria:
- Actionable: Has 6 explicit steps from ImageNet methodology (taxonomy design, scale with purpose, crowdsourced annotation, quality control, iterative refinement, public availability)
- Invocable: Clear trigger phrases for data quality review
- Scoped: Focused solely on dataset quality assessment
- Reusable: Applies to any ML dataset, not domain-specific
- Valuable: Prevents costly downstream model failures, saves weeks of debugging mislabeled data

---

### 2. human-centered-ai-assessment

**Source Pattern:** Human-Centered AI Design (Stanford HAI Framework) + Three Foundational Principles + Stanford HAI Policy Principles
**Purpose:** Evaluate AI systems against human-centered design principles to ensure ethical, beneficial deployment
**Trigger:** "Review this AI system for human-centered design" or "Who benefits from this AI?" or "Is this AI human-centered?"
**Inputs:** AI system description, intended users, deployment context, stakeholder list
**Outputs:** Assessment report covering stakeholder impact, augmentation vs replacement analysis, diversity representation, and governance readiness with specific recommendations
**Reasoning:** Meets all 5 criteria:
- Actionable: 5 explicit stakeholder identification steps plus 4 policy principles (interoperability, transparency, accountability, equity)
- Invocable: Maps to common AI ethics review requests
- Scoped: Focused on human-centered assessment, not technical performance
- Reusable: Applies to any AI system regardless of domain
- Valuable: Prevents harmful deployments, ensures ethical compliance, saves reputation damage and regulatory issues

---

### 3. data-cascade-diagnosis

**Source Pattern:** The Data Cascade Problem
**Purpose:** Identify how data quality issues compound through ML pipelines and recommend interventions
**Trigger:** "Why is my model failing?" or "Diagnose data pipeline issues" or "Where is the bias coming from?"
**Inputs:** Model performance metrics (especially by subgroup), training data description, deployment environment details
**Outputs:** Cascade diagnosis identifying which stage (collection bias, annotation inconsistency, distribution shift, feedback loops) is causing issues, with stage-specific remediation steps
**Reasoning:** Meets all 5 criteria:
- Actionable: 4 explicit stages with diagnostic questions for each ("What populations are missing?", "What quality controls exist?", "Where will this actually run?", "How does the model change its own data?")
- Invocable: Common debugging scenario for ML practitioners
- Scoped: Focused specifically on tracing data cascade failures
- Reusable: Applies to any ML pipeline with performance issues
- Valuable: Saves weeks of debugging by systematically identifying root cause instead of random fixes

---

## MEDIUM Priority

### 4. ambient-intelligence-design

**Source Pattern:** Ambient Intelligence Framework + Ambient Intelligence Application Areas
**Purpose:** Design privacy-preserving, non-intrusive AI monitoring systems for healthcare or care environments
**Trigger:** "Design an ambient AI system for healthcare" or "How do we monitor without invading privacy?" or "Create a care environment AI"
**Inputs:** Target environment (ICU, home, elder care), monitoring objectives, privacy requirements, stakeholder needs
**Outputs:** Ambient intelligence design specification covering sensor selection, privacy-by-design measures, clinician/family collaboration protocols, and ethical considerations
**Reasoning:** Meets all 5 criteria:
- Actionable: 4 design principles (sensor diversity, privacy-by-design, continuous/non-intrusive, clinician collaboration) with domain-specific application guidance
- Invocable: Relevant for healthcare AI projects
- Scoped: Focused on ambient monitoring design
- Reusable: Applies across healthcare settings (ICU, elder care, home health)
- Valuable: Prevents privacy violations and ensures effective care augmentation; however, narrower domain than other candidates (healthcare-specific)

---

### 5. north-star-question

**Source Pattern:** Core Principles to Weave In + Signature Phrases ("Who is this AI for?", "North Star question")
**Purpose:** Force clarity on human purpose before technical optimization by asking the fundamental question
**Trigger:** "Who is this AI for?" or "What problem are we actually solving?" or "Before we optimize further..."
**Inputs:** Technical project description, proposed optimization, target metrics
**Outputs:** North Star clarification identifying: specific beneficiaries, human problem solved, populations potentially excluded, and whether optimization connects to human impact
**Reasoning:** Meets all 5 criteria:
- Actionable: Specific question framework with follow-up probes
- Invocable: Simple trigger phrase
- Scoped: Single responsibility (purpose clarification)
- Reusable: Universal across any AI/technical project
- Valuable: Prevents wasted effort on wrong optimizations; however, simpler than other candidates (fewer steps)

---

## LOW Priority

None identified. All candidates meeting criteria are MEDIUM or HIGH priority based on frequency and value.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Context | Reference knowledge (career arc, dates, positions), not actionable workflow |
| Verified Quotes | Reference material for voice embodiment, not a standalone skill |
| Signature Phrases to Use | Vocabulary guidance, stays in PROMPT.md for voice consistency |
| AI4ALL: Diversity in AI Education | Background context, not an actionable methodology |
| Awards and Recognition | Pure reference data, no workflow |
| Integration Notes | Meta-guidance for expert collaboration, not standalone skill |
| Expert Synergies table | Reference for orchestrator, not invocable skill |
| Anti-Patterns to Avoid | Gotchas and warnings, stays as expertise reference |
| Spatial Intelligence (World Labs) | Emerging research area, insufficient actionable steps currently |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: dataset-quality-audit
Purpose: Systematically evaluate dataset quality for ML training using ImageNet-derived principles
Trigger: "Review this dataset for quality issues" or "Is this training data good enough?"
Integration: fei-fei-li expert
```

```
Skill: human-centered-ai-assessment
Purpose: Evaluate AI systems against human-centered design principles
Trigger: "Review this AI system for human-centered design" or "Who benefits from this AI?"
Integration: fei-fei-li expert
```

```
Skill: data-cascade-diagnosis
Purpose: Identify how data quality issues compound through ML pipelines
Trigger: "Why is my model failing?" or "Diagnose data pipeline issues"
Integration: fei-fei-li expert
```

```
Skill: ambient-intelligence-design
Purpose: Design privacy-preserving ambient AI monitoring systems for healthcare
Trigger: "Design an ambient AI system for healthcare"
Integration: fei-fei-li expert
```

```
Skill: north-star-question
Purpose: Force clarity on human purpose before technical optimization
Trigger: "Who is this AI for?" or "What problem are we actually solving?"
Integration: fei-fei-li expert
```

---

## Overlap Analysis

| Candidate | Potential Overlap | Overlap % | Decision |
|-----------|-------------------|-----------|----------|
| dataset-quality-audit | data-first-analysis | <30% | Distinct (data-first is about approach, this is about quality control) |
| human-centered-ai-assessment | ai-capability-safety-assessment | <30% | Distinct (safety vs human-centered are complementary lenses) |
| data-cascade-diagnosis | root-cause-diagnosis | <30% | Distinct (generic root cause vs specific ML data cascade) |
| ambient-intelligence-design | No overlap found | 0% | New capability |
| north-star-question | No overlap found | 0% | New capability |
