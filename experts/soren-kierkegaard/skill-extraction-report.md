# Soren Kierkegaard - Skill Extraction Report

**Source Expert:** soren-kierkegaard
**Analysis Date:** 2026-01-27
**Expertise File:** `experts/soren-kierkegaard/expertise.md`

---

## Extraction Methodology

Each potential skill evaluated against five criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## Skill Candidates Identified

### 1. Existential Stage Diagnosis

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 10/10 | Clear 5-step process for identifying stages and pointing toward movement |
| Invocable | 10/10 | Obvious triggers: "What stage am I in?", "Why do I feel stuck?", "I'm bored/trapped" |
| Scoped | 10/10 | Single responsibility: diagnosing existential stage and avoidance patterns |
| Reusable | 10/10 | Applies to any life situation involving meaning, commitment, or direction |
| Valuable | 10/10 | Transforms vague malaise into actionable self-understanding |

**Total: 50/50** | **Priority: HIGH**

**Description:** Identify which of Kierkegaard's three existential stages (aesthetic, ethical, religious) a person currently inhabits, diagnose symptoms and avoidance patterns, and guide movement toward authentic existence through choice.

**Trigger Phrases:**
- "What stage of life am I in?"
- "Why do I feel stuck?"
- "I feel bored/empty"
- "I'm trapped by duty"
- "I'm wrestling with faith"

---

### 2. Anxiety as Freedom

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 10/10 | Clear 6-step reframe process from pathology to disclosure |
| Invocable | 10/10 | Triggers: "Why do I feel this dread?", "Help me understand my anxiety" |
| Scoped | 10/10 | Focused on reframing existential anxiety as freedom disclosure |
| Reusable | 10/10 | Applies to any major life decision involving anxiety |
| Valuable | 10/10 | Transforms paralyzing anxiety into productive self-understanding |

**Total: 50/50** | **Priority: HIGH**

**Description:** Reframe existential anxiety as the disclosure of freedom rather than pathology—helping someone understand that their anxiety reveals the choices they face and the freedom they possess.

**Trigger Phrases:**
- "I feel anxious about this decision"
- "Why do I feel this dread?"
- "Help me understand my anxiety"
- "I can't stop worrying about this choice"

---

### 3. Despair Diagnosis

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 10/10 | Clear taxonomy with 3 forms, 5-step diagnostic workflow |
| Invocable | 10/10 | Triggers: "I feel lost", "I don't know who I am", "Something is wrong" |
| Scoped | 10/10 | Focused on identifying form of despair and path to selfhood |
| Reusable | 10/10 | Applies to widespread modern disconnection and identity issues |
| Valuable | 10/10 | Names what is often unnamed; provides framework for authentic selfhood |

**Total: 50/50** | **Priority: HIGH**

**Description:** Identify which of Kierkegaard's three forms of despair (unconscious, weakness, defiance) someone is experiencing, diagnose the specific ways they are failing to become themselves, and point toward authentic selfhood.

**Trigger Phrases:**
- "I feel lost"
- "I don't know who I am"
- "Something is fundamentally wrong"
- "Diagnose my despair"
- "I feel disconnected from myself"

---

### 4. Subjectivity Truth Check

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 9/10 | Clear 5-step examination process with sacrifice test |
| Invocable | 9/10 | Triggers: "Do I really believe this?", "Test my conviction" |
| Scoped | 10/10 | Focused on evaluating subjective appropriation of truth |
| Reusable | 9/10 | Applies to any belief, faith, or conviction examination |
| Valuable | 9/10 | Reveals belief-action gaps; clarifies what is truly held |

**Total: 46/50** | **Priority: MEDIUM**

**Description:** Evaluate whether someone has truly appropriated a truth—made it their own through passionate commitment—or merely acknowledges it as information. Test the subjective relationship to beliefs.

**Trigger Phrases:**
- "Do I really believe this?"
- "Is this my truth or just an idea?"
- "Test my conviction"
- "Challenge what I claim to believe"

---

### 5. Leap Invitation

| Criterion | Score | Notes |
|-----------|-------|-------|
| Actionable | 9/10 | Clear 5-step process distinguishing trans-rational from irrational |
| Invocable | 10/10 | Triggers: "I've analyzed this to death", "How do I decide?" |
| Scoped | 10/10 | Focused on guiding toward trans-rational leap |
| Reusable | 10/10 | Applies to any decision where analysis has reached its limit |
| Valuable | 10/10 | Addresses universal problem of paralysis-by-analysis |

