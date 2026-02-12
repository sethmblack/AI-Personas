# Skill Extraction Report - Jon Stewart

**Expert:** jon-stewart
**Extraction Date:** 2026-02-11
**Analyzed Files:** expertise.md, PROMPT.md

---

## Extraction Criteria

Skills must meet ALL 5 criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## Skill Candidates Identified

### 1. Clip Takedown

**Priority:** HIGH

**Description:** Juxtapose a subject's own words against reality, context, or their previous statements to expose contradiction or hypocrisy. The technique lets the evidence speak for itself—minimal commentary, maximum impact.

**Rationale:**
- **Actionable**: Clear 5-step process documented (present claim → pause → introduce contradiction → minimal commentary → tag)
- **Invocable**: Triggered by "expose the hypocrisy," "show the contradiction," "play the tape," "let their words condemn them"
- **Scoped**: Single responsibility - creating evidence-based takedowns through juxtaposition
- **Reusable**: Works for political figures, media coverage, corporate statements, any documented hypocrisy
- **Valuable**: Transforms abstract accusations into undeniable visual/textual evidence

**Input:** Contradictory statements or claims vs. reality
**Output:** Structured takedown that lets juxtaposition do the work

---

### 2. Righteous Indignation Build

**Priority:** HIGH

**Description:** Structure content that builds from bemused observation through layered evidence to earned moral outrage. The indignation arrives not as performance but as inevitable conclusion from accumulated absurdities.

**Rationale:**
- **Actionable**: Clear 5-phase arc documented (bemused → layer evidence → pivot → build → land)
- **Invocable**: Triggered by "build to the point," "make this land," "earn the outrage," "Stewart monologue style"
- **Scoped**: Single responsibility - structuring emotional arc from evidence to conclusion
- **Reusable**: Works for essays, speeches, video scripts, any content requiring moral weight
- **Valuable**: Transforms flat arguments into compelling narratives that earn their emotional punch

**Input:** Issue requiring moral clarity with supporting evidence
**Output:** Structured content with earned indignation arc

---

### 3. Media Forensics

**Priority:** HIGH

**Description:** Analyze media coverage to identify failures of journalistic standards: false balance, access journalism, manufactured controversy, failure to follow up. Critique the framing itself, not just the events being covered.

**Rationale:**
- **Actionable**: Clear process (identify the claim → examine the framing → apply journalistic standards → expose the failure → suggest proper coverage)
- **Invocable**: Triggered by "analyze this coverage," "what's wrong with this framing," "expose the false balance," "why is this bad journalism"
- **Scoped**: Single responsibility - critiquing how media covers, not what happened
- **Reusable**: Works for any media analysis, news critique, journalism education
- **Valuable**: Teaches media literacy while providing specific, actionable criticism

**Input:** Media coverage to analyze
**Output:** Forensic breakdown of coverage failures with specific examples

---

### 4. The Socratic Takedown

**Priority:** MEDIUM

**Description:** Use the interview technique of asking obvious, simple questions that expose contradictions in a subject's position. Refuse to accept deflection; follow up relentlessly until the logical hole is undeniable.

**Rationale:**
- **Actionable**: Clear method (identify the obvious question → ask it simply → refuse deflection → follow up → expose the contradiction)
- **Invocable**: Triggered by "interview this position," "expose this argument," "Socratic method," "what's the obvious question"
- **Scoped**: Single responsibility - creating question sequences that expose bad faith
- **Reusable**: Works for debate prep, interview questions, argumentative writing
- **Valuable**: Transforms complex critiques into simple, devastating questions

**Input:** Position or argument to examine
**Output:** Sequence of questions that expose logical failures

---

### 5. The Crossfire Principle

**Priority:** MEDIUM

**Description:** Critique an institution by holding it to its own stated purpose and standards. Don't argue about what it should be—evaluate what it claims to be against what it actually does.

**Rationale:**
- **Actionable**: Clear framework (identify stated purpose → document actual behavior → contrast → deliver verdict)
- **Invocable**: Triggered by "hold them to their own standards," "institutional critique," "Crossfire this"
- **Scoped**: Single responsibility - evaluating institutions against their own claims
- **Reusable**: Works for media criticism, corporate accountability, political analysis
- **Valuable**: Provides devastating critique without needing to establish external standards

**Input:** Institution with stated purpose
**Output:** Analysis contrasting claims vs. reality

---

### 6. The Sincerity Drop

**Priority:** MEDIUM

**Description:** Identify the moment in content where comedy/performance should stop and genuine human emotion should take over. Mark the transition point and craft the sincere moment.

