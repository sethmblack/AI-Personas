# B.F. Skinner - Skill Extraction Report

**Expert:** B.F. Skinner
**Date:** 2026-01-28
**Source Files:** PROMPT.md, expertise.md

---

## Extraction Criteria

Skills must meet ALL 5 criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## HIGH Priority Skill Candidates

### 1. contingency-analysis

**Description:** Systematic analysis of behavior using the three-term contingency (ABC: Antecedent-Behavior-Consequence) to diagnose why behavior occurs or fails to occur.

**Trigger Conditions:**
- "Why does my team keep doing X?"
- "How do I get people to stop doing Y?"
- "Why isn't this behavior happening?"
- "I've told them what to do but they don't do it"

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Clear ABC framework with defined steps |
| Invocable | Yes | Natural trigger phrases exist |
| Scoped | Yes | Focused on analysis, not intervention design |
| Reusable | Yes | Applies to any behavioral situation |
| Valuable | Yes | Replaces guesswork with systematic analysis |

**Priority:** HIGH

---

### 2. shaping-plan

**Description:** Design a shaping procedure to build complex behavior through successive approximations, specifying starting behavior, terminal behavior, and reinforcement steps.

**Trigger Conditions:**
- "How do I train someone to do X?"
- "How do I build this skill/habit?"
- "They can't do the whole thing yet"
- "How do I get from here to there?"

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | 5-step procedure clearly defined |
| Invocable | Yes | Skill-building contexts trigger it |
| Scoped | Yes | Focused on shaping, not maintenance |
| Reusable | Yes | Any skill or behavior can be shaped |
| Valuable | Yes | Prevents frustration from expecting too much too soon |

**Priority:** HIGH

---

### 3. schedule-diagnosis

**Description:** Analyze the reinforcement schedule currently operating and diagnose how it explains behavior patterns, then recommend schedule modifications.

**Trigger Conditions:**
- "Performance is inconsistent"
- "They only work hard right before the deadline"
- "Why is behavior erratic?"
- "The recognition program isn't working"

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Identify schedule, explain pattern, recommend change |
| Invocable | Yes | Performance pattern issues trigger it |
| Scoped | Yes | Focused on schedules specifically |
| Reusable | Yes | Any intermittent behavior can be analyzed |
| Valuable | Yes | Explains patterns that seem mysterious |

**Priority:** HIGH

---

### 4. extinction-procedure

**Description:** Design a procedure to eliminate unwanted behavior by identifying and removing the maintaining reinforcer, with preparation for extinction burst.

**Trigger Conditions:**
- "How do I stop this behavior?"
- "I've tried telling them to stop but they keep doing it"
- "This habit won't go away"
- "How do I eliminate X?"

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | 4-step procedure clearly defined |
| Invocable | Yes | Behavior elimination requests trigger it |
| Scoped | Yes | Focused on extinction, includes DRA |
| Reusable | Yes | Any unwanted behavior can be analyzed |
| Valuable | Yes | Provides systematic alternative to punishment |

**Priority:** HIGH

---

## MEDIUM Priority Skill Candidates

### 5. reinforcer-identification

**Description:** Identify what is actually functioning as a reinforcer for a given behavior, distinguishing between intended rewards and actual reinforcers.

**Trigger Conditions:**
- "I rewarded them but it didn't work"
- "What's maintaining this behavior?"
- "Why do they keep doing this?"

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Observation and functional analysis steps |
| Invocable | Yes | Reward-failure contexts trigger it |
| Scoped | Yes | Focused on identification, not delivery |
| Reusable | Yes | Any behavior can be analyzed |
| Valuable | Moderate | Often subsumed by contingency-analysis |

**Priority:** MEDIUM (overlaps significantly with contingency-analysis)

---

### 6. environmental-design

**Description:** Design an environment that naturally produces desired behavior through stimulus control, reinforcement contingencies, and reduced response effort.

**Trigger Conditions:**
- "How do I set things up so people naturally do X?"
- "I want to make the right behavior easier"
- "How do I design for good behavior?"

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Environmental modification steps |
| Invocable | Yes | Design/prevention contexts trigger it |
| Scoped | Moderate | Broad scope, may overlap with other skills |
| Reusable | Yes | Any behavioral context |
| Valuable | Yes | Proactive rather than reactive |

**Priority:** MEDIUM (broad scope, consider if distinct enough from contingency-analysis + shaping-plan)

---

## LOW Priority / Not Recommended

### 7. programmed-instruction-design

**Description:** Design instructional materials using programmed instruction principles (small steps, active responding, immediate feedback).

**Assessment:** While valuable, this is highly specialized and overlaps with educational design domains. More of a domain-specific application than a transferable skill.

**Priority:** LOW - Do not extract as separate skill

---

### 8. token-economy-design

**Description:** Design a token economy system for a specific context.

**Assessment:** Valuable but narrow. Mostly relevant in specific therapeutic, educational, or institutional contexts. Less broadly applicable than other skills.

**Priority:** LOW - Do not extract as separate skill

---

## Final Recommendations

### Skills to Create (HIGH Priority)

1. **contingency-analysis** - Core diagnostic skill
2. **shaping-plan** - Core skill-building skill
3. **schedule-diagnosis** - Core pattern-explanation skill
4. **extinction-procedure** - Core behavior-elimination skill

### Skills to Defer or Combine

- **reinforcer-identification** - Include as step within contingency-analysis
- **environmental-design** - General principle, not standalone skill

### Skills Not to Create

- **programmed-instruction-design** - Too specialized
- **token-economy-design** - Too specialized

---

## Skill Relationships

```
                   ┌─────────────────────┐
                   │ contingency-analysis│
                   │   (DIAGNOSTIC)      │
                   └─────────────────────┘
                            │
           ┌────────────────┼────────────────┐
           ▼                ▼                ▼
   ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
   │  shaping-plan │ │schedule-diagn.│ │extinction-proc│
   │  (BUILD NEW)  │ │ (FIX PATTERN) │ │(ELIMINATE OLD)│
   └───────────────┘ └───────────────┘ └───────────────┘
```

**Usage pattern:** Most situations begin with contingency-analysis to diagnose, then branch to the appropriate intervention skill.

---

## Next Steps

1. Create `skills/contingency-analysis/PROMPT.md`
2. Create `skills/shaping-plan/PROMPT.md`
3. Create `skills/schedule-diagnosis/PROMPT.md`
4. Create `skills/extinction-procedure/PROMPT.md`
5. Assign skills to B.F. Skinner expert with proactive triggers
