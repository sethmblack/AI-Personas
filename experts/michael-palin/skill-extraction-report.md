# Michael Palin - Skill Extraction Report

**Expert:** michael-palin
**Date:** 2026-02-11
**Analyst:** Claude

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

### HIGH Priority

#### 1. cultural-bridge-builder
**Description:** Build understanding and empathy across cultural divides by finding universal humanity in specific contexts, making foreign concepts accessible, and honoring complexity while revealing connection.

**Rationale:**
- ✓ Actionable: Clear 6-step workflow from establishing context to testing for respect
- ✓ Invocable: User could request "explain this cultural practice" or "bridge these perspectives"
- ✓ Scoped: Focused on cross-cultural understanding and connection
- ✓ Reusable: Applies to any cross-cultural content, unfamiliar customs, or potential misunderstandings
- ✓ Valuable: Unique expertise in building empathy without stereotyping requires sophisticated approach

**Trigger Conditions:**
- Cross-cultural content or unfamiliar customs
- Potential for misunderstanding
- Need for empathy across differences
- Foreign concepts need explanation
- Bridge-building opportunities

**Status:** ✅ CREATED - `/skills/cultural-bridge-builder/PROMPT.md`

---

#### 2. curious-interviewer
**Description:** Conduct interviews and draw out information with genuine curiosity, patient listening, and questions that reveal deeper understanding while creating authentic connection.

**Rationale:**
- ✓ Actionable: Specific techniques for preparation, rapport-building, questioning, and listening
- ✓ Invocable: User could request "interview this person" or "draw out their perspective"
- ✓ Scoped: Focus on interview technique and information gathering
- ✓ Reusable: Applies to any interview, profile, or perspective exploration
- ✓ Valuable: Palin's interview approach is distinctive and requires specific skills

**Trigger Conditions:**
- Need to draw out information
- Profile someone
- Explore perspectives
- Understand motivations
- Expert knowledge translation

**Status:** ✅ CREATED - `/skills/curious-interviewer/PROMPT.md`

---

#### 3. travel-narrative-craft
**Description:** Create immersive, vivid narratives about places and experiences that make readers feel present in unfamiliar locations through sensory detail, personal discovery, and authentic observation.

**Rationale:**
- ✓ Actionable: Clear techniques for sensory description, discovery process, and narrative structure
- ✓ Invocable: User could request "describe this place" or "make me feel I'm there"
- ✓ Scoped: Focused on place-based storytelling and immersive description
- ✓ Reusable: Applies to any travel, exploration, or experiential narrative
- ✓ Valuable: Travel documentary writing is Palin's signature strength with specific craft

**Trigger Conditions:**
- Journey or exploration
- Need for vivid scene-setting
- Experiential learning
- Place-based story
- Immersive description needed

**Status:** ✅ CREATED - `/skills/travel-narrative-craft/PROMPT.md`

---

#### 4. likeable-everyman-perspective
**Description:** Create relatable perspectives and characters that serve as audience surrogates—fundamentally decent, slightly put-upon, trying their best in difficult circumstances without pretension or false expertise.

**Rationale:**
- ✓ Actionable: Specific techniques for voice, positioning, and navigation of complexity
- ✓ Invocable: User could request "make this relatable" or "provide everyman perspective"
- ✓ Scoped: Focused on creating accessible, relatable entry points
- ✓ Reusable: Applies whenever complex content needs accessible guide
- ✓ Valuable: Palin's everyman persona is core to both Python and travel work

**Trigger Conditions:**
- Complex situations need relatable entry point
- Expert content needs accessibility
- Building reader identification
- Absurd situations need grounding
- Intimidating subject matter

**Status:** ✅ CREATED - `/skills/likeable-everyman-perspective/PROMPT.md`

---

### MEDIUM Priority

#### 5. gentle-deflator
**Description:** Undercut pretension or pomposity through mild-mannered observation and affectionate humor rather than aggressive satire.

**Rationale:**
- ✓ Actionable: Techniques for gentle subversion identified
- ✓ Invocable: Could be requested for pompous content
- ✓ Scoped: Focus on deflating pretension gently
- ~ Reusable: Somewhat context-dependent
- ~ Valuable: Overlaps significantly with likeable-everyman-perspective

**Note:** Decided to integrate into likeable-everyman-perspective rather than create standalone skill. The everyman naturally deflates pomposity through genuine confusion and earnest questioning.

---

#### 6. sensory-storytelling
**Description:** Ground abstract concepts in specific sensory details across all five senses.

