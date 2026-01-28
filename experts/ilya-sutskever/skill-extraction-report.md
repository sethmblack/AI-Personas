# Ilya Sutskever - Skill Extraction Report

**Date:** 2026-01-28
**Source:** `experts/ilya-sutskever/expertise.md` (362 lines)
**Training Commits:** 5

---

## Extraction Criteria

Each skill candidate must meet ALL 5 criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## Skill Candidates

### 1. Scale Hypothesis Evaluation

| Criterion | Met? | Evidence |
|-----------|------|----------|
| Actionable | Yes | Clear steps: evaluate scaling properties, extrapolate curves, prefer scale over tricks |
| Invocable | Yes | Trigger: "evaluate this architecture", "will this approach scale", "model selection" |
| Scoped | Yes | Focused on evaluating scaling properties of AI approaches |
| Reusable | Yes | Applies to any AI/ML architecture decision |
| Valuable | Yes | Prevents wasted effort on non-scalable approaches |

**Priority: HIGH**

**Description:** Apply Sutskever's scale hypothesis framework to evaluate AI architectures, model choices, or technical approaches. Uses empirical scaling patterns to predict capability trajectory.

**Workflow:**
1. Identify the scaling dimensions (compute, data, parameters)
2. Evaluate historical scaling behavior for the approach
3. Project capability improvements from increased scale
4. Compare to alternatives on scaling properties
5. Recommend based on scaling trajectory, not current performance

---

### 2. Compression-as-Intelligence Analysis

| Criterion | Met? | Evidence |
|-----------|------|----------|
| Actionable | Yes | Frame as compression problem, evaluate compression efficiency, predict emergent capabilities |
| Invocable | Yes | Trigger: "why does this model understand X", "explain emergent capabilities", "prediction vs understanding" |
| Scoped | Yes | Focused on analyzing model capabilities through compression lens |
| Reusable | Yes | Applies to any discussion of model understanding or capability |
| Valuable | Yes | Provides principled framework for capability analysis |

**Priority: HIGH**

**Description:** Apply the "prediction is compression, compression requires understanding" framework to analyze AI model capabilities. Explains emergent abilities as natural consequences of improved compression.

**Workflow:**
1. Identify the prediction task the model performs
2. Analyze what must be compressed to predict well
3. Explain how compression implies understanding of underlying structure
4. Connect prediction performance to capability emergence
5. Project future capabilities from improved compression

---

### 3. Alignment Impact Assessment

| Criterion | Met? | Evidence |
|-----------|------|----------|
| Actionable | Yes | Evaluate through alignment lens, consider long-term implications, prioritize interpretability |
| Invocable | Yes | Trigger: "safety implications", "alignment concerns", "superintelligence risk" |
| Scoped | Yes | Focused on alignment/safety evaluation of AI developments |
| Reusable | Yes | Applies to any AI capability or deployment decision |
| Valuable | Yes | Critical for responsible AI development |

**Priority: HIGH**

**Description:** Apply Sutskever's alignment-first methodology to evaluate AI developments. Reasons backward from superintelligence to determine present priorities and safety implications.

**Workflow:**
1. Identify capability increase or deployment context
2. Project capability trajectory toward superintelligence
3. Assess alignment implications at projected capability levels
4. Evaluate interpretability and control properties
5. Recommend safety-first priorities and mitigations

---

### 4. AGI Timeline Reasoning

| Criterion | Met? | Evidence |
|-----------|------|----------|
| Actionable | Yes | Consider probability ranges, reference scaling curves, state assumptions explicitly |
| Invocable | Yes | Trigger: "when will AGI happen", "AI timeline", "future of AI capabilities" |
| Scoped | Partial | Overlaps with scale hypothesis and alignment assessment |
| Reusable | Yes | Applies to any AGI/capability timeline discussion |
| Valuable | Yes | Provides grounded perspective on AI development trajectory |

**Priority: MEDIUM**

**Description:** Provide Sutskever-informed perspective on AGI timelines using empirical scaling observations and probability ranges.

**Workflow:**
1. Reference the 5-20 year timeline and its basis
2. Explain current limitations (generalization, sample efficiency)
3. Describe what breakthroughs are needed
4. Provide probability ranges, not point estimates
5. Connect to institutional planning horizons

---

### 5. Age-of-Research Framing

| Criterion | Met? | Evidence |
|-----------|------|----------|
| Actionable | Yes | Identify scaling limits, emphasize ideas over compute, focus on generalization |
| Invocable | Yes | Trigger: "why isn't scaling enough", "what's next for AI", "data limits" |
| Scoped | Partial | Broad framework that overlaps with other analyses |
| Reusable | Yes | Applies to AI strategy and research direction discussions |
| Valuable | Yes | Provides current-state context for AI development |

**Priority: MEDIUM**

**Description:** Apply Sutskever's "age of research" framework to contextualize AI development challenges and opportunities in the post-scaling era.

**Workflow:**
1. Explain the end of the "age of scaling" (2020-2025)
2. Identify data constraints ("peak data")
3. Highlight generalization/sample efficiency as key frontier
4. Emphasize ideas over compute as current bottleneck
5. Recommend research priorities for the new era

---

### 6. Deep Learning Conviction Assessment

| Criterion | Met? | Evidence |
|-----------|------|----------|
| Actionable | Partial | Philosophy rather than procedural steps |
| Invocable | Yes | Trigger: "should we bet on deep learning", "will this approach work" |
| Scoped | Partial | Broad philosophical stance |
| Reusable | Yes | Applies to any AI bet or research direction |
| Valuable | Partial | Inspirational but not highly procedural |

**Priority: LOW**

**Description:** Apply the "don't bet against deep learning" conviction to evaluate research directions and technology bets.

---

## Summary

| Priority | Count | Skills |
|----------|-------|--------|
| HIGH | 3 | Scale Hypothesis Evaluation, Compression-as-Intelligence Analysis, Alignment Impact Assessment |
| MEDIUM | 2 | AGI Timeline Reasoning, Age-of-Research Framing |
| LOW | 1 | Deep Learning Conviction Assessment |

---

## Recommendations

### Create PROMPT.md Files For:

1. **scale-hypothesis-evaluation** (HIGH) - Evaluate AI approaches using scaling principles
2. **compression-intelligence-analysis** (HIGH) - Analyze model capabilities through prediction/compression lens
3. **alignment-impact-assessment** (HIGH) - Assess safety implications of AI developments

### Defer or Merge:

- **AGI Timeline Reasoning** - Can be incorporated into alignment-impact-assessment
- **Age-of-Research Framing** - Context material; keep in expertise.md
- **Deep Learning Conviction Assessment** - Philosophical stance; keep in PROMPT.md voice

---

## Notes

Sutskever's expertise is highly theoretical and strategic rather than procedural. The extracted skills focus on analytical frameworks rather than step-by-step processes. This reflects his role as a researcher and strategic thinker rather than an implementer.

The three HIGH priority skills form a coherent triad:
1. **Scale Hypothesis** - How to evaluate AI approaches
2. **Compression-Intelligence** - How to understand AI capabilities
3. **Alignment Impact** - How to assess AI implications

These skills complement each other and represent Sutskever's core intellectual contributions.
