# Skill Extraction Report: rosalind-franklin

**Source:** experts/rosalind-franklin/expertise.md
**Analyzed:** 2026-01-18
**Candidates Found:** 5

---

## Scoring Criteria

Each skill is evaluated on 5 criteria, 10 points each (max 50):

1. **Actionable** — Has explicit steps and clear outputs
2. **Invocable** — Natural trigger phrases exist
3. **Scoped** — Single, focused responsibility
4. **Reusable** — Applies across multiple domains
5. **Valuable** — Produces significant time savings or quality improvement

**Priority Thresholds:**
- HIGH: 40+ points
- MEDIUM: 30-39 points
- LOW: Below 30 points

---

## HIGH Priority

### 1. experimental-design-framework

**Source Pattern:** Scientific Methodology / Experimental Rigor
**Purpose:** Design rigorous experiments with controlled variables, precise measurements, and systematic documentation.
**Trigger:** "Help me design an experiment" or "How would you investigate this?" or "What's the right methodology?"
**Inputs:** Research question, available resources, constraints, prior knowledge
**Outputs:** Experimental design including: precise question formulation, variable identification (independent, dependent, controlled), measurement protocols, documentation requirements, anticipated confounds

**Criterion Evaluation:**
- Actionable: 10/10 — Clear 6-step framework from question to documentation
- Invocable: 9/10 — Natural triggers for research and investigation
- Scoped: 9/10 — Focused on experimental design (does not include execution or analysis)
- Reusable: 10/10 — Applies to scientific research, A/B testing, product experiments, market research
- Valuable: 10/10 — Prevents costly experimental failures and wasted resources

**Total: 48/50 — HIGH PRIORITY**

---

### 2. data-first-analysis

**Source Pattern:** The Methodological Difference / Cautious Conclusions
**Purpose:** Analyze evidence with crystallographic precision, distinguishing what is demonstrated from what is speculated.
**Trigger:** "What does the data actually show?" or "Analyze this evidence" or "Am I overreaching?"
**Inputs:** Data or evidence, claims being made, context
**Outputs:** Tiered assessment: (1) What is demonstrated with high confidence, (2) What is probable given the evidence, (3) What is possible but unconfirmed, (4) What remains unknown, (5) What further evidence would clarify

**Criterion Evaluation:**
- Actionable: 10/10 — 5-tier output structure with clear distinctions
- Invocable: 10/10 — Very natural trigger phrases
- Scoped: 9/10 — Focused on evidence interpretation (distinct from gathering or acting on it)
- Reusable: 10/10 — Applies to research, business decisions, claims evaluation, journalism
- Valuable: 10/10 — Prevents overconfident conclusions; especially valuable in high-stakes decisions

**Total: 49/50 — HIGH PRIORITY**

---

### 3. variable-control-analysis

**Source Pattern:** The A-form and B-form Distinction / Experimental Rigor
**Purpose:** Identify hidden variables causing inconsistent results; systematically isolate the source of variation.
**Trigger:** "Why are my results inconsistent?" or "What am I not controlling for?" or "Debug this experiment"
**Inputs:** Description of inconsistent results, known conditions, what has been tried
**Outputs:** Systematic diagnosis: (1) Inventory of potential variables, (2) Comparison of conditions across runs, (3) Hypotheses for source of variation, (4) Isolation protocol to test each hypothesis, (5) Recommended controls for future runs

**Criterion Evaluation:**
- Actionable: 10/10 — Clear diagnostic process with specific outputs
- Invocable: 10/10 — Perfect trigger for troubleshooting scenarios
- Scoped: 9/10 — Focused on identifying and controlling variables
- Reusable: 10/10 — Applies to experiments, software debugging, manufacturing, process improvement
- Valuable: 10/10 — Solves common and frustrating problem of irreproducible results

**Total: 49/50 — HIGH PRIORITY**

---

## MEDIUM Priority

### 4. precision-measurement-protocol

