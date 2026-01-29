# Skill Extraction Report: robert-greene

**Source:** experts/robert-greene/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 4

---

## HIGH Priority

### 1. law-framework-analysis

**Source Pattern:** The Law Framework (from PROMPT.md "Signature Techniques" and expertise.md structure)
**Purpose:** Analyze a situation or challenge and formulate insights as numbered laws with historical case studies, keys to power, and reversals following Robert Greene's methodology
**Trigger:** "What are the laws governing this situation?" or "Give me the Greene treatment" or "Analyze this like Robert Greene"
**Inputs:** A situation, challenge, or domain to analyze; optional focus area (power, seduction, strategy, human nature)
**Outputs:** Numbered laws with: statement, historical transgression example, historical observance example, keys to power/application, reversal/caveat
**Reasoning:** Core methodology that defines Greene's entire body of work. ALL 5 criteria met: (1) Actionable - clear multi-step process from his book structure, (2) Invocable - natural trigger phrases, (3) Scoped - one purpose: law formulation, (4) Reusable - applies to any domain/situation, (5) Valuable - transforms analysis into memorable, actionable principles with historical grounding. Estimated 3+ uses/week, saves 30+ minutes per analysis.

---

### 2. historical-case-study-method

**Source Pattern:** Historical Case Study technique, Notecard System methodology, and "Historical Figures Frequently Referenced" table
**Purpose:** Research and construct a vivid historical case study to illustrate a principle, complete with protagonist, strategic challenge, tactics employed, and outcome
**Trigger:** "Find a historical example for..." or "Illustrate this principle with history" or "Who in history faced this?"
**Inputs:** A principle or insight to illustrate; optional era or domain constraints
**Outputs:** A narrative case study with: historical figure identified, context/challenge described, specific tactics detailed, outcome analyzed, lesson extracted
**Reasoning:** Greene reads 300-400 books per project and distills them into vivid teaching narratives. ALL 5 criteria met: (1) Actionable - clear research and narrative construction steps, (2) Invocable - direct trigger for illustration needs, (3) Scoped - one purpose: case study construction, (4) Reusable - any principle can be illustrated, (5) Valuable - transforms abstract ideas into memorable stories. Estimated 3+ uses/week, saves 30+ minutes of research.

---

## MEDIUM Priority

### 3. psychological-thumbscrew-diagnosis

**Source Pattern:** Law 33 "Discover Each Man's Thumbscrew" and Laws of Human Nature framework (narcissism, envy, shadow)
**Purpose:** Diagnose the psychological vulnerabilities, hidden motivations, and emotional drivers of a person or type of person based on behavioral signals
**Trigger:** "What's their thumbscrew?" or "Diagnose their psychology" or "What's really driving them?"
**Inputs:** Description of a person's behavior, statements, reactions, or pattern; optional relationship context
**Outputs:** Diagnosis including: identified vulnerability/insecurity, hidden motivation, recommended approach, warning signs, reversal (when this diagnosis might be wrong)
**Reasoning:** Central to Greene's approach—understanding what drives people emotionally. ALL 5 criteria met: (1) Actionable - clear diagnostic framework from Laws of Human Nature, (2) Invocable - natural "what makes them tick" trigger, (3) Scoped - one purpose: psychological diagnosis, (4) Reusable - applies to any interpersonal situation, (5) Valuable - transforms confusing behavior into strategic understanding. Estimated 2 uses/week, saves 20+ minutes.

---

### 4. mastery-path-assessment

**Source Pattern:** Mastery book framework—apprenticeship, creative-active, mastery phases; Life's Task discovery
**Purpose:** Assess where someone is on their path to mastery, identify phase-appropriate strategies, and diagnose obstacles to advancement
**Trigger:** "Where am I on the mastery path?" or "Assess my apprenticeship" or "Am I making progress toward mastery?"
**Inputs:** Description of current skill level, years in field, recent learning experiences, relationship with mentors, creative output
**Outputs:** Phase diagnosis (apprenticeship/creative-active/mastery), specific recommendations for current phase, identified obstacles, Life's Task alignment assessment
**Reasoning:** Mastery is one of Greene's most popular frameworks. ALL 5 criteria met: (1) Actionable - clear three-phase model with specific strategies per phase, (2) Invocable - career development trigger, (3) Scoped - one purpose: mastery progression assessment, (4) Reusable - applies to any skill domain, (5) Valuable - provides roadmap for long-term development. Estimated 1-2 uses/week, saves 20+ minutes. Note: Similar to existing `mastery-path-assessment` skill—check for overlap.

---

## LOW Priority

*None identified at LOW priority—all extracted candidates met HIGH or MEDIUM thresholds.*

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Complete 48 Laws list | Reference knowledge—no actionable workflow beyond the laws themselves |
| Nine Seducer Types | Classification reference—useful for diagnosis but covered by psychological-thumbscrew |
| 18 Laws of Human Nature list | Reference knowledge—individual laws become part of diagnosis skill |
| Notecard System methodology | Process documentation—not invocable as a distinct skill (part of historical-case-study-method) |
| Famous Quotes | Reference material—no workflow component |
| Historical Figures table | Reference material—feeds into historical-case-study-method |
| Writing Style Characteristics | Reference/expertise—describes voice, doesn't create actionable workflow |
| Anti-Seducer types | Warning/gotcha pattern—stays as expertise reference |
| 33 Strategies of War structure | Too broad—individual strategies could be skills but overlap with existing strategy skills |
| The Sublime concept | Single concept explanation without workflow |
| Formlessness (Law 48) | Philosophical principle—invoked within law-framework-analysis |
| Death Ground Strategy | Covered by existing strategic skills (decisive-action-framework, rubicon-decision-framework) |

---

## Overlap Analysis

| Candidate | Existing Skill | Overlap % | Recommendation |
|-----------|---------------|-----------|----------------|
| mastery-path-assessment | mastery-path-assessment | 90%+ | SKIP—already exists |
| law-framework-analysis | power-dynamics-assessment | ~35% | Distinct—Greene's law structure is unique methodology |
| historical-case-study-method | None found | <10% | Proceed—unique approach |
| psychological-thumbscrew-diagnosis | psychological-type-analysis, character-assessment | ~40% | Distinct—Greene's specific framework is unique |

---

## Final Candidates (after deduplication)

1. **law-framework-analysis** - HIGH priority, proceed
2. **historical-case-study-method** - HIGH priority, proceed
3. **psychological-thumbscrew-diagnosis** - MEDIUM priority, proceed

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: law-framework-analysis
Purpose: Analyze situations using Robert Greene's law formulation methodology with historical examples and reversals
Trigger: "What are the laws governing this?" or "Give me the Greene treatment"
Integration: robert-greene expert
```

```
Skill: historical-case-study-method
Purpose: Research and construct vivid historical case studies to illustrate principles
Trigger: "Find a historical example for..." or "Illustrate with history"
Integration: robert-greene expert
```

```
Skill: psychological-thumbscrew-diagnosis
Purpose: Diagnose psychological vulnerabilities and hidden motivations using Greene's framework
Trigger: "What's their thumbscrew?" or "What's really driving them?"
Integration: robert-greene expert
```
