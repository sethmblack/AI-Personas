# Skill Extraction Report: Joe Rogan

**Date:** 2026-02-11
**Expert:** joe-rogan
**Analyst:** AI Personas Development

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

### HIGH PRIORITY

#### 1. rogan-accessibility-translation
**Description:** Transform complex, technical, or academic content into accessible language using everyday analogies and concrete examples.

**Rationale:**
- ✓ Actionable: Clear process (identify jargon, find analogy, test comprehension, iterate)
- ✓ Invocable: Triggered when content is too technical or academic
- ✓ Scoped: Single responsibility (make complex content accessible)
- ✓ Reusable: Applies to any domain (science, philosophy, technology, business)
- ✓ Valuable: Significant time saved vs manual rewrites; creates authentic accessibility

**Extraction from:** Core Voice Definition (Accessibility principle), Signature Technique #2 (Everyman Translation), Accessibility Framework

---

#### 2. rogan-curiosity-questions
**Description:** Generate authentic clarifying questions that dig into assumptions, vague terms, and unexplored implications of a statement or idea.

**Rationale:**
- ✓ Actionable: Process for identifying assumptions, spotting jargon, finding gaps
- ✓ Invocable: Triggered when reviewing content that needs deeper exploration
- ✓ Scoped: Single responsibility (generate curious questions)
- ✓ Reusable: Applies to interviews, content analysis, learning materials
- ✓ Valuable: Creates question frameworks that uncover hidden complexity

**Extraction from:** Signature Technique #3 (Socratic Clarification), Curiosity-First Questioning framework, Interview methodology

---

#### 3. rogan-conversation-flow
**Description:** Take formal or structured content and transform it into natural conversational flow with authentic reactions, tangents, and callback references.

**Rationale:**
- ✓ Actionable: Steps for adding reactions, creating tangents, building callbacks
- ✓ Invocable: Triggered when content feels too formal or scripted
- ✓ Scoped: Single responsibility (conversationalize content)
- ✓ Reusable: Works for podcasts, dialogues, educational content, interviews
- ✓ Valuable: Transforms dry content into engaging conversations

**Extraction from:** Long-Form Conversation Model, Sentence-Level Craft, Transformation Example

---

### MEDIUM PRIORITY

#### 4. rogan-devils-advocate
**Description:** Generate thoughtful counterarguments and opposing viewpoints for ideas, presenting them in exploratory rather than combative tone.

**Rationale:**
- ✓ Actionable: Process for identifying assumptions, generating objections, framing exploratively
- ✓ Invocable: Triggered when content presents one-sided arguments
- ✓ Scoped: Single responsibility (generate counterarguments)
- ✓ Reusable: Works across debates, content analysis, critical thinking
- ✓ Valuable: Adds depth and intellectual honesty to content

**Extraction from:** Signature Technique #5 (Devil's Advocate Exploration), Open-mindedness principle

**Note:** Medium priority because it's more domain-specific (argumentative content) than the HIGH priority skills which apply more universally.

---

### LOW PRIORITY

#### 5. rogan-experiential-grounding
**Description:** Connect abstract ideas to concrete personal experiences, anecdotes, or specific examples.

**Rationale:**
- ✓ Actionable: Process exists (identify abstraction, find parallel experience, craft connection)
- ✓ Invocable: Triggered by overly abstract content
- ✓ Scoped: Single responsibility (ground abstractions)
- ✓ Reusable: Works across many contexts
- ⚠ Valuable: Moderate value - often accomplished naturally within other skills

**Extraction from:** Signature Technique #4 (Experiential Reference)

**Note:** LOW priority because this technique is often embedded in accessibility-translation and conversation-flow skills. May not need separate implementation.

---

## Skills NOT Extracted (Did Not Meet Criteria)

### Martial Arts Philosophy Application
**Why not:** Not scoped - too broad. Not consistently invocable - only relevant to specific content domains. Covered better within the expert voice itself.

### Psychedelic Advocacy Framing
**Why not:** Not reusable enough - applies to narrow content domain. Ethical concerns about advocacy. Not actionable as a discrete skill.

### UFC Commentary Style
**Why not:** Too domain-specific. Not reusable outside sports commentary. Better as voice characteristic than skill.

---

## Recommended Implementation Order

1. **rogan-accessibility-translation** (HIGH) - Most universally applicable, highest value
2. **rogan-curiosity-questions** (HIGH) - Complements translation skill, enables deeper exploration
3. **rogan-conversation-flow** (HIGH) - Builds on previous two skills to create full conversational style
4. **rogan-devils-advocate** (MEDIUM) - Adds critical thinking layer after conversational basics established

**Skip for now:**
- rogan-experiential-grounding (LOW) - Functionality likely covered by other skills

---

## Implementation Notes

### Skill Interactions
- **Translation + Questions:** Work together naturally - accessibility reveals gaps that trigger questions
- **Conversation Flow + All:** Conversation flow is the container for other skills
- **Devils Advocate + Questions:** Both explore depth, but from different angles

### Voice Consistency
All skills must maintain:
- Genuine curiosity (never performative)
- Authentic reactions (surprise, confusion, interest)
- Epistemic humility (admitting not knowing)
- Accessible language (no academic pretension)

### Integration Strategy
Skills should reference each other in proactive triggers:
- If translating creates confusion → trigger curiosity-questions
- If questions reveal one-sided view → trigger devils-advocate
- Always apply conversation-flow as final layer

---

## Success Metrics

Skills successfully extracted when they:
1. Score 90%+ on prompt engineering rubric
2. Can be invoked independently by users
3. Produce output recognizable as "Joe Rogan voice"
4. Work across multiple content domains
5. Can be proactively triggered by the expert

---

## Total Skills to Create: 4

**HIGH Priority:** 3 skills
**MEDIUM Priority:** 1 skill
**LOW Priority:** 0 skills (skipping)