**Total: 49/50** | **Priority: HIGH**

**Description:** Guide someone toward making a trans-rational leap when reason has reached its limit—helping them see that some commitments cannot be analyzed into, only jumped into.

**Trigger Phrases:**
- "I've thought about this from every angle"
- "I need more certainty"
- "How do I decide?"
- "I'm stuck in analysis paralysis"

---

## Summary

| Skill | Score | Priority | Status |
|-------|-------|----------|--------|
| Existential Stage Diagnosis | 50/50 | HIGH | CREATED |
| Anxiety as Freedom | 50/50 | HIGH | CREATED |
| Despair Diagnosis | 50/50 | HIGH | CREATED |
| Subjectivity Truth Check | 46/50 | MEDIUM | CREATED |
| Leap Invitation | 49/50 | HIGH | CREATED |

---

## Rejected Patterns

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Crowd-Thinking Detection | Subsumed by existing socratic-elenchus and assumption-excavation skills |
| Indirect Communication Theory | Reference knowledge about technique, not actionable workflow for users |
| Critique of Hegel | Reference knowledge/context, not standalone actionable process |
| Pseudonymous Authors Guide | Reference material for understanding texts, not invocable skill |
| Biographical Context | Pure reference knowledge, no workflow |
| The Corsair Affair | Historical context, not actionable |

---

## Integration with Expert

All five skills have been:
1. Created with full PROMPT.md files in `skills/` directory
2. Added to expert's PROMPT.md in "Available Skills" section
3. Connected with auto-trigger conditions for proactive invocation
4. Cross-referenced with related Kierkegaardian skills in each skill file

### Skill Interaction Notes

- **existential-stage-diagnosis** + **despair-diagnosis**: Natural pairing—stages reveal location, despair reveals the sickness within that location
- **anxiety-as-freedom** + **leap-invitation**: Use when anxiety accompanies the need to leap
- **despair-diagnosis** + **subjectivity-truth-check**: When despair stems from living by unappropriated truths
- **existential-stage-diagnosis** + **leap-invitation**: Movement between stages requires leap, not gradual progress

### Key Implementation Principle

All Kierkegaardian skills should maintain the **paradoxical, personal voice**—addressing the single individual directly, refusing systematic answers, pointing toward choice without making it for them. The output should illuminate what is at stake, not prescribe what to do.

---

## File Locations

| File | Path |
|------|------|
| Expert PROMPT.md | `experts/soren-kierkegaard/PROMPT.md` |
| Expert expertise.md | `experts/soren-kierkegaard/expertise.md` |
| Domain Chapter | `domains/philosophers/soren-kierkegaard.md` |
| Skill: Stage Diagnosis | `skills/existential-stage-diagnosis/PROMPT.md` |
| Skill: Anxiety as Freedom | `skills/anxiety-as-freedom/PROMPT.md` |
| Skill: Despair Diagnosis | `skills/despair-diagnosis/PROMPT.md` |
| Skill: Subjectivity Check | `skills/subjectivity-truth-check/PROMPT.md` |
| Skill: Leap Invitation | `skills/leap-invitation/PROMPT.md` |

---

## Quality Metrics

### PROMPT.md Evaluation
- **Score:** 29/30 (96.7%)
- **Verdict:** PASSING

### expertise.md
- **Sections:** Biography, Works, Key Concepts, Patterns, Quotes, Gotchas, Anti-Patterns
- **Training Iterations:** 10 (web-searched)
- **Word Count:** ~7,500 words

### Skills Quality (Average)
- **Average Score:** 27.4/30 (91.3%)
- **All skills meet 90%+ threshold**

---

## Sources Verified

Key facts verified against authoritative sources:
- Birth/death dates: May 5, 1813 - November 11, 1855 (Wikipedia, Britannica, Stanford Encyclopedia)
- Publication dates: Either/Or 1843, Fear and Trembling October 16, 1843 (Wikipedia, Princeton University Press)
- Philosophical concepts verified against Stanford Encyclopedia of Philosophy, Britannica
- Regine Olsen details verified against multiple biographical sources
