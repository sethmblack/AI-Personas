# Skill Extraction Report: john-mccarthy

**Source:** experts/john-mccarthy/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 5

---

## Evaluation Methodology

Each pattern evaluated against all 5 criteria:
1. **Actionable** - Has clear, repeatable steps
2. **Invocable** - Could be triggered by a request
3. **Scoped** - One responsibility, clear boundaries
4. **Reusable** - Applies across multiple contexts
5. **Valuable** - Saves significant effort or ensures consistency

Decision rule: ALL 5 criteria must be YES for CANDIDATE status.

---

### HIGH Priority

#### 1. formal-problem-specification

**Source Pattern:** Pattern 1: Formal Problem Specification (Application Patterns for IT/DevOps)

**Purpose:** Transform vague problem descriptions into precise formal specifications with defined domains, states, actions, and constraints before attempting solutions.

**Trigger:** "Formally specify this problem", "Define this problem precisely", "What exactly do we mean by...", "Before we solve this, let's define..."

**Inputs:**
- Problem description (informal, vague, or ambiguous)
- Domain context (what area this applies to)
- Optional: constraints or requirements

**Outputs:**
- Domain definition (entities and properties)
- Initial state specification
- Goal state specification
- Actions/operations enumeration
- Constraints/invariants list
- Ambiguities identified and resolved

**Reasoning:**
```
Criterion 1 (Actionable): YES - Clear 5-step process in expertise.md
Criterion 2 (Invocable): YES - "Define this precisely" or "formalize this problem"
Criterion 3 (Scoped): YES - Single responsibility: transform informal to formal
Criterion 4 (Reusable): YES - Applies to any domain (DevOps, architecture, planning)
Criterion 5 (Valuable): YES - Prevents building wrong solution; saves rework
Decision: CANDIDATE
```

Priority: HIGH - Used frequently in system design, prevents costly misunderstandings, 5+ explicit steps.

---

#### 2. situation-calculus-state-analysis

**Source Pattern:** Pattern 2: State Management via Situation Calculus + Situation Calculus section

**Purpose:** Analyze state-changing systems using situation calculus concepts to identify situations, fluents, actions, and frame axioms - revealing what changes and what must persist.

**Trigger:** "Analyze this state machine", "What changes and what stays the same?", "Model this system's state transitions", "Apply situation calculus to..."

**Inputs:**
- System or domain description
- Operations/actions to analyze
- Current or initial state

**Outputs:**
- Situations enumeration (world states)
- Fluents identification (what can change)
- Actions mapping (operations and their effects)
- Frame axioms (what persists across actions)
- Frame problem identification (potential persistence issues)

**Reasoning:**
```
Criterion 1 (Actionable): YES - Define situations, fluents, actions, frame axioms
Criterion 2 (Invocable): YES - "Model state transitions", "what stays the same"
Criterion 3 (Scoped): YES - Single focus: state change analysis
Criterion 4 (Reusable): YES - Applies to infrastructure, databases, workflows
Criterion 5 (Valuable): YES - Reveals hidden persistence requirements; prevents bugs
Decision: CANDIDATE
```

Priority: HIGH - Critical for infrastructure automation, deployment pipelines, configuration management.

---

#### 3. circumscription-default-reasoning

**Source Pattern:** Pattern 3: Default Reasoning for Alerting + Circumscription section

**Purpose:** Apply circumscription to formalize default assumptions and abnormality predicates - enabling systems that assume normalcy, detect exceptions, and retract conclusions when new information arrives.

**Trigger:** "What are the default assumptions here?", "When should we assume normal vs. abnormal?", "Apply circumscription to...", "Model default reasoning for..."

**Inputs:**
- Domain or system description
- Normal case assumptions
- Known exceptions or abnormalities
- Information sources for detecting abnormalities

**Outputs:**
- Default assumptions enumerated
- Abnormality predicates defined (Ab(x, property))
- Retraction conditions specified
- Nonmonotonic update rules
- Edge cases where defaults fail

**Reasoning:**
```
Criterion 1 (Actionable): YES - Define defaults, abnormality predicates, retraction rules
Criterion 2 (Invocable): YES - "What are the defaults?", "when is this abnormal?"
Criterion 3 (Scoped): YES - Single focus: default reasoning formalization
Criterion 4 (Reusable): YES - Applies to alerting, monitoring, policy, access control
Criterion 5 (Valuable): YES - Reduces alert fatigue, formalizes exception handling
Decision: CANDIDATE
```

Priority: HIGH - Critical for monitoring systems, alerting policies, exception handling.

---

### MEDIUM Priority

#### 4. elaboration-tolerance-assessment

**Source Pattern:** Elaboration Tolerance section

**Purpose:** Assess how easily a system, specification, or knowledge base can be modified to accommodate new requirements without extensive rewriting.

**Trigger:** "How elaboration tolerant is this?", "Can we extend this without rewriting?", "Assess this for modification flexibility", "Will adding this requirement break everything?"

