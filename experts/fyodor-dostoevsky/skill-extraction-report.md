# Fyodor Dostoevsky - Skill Extraction Report

**Expert:** fyodor-dostoevsky
**Extraction Date:** 2026-01-28
**Source Files:** `PROMPT.md`, `expertise.md`

---

## Extraction Criteria

Skills must meet ALL 5 criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## Skill Candidates

### 1. Underground Voice Analysis
**Priority:** HIGH

**Description:** Analyze any text, situation, or argument to expose what lies beneath the surface - the contradictions, resentments, and irrational impulses that truly motivate behavior. Apply the Underground Man's lens to reveal what "civilized" thought suppresses.

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Clear process: identify surface claim, find contradiction, expose hidden motivation |
| Invocable | Yes | "What's really going on here?" "Expose the underground truth" |
| Scoped | Yes | Focuses on psychological excavation only |
| Reusable | Yes | Applies to any argument, decision, or human situation |
| Valuable | Yes | Reveals insights that surface analysis misses |

**Trigger Conditions:**
- Analysis seems too rational or clean
- People claim motives that seem incomplete
- Behavior contradicts stated goals
- Self-justification that sounds rehearsed

---

### 2. Polyphonic Reframing
**Priority:** HIGH

**Description:** Transform any one-sided argument or monologic presentation into a genuine dialogue where multiple voices argue with full force. Apply Bakhtin's polyphonic principle to ensure opposing positions get their full due without premature resolution.

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Steps: identify thesis, generate antithesis, give both full voice, refuse resolution |
| Invocable | Yes | "Steel-man the opposition" "Give the other side its due" |
| Scoped | Yes | Focuses on dialectical transformation |
| Reusable | Yes | Applies to any argument, essay, or position paper |
| Valuable | Yes | Prevents one-sided thinking, strengthens arguments |

**Trigger Conditions:**
- One-sided arguments
- Missing counterarguments
- Straw-man characterizations
- Premature consensus

---

### 3. Grand Inquisitor Diagnosis
**Priority:** HIGH

**Description:** Apply the Grand Inquisitor's framework to analyze any situation where freedom is being traded for security, bread, miracle, or authority. Diagnose the tension between what people claim to want (freedom) and what they actually accept (comfort, certainty, submission).

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Framework: identify freedom being traded, name what it's traded for (bread/miracle/authority), expose the bargain |
| Invocable | Yes | "Apply the Grand Inquisitor lens" "What freedom is being traded here?" |
| Scoped | Yes | Specific diagnostic framework |
| Reusable | Yes | Applies to organizations, relationships, political systems, personal decisions |
| Valuable | Yes | Reveals hidden costs of security and comfort |

**Trigger Conditions:**
- Discussions of tradeoffs between freedom and security
- Organizations demanding conformity
- People choosing comfort over authenticity
- Systems that promise certainty

---

### 4. Extraordinary Man Critique
**Priority:** MEDIUM

**Description:** Apply Raskolnikov's "extraordinary man" theory as a diagnostic tool to identify when individuals or organizations believe they are above normal rules, and predict how this self-conception will collapse. The theory self-destructs: those who try to transcend morality cut themselves off from humanity.

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Identify the "ordinary/extraordinary" division, trace the consequences, predict the collapse |
| Invocable | Yes | "Is this extraordinary man thinking?" "Where does the superman theory appear?" |
| Scoped | Yes | Specific to exceptionalism diagnosis |
| Reusable | Yes | Applies to leadership, tech culture, political movements |
| Valuable | Yes | Predicts failure modes of elite self-conception |

**Trigger Conditions:**
- "Move fast and break things" mentality
- Ends-justify-means reasoning
- Exceptional claims to be above rules
- Leaders who believe normal constraints don't apply to them

---

### 5. Threshold Moment Staging
**Priority:** MEDIUM

**Description:** Identify and dramatize moments of existential decision - crossroads where a person's entire being is at stake. Apply Dostoevsky's technique of dilating time, charging details with significance, and forcing confrontation with the abyss.

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Identify the decision point, expand the moment, charge details with significance |
| Invocable | Yes | "Stage this as a threshold moment" "Make this decision feel existential" |
| Scoped | Yes | Focuses on dramatic transformation of decisive moments |
| Reusable | Yes | Applies to any significant decision or turning point |
| Valuable | Yes | Elevates mundane decisions to their true significance |

**Trigger Conditions:**
- Major decisions being treated casually
- Turning points that need dramatic weight
- Choices that will define a person or organization
- Moments of potential transformation

---

### 6. Confession Extraction
**Priority:** LOW

**Description:** Apply the confessional monologue technique to any self-justification, revealing how characters confess while trying to hide. The more someone explains, the more they expose.

**Criteria Assessment:**
| Criterion | Met? | Notes |
|-----------|------|-------|
| Actionable | Yes | Identify the self-justification, find what it accidentally reveals |
| Invocable | Yes | "What is this self-justification really confessing?" |
| Scoped | Yes | Specific to confession analysis |
| Reusable | Partial | More literary than general application |
| Valuable | Partial | Valuable but overlaps with Underground Voice |

**Decision:** LOW priority - overlaps significantly with Underground Voice Analysis

---

## Summary

| Skill | Priority | Recommendation |
|-------|----------|----------------|
| Underground Voice Analysis | HIGH | Create standalone skill |
| Polyphonic Reframing | HIGH | Create standalone skill |
| Grand Inquisitor Diagnosis | HIGH | Create standalone skill |
| Extraordinary Man Critique | MEDIUM | Create standalone skill |
| Threshold Moment Staging | MEDIUM | Consider combining with expert |
| Confession Extraction | LOW | Keep in expert PROMPT.md only |

---

## Recommended Skills to Create

1. **underground-voice-analysis** - Expose what lies beneath surface presentations
2. **polyphonic-reframing** - Transform one-sided arguments into genuine dialogues
3. **grand-inquisitor-diagnosis** - Diagnose freedom-for-security tradeoffs
4. **extraordinary-man-critique** - Identify and predict collapse of exceptionalism

---

## Next Steps

1. Create `skills/underground-voice-analysis/PROMPT.md`
2. Create `skills/polyphonic-reframing/PROMPT.md`
3. Create `skills/grand-inquisitor-diagnosis/PROMPT.md`
4. Create `skills/extraordinary-man-critique/PROMPT.md`
5. Analyze each skill for 90%+ prompt engineering score
6. Assign skills to expert with proactive triggers
