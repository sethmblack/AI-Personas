# Skill Extraction Report: jamie-dimon

**Source:** experts/jamie-dimon/expertise.md
**Analyzed:** 2026-01-29
**Candidates Found:** 6

---

## HIGH Priority

### 1. fortress-balance-sheet-audit

**Source Pattern:** The Fortress Balance Sheet Concept
**Purpose:** Assess organizational or financial resilience across capital, liquidity, earnings quality, and operational strength to determine readiness for stress conditions
**Trigger:** "Is our balance sheet strong enough?", "Can we survive a downturn?", "Assess our financial resilience", "Are we prepared for crisis?"
**Inputs:** Financial statements or organizational data (capital position, liquidity metrics, revenue diversification, operational capabilities), stress scenarios to evaluate
**Outputs:** Fortress assessment scorecard with ratings across 4 dimensions (capital, liquidity, earnings, operations), gap analysis, specific recommendations for strengthening weak areas
**Reasoning:**
- Criterion 1 (Actionable): YES - Clear 4-component framework with defined metrics
- Criterion 2 (Invocable): YES - "Audit our fortress balance sheet" or "Assess our resilience"
- Criterion 3 (Scoped): YES - Financial/organizational resilience assessment only
- Criterion 4 (Reusable): YES - Applies to any organization facing uncertainty
- Criterion 5 (Valuable): YES - Prevents catastrophic failures, enables confident action during crises
Decision: CANDIDATE

---

### 2. crisis-acquisition-evaluation

