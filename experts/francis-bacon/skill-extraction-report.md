# Skill Extraction Report: francis-bacon

**Source:** experts/francis-bacon/expertise.md
**Analyzed:** 2026-01-27
**Candidates Found:** 4

---

## Extraction Methodology

Each potential skill evaluated against five criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## Skill Candidates Identified

### 1. Idol Diagnosis

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 10/10 | Four distinct idols with specific characteristics to identify |
| Invocable | 10/10 | Obvious trigger: "Why can't we think clearly about this?" |
| Scoped | 10/10 | Single responsibility: identifying cognitive obstacles |
| Reusable | 10/10 | Applies to any decision, analysis, or problem-solving situation |
| Valuable | 10/10 | Surfaces hidden biases before they derail conclusions |

**Total: 50/50** | **Priority: HIGH**

**Description:** A systematic diagnostic for identifying which of the Four Idols (Tribe, Cave, Marketplace, Theatre) are obstructing clear thinking in a given situation. Examines human nature biases, individual biases, language confusions, and inherited dogmas.

**Trigger Phrases:**
- "Why can't we agree on this?"
- "What biases might be affecting our thinking?"
- "Diagnose the obstacles to clear understanding"
- "What are we failing to see?"
- "Run an idol diagnosis"

---

### 2. Tables of Investigation (Inductive Method)

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 10/10 | Three explicit tables to construct, clear exclusion process |
| Invocable | 10/10 | Trigger: "Why does X happen?" "What causes Y?" |
| Scoped | 10/10 | Focused on causal investigation through systematic observation |
| Reusable | 10/10 | Applies to any causal question in any domain |
| Valuable | 10/10 | Prevents hasty generalization; builds genuine understanding |

**Total: 50/50** | **Priority: HIGH**

**Description:** Bacon's systematic method for investigating causes. Constructs Table of Presence (instances where phenomenon occurs), Table of Absence (similar conditions but phenomenon absent), and Table of Degrees (variations). Applies exclusion process to eliminate false causes and harvest tentative hypothesis.

**Trigger Phrases:**
- "Why does this happen?"
- "What causes X?"
- "I need to understand the root cause"
- "Investigate this systematically"
- "Build an inductive analysis"

---

### 3. Experiments of Light vs. Fruit

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 9/10 | Clear distinction to apply; evaluation framework |
| Invocable | 9/10 | Trigger: "Should we pursue this?" "What kind of investigation is this?" |
| Scoped | 10/10 | Single responsibility: classifying and prioritizing investigations |
| Reusable | 9/10 | Applies to research, experimentation, learning strategies |
| Valuable | 9/10 | Ensures understanding precedes application; prevents blind optimization |

**Total: 46/50** | **Priority: HIGH**

**Description:** Framework for distinguishing between investigations that illuminate causes ("experiments of light") versus those that produce useful results ("experiments of fruit"). Evaluates whether current work builds understanding or merely achieves outcomes, ensuring light precedes fruit.

**Trigger Phrases:**
- "Do we understand why this works?"
- "Are we optimizing blindly?"
- "Is this research or development?"
- "What kind of investigation should this be?"
- "Classify this experiment"

---

### 4. Anticipation vs. Interpretation

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 9/10 | Clear test to distinguish hasty from proper inference |
| Invocable | 9/10 | Trigger: "Is this conclusion justified?" "Are we jumping to conclusions?" |
| Scoped | 10/10 | Single responsibility: evaluating quality of inductive reasoning |
| Reusable | 9/10 | Applies to any generalization or conclusion |
| Valuable | 9/10 | Catches premature conclusions before they mislead |

**Total: 46/50** | **Priority: MEDIUM**

**Description:** Evaluates whether a conclusion is an "anticipation of nature" (hasty generalization from insufficient evidence) or a proper "interpretation of nature" (conclusion properly induced through systematic observation). Tests whether the inferential path is adequate.

**Trigger Phrases:**
- "Is this conclusion justified?"
- "Are we generalizing too quickly?"
- "Check this inference"
- "Is this an anticipation or interpretation?"
- "Validate this generalization"

---

## Summary

| Skill | Score | Priority | Create Skill? |
|-------|-------|----------|---------------|
| Idol Diagnosis | 50/50 | HIGH | YES |
| Tables of Investigation | 50/50 | HIGH | YES |
| Experiments of Light vs. Fruit | 46/50 | HIGH | YES |
| Anticipation vs. Interpretation | 46/50 | MEDIUM | YES |

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Bacon's Fall from Power | Historical narrative; no actionable workflow |
| Classification of Knowledge (Memory/Imagination/Reason) | Taxonomic reference, not a process to invoke |
| Famous Maxims | Reference quotes; no procedural steps |
| Salomon's House Organization | Historical description of research institution; not a personal methodology |
| Bacon vs. Aristotle Critique | Philosophical context; no repeatable workflow |
| Thomas Hobbes Connection | Historical note; informational only |
| Legacy and Influence | Reference material on historical impact |

---

## Overlap Analysis

| Candidate | Existing Skill | Overlap % | Decision |
|-----------|---------------|-----------|----------|
| Tables of Investigation | induction-audit (David Hume) | 25% | Distinct - Hume audits inductive assumptions; Bacon provides the method for conducting induction properly |
| Anticipation vs. Interpretation | induction-audit | 30% | Distinct - Bacon evaluates quality of specific inferences; Hume examines philosophical limits |
| Idol Diagnosis | bias-audit | 20% | Distinct - Bacon's framework is specific (4 Idols); general bias audit is different approach |
| Experiments of Light/Fruit | practical-experiment | 15% | Distinct - Bacon classifies investigation types; practical-experiment focuses on execution |

---

## Recommended Implementation

**Phase 1 - Core Skills (HIGH Priority):**
1. `idol-diagnosis` - The foundational bias/obstacle identification framework
2. `tables-of-investigation` - Bacon's systematic inductive method
3. `light-vs-fruit-classification` - Distinguishing understanding from results

**Phase 2 - Extended Skills (MEDIUM Priority):**
4. `anticipation-vs-interpretation` - Quality assessment of inductive conclusions

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: idol-diagnosis
Purpose: Identify which of the Four Idols obstruct clear thinking
Trigger: "What biases are affecting this?" "Why can't we see clearly?"
Integration: francis-bacon expert

Skill: tables-of-investigation
Purpose: Systematic inductive method through presence, absence, degrees
Trigger: "What causes this?" "Investigate systematically"
Integration: francis-bacon expert

Skill: light-vs-fruit-classification
Purpose: Distinguish investigations that illuminate from those that produce
Trigger: "Do we understand why this works?" "What type of investigation?"
Integration: francis-bacon expert

Skill: anticipation-vs-interpretation
Purpose: Evaluate whether conclusions are hasty or properly induced
Trigger: "Is this conclusion justified?" "Are we generalizing too quickly?"
Integration: francis-bacon expert
```

---

## Integration with Expert

These skills should be:
1. Added to `experts/francis-bacon/PROMPT.md` in an "Available Skills" section
2. Triggered proactively when the Francis Bacon expert detects relevant situations
3. Usable independently of the expert persona when invoked directly

### Skill Interaction Notes

- **idol-diagnosis** + **tables-of-investigation**: Natural sequence - clear idols first, then investigate
- **tables-of-investigation** + **anticipation-vs-interpretation**: Complementary - method produces conclusions, then validate quality
- **light-vs-fruit-classification** + **tables-of-investigation**: Ensures you're seeking light before fruit
