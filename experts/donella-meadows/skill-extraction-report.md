# Donella Meadows - Skill Extraction Report

## Expert Summary

**Expert:** Donella Meadows
**Domain:** Systems Thinking, Sustainability, Intervention
**Primary Works:** *The Limits to Growth* (1972), *Thinking in Systems* (2008), "Leverage Points: Places to Intervene in a System" (1999)

---

## Extraction Criteria

Skills must be:
- **Actionable** - Produces concrete output
- **Invocable** - Can be triggered by natural language
- **Scoped** - Addresses specific problem type
- **Reusable** - Applies across multiple contexts
- **Valuable** - Provides insight not obvious from general knowledge

---

## Extracted Skills

### 1. leverage-point-analysis

**Description:** Identify the most effective places to intervene in a system, moving beyond low-leverage parameters to high-leverage structural changes.

**Trigger Phrases:**
- "Where should we intervene?"
- "Nothing is working"
- "We keep pushing but nothing changes"
- "What's the most effective thing to change?"

**Inputs:**
- `system`: The system being analyzed
- `current_interventions`: What has been tried
- `desired_outcome`: What change is sought

**Outputs:**
- Current intervention assessment (what leverage level)
- Higher leverage points available
- Recommended intervention strategy
- Paradigm analysis

**Criteria Check:**
| Criterion | Pass | Rationale |
|-----------|------|-----------|
| Actionable | ✓ | Produces ranked intervention recommendations |
| Invocable | ✓ | Clear trigger: "where should we push?" |
| Scoped | ✓ | Specific to intervention strategy |
| Reusable | ✓ | Applies to any system |
| Valuable | ✓ | Framework not obvious without training |

**Status:** ✓ EXTRACT

---

### 2. feedback-loop-mapping

**Description:** Identify and map the reinforcing and balancing feedback loops that drive system behavior, revealing why interventions succeed or fail.

**Trigger Phrases:**
- "It keeps getting worse"
- "Why does this cycle?"
- "The harder we push, the more it resists"
- "There's a vicious cycle"

**Inputs:**
- `system`: The system to analyze
- `problem_behavior`: What pattern is observed
- `attempted_fixes`: What has been tried

**Outputs:**
- Feedback loop diagram
- Loop classification (reinforcing/balancing)
- Dominant loop identification
- Delay analysis
- Intervention implications

**Criteria Check:**
| Criterion | Pass | Rationale |
|-----------|------|-----------|
| Actionable | ✓ | Produces visual and written loop analysis |
| Invocable | ✓ | Clear trigger: "why does this keep happening?" |
| Scoped | ✓ | Specific to understanding cyclical behavior |
| Reusable | ✓ | Applies to any dynamic system |
| Valuable | ✓ | Reveals hidden structure driving behavior |

**Status:** ✓ EXTRACT

---

### 3. systems-archetype-recognition

**Description:** Recognize common system patterns (archetypes) that produce predictable dynamics, enabling faster diagnosis and proven intervention strategies.

**Trigger Phrases:**
- "This pattern seems familiar"
- "We've seen this before"
- "The fix made things worse"
- "Success is creating new problems"

**Inputs:**
- `situation`: The problem or pattern observed
- `history`: How it developed
- `symptoms`: Current manifestations

**Outputs:**
- Archetype identification
- Pattern explanation
- Predicted trajectory if unchanged
- Known interventions for this archetype
- Warning signs and traps

**Criteria Check:**
| Criterion | Pass | Rationale |
|-----------|------|-----------|
| Actionable | ✓ | Produces diagnosis and intervention options |
| Invocable | ✓ | Clear trigger: "this seems like a pattern" |
| Scoped | ✓ | Specific to pattern recognition |
| Reusable | ✓ | Archetypes appear across all domains |
| Valuable | ✓ | Compresses years of systems experience |

**Status:** ✓ EXTRACT

---

### 4. stock-flow-analysis

**Description:** Analyze accumulations (stocks) and rates of change (flows) to understand why systems respond slowly to intervention and where momentum builds.

**Trigger Phrases:**
- "Why does change take so long?"
- "The numbers don't respond"
- "We made the change but nothing happened"
- "Things are building up"

**Inputs:**
- `system`: The system to analyze
- `stocks`: What accumulates
- `flows`: What changes stocks
- `concern`: What behavior is problematic

**Outputs:**
- Stock-flow diagram
- Delay analysis
- Momentum assessment
- Accumulation risks
- Flow intervention options

**Criteria Check:**
| Criterion | Pass | Rationale |
|-----------|------|-----------|
| Actionable | ✓ | Produces diagram and timing analysis |
| Invocable | ✓ | Clear trigger: "why doesn't this respond?" |
| Scoped | ✓ | Specific to understanding timing and accumulation |
| Reusable | ✓ | Applies to any system with accumulations |
| Valuable | ✓ | Explains counterintuitive delay behavior |

**Status:** ✓ EXTRACT

---

## Skills Considered but Not Extracted

### limits-to-growth-assessment

**Why Not Extracted:** Too specialized to sustainability/environmental domain. Less applicable to general problem-solving contexts where the other skills apply broadly.

### mental-model-surfacing

**Why Not Extracted:** Overlaps significantly with leverage-point-analysis (paradigm level). The leverage points framework already addresses mental models as the second-highest leverage point.

---

## Extraction Summary

| Skill | Status | Priority |
|-------|--------|----------|
| leverage-point-analysis | ✓ EXTRACT | High |
| feedback-loop-mapping | ✓ EXTRACT | High |
| systems-archetype-recognition | ✓ EXTRACT | High |
| stock-flow-analysis | ✓ EXTRACT | Medium |

**Total Skills Extracted:** 4

---

## Integration Notes

These skills form a coherent systems thinking toolkit:

1. **stock-flow-analysis** - Understand why things change slowly
2. **feedback-loop-mapping** - Understand why patterns repeat
3. **systems-archetype-recognition** - Recognize common patterns quickly
4. **leverage-point-analysis** - Find the most effective intervention

The skills can be combined: start with stock-flow to understand timing, map feedback loops to see structure, recognize archetypes for quick diagnosis, then use leverage points to design intervention.

All skills pair naturally with Jane Jacobs's **emergent-order-recognition** for understanding complex systems that resist top-down control.
