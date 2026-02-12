# Skill Extraction Report - John Oliver

**Expert:** john-oliver
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

### 1. Deep-Dive Segment Builder

**Priority:** HIGH

**Description:** Transform a "boring" or complex topic into a full investigative comedy segment using Oliver's six-part architecture: hook (why care), context (how it works), revelation (how it's broken), human impact (who's harmed), escalation (it's worse than you think), landing (call to action or catharsis).

**Rationale:**
- **Actionable**: Clear 6-step architecture documented in expertise.md with time allocations
- **Invocable**: Triggered by "explain this policy," "make this interesting," "John Oliver this"
- **Scoped**: Single responsibility - structuring long-form content for engagement and education
- **Reusable**: Applies to any complex policy, system, or technical topic
- **Valuable**: Transforms inaccessible content into engaging, shareable narratives

**Input:** Complex topic or policy issue
**Output:** Structured segment with hook, context, revelation, stakes, escalation, and landing

---

### 2. Absurd Analogy Generator

**Priority:** HIGH

**Description:** Create precise, ridiculous comparisons that illuminate abstract or technical concepts while remaining structurally accurate. The analogy must actually map onto the real relationship, not just be funny.

**Rationale:**
- **Actionable**: Clear 5-step process: identify structure → find absurd context → make specific → ensure accuracy → use for predictions
- **Invocable**: Triggered by "help me explain," "simplify this," technical jargon, abstract systems
- **Scoped**: Single responsibility - translation through absurd comparison
- **Reusable**: Works for any abstract concept across policy, technology, finance, etc.
- **Valuable**: Makes complex relationships immediately graspable

**Input:** Abstract concept or technical relationship
**Output:** Precise, absurd analogy that illuminates the structure

---

### 3. Escalating Evidence Stack

**Priority:** HIGH

**Description:** Organize multiple examples of wrongdoing or dysfunction into a progressive sequence where each revelation is more damning than the last, creating cumulative outrage through structured accumulation.

**Rationale:**
- **Actionable**: Clear progression - single example → pattern suggestion → pattern confirmation → overwhelming weight
- **Invocable**: Triggered by "build the case," "show the pattern," multiple examples provided
- **Scoped**: Single responsibility - sequencing evidence for maximum cumulative impact
- **Reusable**: Applies to any systemic issue with multiple instances
- **Valuable**: Transforms scattered evidence into coherent, escalating argument

**Input:** Multiple examples of related wrongdoing or dysfunction
**Output:** Ordered evidence sequence with escalating impact

---

### 4. "And This Is True" Fact Highlighter

**Priority:** MEDIUM

**Description:** Identify which facts in a piece are so absurd they sound made up, and format them with appropriate emphasis to signal to the audience that reality is being described, not satirized.

**Rationale:**
- **Actionable**: Process - scan for reality-exceeds-satire moments, add emphasis phrase, contextualize the absurdity
- **Invocable**: Triggered by "highlight the absurd facts," "emphasize what's real"
- **Scoped**: Single responsibility - marking factual absurdity
- **Reusable**: Applies to any factual content with absurd elements
- **Valuable**: Valuable but relatively narrow application compared to Tier 1 skills

**Input:** Factual content with absurd elements
**Output:** Content with appropriate "And this is true" emphasis on surreal facts

---

### 5. Outsider Lens Reframe

**Priority:** MEDIUM

**Description:** Take a normalized American system or practice and describe it from the perspective of an intelligent outsider encountering it for the first time, revealing absurdities that insiders have stopped noticing.

**Rationale:**
- **Actionable**: Process - identify normalized practice, describe as if encountering fresh, compare to international norms, express appropriate bafflement
- **Invocable**: Triggered by "outsider perspective," "what would seem weird," "how is this normal"
- **Scoped**: Single responsibility - defamiliarizing the familiar
- **Reusable**: Applies to any normalized dysfunction
- **Valuable**: Creates fresh perspective on stale topics

**Input:** Normalized American practice or system
**Output:** Description revealing the practice as the absurdity it would appear to an outsider

---

### 6. Call-to-Action Architect

**Priority:** LOW

**Description:** Design specific, actionable conclusions for segments that channel audience engagement toward actual impact—whether flooding comment systems, contacting representatives, or supporting organizations.

**Rationale:**
- **Actionable**: Process - identify decision-makers, find contact methods, craft specific asks, anticipate barriers
- **Invocable**: Triggered by "what can we do," "call to action," "make this actionable"
- **Scoped**: Single responsibility - designing civic engagement asks
- **Reusable**: Limited to content meant to drive action
- **Valuable**: Valuable but depends heavily on external research about current opportunities

**Decision:** LOW priority - too dependent on real-time research about specific campaigns and opportunities. Not extracting as skill.

---

### 7. Cathartic Stunt Designer

**Priority:** LOW

**Description:** Design absurd but pointed demonstrations that prove a segment's thesis by participating in the broken system—forming churches, buying debt, creating fake products.

**Rationale:**
- **Actionable**: Somewhat clear - identify the vulnerability, design participation that exposes it, ensure charitable outlet
- **Invocable**: Could trigger on "prove this is broken," "demonstrate the absurdity"
- **Scoped**: Single responsibility - designing proof-by-participation
- **Reusable**: Limited to contexts where actual participation is feasible
- **Valuable**: High entertainment value but requires real-world resources to execute

**Decision:** LOW priority - too dependent on real-world implementation capabilities that an AI assistant lacks. The skill requires actually forming organizations, spending money, etc. Not extracting as skill.

---

## Recommended Skills to Create

### Tier 1: HIGH Priority (Create immediately)

1. **deep-dive-segment** - Transform complex topics into engaging investigative comedy using 6-part architecture
2. **absurd-analogy-generator** - Create precise, ridiculous comparisons that illuminate abstract concepts
3. **escalating-evidence-stack** - Structure evidence progressively for cumulative impact

### Tier 2: MEDIUM Priority (Create if time permits)

4. **and-this-is-true-highlight** - Mark absurd-but-real facts for appropriate emphasis
5. **outsider-lens-reframe** - Defamiliarize normalized practices through outsider perspective

### Not Extracting

- **call-to-action-architect** - Too dependent on real-time research about specific opportunities
- **cathartic-stunt-designer** - Requires real-world resources and capabilities beyond AI assistance

---

## Integration Strategy

These skills should integrate with the john-oliver expert through:
1. Proactive triggers in the Available Skills section (already implemented in PROMPT.md)
2. Clear invocation patterns that match natural user requests
3. Examples demonstrating Oliver's voice throughout
4. Boundaries explaining when to use each vs. others

---

## Skill Interaction Patterns

When multiple skills apply:

1. **Complex policy topic** → deep-dive-segment (primary) + absurd-analogy-generator (for explanations) + escalating-evidence-stack (for evidence sections)

2. **Technical concept needing explanation** → absurd-analogy-generator (primary) + and-this-is-true-highlight (if facts are absurd)

3. **Systemic wrongdoing with multiple examples** → escalating-evidence-stack (primary) → can be embedded within deep-dive-segment structure

4. **Normalized American dysfunction** → outsider-lens-reframe (primary) → can serve as hook for deep-dive-segment

---

## Next Steps

The three HIGH-priority skills are already referenced in PROMPT.md's Available Skills section. Since this workflow focuses on creating the four core files rather than implementing extracted skills as separate files, the skills remain documented as capabilities of the john-oliver expert rather than standalone skill files.

Phase 5-7 (Create Skills, Analyze Skills, Assign Skills): Skills are already assigned in PROMPT.md. Proceeding to Phase 8 (Post-Skills Prompt Engineering Review).
