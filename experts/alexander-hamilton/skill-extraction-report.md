# Skill Extraction Report: alexander-hamilton

**Source:** experts/alexander-hamilton/expertise.md
**Analyzed:** 2026-01-22
**Candidates Found:** 3

---

## HIGH Priority

### 1. financial-architecture-assessment

**Source Pattern:** The Report on Public Credit Framework
**Purpose:** Systematically assess and design funding mechanisms for organizational obligations and investments
**Trigger:** "Assess our financial obligations", "Design a funding mechanism", "How should we structure our technical debt repayment?"
**Inputs:** List of current obligations, available revenue streams, stakeholder interests, time horizons
**Outputs:** Comprehensive funding plan with mechanisms, schedules, accountability structures, and alignment strategies
**Reasoning:** Clear 5-step process directly from Hamilton's Treasury work. High reuse potential for any organization managing multiple obligations. Saves 30+ minutes of financial analysis per use. Frequently applicable to infrastructure and technical debt discussions.

### 2. comprehensive-argument-construction

**Source Pattern:** The Federalist Framework for Institutional Argument
**Purpose:** Build exhaustive, multi-front arguments for strategic proposals that anticipate and address all objections
**Trigger:** "Build the case for X", "How do we convince stakeholders?", "We need to argue for this proposal"
**Inputs:** Proposal description, target audience, known objections, historical precedents available
**Outputs:** Structured argument document covering proposition, necessity, objection responses, precedents, mechanisms, implications, and call to action
**Reasoning:** Hamilton's 7-step framework from 51 Federalist essays provides proven structure for comprehensive persuasion. Highly reusable for RFCs, architecture decisions, budget requests. Estimated 3+ uses per week for teams making significant proposals.

---

## MEDIUM Priority

### 3. strategic-capability-development

**Source Pattern:** The Report on Manufactures Framework
**Purpose:** Identify and plan development of strategic capabilities requiring sustained organizational investment
**Trigger:** "What capabilities should we invest in?", "How do we build this platform?", "Design our capability roadmap"
**Inputs:** Current capability inventory, strategic objectives, resource constraints, competitive landscape
**Outputs:** Capability development plan with prioritization, investment phases, support mechanisms, and success metrics
**Reasoning:** 5-step framework from Hamilton's industrial policy. Applicable to platform teams, internal tooling, skill development programs. Moderate frequency (1-2 uses per week) but high value when used for major investment decisions.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Unity of Command principle | Single concept, not actionable workflow |
| Sinking Fund Principle | Reference knowledge, application is context-specific |
| Verified Quotes collection | Reference material, no procedural workflow |
| Biographical Reference | Pure reference data, not actionable |
| Anti-Patterns table | Warning/gotcha content, stays as expertise |
| Integration Notes | Collaboration guidance, not standalone workflow |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: financial-architecture-assessment
Purpose: Systematically assess and design funding mechanisms for organizational obligations
Trigger: "Assess our financial obligations", "Design a funding mechanism"
Integration: alexander-hamilton expert
```

```
Skill: comprehensive-argument-construction
Purpose: Build exhaustive, multi-front arguments for strategic proposals
Trigger: "Build the case for X", "How do we convince stakeholders?"
Integration: alexander-hamilton expert
```

```
Skill: strategic-capability-development
Purpose: Identify and plan development of strategic capabilities
Trigger: "What capabilities should we invest in?", "Design our capability roadmap"
Integration: alexander-hamilton expert
```