**Source Pattern:** Meticulous preparation / Quality of Work
**Purpose:** Establish rigorous measurement standards and documentation practices.
**Trigger:** "How do I measure this precisely?" or "What's the right way to collect this data?" or "Set up measurement standards"
**Inputs:** What needs to be measured, accuracy requirements, available tools
**Outputs:** Measurement protocol including: instrument specifications, calibration requirements, environmental conditions, documentation template, quality checks, reproducibility verification

**Criterion Evaluation:**
- Actionable: 9/10 — Clear protocol structure, though specifics vary by domain
- Invocable: 8/10 — Trigger phrases are natural but somewhat technical
- Scoped: 9/10 — Focused on measurement setup (distinct from design and analysis)
- Reusable: 8/10 — Most applicable to scientific and technical contexts
- Valuable: 8/10 — Significant value in research contexts, less universal than other skills

**Total: 42/50 — HIGH PRIORITY (borderline)**

---

### 5. evidence-sufficiency-assessment

**Source Pattern:** Cautious Conclusions / "X-ray evidence cannot, at present, be taken as direct proof"
**Purpose:** Determine whether evidence is sufficient to support a claim before publishing, presenting, or deciding.
**Trigger:** "Is this enough evidence?" or "Can I make this claim?" or "Should I publish/present this?"
**Inputs:** Evidence available, claim to be made, stakes involved, audience expectations
**Outputs:** Sufficiency assessment: (1) Strength of evidence (proof / strong indication / suggestive / insufficient), (2) Gaps that would strengthen the case, (3) Appropriate qualifications for the claim, (4) Recommended language for different certainty levels, (5) What additional evidence would change the assessment

**Criterion Evaluation:**
- Actionable: 9/10 — Clear assessment framework with categorized outputs
- Invocable: 9/10 — Natural triggers for decision points
- Scoped: 8/10 — Focused on go/no-go assessment, though overlaps with data-first-analysis
- Reusable: 9/10 — Applies to publishing, presenting, making recommendations, decision-making
- Valuable: 9/10 — Prevents embarrassing overreach and protects credibility

**Total: 44/50 — HIGH PRIORITY**

---

## LOW Priority

*None identified. All candidate patterns met minimum thresholds.*

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| X-ray Crystallography Technique | Domain-specific technical method, not generalizable workflow |
| Heavy Atom Substitution | Specialized crystallography technique, not applicable outside chemistry |
| Carbon Structure Analysis | Specific to materials science, insufficient general application |
| Virus Structure Determination | Specific research domain, not transferable |
| A-form vs B-form Classification | Subsumed by variable-control-analysis as an example of the principle |
| Biographical Context | Reference material, not actionable workflow |
| Personality Traits | Descriptive information, not a skill |
| Working Environment Analysis | Contextual, not a structured methodology |

---

## Summary

| Skill | Score | Priority |
|-------|-------|----------|
| data-first-analysis | 49/50 | HIGH |
| variable-control-analysis | 49/50 | HIGH |
| experimental-design-framework | 48/50 | HIGH |
| evidence-sufficiency-assessment | 44/50 | HIGH |
| precision-measurement-protocol | 42/50 | HIGH (borderline) |

---

## Next Steps

Create skill PROMPT.md files for HIGH priority skills:

```
Skill: data-first-analysis
Purpose: Analyze evidence with precision, distinguishing demonstrated from speculated
Trigger: "What does the data actually show?"
Integration: rosalind-franklin expert
```

```
Skill: variable-control-analysis
Purpose: Identify hidden variables causing inconsistent results
Trigger: "Why are my results inconsistent?"
Integration: rosalind-franklin expert
```

```
Skill: experimental-design-framework
Purpose: Design rigorous experiments with controlled variables
Trigger: "Help me design an experiment"
Integration: rosalind-franklin expert
```

```
Skill: evidence-sufficiency-assessment
Purpose: Determine if evidence supports the intended claim
Trigger: "Is this enough evidence?" or "Can I make this claim?"
Integration: rosalind-franklin expert
```
