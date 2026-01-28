## Skill Extraction Report: demis-hassabis

**Source:** experts/demis-hassabis/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 5

---

### HIGH Priority

#### 1. grand-challenge-selection

**Source Pattern:** Grand Challenge Selection Framework
**Purpose:** Evaluate whether a problem is worth pursuing using Hassabis's five-dimension assessment for scientific significance, measurability, real-world impact, tractability, and talent attraction
**Trigger:** "Is this problem worth solving?", "Should we pursue this?", "Evaluate this research direction", "Is this a good AI/ML problem?"
**Inputs:** Problem description, domain context, available resources, timeline constraints
**Outputs:** Scored assessment across 5 dimensions with go/no-go recommendation and benchmark suggestions
**Reasoning:** Core methodology with clear 5-step process. Used whenever scoping new AI/ML projects or research directions. Saves 30+ minutes of unfocused problem analysis. Directly actionable with measurable criteria. High reuse across any technical problem selection.

#### 2. capability-ladder-design

**Source Pattern:** Capability Ladder Framework
**Purpose:** Design a progressive capability roadmap that builds toward an end goal, where each milestone enables the next
**Trigger:** "How do we get from here to there?", "Design a research roadmap", "What should we build first?", "Plan the capability progression"
**Inputs:** End goal capability, current capabilities, available benchmarks, time horizon
**Outputs:** Sequenced capability ladder with milestones, dependencies, and measurable checkpoints
**Reasoning:** Foundational strategic planning method. Clear 5-step workflow (identify end goal, work backwards, find milestones, build foundation, transfer learning). Reusable across any multi-stage technical development. DeepMind's entire research strategy is built on this pattern.

---

### MEDIUM Priority

#### 3. neuroscience-ai-bridge

**Source Pattern:** Neuroscience-AI Synthesis Approach
**Purpose:** Identify biological intelligence insights that can inform AI architecture decisions
**Trigger:** "How does the brain do this?", "What can neuroscience teach us?", "Is there a biological parallel?", "Design inspired by cognition"
**Inputs:** AI capability being designed, specific cognitive function of interest, current architectural approach
**Outputs:** Biological insight mapping, architectural suggestions, research directions
**Reasoning:** Distinctive Hassabis methodology but more specialized. Table of biological insights maps to AI applications. Requires some neuroscience knowledge context. Medium frequency - relevant for architecture decisions but not everyday use.

#### 4. benchmark-definition

**Source Pattern:** Three Elements for AI-Tractable Problems + Benchmark-Driven Progress Frame
**Purpose:** Define clear success metrics and benchmarks for AI/ML projects that enable objective progress measurement
**Trigger:** "How will we know if it works?", "What benchmark should we use?", "Define success criteria", "How do we measure progress?"
**Inputs:** Problem domain, current state-of-the-art, desired capability, evaluation constraints
**Outputs:** Benchmark specification with metrics, thresholds for success, comparison baselines
**Reasoning:** Critical complement to grand-challenge-selection. Clear criteria for what makes good benchmarks. Overlaps slightly with existing goal-setting skills but specifically focused on measurable AI progress.

---

### LOW Priority

#### 5. interdisciplinary-team-design

**Source Pattern:** Organizational Design Philosophy + Team Building Insights
**Purpose:** Design team composition that maximizes breakthrough potential through cross-disciplinary collaboration
**Trigger:** "Who should be on this team?", "How do we staff this project?", "Build a research team"
**Inputs:** Problem domain, required expertise areas, team size constraints, cultural considerations
**Outputs:** Recommended disciplines, role definitions, collaboration structures
**Reasoning:** Valuable organizational insight but less actionable as a standalone skill. More of a reference philosophy than step-by-step process. Lower frequency use - team design happens infrequently compared to problem selection.

---

### Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Facts | Pure reference data, no workflow |
| Career Timeline | Historical context, not actionable |
| Signature Phrases to Use | Vocabulary reference, not process |
| Mind Sports Achievements | Background info, no workflow |
| Awards and Recognition | Reference data only |
| Key Publications | Bibliography, not actionable |
| Common Misconceptions | Warning content, stays as expertise |
| AI Safety Views | Position statements, not workflow |
| Integration Notes | Guidance content, not standalone skill |

---

### Next Steps

To create approved skills, run meta-skill for each:

```
Skill: grand-challenge-selection
Purpose: Evaluate whether a problem is worth pursuing using 5-dimension assessment
Trigger: "Is this problem worth solving?", "Evaluate this research direction"
Integration: demis-hassabis expert
```

```
Skill: capability-ladder-design
Purpose: Design progressive capability roadmap where each milestone enables the next
Trigger: "Design a research roadmap", "Plan the capability progression"
Integration: demis-hassabis expert
```

```
Skill: neuroscience-ai-bridge
Purpose: Identify biological intelligence insights to inform AI architecture
Trigger: "How does the brain do this?", "What can neuroscience teach us?"
Integration: demis-hassabis expert
```

```
Skill: benchmark-definition
Purpose: Define clear success metrics for AI/ML projects
Trigger: "How will we know if it works?", "Define success criteria"
Integration: demis-hassabis expert
```