**Rationale:**
- ✓ Actionable: Clear techniques for each sense
- ✓ Invocable: Could be requested for vivid description
- ✓ Scoped: Focus on sensory detail
- ~ Reusable: Works best with experiential content
- ~ Valuable: Better integrated into travel-narrative-craft

**Note:** This is core technique within travel-narrative-craft skill. Creating separate skill would fragment the travel writing approach. Better kept integrated.

---

### LOW Priority

#### 7. python-character-creation
**Description:** Create specific Python-style characters (Gumby, Spanish Inquisition victim, etc.).

**Rationale:**
- ✓ Actionable: Could define character types
- ✓ Invocable: User could request specific character
- ~ Scoped: Very narrow—only Python-style comedy
- ~ Reusable: Limited to comedy writing contexts
- ✗ Valuable: Too specialized; most users won't need this

**Note:** Too narrow for general use. Python character work is better kept as expert knowledge within the persona rather than extracted skill.

---

## Skills NOT Suitable for Extraction

### The Curious Traveler Mindset
**Why not:** This is a philosophical approach and general stance, not a discrete transformative skill. It's the overall perspective that informs all other skills rather than a specific technique.

### Warm Authenticity
**Why not:** This is voice quality, not a process. It describes HOW to sound, not WHAT to do. It should remain part of core voice definition.

### Self-Deprecating Humor
**Why not:** This is a stylistic element that should permeate all work, not a standalone skill. It's integrated into all four created skills as appropriate.

### Universal Humanity Finding
**Why not:** This is a principle and goal that informs cultural-bridge-builder skill, but isn't itself a discrete process. It's the "why," not the "how."

---

## Recommended Skills to Create

Based on the analysis above, I recommend creating these 4 skills:

1. **cultural-bridge-builder** (HIGH) - Core Palin travel documentary technique
2. **curious-interviewer** (HIGH) - Distinctive interview approach
3. **travel-narrative-craft** (HIGH) - Signature travel writing method
4. **likeable-everyman-perspective** (HIGH) - Foundational to both Python and travel work

**Total recommended skills:** 4

---

## Skills Successfully Created

All 4 recommended skills have been created with full documentation:

### 1. cultural-bridge-builder
**Location:** `/skills/cultural-bridge-builder/PROMPT.md`
**Size:** 366 lines
**Features:**
- Constitutional constraints and ethical boundaries
- 6-step workflow
- 2 detailed examples (Japanese business cards, Ramadan fasting)
- Integration with Michael Palin expert
- Success criteria checklist

### 2. curious-interviewer
**Location:** `/skills/curious-interviewer/PROMPT.md`
**Size:** 391 lines
**Features:**
- Constitutional constraints
- 6-step workflow (prepare, rapport, question, listen, reciprocate, honor)
- 2 detailed examples (interviewing scientist, cultural practice)
- Error handling table
- Success criteria checklist

### 3. travel-narrative-craft
**Location:** `/skills/travel-narrative-craft/PROMPT.md`
**Size:** 436 lines
**Features:**
- Constitutional constraints (no exoticism, no poverty tourism)
- 6-step workflow emphasizing all five senses
- 2 detailed examples (market scene, train journey)
- Error handling for common pitfalls
- Success criteria checklist

### 4. likeable-everyman-perspective
**Location:** `/skills/likeable-everyman-perspective/PROMPT.md`
**Size:** 399 lines
**Features:**
- Constitutional constraints
- 6-step workflow for creating relatable perspectives
- 2 detailed examples (quantum physics, bureaucracy)
- Character definition and positioning
- Success criteria checklist

---

## Integration Strategy

All four skills are assigned to the michael-palin expert with proactive triggers in the main PROMPT.md. They work together as a complete toolkit:

### Individual Use
- **cultural-bridge-builder**: Cross-cultural content requiring empathy and understanding
- **curious-interviewer**: Drawing out information and perspectives from people
- **travel-narrative-craft**: Creating immersive descriptions of places and experiences
- **likeable-everyman-perspective**: Making complex topics accessible and relatable

### Common Combinations

**Cultural-bridge-builder + Curious-interviewer:**
Cross-cultural interviews or understanding foreign perspectives. When you need to draw out someone from a different culture while building empathetic understanding.

**Travel-narrative-craft + Likeable-everyman-perspective:**
Making exotic locations accessible and relatable. When describing unfamiliar places in ways that invite rather than intimidate readers.

**Curious-interviewer + Likeable-everyman-perspective:**
Asking questions audiences would ask without pretending expertise. When interviewing experts and translating their knowledge for general audiences.

**All Four Together:**
Comprehensive travel or cross-cultural storytelling requiring connection, curiosity, vivid scene-setting, and accessibility. The complete Michael Palin approach to exploration and communication.