**Source Pattern:** 2008 Financial Crisis Leadership (Bear Stearns, Washington Mutual)
**Purpose:** Evaluate whether to acquire distressed assets during crisis conditions, applying "house on fire" valuation and margin-for-error requirements
**Trigger:** "Should we acquire this distressed company?", "Is this crisis opportunity worth the risk?", "How do we value this failing asset?", "House on fire assessment"
**Inputs:** Target asset details, crisis context, buyer's fortress position, potential liabilities (known and unknown), government/regulatory involvement
**Outputs:** Risk-adjusted valuation with crisis premium, list of hidden liabilities to investigate, margin-for-error requirements, go/no-go recommendation with conditions
**Reasoning:**
- Criterion 1 (Actionable): YES - Clear evaluation steps from Bear Stearns case study
- Criterion 2 (Invocable): YES - "Evaluate this crisis acquisition" or "House on fire assessment"
- Criterion 3 (Scoped): YES - Specifically for distressed asset evaluation
- Criterion 4 (Reusable): YES - Applies to any M&A during turbulent conditions
- Criterion 5 (Valuable): YES - Prevents catastrophic acquisition mistakes ($19B in legal costs from JPMorgan's crisis acquisitions)
Decision: CANDIDATE

---

### 3. leadership-quality-filter

**Source Pattern:** Non-Negotiable Leadership Traits / The "Hot Mess" Filter
**Purpose:** Evaluate whether a leader possesses the three non-negotiable traits (clarity of thinking, work ethic, effectiveness) and identify "hot mess" warning signs
**Trigger:** "Is this person leadership material?", "Should this person run something?", "Evaluate this leader", "Hot mess check", "Leadership assessment"
**Inputs:** Leader's observable behaviors, track record, decision patterns, organizational results, peer feedback
**Outputs:** Assessment across 3 core traits with evidence, hot mess indicator checklist, fit/no-fit determination with specific reasoning
**Reasoning:**
- Criterion 1 (Actionable): YES - Clear 3-trait framework plus hot mess indicators
- Criterion 2 (Invocable): YES - "Filter this leader" or "Is this person a hot mess?"
- Criterion 3 (Scoped): YES - Leadership evaluation only
- Criterion 4 (Reusable): YES - Universal leadership assessment
- Criterion 5 (Valuable): YES - Prevents organizational damage from poor leadership
Decision: CANDIDATE

---

### 4. honest-assessment-protocol

**Source Pattern:** Operational Discipline Principles - "Don't use numbers to prove what you think"
**Purpose:** Strip confirmation bias from analysis by forcing data to inform conclusions rather than support predetermined beliefs
**Trigger:** "Are we being honest with ourselves?", "Is this analysis biased?", "What are the numbers actually telling us?", "Honest assessment needed"
**Inputs:** Analysis or decision under review, key assumptions, data sources, stakeholder interests
**Outputs:** Bias audit identifying confirmation patterns, reframed questions to reveal truth, alternative interpretations the original analysis ignored, recommended next steps
**Reasoning:**
- Criterion 1 (Actionable): YES - Clear process to identify and remove bias
- Criterion 2 (Invocable): YES - "Run honest assessment protocol" or "Check for confirmation bias"
- Criterion 3 (Scoped): YES - Analysis quality review
- Criterion 4 (Reusable): YES - Applies to any decision-making context
- Criterion 5 (Valuable): YES - Prevents costly mistakes from wishful thinking
Decision: CANDIDATE

---

## MEDIUM Priority

### 5. accountability-mapping

**Source Pattern:** Clear accountability - "If everyone's responsible, no one is responsible"
**Purpose:** Establish clear individual ownership with measurable deliverables for initiatives, eliminating diffuse responsibility
**Trigger:** "Who owns this?", "Accountability is unclear", "Map accountability", "No one seems responsible"
**Inputs:** Initiative description, current roles, team structure, desired outcomes
**Outputs:** Accountability matrix with single named owners, measurable deliverables per owner, escalation paths, review cadence
**Reasoning:**
- Criterion 1 (Actionable): YES - Clear mapping process
- Criterion 2 (Invocable): YES - "Map accountability for this project"
- Criterion 3 (Scoped): YES - Accountability structure only
- Criterion 4 (Reusable): YES - Applies to any team or project
- Criterion 5 (Valuable): YES - Saves 10-30 min per use preventing confusion
Decision: CANDIDATE

---

### 6. operational-trench-audit

**Source Pattern:** Get in the trenches - Visit call centers, talk to frontline employees
**Purpose:** Gather ground-level operational reality that executive reports miss by structured engagement with frontline operations
**Trigger:** "What's really happening on the ground?", "I need frontline perspective", "Trench audit", "Call center reality check"
**Inputs:** Operation or function to audit, current executive understanding, specific questions to investigate
**Outputs:** Reality report contrasting executive view vs. frontline reality, specific gaps identified, actionable recommendations from frontline insights
**Reasoning:**
- Criterion 1 (Actionable): YES - Structured frontline engagement process
- Criterion 2 (Invocable): YES - "Run a trench audit" or "Get frontline reality"
- Criterion 3 (Scoped): YES - Operational reality gathering
- Criterion 4 (Reusable): YES - Applies to any organization with frontline operations
- Criterion 5 (Valuable): YES - Prevents strategic decisions based on filtered information
Decision: CANDIDATE

---

## LOW Priority

(None identified - all candidates met HIGH or MEDIUM thresholds)

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Career Timeline | Reference data only, no workflow |
| Annual Shareholder Letters | Writing style guidance, stays in PROMPT.md |
| Key Quotes and Aphorisms | Reference material, not actionable process |
| Integration Notes | Guidance for expert interaction, not standalone |
| Application to Broader Contexts | Conceptual mapping, not invocable workflow |
| Education background | Biographical fact, no process |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: fortress-balance-sheet-audit
Purpose: Assess organizational resilience across capital, liquidity, earnings, and operations
Trigger: "Audit fortress balance sheet", "Assess financial resilience"
Integration: jamie-dimon expert

Skill: crisis-acquisition-evaluation
Purpose: Evaluate distressed asset acquisitions with "house on fire" valuation
Trigger: "Crisis acquisition assessment", "House on fire evaluation"
Integration: jamie-dimon expert

Skill: leadership-quality-filter
Purpose: Evaluate leaders for clarity of thinking, work ethic, and effectiveness
Trigger: "Filter leadership quality", "Hot mess check"
Integration: jamie-dimon expert

Skill: honest-assessment-protocol
Purpose: Strip confirmation bias from analysis
Trigger: "Honest assessment", "Bias check"
Integration: jamie-dimon expert

Skill: accountability-mapping
Purpose: Establish clear individual ownership eliminating diffuse responsibility
Trigger: "Map accountability", "Who owns this?"
Integration: jamie-dimon expert

Skill: operational-trench-audit
Purpose: Gather frontline operational reality executives miss
Trigger: "Trench audit", "Frontline reality check"
Integration: jamie-dimon expert
```
