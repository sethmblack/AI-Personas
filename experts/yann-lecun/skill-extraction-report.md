# Yann LeCun - Skill Extraction Report

**Generated:** 2026-01-26
**Source:** `experts/yann-lecun/expertise.md`
**Expert:** Yann LeCun

---

## Extraction Criteria

Each skill candidate must meet ALL 5 criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## HIGH PRIORITY CANDIDATES

### 1. LLM Capability Reality Check

**Description:** Systematic assessment of whether AI/LLM claims match fundamental architectural capabilities using LeCun's critique framework.

| Criterion | Assessment |
|-----------|------------|
| Actionable | Yes - Apply 5-point checklist (persistent memory, world model, common sense, planning, causal reasoning) |
| Invocable | Yes - "Does this AI actually X?" or "Check this claim" |
| Scoped | Yes - Evaluates capability claims against architectural limits |
| Reusable | Yes - Applies to any AI system evaluation |
| Valuable | High - Cuts through hype, prevents overcommitment to limited systems |

**Trigger Phrases:**
- "Does ChatGPT/this LLM actually understand..."
- "Can AI really..."
- "Evaluate this AI claim"
- "Is this AI hype?"

**Priority:** HIGH

---

### 2. World Model Architecture Assessment

**Description:** Evaluate whether a proposed AI system has the components needed for genuine intelligence using LeCun's 6-component framework.

| Criterion | Assessment |
|-----------|------------|
| Actionable | Yes - Check for perception, world model, cost, actor, memory, configurator modules |
| Invocable | Yes - "Does this system have a world model?" or "Analyze this architecture" |
| Scoped | Yes - Architecture evaluation only |
| Reusable | Yes - Applies to any AI system design |
| Valuable | High - Distinguishes genuinely capable systems from reactive pattern matchers |

**Trigger Phrases:**
- "Can this system plan?"
- "Does this have a world model?"
- "Evaluate this AI architecture"
- "Will this system hallucinate?"

**Priority:** HIGH

---

### 3. AI Hype Deflation

**Description:** Apply LeCun's contrarian perspective to challenge overhyped AI predictions and claims, grounding them in engineering reality and historical perspective.

| Criterion | Assessment |
|-----------|------------|
| Actionable | Yes - Apply cat/dog benchmark, check for unfounded AGI claims, reference AI winter lessons |
| Invocable | Yes - "Is this AI prediction realistic?" or "Challenge this claim" |
| Scoped | Yes - Evaluates predictions/claims against realistic timelines |
| Reusable | Yes - Applies to any AI forecast or capability claim |
| Valuable | High - Prevents bad decisions based on unrealistic expectations |

**Trigger Phrases:**
- "AGI will arrive by..."
- "AI will replace..."
- "Is this prediction realistic?"
- "Evaluate this AI forecast"

**Priority:** HIGH

---

### 4. Generative vs Predictive Architecture Comparison

**Description:** Compare autoregressive/generative approaches (GPT-style) with predictive/JEPA approaches, explaining trade-offs and appropriate use cases.

| Criterion | Assessment |
|-----------|------------|
| Actionable | Yes - Structured comparison of approaches with specific criteria |
| Invocable | Yes - "Should we use LLM or world model approach?" |
| Scoped | Yes - Architecture comparison only |
| Reusable | Yes - Applies to AI architecture decisions |
| Valuable | Medium-High - Informs strategic technical choices |

**Trigger Phrases:**
- "Should we use an LLM for this?"
- "Compare generative vs predictive"
- "What architecture should we use?"
- "Explain JEPA vs GPT"

**Priority:** HIGH

---

## MEDIUM PRIORITY CANDIDATES

### 5. System 1/System 2 AI Analysis

**Description:** Analyze whether an AI system operates in reactive (System 1/Mode-1) or deliberative (System 2/Mode-2) mode, and what would be needed for the latter.

| Criterion | Assessment |
|-----------|------------|
| Actionable | Yes - Apply Kahneman/LeCun framework to classify systems |
| Invocable | Yes - "Is this AI doing System 1 or System 2?" |
| Scoped | Partial - Overlaps with world model assessment |
| Reusable | Yes - Applies to any AI system |
| Valuable | Medium - Useful conceptual frame but somewhat redundant with #2 |

**Trigger Phrases:**
- "Can this system reason?"
- "Is this reactive or deliberative?"
- "Does this use System 2 thinking?"

**Priority:** MEDIUM (overlaps with #2)

---

## LOW PRIORITY / REJECTED CANDIDATES

### 6. Historical Deep Learning Perspective

**Assessment:** Rich biographical and historical content but not actionable as a skill.
**Reason for Rejection:** Reference material, not a procedural workflow.

### 7. Regulatory Position Generator

**Assessment:** LeCun has strong views on AI regulation, but generating policy positions is not a repeatable technical skill.
**Reason for Rejection:** Opinion-based rather than procedural.

### 8. Twitter Debate Response

**Assessment:** LeCun's debate style is distinctive but too specific and potentially contentious.
**Reason for Rejection:** Not a professional skill, could generate unhelpful conflict.

---

## RECOMMENDED SKILLS TO CREATE

| # | Skill Name | Priority | Description |
|---|------------|----------|-------------|
| 1 | `yann-lecun--llm-capability-check` | HIGH | Reality-check AI/LLM claims against architectural limits |
| 2 | `yann-lecun--world-model-assessment` | HIGH | Evaluate AI architectures for world model components |
| 3 | `yann-lecun--ai-hype-deflation` | HIGH | Challenge overhyped AI predictions with engineering reality |
| 4 | `yann-lecun--architecture-comparison` | HIGH | Compare generative vs predictive AI approaches |

---

## SKILL INTEGRATION NOTES

These skills complement each other:
- **llm-capability-check** is the quick diagnostic
- **world-model-assessment** is the deep architecture review
- **ai-hype-deflation** is for evaluating external claims and predictions
- **architecture-comparison** is for making design decisions

**Recommended Chaining:**
1. When evaluating an AI claim: Start with `llm-capability-check`, escalate to `world-model-assessment` if needed
2. When making architecture decisions: Use `architecture-comparison` first, then `world-model-assessment` for validation
3. When reviewing predictions/roadmaps: Use `ai-hype-deflation`
