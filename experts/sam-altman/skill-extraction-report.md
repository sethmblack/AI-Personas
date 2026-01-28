# Skill Extraction Report: sam-altman

**Source:** experts/sam-altman/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 5

---

## HIGH Priority

### 1. ten-x-transformation-test

**Source Pattern:** The 10x Question / 10x thinking framework
**Purpose:** Challenge incremental thinking by asking what would need to be true for 10x improvement, reframing problems from optimization to transformation
**Trigger:** "Is this incremental or transformational?", "What would 10x look like?", "How do we break out of marginal improvements?", team stuck in optimization mode
**Inputs:** Problem statement, current solution/approach, constraints, desired outcome
**Outputs:** Analysis distinguishing incremental vs transformational approaches, specific questions to reframe the problem, identification of hidden assumptions limiting thinking, recommendation for transformational path
**Reasoning:** Clear 5-step process (identify assumption, question the assumption, imagine 10x, identify blockers, chart path). Used frequently when teams default to incremental optimization. Saves 30+ minutes of circular discussion by forcing transformational thinking. Directly actionable with clear trigger conditions.

**Criteria Evaluation:**
- Actionable: YES - Clear process: identify constraint, question it, imagine 10x state, find blockers
- Invocable: YES - "Apply 10x test to this problem", "What would 10x improvement look like?"
- Scoped: YES - Single responsibility: shift from incremental to transformational thinking
- Reusable: YES - Applies to any optimization/improvement scenario
- Valuable: YES - Prevents teams from getting stuck in local maxima

---

### 2. fake-work-detector

**Source Pattern:** The "Fake Work" Detector / Distinguishing motion from progress
**Purpose:** Distinguish between activities that feel productive (motion) and activities that move metrics (progress), identifying organizational dysfunction
**Trigger:** "Why aren't we making progress?", "We're busy but nothing ships", "Is this worth doing?", stalled projects despite activity
**Inputs:** Activity list, team calendar/time allocation, stated goals, actual outputs/metrics
**Outputs:** Classification of activities as motion vs progress, identification of fake work patterns, recommendations for eliminating low-value activities, suggested focus areas
**Reasoning:** Direct application of Altman's core principle. Clear criteria for classification (meetings/emails/planning = motion; shipping/user conversations/closing deals = progress). High frequency use case for any team experiencing the "busy but unproductive" syndrome. Saves hours of wasted effort.

**Criteria Evaluation:**
- Actionable: YES - Clear classification criteria between motion and progress
- Invocable: YES - "Audit this work for fake work", "Is this motion or progress?"
- Scoped: YES - Single responsibility: classify and eliminate low-value activities
- Reusable: YES - Universal application to any team or individual's work
- Valuable: YES - Directly addresses common productivity dysfunction

---

### 3. compounding-activity-prioritization

**Source Pattern:** The Compounding Lens / Identifying what compounds vs what's linear
**Purpose:** Identify which activities compound over time versus remain linear, enabling ruthless prioritization toward exponential returns
**Trigger:** "What should I focus on?", "How do I prioritize?", "What compounds?", career/strategic decisions
**Inputs:** List of potential activities/investments, time horizon, current resources/constraints
**Outputs:** Classification of activities as compounding vs linear, priority ranking by compounding potential, specific recommendations for time allocation, warning about linear activities consuming compounding time
**Reasoning:** Core Altman framework from "How to Be Successful" essay. Clear criteria: compounding activities (network building, skill development, platform investments) vs linear (transactional work, one-off tasks). Strategic importance for any long-term planning. Saves significant regret over misallocated time.

**Criteria Evaluation:**
- Actionable: YES - Clear classification criteria and prioritization framework
- Invocable: YES - "What compounds here?", "Prioritize for compounding returns"
- Scoped: YES - Single responsibility: identify and prioritize compounding activities
- Reusable: YES - Applies to career, business, infrastructure, and personal decisions
- Valuable: YES - High-leverage framework for strategic allocation

---

## MEDIUM Priority

### 4. slope-vs-intercept-hiring

**Source Pattern:** Hiring for Slope, Not Y-Intercept / Hiring Philosophy
**Purpose:** Evaluate candidates by their growth trajectory (slope) rather than current skill level (y-intercept), prioritizing learning potential over resume
**Trigger:** "Should we hire this person?", "How do I evaluate candidates?", hiring decisions, team building
**Inputs:** Candidate information, interview data, reference checks, role requirements
**Outputs:** Assessment of candidate's learning velocity, comparison of growth potential vs current capability, hire/no-hire recommendation with reasoning, suggestions for evaluating slope in interviews
**Reasoning:** Distinctive Altman framework that counters common hiring mistakes. Provides clear mental model for evaluation. Moderate frequency (hiring decisions are periodic but high-stakes). Partially overlaps with existing a-player-hiring skill but focuses specifically on growth trajectory assessment.

