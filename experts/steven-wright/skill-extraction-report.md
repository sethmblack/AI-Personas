# Skill Extraction Report - Steven Wright

**Date:** 2026-02-11
**Expert:** steven-wright
**Expertise File:** experts/steven-wright/expertise.md

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

### 1. Deadpan One-Liner Constructor

**Priority:** HIGH

**Description:** Transform mundane observations into compressed, absurdist one-liners using Steven Wright's paraprosdokian and surrealist techniques.

**Rationale:**
- ✓ **Actionable:** 5-step process clearly defined (identify premise → locate assumption → invert element → compress → flatten delivery)
- ✓ **Invocable:** User provides observation/topic, skill returns Wright-style one-liner
- ✓ **Scoped:** Single responsibility: create one deadpan one-liner per invocation
- ✓ **Reusable:** Applies to any topic, content type, or observation
- ✓ **Valuable:** Saves hours of trial-and-error in comedy writing; teaches specific technique

**Source Material:**
- The One-Liner Architecture framework
- 5-step transformation process from PROMPT.md
- Linguistic techniques (paraprosdokian, non sequitur, linguistic paradox, impossible causality)

---

### 2. Paraprosdokian Twist Generator

**Priority:** MEDIUM

**Description:** Apply paraprosdokian structure to create unexpected endings that force reinterpretation of the premise.

**Rationale:**
- ✓ **Actionable:** Defined structure (setup → twist that reframes)
- ✓ **Invocable:** User provides premise, skill returns paraprosdokian version
- ⚠ **Scoped:** Somewhat overlaps with #1 (one-liner constructor), but focuses specifically on this one technique
- ✓ **Reusable:** Applies broadly to comedy, creative writing, advertising
- ✓ **Valuable:** Paraprosdokian is a learnable technique with wide application

**Decision:** MEDIUM priority - Consider integrating into #1 as a technique option rather than standalone skill

**Source Material:**
- Paraprosdokian technique section
- Examples collection

---

### 3. Absurdist Logic Analyzer

**Priority:** LOW

**Description:** Analyze existing comedy or content to identify where absurdist logic could be applied.

**Rationale:**
- ⚠ **Actionable:** Analysis steps are less clear than construction steps
- ✓ **Invocable:** User provides content, skill returns analysis
- ✓ **Scoped:** Single responsibility: analyze for absurdist potential
- ✓ **Reusable:** Applies to reviewing/improving comedy
- ⚠ **Valuable:** Less valuable than construction; analysis without reconstruction is incomplete

**Decision:** LOW priority - Analysis alone is less valuable than the constructive skill #1

**Source Material:**
- Surrealist Logic Matrix
- Core Philosophical Themes

---

### 4. Timeless Material Conversion

**Priority:** LOW

**Description:** Convert topical, time-bound jokes into timeless material by removing dated references.

**Rationale:**
- ✓ **Actionable:** Clear process (identify topical elements → replace with timeless equivalents)
- ✓ **Invocable:** User provides topical joke, skill returns timeless version
- ✓ **Scoped:** Single responsibility: remove temporal dependencies
- ⚠ **Reusable:** Narrow application (only for revising existing comedy)
- ⚠ **Valuable:** Useful but not core to Wright's methodology; more of a content editing task

**Decision:** LOW priority - Wright's rule about avoiding topical references is a constraint, not a generative technique

**Source Material:**
- Timeless Comedy Construction section

---

## Skills Recommended for Creation

### HIGH Priority (Create These)

1. **deadpan-one-liner-constructor**
   - Primary skill embodying Wright's core methodology
   - Clear workflow, high value, broad application
   - Should include all linguistic techniques as options (paraprosdokian, non sequitur, linguistic paradox, causal impossibility)

### MEDIUM Priority (Consider)

None at this stage. Paraprosdokian technique should be integrated into skill #1 rather than created as standalone.

### LOW Priority (Skip)

2. Absurdist Logic Analyzer - Analysis without construction lacks value
3. Timeless Material Conversion - Too narrow, not core to methodology

---

## Decision Summary

**Create 1 high-value skill:**
- deadpan-one-liner-constructor (comprehensive skill covering all Wright techniques)

**Rationale for single skill:**
- Wright's methodology is highly focused: create compressed, deadpan one-liners
- All his techniques (paraprosdokian, non sequitur, paradox, impossible causality) serve this single goal
- Better to have one comprehensive, powerful skill than multiple fragmented ones
- The 5-step process from PROMPT.md provides clear, actionable workflow
- Skill can include technique selection as an input parameter

---

## Integration with Expert

After creating the skill, the expert's PROMPT.md should include:

**Skill Trigger Conditions:**
- User requests "create a one-liner about..."
- User provides observation or statement to transform
- User asks "make this funny in Steven Wright's style"
- User requests specific technique (paraprosdokian, non sequitur, etc.)

**Proactive Usage:**
When Steven Wright expert receives any content that could be transformed into absurdist comedy, automatically invoke the skill rather than attempting transformation manually.
