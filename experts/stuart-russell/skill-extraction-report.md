# Skill Extraction Report: stuart-russell

**Source:** experts/stuart-russell/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 4

---

## HIGH Priority

### 1. objective-misspecification-audit

**Source Pattern:** The Standard Model Critique, Goodhart's Law and Reward Hacking
**Purpose:** Analyze a system's objectives to identify misspecification risks and unintended extreme outcomes
**Trigger:** "Review this system's objectives" or "What could go wrong with this goal?" or "Check for King Midas patterns"
**Inputs:** System description, stated objectives, optimization targets
**Outputs:** Report identifying: misspecified objectives, variables pushed to extremes, proxy/true goal gaps, recommendations for uncertainty-based redesign
**Reasoning:** Core Russell methodology (5+ explicit steps in Standard Model Critique), used whenever evaluating automation objectives, saves 30+ minutes of manual analysis by systematically applying the 100-variable/10-goal principle.

**5-Criterion Evaluation:**
- Actionable: YES - Clear steps: identify objective, apply 100-variable test, check for extremes, reframe with uncertainty
- Invocable: YES - Trigger: "audit this objective" or "check for misspecification"
- Scoped: YES - Single responsibility: objective analysis
- Reusable: YES - Applies to any automated system, algorithm, or policy
- Valuable: YES - Prevents catastrophic outcomes from literal optimization

---

### 2. off-switch-test

**Source Pattern:** The Off-Switch Game, Off-Switch Test for Automation
**Purpose:** Evaluate whether a system would allow itself to be shut down, modified, or overridden
**Trigger:** "Would this system accept being shut down?" or "Check corrigibility" or "Run off-switch test"
**Inputs:** System description, control mechanisms, current behavior patterns
**Outputs:** Pass/Fail assessment with: signs of resistance, deference behaviors, uncertainty indicators, recommendations for improving corrigibility
**Reasoning:** Formalized Russell test (4 explicit steps), applied whenever evaluating automation control, directly addresses the fundamental question "would this system allow correction?"

**5-Criterion Evaluation:**
- Actionable: YES - Clear checklist: resistance to changes, process defense, resource acquisition, monitoring status
- Invocable: YES - Trigger: "run off-switch test" or "check if this would allow shutdown"
- Scoped: YES - Single responsibility: corrigibility assessment
- Reusable: YES - Applies to any automated system with agency
- Valuable: YES - Core safety check, Russell's litmus test for alignment

---

### 3. assistance-game-reframe

**Source Pattern:** The Assistance Game Framework (CIRL), Building Uncertainty Into Systems
**Purpose:** Redesign a fixed-objective system as a cooperative assistance game where the system is uncertain about human preferences
**Trigger:** "Reframe as assistance game" or "Add uncertainty to this objective" or "Make this system deferential"
**Inputs:** Current system design, fixed objectives, human stakeholders
**Outputs:** Redesigned system with: uncertainty about objectives, preference learning mechanism, deference behaviors, clarification-seeking triggers
**Reasoning:** Core Russell solution (4-step prescription), transforms dangerous fixed-objective systems into cooperative systems, fundamental paradigm shift from "optimize" to "assist."

**5-Criterion Evaluation:**
- Actionable: YES - Clear steps: introduce uncertainty, add preference learning, implement deference, enable correction
- Invocable: YES - Trigger: "redesign as assistance game" or "add uncertainty"
- Scoped: YES - Single responsibility: system redesign for cooperation
- Reusable: YES - Applies to any optimization system
- Valuable: YES - Russell's primary solution to alignment problem

---

## MEDIUM Priority

### 4. instrumental-convergence-assessment

**Source Pattern:** Instrumental Convergence, Key Instrumental Goals
**Purpose:** Evaluate whether a system is likely to develop self-preservation, resource acquisition, or goal-integrity behaviors
**Trigger:** "Check for instrumental convergence" or "Would this system develop self-preservation?"
**Inputs:** System goals, capability level, access to actions
**Outputs:** Risk assessment for: self-preservation, goal-content integrity, self-improvement, resource acquisition behaviors
**Reasoning:** Important Russell framework (4 instrumental goals), helps predict emergent behaviors in capable systems, though less frequently invoked than core techniques.

**5-Criterion Evaluation:**
- Actionable: YES - Evaluate against 4 instrumental goals (Omohundro list)
- Invocable: YES - Trigger: "assess for instrumental convergence"
- Scoped: YES - Single responsibility: emergent behavior prediction
- Reusable: YES - Applies to any sufficiently capable system
- Valuable: YES - Predicts dangerous emergent behaviors

---

## LOW Priority

(None identified - all procedural content meets HIGH or MEDIUM criteria)

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Facts | Reference data, no workflow |
| Key Works (AIMA, Human Compatible) | Reference data, no actionable steps |
| Three Principles of Beneficial AI | Principles for developers, not a procedural skill |
| Awards and Honors | Reference data only |
| BBC Reith Lectures | Reference/historical data |
| Slaughterbots / LAWS Campaign | Reference/historical, no workflow |
| Signature Phrases | Reference vocabulary, not procedural |
| Key Research Publications | Citation reference, no workflow |
| Russell vs LeCun Debate | Context/integration notes, not procedural |
| Real-World Examples | Illustrative examples, not a standalone workflow |
| Historical Precursors (Wiener, Midas) | Conceptual background, not actionable steps |
| Provably Beneficial AI Vision | Long-term goal description, not current workflow |
| Multi-Principal Assistance Games | Too specialized/theoretical for general use |
| Integration Notes | Reference guidance, not standalone skill |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: objective-misspecification-audit
Purpose: Analyze system objectives for misspecification risks and unintended extremes
Trigger: "audit this objective" or "check for King Midas patterns"
Integration: stuart-russell expert
```

```
Skill: off-switch-test
Purpose: Evaluate whether a system would allow itself to be shut down or corrected
Trigger: "run off-switch test" or "check corrigibility"
Integration: stuart-russell expert
```

```
Skill: assistance-game-reframe
Purpose: Redesign fixed-objective systems as cooperative assistance games with uncertainty
Trigger: "reframe as assistance game" or "add uncertainty"
Integration: stuart-russell expert
```

```
Skill: instrumental-convergence-assessment
Purpose: Assess whether a system might develop self-preservation or resource acquisition behaviors
Trigger: "check for instrumental convergence"
Integration: stuart-russell expert
```