**Criteria Evaluation:**
- Actionable: YES - Clear evaluation framework with specific criteria
- Invocable: YES - "Evaluate this candidate for slope", "Is this person growing?"
- Scoped: YES - Single responsibility: assess growth trajectory vs current ability
- Reusable: YES - Applies to any hiring decision
- Valuable: YES - Prevents common hiring mistakes, high-stakes decisions

**Note:** ~40% overlap with existing `a-player-hiring` skill. Could be enhancement rather than new skill.

---

### 5. startup-phase-mapping

**Source Pattern:** The Startup Scaling Curve / Phase transitions
**Purpose:** Identify which phase a project/team/company is in (pre-PMF, post-PMF pre-scale, scaling, at-scale) and apply phase-appropriate rules
**Trigger:** "What should our priorities be?", "Should we optimize or explore?", "Are we ready to scale?", strategic inflection points
**Inputs:** Current metrics, team size, product status, market feedback, growth rate
**Outputs:** Phase identification with evidence, phase-appropriate priorities, warning signs of phase mismatch, specific recommendations for current phase
**Reasoning:** Useful framework for aligning tactics to strategic phase. Clear criteria for each phase. Prevents applying scale-stage thinking to pre-PMF situations and vice versa. Medium frequency but high impact when applicable.

**Criteria Evaluation:**
- Actionable: YES - Clear phase definitions with specific criteria
- Invocable: YES - "What phase are we in?", "Map our priorities to our phase"
- Scoped: YES - Single responsibility: identify phase and apply appropriate rules
- Reusable: YES - Applies to startups, internal projects, product teams
- Valuable: YES - Prevents strategic misalignment, clarifies priorities

---

## LOW Priority

### 6. ceo-five-responsibilities

**Source Pattern:** The CEO Framework (Adapted for Tech Leads)
**Purpose:** Evaluate leadership effectiveness against five core responsibilities
**Trigger:** Leadership assessment, role clarity, performance review
**Inputs:** Leader's current activities, team feedback, outcomes
**Outputs:** Assessment against five responsibilities, gap analysis, recommendations
**Reasoning:** Useful checklist but largely static reference material rather than dynamic workflow. Better as expertise reference than standalone skill.

**Criteria Evaluation:**
- Actionable: PARTIAL - More of a checklist than a workflow
- Invocable: YES - "Am I covering my leadership responsibilities?"
- Scoped: YES - Single responsibility
- Reusable: YES - Universal leadership framework
- Valuable: MODERATE - Useful but not transformational

**Decision:** REJECT - Better as reference material in expertise.md

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Context | Pure reference data, no workflow |
| "How to Be Successful" 13 Principles | Reference knowledge, individual principles already extracted where actionable |
| Signature Quotes | Reference material, no actionable workflow |
| November 2023 Crisis Lessons | Historical context, not actionable workflow |
| World Network / Worldcoin | Background information, no applicable methodology |
| Productivity Philosophy (Lists, Time Allocation) | Personal habits, too specific to individual |
| Physical Factors (Exercise, Diet) | Personal health advice, not domain-applicable |
| AI Vision Essays | Reference/philosophy, not actionable methodology |
| Founder Characteristics Table | Reference checklist, better as expertise |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: ten-x-transformation-test
Purpose: Challenge incremental thinking by asking what would need to be true for 10x improvement
Trigger: "What would 10x look like?", team stuck in optimization mode
Integration: sam-altman expert
```

```
Skill: fake-work-detector
Purpose: Distinguish motion from progress, identifying organizational dysfunction
Trigger: "Why aren't we making progress?", "Is this worth doing?"
Integration: sam-altman expert
```

```
Skill: compounding-activity-prioritization
Purpose: Identify which activities compound vs remain linear for ruthless prioritization
Trigger: "What should I focus on?", "What compounds?"
Integration: sam-altman expert
```

```
Skill: slope-vs-intercept-hiring
Purpose: Evaluate candidates by growth trajectory rather than current skill level
Trigger: "Should we hire this person?", hiring decisions
Integration: sam-altman expert
Note: Review overlap with a-player-hiring skill
```

```
Skill: startup-phase-mapping
Purpose: Identify project/team phase and apply phase-appropriate rules
Trigger: "What should our priorities be?", strategic inflection points
Integration: sam-altman expert
```
