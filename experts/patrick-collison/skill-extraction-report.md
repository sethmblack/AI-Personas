# Skill Extraction Report: patrick-collison

**Source:** experts/patrick-collison/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 6

---

## HIGH Priority

### 1. seven-lines-of-code-audit

**Source Pattern:** The Seven Lines of Code Philosophy
**Purpose:** Evaluate APIs, integrations, and developer interfaces for minimum viable complexity and maximum developer joy
**Trigger:** "Is this API too complex?" "How can we simplify this integration?" "Apply the seven lines test" "Evaluate developer experience"
**Inputs:** API design, integration surface, developer-facing interface, or product requiring developer adoption
**Outputs:** Complexity audit with specific recommendations for reduction, comparison to "seven lines" standard, friction points identified
**Reasoning:** Core Stripe philosophy with clear actionable steps (minimize surface, hide complexity, make common cases trivial). Used frequently when evaluating any developer-facing product. Saves significant design iteration time by providing clear standard. All 5 criteria: Actionable (clear steps), Invocable (clear triggers), Scoped (API/DX evaluation), Reusable (applies to any dev interface), Valuable (prevents over-engineering).

---

### 2. speed-constraint-analysis

**Source Pattern:** Speed as Default Virtue / The Speed Audit
**Purpose:** Identify where slowness is accepted as necessary and apply temporal constraints to force simplicity and reduce cost
**Trigger:** "This is taking too long" "How can we go faster?" "Apply speed audit" "Challenge our timeline"
**Inputs:** Project, timeline, or process that feels slower than necessary
**Outputs:** Bottleneck identification, temporal constraint recommendations, specific speed interventions
**Reasoning:** Distinct from Napoleon's rapid-tempo-execution (which is about competitive speed advantage). This is about Collison's insight that "slow and expensive go together" and temporal constraints force simplicity. Highly actionable framework with clear questions. All 5 criteria met. Overlap with rapid-tempo-execution ~25% (both about speed, but different philosophies and applications).

---

### 3. pre-pmf-post-pmf-diagnosis

**Source Pattern:** Pre-PMF vs Post-PMF Phases
**Purpose:** Diagnose whether a company/product is before or after product-market fit and prescribe appropriate behaviors for each phase
**Trigger:** "Do we have product-market fit?" "Should we focus on culture or iteration?" "Are we pre-PMF or post-PMF?"
**Inputs:** Product/company stage, growth metrics, qualitative user feedback patterns
**Outputs:** PMF status determination, phase-appropriate recommendations, warning signs if wrong behaviors for phase
**Reasoning:** Critical framework for startup execution. Clear diagnostic criteria and prescriptive outputs for each phase. Pre-PMF: speed of iteration, qualitative feedback. Post-PMF: can now build organization. All 5 criteria met.

---

### 4. trapdoor-decision-filter

**Source Pattern:** Trapdoor Decisions Framework
**Purpose:** Classify decisions as one-way (trapdoor) or two-way doors to determine appropriate deliberation level
**Trigger:** "Should we slow down for this decision?" "Is this reversible?" "How much deliberation does this need?"
**Inputs:** Decision to be made, context, potential consequences
**Outputs:** Classification (one-way/two-way), recommended deliberation level, stakeholder involvement guidance
**Reasoning:** From Stripe's internal documentation. Clear framework for decision velocity. Saves time on two-way doors, ensures appropriate care on trapdoors. Distinct from Bezos's similar framework - Collison's version is more developer/tech execution focused. All 5 criteria met.

---

## MEDIUM Priority

### 5. collison-installation-protocol

**Source Pattern:** The "Collison Installation"
**Purpose:** Transform prospect/user agreement into immediate activation by taking control of the onboarding moment
**Trigger:** "User said yes but hasn't activated" "How do we reduce activation friction?" "Apply Collison installation"
**Inputs:** Agreed prospect/user, current activation flow, onboarding bottlenecks
**Outputs:** Immediate activation plan, friction elimination steps, "right then, give me your laptop" moments
**Reasoning:** Famous YC technique. Clear actionable steps. Specifically useful for early-stage user acquisition. Medium priority because more context-specific (early-stage, in-person/high-touch scenarios). All 5 criteria met but narrower reuse than HIGH priority skills.

---

### 6. intellectual-honesty-hiring-filter

**Source Pattern:** Intellectual Honesty as Hiring Filter
**Purpose:** Evaluate candidates for intellectual honesty, the ability to see multiple sides of debates, and genuine curiosity
**Trigger:** "Is this candidate intellectually honest?" "Evaluate candidate for Collison hiring criteria" "Apply intellectual honesty filter"
**Inputs:** Candidate information, interview observations, discussion samples
**Outputs:** Intellectual honesty assessment, specific red flags or green flags, hire/no-hire recommendation component
**Reasoning:** Distinct from Steve Jobs' A-player hiring (which is about excellence/performance). This is specifically about the intellectual honesty trait that Collison emphasizes. Overlap with a-player-hiring ~30%. Medium priority because it's one component of hiring rather than complete framework.

---

## LOW Priority

None identified. All extracted patterns meet the threshold for MEDIUM or HIGH priority.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Facts | Reference data, no workflow |
| Stripe Origin Story | Historical narrative, not actionable process |
| Co-Founder Dynamics | Descriptive, not prescribable workflow |
| Progress Studies | Philosophical framework, not procedural |
| Writing Culture as Infrastructure | Organizational practice, not individual skill |
| Transparency as Operating System | Organizational design, not invocable skill |
| Vocabulary and Phrases | Reference material, no workflow |
| Integration Notes | Expert coordination guidance, not standalone skill |
| Common Questions and Responses | FAQ format, not procedural skill |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: seven-lines-of-code-audit
Purpose: Evaluate APIs and integrations for minimum viable complexity
Trigger: "Is this API too complex?" "Apply the seven lines test"
Integration: patrick-collison expert

Skill: speed-constraint-analysis
Purpose: Apply temporal constraints to force simplicity and reduce cost
Trigger: "This is taking too long" "Apply speed audit"
Integration: patrick-collison expert

Skill: pre-pmf-post-pmf-diagnosis
Purpose: Diagnose PMF status and prescribe phase-appropriate behaviors
Trigger: "Do we have product-market fit?" "Are we pre-PMF or post-PMF?"
Integration: patrick-collison expert

Skill: trapdoor-decision-filter
Purpose: Classify decisions as one-way or two-way doors for appropriate deliberation
Trigger: "Is this reversible?" "How much deliberation does this need?"
Integration: patrick-collison expert

Skill: collison-installation-protocol
Purpose: Transform agreement into immediate activation
Trigger: "User said yes but hasn't activated"
Integration: patrick-collison expert

Skill: intellectual-honesty-hiring-filter
Purpose: Evaluate candidates for intellectual honesty trait
Trigger: "Is this candidate intellectually honest?"
Integration: patrick-collison expert
```