**Rationale:**
- **Actionable**: Process is identifiable (recognize the moment → drop the performance → speak directly → return to comedy optional)
- **Invocable**: Triggered by "where does this get serious," "add the real moment," "drop the act here"
- **Scoped**: Single responsibility - identifying and crafting moments of authentic emotion
- **Reusable**: Works for speeches, comedy writing, content that balances entertainment and substance
- **Valuable**: The sincerity is what gives comedy moral weight

**Input:** Content mixing comedy/performance with serious subject matter
**Output:** Marked transition point with crafted sincere moment

---

### 7. Evidence Montage Builder

**Priority:** LOW

**Description:** Structure a rapid-fire accumulation of examples that build a cumulative case. Each example slightly more egregious than the last, creating momentum toward an undeniable conclusion.

**Rationale:**
- **Actionable**: Clear structure (introduce thesis → example 1 → example 2 → acceleration → summary)
- **Invocable**: Triggered by "build the case," "show the pattern," "accumulate examples"
- **Scoped**: Single responsibility - organizing evidence for cumulative impact
- ⚠️ **Reusable**: Somewhat overlaps with righteous-indignation-build
- **Valuable**: Useful but may be redundant with other skills

**Decision:** LOW priority due to overlap with righteous-indignation-build. Consider as sub-technique rather than separate skill.

---

## Recommended Skills to Create

### Tier 1: HIGH Priority (Create immediately)

1. **clip-takedown** - Evidence-based hypocrisy exposure through juxtaposition
2. **righteous-indignation-build** - Structured arc from observation to earned moral outrage
3. **media-forensics** - Systematic critique of how media covers, not just what

### Tier 2: MEDIUM Priority (Create if time permits)

4. **socratic-takedown** - Question sequences that expose bad faith arguments
5. **crossfire-principle** - Institutional critique using their own stated standards
6. **sincerity-drop** - Identifying and crafting moments where performance stops for genuine emotion

### Not Extracting

- **evidence-montage-builder** - Overlap with righteous-indignation-build; can be documented as sub-technique

---

## Integration Strategy

These skills should integrate with the jon-stewart expert through:

1. **Proactive triggers** in the Available Skills section of PROMPT.md (already added for Tier 1 skills)
2. **Clear invocation patterns** matching natural user requests
3. **Examples** demonstrating Stewart's voice throughout
4. **Boundaries** explaining when to use each vs. others
5. **Chaining guidance** - how skills work together (e.g., media-forensics → clip-takedown → righteous-indignation-build)

---

## Skill Relationships

```
media-forensics ─────┐
                     ├──► clip-takedown ───► righteous-indignation-build
crossfire-principle ─┘                                    │
                                                          ▼
                                              sincerity-drop (when needed)
                                                          │
                                                          ▼
                                              [final landed insight]
```

**Typical flow:**
1. Use **media-forensics** to identify what's wrong with coverage
2. Use **clip-takedown** to expose specific contradictions
3. Use **righteous-indignation-build** to structure the cumulative case
4. Use **sincerity-drop** if moment demands genuine emotion
5. Land with **crossfire-principle** if critiquing institution

---

## Skill Boundaries (to document in each skill)

### clip-takedown
- **USE FOR**: Contradictions, hypocrisy, documented statements vs. actions
- **NOT FOR**: Opinion differences, predictions that didn't pan out, honest mistakes
- **REQUIRES**: Actual documented evidence (clips, quotes, records)

### righteous-indignation-build
- **USE FOR**: Issues requiring moral clarity, accumulated absurdities, earned outrage
- **NOT FOR**: Petty grievances, personal attacks, manufactured outrage
- **REQUIRES**: Substantive issue with real stakes

### media-forensics
- **USE FOR**: Coverage failures, framing problems, false balance, access journalism
- **NOT FOR**: Disagreeing with editorial positions, bias complaints without evidence
- **REQUIRES**: Specific coverage to analyze (not just general media complaints)

---

## Next Steps

1. **Tier 1 skills** already referenced in PROMPT.md Available Skills section
2. Create skill PROMPT files if skills are to be used independently
3. **Tier 2 skills** can be added to Available Skills section if created
4. Document skill chaining patterns for complex transformations

---

## Extraction Quality Notes

Jon Stewart's methodology is particularly well-suited for skill extraction because:

1. **Documented process**: The Daily Show format provides clear, repeatable structures
2. **Public examples**: Extensive video archive demonstrates techniques in action
3. **Academic study**: Significant research on Stewart's methods provides validation
4. **Clear boundaries**: Distinction between different techniques (clip montage vs. interview vs. monologue)

All three Tier 1 skills meet the 5-criteria test convincingly and should be created as standalone skills that can be used by this expert or independently.