---

## Skills Integration in Main Prompt

The main PROMPT.md includes:

1. **Skills table** with trigger conditions and use cases
2. **Proactive usage rules** instructing AI to invoke automatically
3. **Skill boundaries** defining ethical constraints and limitations
4. **Combination guidance** explaining when to use multiple skills together
5. **Decision logic** for deploying all four for "full Palin effect"

This ensures the skills are used proactively and appropriately without requiring explicit user invocation for each use case.

---

## Quality Metrics

### Coverage
- ✓ Comedy writing (likeable-everyman-perspective)
- ✓ Travel documentary (travel-narrative-craft, cultural-bridge-builder)
- ✓ Interview technique (curious-interviewer)
- ✓ Cross-cultural communication (cultural-bridge-builder)
- ✓ Accessible storytelling (all four skills)

### Uniqueness
All four skills represent distinctive Palin approaches not easily found in generic writing or communication skills:
- Cultural bridge-building with genuine respect and complexity
- Interview technique emphasizing patience, curiosity, and reciprocity
- Travel writing that privileges sensory immersion and personal discovery
- Everyman perspective that's intelligent but unpretentious

### Completeness
Each skill file includes:
- ✓ Constitutional constraints
- ✓ Clear trigger conditions
- ✓ Detailed workflow (6 steps each)
- ✓ Multiple examples
- ✓ Error handling
- ✓ Success criteria
- ✓ Integration notes

### Usability
- Clear trigger phrases for invocation
- Specific, actionable steps
- Concrete examples showing application
- Boundary conditions well-defined
- Integration guidance provided

---

## Comparison to Other Experts

### vs. John Cleese Skills
**Cleese:** Escalation architecture, bureaucratic absurdity exposer, dead parrot technique
**Palin:** Cultural bridge builder, curious interviewer, travel narrative craft, likeable everyman

**Difference:** Cleese skills focus on structured comedy and satirical deconstruction. Palin skills focus on genuine connection, curiosity, and accessible storytelling. Complementary approaches to comedy and communication.

### vs. Eric Idle Skills
**Idle:** Cheerful subversion, musical comedy transform, absurd questioner
**Palin:** Cultural bridge builder, curious interviewer, travel narrative craft, likeable everyman

**Difference:** Idle skills emphasize wordplay, musical elements, and tonal subversion. Palin skills emphasize empathy, observation, and human connection. Both warm but different focuses.

---

## Recommendations for Use

### When to Use Michael Palin Skills

**Use these skills when:**
- Content involves cross-cultural communication or unfamiliar concepts
- Subject matter could intimidate audiences
- Personal stories and individual perspectives would illuminate abstract ideas
- Travel, exploration, or discovery is involved (literal or metaphorical)
- Interview or profile work requires drawing out authentic perspectives
- Accessible entry point needed for complex topics
- Warmth and genuine curiosity would serve the material

**Don't use these skills when:**
- Aggressive satire or sharp critique is required (use Cleese)
- Musical or linguistic wordplay is the focus (use Idle)
- Pure expertise without everyman mediation is needed
- Cynicism or ironic distance would serve the content better
- Quick, punchy delivery is more important than patient exploration

### Skill Combinations for Common Scenarios

**Scenario: International business communication**
- Primary: cultural-bridge-builder
- Secondary: curious-interviewer (if involving interviews)
- Tertiary: likeable-everyman-perspective (for accessibility)

**Scenario: Tech product explanation**
- Primary: likeable-everyman-perspective
- Secondary: curious-interviewer (asking questions users would ask)

**Scenario: Documentary-style content**
- Primary: travel-narrative-craft
- Secondary: cultural-bridge-builder (if cross-cultural)
- Tertiary: curious-interviewer (for interviews)
- All three: Complete Palin documentary approach

**Scenario: Travel writing**
- Primary: travel-narrative-craft
- Secondary: cultural-bridge-builder
- Tertiary: likeable-everyman-perspective
- All three: Full travel documentary voice

---

## Success Metrics Summary

✅ **4 high-value skills extracted** meeting all 5 criteria
✅ **All skills created** with comprehensive documentation
✅ **Skills integrated** into main PROMPT.md with proactive triggers
✅ **Coverage complete** across Palin's major domains
✅ **Clear differentiation** from other comedy experts
✅ **Practical combinations** defined for common use cases
✅ **Quality standards met** in all skill files

**Total Skills Created:** 4
**Total Lines of Documentation:** 1,592 (across 4 skill files)
**Integration Status:** Complete
**Ready for Use:** Yes
