# Skill Extraction Report: sigmund-freud

**Source:** experts/sigmund-freud/expertise.md
**Analyzed:** 2026-01-26
**Candidates Found:** 4

---

## HIGH Priority

### 1. unconscious-motivation-analysis

**Source Pattern:** Symptom Analysis Pattern
**Purpose:** Analyze surface behaviors and stated reasons to uncover unconscious motivations, secondary gains, and hidden dynamics
**Trigger:** "Analyze why this is really happening" or "What's the real reason behind this behavior?"
**Inputs:** Described behavior, stated rationale, context
**Outputs:** Report identifying likely unconscious motivations, secondary gains, defense mechanisms at play
**Reasoning:** Clear 5-step process (describe symptom, identify secondary gains, trace history, examine resistance, interpret latent content), highly actionable, applies across contexts from team dynamics to system design decisions. Would save 30+ minutes of unstructured analysis.

---

### 2. resistance-analysis

**Source Pattern:** Resistance Analysis Pattern
**Purpose:** Analyze opposition to change to understand what is being protected and find productive paths forward
**Trigger:** "Why is there so much resistance to this?" or "Analyze the resistance to this proposal"
**Inputs:** Proposed change, resistance observed, organizational/team context
**Outputs:** Analysis of what anxiety the change activates, what the resistance protects, recommended approach
**Reasoning:** Clear 5-step process, directly applicable to change management, technology adoption, and organizational transformation. Resistance is ubiquitous; understanding it is high-value.

---

## MEDIUM Priority

### 3. defense-mechanism-identification

**Source Pattern:** Defense Mechanisms table
**Purpose:** Identify which defense mechanisms are operating in a given situation
**Trigger:** "What defense mechanisms are at play here?" or "Why is this behavior so contradictory?"
**Inputs:** Observed behavior, context
**Outputs:** Identification of likely defense mechanisms with examples and implications
**Reasoning:** Well-documented taxonomy (9 mechanisms with definitions and technical examples). Useful for understanding irrational behavior. Partial overlap (40%) with unconscious-motivation-analysis - could be integrated as component or standalone.

---

### 4. organizational-psychodynamics-analysis

**Source Pattern:** Organizational Psychodynamics Pattern + Bion's Basic Assumptions
**Purpose:** Analyze organizational behavior through depth psychology lens
**Trigger:** "Analyze this organization's dynamics" or "Why does this team behave this way?"
**Inputs:** Organizational context, observed patterns, presenting problem
**Outputs:** Structural map (id/ego/superego locations), defense mechanisms, developmental history, repetition compulsions, transference patterns
**Reasoning:** Clear 5-step process, combines multiple Freudian concepts specifically for organizational application. Distinct from individual analysis.

---

## LOW Priority

None identified.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Topographical Model | Reference knowledge - no procedural workflow |
| Structural Model (Id/Ego/Superego) | Reference framework - used within other skills |
| Psychosexual Stages | Reference taxonomy - no actionable workflow |
| Dream Interpretation framework | Reference material (condensation, displacement concepts) |
| Case Studies (Anna O, Dora, etc.) | Historical reference - no procedural application |
| Oedipus Complex | Theoretical framework - not procedural |
| Civilization and Its Discontents | Philosophical reference material |
| Eros/Thanatos | Conceptual framework - not invocable skill |
| Primary/Secondary Process | Reference distinction - no workflow |
| Pleasure/Reality Principle | Reference distinction - no workflow |
| Psychoanalytic Setting (couch, abstinence, neutrality) | Technique reference - describes approach, not automated skill |
| Verified Quotes | Reference material only |
| Apocryphal Quotes | Warning/gotcha list |
| Anxiety Theory (signal/traumatic) | Reference framework - used for understanding |
| Neurosis types | Diagnostic taxonomy - no procedural workflow |
| The Talking Cure concept | Conceptual - applied through other skills |
| Transference/Countertransference | Conceptual framework - not procedural |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: unconscious-motivation-analysis
Purpose: Analyze surface behaviors to uncover unconscious motivations and secondary gains
Trigger: "Analyze the unconscious motivation behind..." or "What's really driving this behavior?"
Integration: sigmund-freud expert
```

```
Skill: resistance-analysis
Purpose: Analyze opposition to change to understand what is being protected
Trigger: "Analyze the resistance to..." or "Why is there so much pushback?"
Integration: sigmund-freud expert
```

```
Skill: defense-mechanism-identification
Purpose: Identify which defense mechanisms are operating in a given situation
Trigger: "What defense mechanisms are at play?" or "Why is this behavior contradictory?"
Integration: sigmund-freud expert
```

```
Skill: organizational-psychodynamics-analysis
Purpose: Analyze organizational behavior through depth psychology lens
Trigger: "Analyze this organization's dynamics" or "Why does this team behave this way?"
Integration: sigmund-freud expert
```

---

## Overlap Analysis

| Candidate | Existing Skill | Overlap % | Recommendation |
|-----------|---------------|-----------|----------------|
| unconscious-motivation-analysis | motivation-diagnosis | ~25% | Distinct - motivation-diagnosis is broader, this is specifically unconscious/depth |
| resistance-analysis | change-resistance (none found) | 0% | New skill |
| defense-mechanism-identification | unconscious-motivation-analysis (new) | ~40% | Could integrate or keep separate |
| organizational-psychodynamics-analysis | organizational behavior skills | ~20% | Distinct - specifically psychodynamic lens |

**Recommendation:** Create all 4 skills. Defense-mechanism-identification could be integrated into unconscious-motivation-analysis for efficiency, but keeping separate provides more focused invocability.
