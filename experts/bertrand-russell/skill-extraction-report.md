# Skill Extraction Report: bertrand-russell

**Source:** experts/bertrand-russell/expertise.md
**Analyzed:** 2026-01-27
**Candidates Found:** 4

---

## HIGH Priority

### 1. logical-analysis
**Source Pattern:** Logical Analysis Pattern
**Purpose:** Decompose complex statements into logical components to determine if they are meaningful, true, false, or confused
**Trigger:** "Is this statement meaningful?" or "Analyze this argument" or "What does this actually claim?"
**Inputs:** A statement, argument, or claim to be analyzed
**Outputs:** Logical decomposition showing the claim's structure, hidden assumptions, truth conditions, and assessment
**Reasoning:** Core Russell methodology with clear 6-step process; used in every intellectual domain; no existing skill provides this specific logical decomposition approach.

---

### 2. paradox-detection
**Source Pattern:** Paradox Detection Pattern
**Purpose:** Identify self-referential contradictions and foundational problems in reasoning, claims, or systems
**Trigger:** "Is there a paradox here?" or "Test this foundation" or "Does this system have contradictions?"
**Inputs:** A claim, system, or set of rules to examine for self-reference issues
**Outputs:** Analysis identifying any circular definitions, self-referential contradictions, or foundational problems
**Reasoning:** Russell's discovery of his famous paradox represents his signature contribution; this skill codifies the methodology; critical for evaluating foundations of any system.

---

## MEDIUM Priority

### 3. proportioned-belief
**Source Pattern:** Skeptical Inquiry Pattern
**Purpose:** Evaluate claims and proportion confidence to available evidence, avoiding both credulity and excessive skepticism
**Trigger:** "Should I believe this?" or "How confident should I be?" or "Evaluate this claim"
**Inputs:** A claim or belief to evaluate, along with available evidence
**Outputs:** Assessment of evidence quality, alternative explanations, and recommended confidence level
**Reasoning:** Russell's scientific temper approach; differs from mitigated-skepticism which focuses on philosophical skepticism rather than practical belief calibration.

---

### 4. clarity-rewrite
**Source Pattern:** Clarity Through Decomposition Pattern
**Purpose:** Transform complex, obscure, or muddled writing into clear, precise, accessible prose
**Trigger:** "Make this clearer" or "Simplify this explanation" or "Write this more clearly"
**Inputs:** Complex or unclear text to be clarified
**Outputs:** Rewritten version with precise definitions, concrete examples, simplified structure
**Reasoning:** Russell's legendary writing style; differs from essay-clarity-rewrite (which exists) but has minimal overlap (~25%) since that focuses on essay structure rather than Russell's specific decomposition methodology.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Occam's Razor Application | >50% overlap with existing `via-negativa-reduction` skill |
| Theory of Descriptions | Too specialized/technical for general use; better as expertise reference |
| Logical Atomism | Metaphysical framework, not actionable workflow |
| Neutral Monism | Reference knowledge, not actionable workflow |
| Writing style characteristics | Already captured in PROMPT.md voice definition |
| Biographical details | Reference material, no workflow |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: logical-analysis
Purpose: Decompose complex statements into logical components to determine if meaningful, true, false, or confused
Trigger: "Analyze this argument" or "What does this claim mean?"
Integration: bertrand-russell expert
```

```
Skill: paradox-detection
Purpose: Identify self-referential contradictions and foundational problems in reasoning
Trigger: "Is there a paradox here?" or "Test this foundation"
Integration: bertrand-russell expert
```

```
Skill: proportioned-belief
Purpose: Evaluate claims and proportion confidence to available evidence
Trigger: "Should I believe this?" or "How confident should I be?"
Integration: bertrand-russell expert
```

```
Skill: clarity-rewrite
Purpose: Transform complex/muddled writing into clear, precise, accessible prose
Trigger: "Make this clearer" or "Simplify this"
Integration: bertrand-russell expert
```
