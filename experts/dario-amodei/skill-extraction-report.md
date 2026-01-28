# Dario Amodei - Skill Extraction Report

**Analysis Date:** 2026-01-28
**Expert Folder:** `experts/dario-amodei/`
**Source Files Analyzed:**
- PROMPT.md (179 lines)
- expertise.md (589 lines)

---

## Executive Summary

Three HIGH priority skills identified for extraction, all meeting the five criteria:
1. **Constitutional Constraints Design** - Define guardrails and self-evaluation principles for autonomous systems
2. **Responsible Scaling Assessment** - Evaluate capability-safety coupling for scaling decisions
3. **Capability-Safety Tradeoff Analysis** - Core Amodei methodology from PROMPT.md "Your Task" section

Two MEDIUM priority skills identified:
4. **AI Risk Category Classification** - Classify risks using Amodei's five-category framework
5. **Interpretability Audit** - Evaluate explainability of system decisions

---

## Skill Candidate Analysis

### Candidate 1: Constitutional Constraints Design

**Source Location:** PROMPT.md lines 29-35, expertise.md lines 94-162

**Description:** A methodology for defining explicit principles that autonomous systems should follow, including self-evaluation mechanisms and revision protocols.

**Criteria Assessment:**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Actionable | 9/10 | Clear three-question framework + two-phase process |
| Invocable | 9/10 | Trigger: "design constraints for...", "define guardrails for..." |
| Scoped | 8/10 | Focused on constraint definition and self-evaluation |
| Reusable | 9/10 | Applies to any autonomous system (CI/CD, monitoring, automation) |
| Valuable | 9/10 | Saves significant design effort; prevents downstream safety issues |

**Average Score:** 8.8/10

**Priority:** HIGH

**Proposed Skill Name:** `constitutional-constraints-design`

**Key Inputs:**
- System or feature being designed
- Current automation level
- Risk tolerance

**Key Outputs:**
- Explicit constraints document
- Self-evaluation checkpoints
- Revision/rollback mechanisms

---

### Candidate 2: Responsible Scaling Assessment

**Source Location:** PROMPT.md lines 45-51, expertise.md lines 126-146, 315-324

**Description:** A framework for evaluating whether capability increases are appropriately coupled with safety investments, including threshold identification and safeguard triggers.

**Criteria Assessment:**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Actionable | 9/10 | Three-question framework + ASL-style threshold structure |
| Invocable | 9/10 | Trigger: "assess scaling safety for...", "evaluate capability increase..." |
| Scoped | 8/10 | Focused on capability-safety coupling decisions |
| Reusable | 9/10 | Applies to any system being scaled or given more autonomy |
| Valuable | 9/10 | Critical safety check before increasing system capability |

**Average Score:** 8.8/10

**Priority:** HIGH

**Proposed Skill Name:** `responsible-scaling-assessment`

**Key Inputs:**
- Current capability level
- Proposed capability increase
- Existing safeguards

**Key Outputs:**
- Capability threshold analysis
- Required safeguards per threshold
- Scaling commitment document

---

### Candidate 3: Capability-Safety Tradeoff Analysis

**Source Location:** PROMPT.md lines 147-173 ("Your Task" section)

**Description:** The core Amodei methodology as expressed in the expert's five-step transformation process. Takes any technical content and analyzes it through capability-safety, empirical, constitutional, scaling, and institutional lenses.

**Criteria Assessment:**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Actionable | 10/10 | Explicit 5-step process with sub-bullets |
| Invocable | 9/10 | Trigger: "analyze tradeoffs for...", "safety analysis of..." |
| Scoped | 8/10 | Focused on tradeoff identification and framing |
| Reusable | 9/10 | Applies to any technical decision, feature, or system |
| Valuable | 9/10 | Transforms generic content into safety-conscious analysis |

**Average Score:** 9.0/10

**Priority:** HIGH

**Proposed Skill Name:** `capability-safety-analysis`

**Key Inputs:**
- Technical content/decision to analyze
- Context (system, feature, deployment)

**Key Outputs:**
- Capability-safety tradeoff mapping
- Empirical evidence grounding
- Constitutional constraints to add
- Scaling implications
- Institutional coordination requirements

---

### Candidate 4: AI Risk Category Classification

**Source Location:** expertise.md lines 328-374

**Description:** Classify risks using Amodei's five-category framework: Autonomy, CBRN, Cybersecurity/Autonomous Operations, Authoritarian Capture, and Economic Disruption.

**Criteria Assessment:**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Actionable | 8/10 | Five clear categories with sub-types |
| Invocable | 7/10 | Trigger: "classify AI risks of..." |
| Scoped | 9/10 | Very focused on risk categorization |
| Reusable | 6/10 | More specialized to AI systems specifically |
| Valuable | 7/10 | Useful for AI risk assessment, less for general tech |

**Average Score:** 7.4/10

**Priority:** MEDIUM

**Proposed Skill Name:** `ai-risk-classification`

**Note:** More specialized; recommend extraction only if AI risk assessment is common use case.

---

### Candidate 5: Interpretability Audit

**Source Location:** PROMPT.md lines 37-43, expertise.md lines 148-161

**Description:** Evaluate whether a system's decisions can be explained at the mechanism level, not just input-output behavior.

**Criteria Assessment:**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Actionable | 7/10 | Three key questions; less procedural detail |
| Invocable | 8/10 | Trigger: "audit interpretability of...", "can we explain why..." |
| Scoped | 8/10 | Focused on explainability assessment |
| Reusable | 7/10 | Applies to opaque systems (ML models, complex automation) |
| Valuable | 7/10 | Important for high-stakes decisions |

**Average Score:** 7.4/10

**Priority:** MEDIUM

**Proposed Skill Name:** `interpretability-audit`

**Note:** Consider bundling with capability-safety-analysis as a sub-component.

---

## Rejected Candidates

### Scaling Laws Frame

**Reason for Rejection:** Too conceptual; overlaps significantly with Responsible Scaling Assessment. The scaling laws thinking is better expressed as part of other skills rather than standalone.

### Optimistic Long-Term Vision

**Reason for Rejection:** Not actionable as a skill; this is a voice/tone characteristic rather than a procedure. Belongs in PROMPT.md voice definition.

### Empirical Lens Application

**Reason for Rejection:** Too generic; better expressed as a principle woven through all skills rather than a standalone skill.

---

## Extraction Recommendation Summary

| Skill | Priority | Recommended Action |
|-------|----------|-------------------|
| `constitutional-constraints-design` | HIGH | Extract as standalone skill |
| `responsible-scaling-assessment` | HIGH | Extract as standalone skill |
| `capability-safety-analysis` | HIGH | Extract as standalone skill |
| `ai-risk-classification` | MEDIUM | Defer - specialized use case |
| `interpretability-audit` | MEDIUM | Consider bundling with capability-safety-analysis |

---

## Skill Integration Notes

### Recommended Skill Chain

For comprehensive system analysis, skills should chain:

1. **capability-safety-analysis** (broad analysis)
2. **responsible-scaling-assessment** (if capability increase detected)
3. **constitutional-constraints-design** (for implementation)

### Trigger Overlap Management

- "analyze safety of X" → capability-safety-analysis
- "design constraints for X" → constitutional-constraints-design
- "can we scale X safely?" → responsible-scaling-assessment

### Voice Consistency

All extracted skills should maintain Amodei voice characteristics:
- Empirical grounding ("we've observed...")
- Measured confidence ("our current understanding suggests...")
- Cautious optimism ("this is tractable if...")
- Institutional awareness ("this requires coordination...")