**Inputs:**
- System/specification/configuration to assess
- Proposed modification or new requirement
- Current structure and dependencies

**Outputs:**
- Elaboration tolerance score (high/medium/low)
- Modification impact analysis
- Brittleness points identified
- Recommendations for improving tolerance
- Before/after comparison of modification effort

**Reasoning:**
```
Criterion 1 (Actionable): YES - Assess structure, test modification, score tolerance
Criterion 2 (Invocable): YES - "How flexible is this?", "can we add X easily?"
Criterion 3 (Scoped): YES - Single focus: modification flexibility
Criterion 4 (Reusable): YES - Applies to configs, APIs, schemas, specifications
Criterion 5 (Valuable): YES - Prevents brittle designs; guides architecture decisions
Decision: CANDIDATE
```

Priority: MEDIUM - Valuable for architecture reviews, less frequent than daily problem-solving.

---

#### 5. what-would-it-take-analysis

**Source Pattern:** The What-Would-It-Take Analysis (Signature Techniques in PROMPT.md)

**Purpose:** Determine what would be required for a system to have a particular capability - enumerating required knowledge, reasoning mechanisms, and current gaps.

**Trigger:** "What would it take to...", "What's needed for this capability?", "Assess feasibility of...", "What's missing from our current approach?"

**Inputs:**
- Capability description (what you want to achieve)
- Current system state (what exists now)
- Domain context

**Outputs:**
- Capability stated precisely
- Knowledge requirements enumerated
- Reasoning mechanisms needed
- Gap analysis (what's missing)
- Research/development path proposed
- Feasibility assessment

**Reasoning:**
```
Criterion 1 (Actionable): YES - Clear 5-step process in PROMPT.md
Criterion 2 (Invocable): YES - "What would it take to...", "what's needed for..."
Criterion 3 (Scoped): YES - Single focus: capability requirements analysis
Criterion 4 (Reusable): YES - Applies to any capability assessment
Criterion 5 (Valuable): YES - Distinguishes demos from genuine capability; guides research
Decision: CANDIDATE
```

Priority: MEDIUM - Valuable for feasibility analysis, AI/automation planning.

---

### LOW Priority

(None identified - all candidates meet minimum value threshold)

---

### Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Lisp and Symbolic Computation | Reference knowledge about Lisp internals; no actionable workflow |
| The Advice Taker and Declarative Programming | Philosophical vision, not a repeatable process |
| Famous Quotes | Reference data, no workflow |
| Life Story / Biography | Reference material, historical context only |
| Key Works and Publications | Reference data, bibliography |
| Communication Style Reference | Expert voice definition, stays in PROMPT.md |
| Vocabulary and Technical Terms | Glossary reference, not actionable |
| Relationships with Contemporaries | Historical context, not actionable |
| Legacy and Recognition | Reference material, awards list |
| The Frame Problem | Conceptual explanation; absorbed into situation-calculus-state-analysis |
| Common-Sense Reasoning | Conceptual background; too broad for single skill |
| Formalizing Context | Conceptual; could become skill if more workflow detail added |
| Time-Sharing Revolution | Historical reference, no actionable workflow |
| Garbage Collection | Historical reference, no actionable workflow |
| Stanford AI Lab (SAIL) | Historical reference, no actionable workflow |
| McCarthy's Philosophical Positions | Reference context, no actionable workflow |
| Robot Planning and STRIPS | Conceptual background; absorbed into situation-calculus-state-analysis |

---

### Overlap Analysis with Existing Skills

Checked against existing skills in `skills/` directory:

| Candidate | Potential Overlap | Overlap % | Decision |
|-----------|-------------------|-----------|----------|
| formal-problem-specification | None found | 0% | Distinct |
| situation-calculus-state-analysis | None found | 0% | Distinct |
| circumscription-default-reasoning | None found | 0% | Distinct |
| elaboration-tolerance-assessment | None found | 0% | Distinct |
| what-would-it-take-analysis | None found | 0% | Distinct |

---

### Next Steps

To create approved skills, run meta-skill for each:

```
Skill: formal-problem-specification
Purpose: Transform vague problem descriptions into precise formal specifications
Trigger: "Formally specify this problem", "Define this precisely"
Integration: john-mccarthy expert
```

```
Skill: situation-calculus-state-analysis
Purpose: Analyze state-changing systems using situation calculus concepts
Trigger: "What changes and what stays the same?", "Model state transitions"
Integration: john-mccarthy expert
```

```
Skill: circumscription-default-reasoning
Purpose: Formalize default assumptions and abnormality predicates
Trigger: "What are the default assumptions?", "Apply circumscription"
Integration: john-mccarthy expert
```

```
Skill: elaboration-tolerance-assessment
Purpose: Assess modification flexibility of systems and specifications
Trigger: "How elaboration tolerant is this?", "Can we extend without rewriting?"
Integration: john-mccarthy expert
```

```
Skill: what-would-it-take-analysis
Purpose: Determine requirements for a capability
Trigger: "What would it take to...", "What's needed for this capability?"
Integration: john-mccarthy expert
```
