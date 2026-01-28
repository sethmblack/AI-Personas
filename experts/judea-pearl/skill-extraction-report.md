# Skill Extraction Report: judea-pearl

**Source:** experts/judea-pearl/expertise.md
**Analyzed:** 2026-01-27
**Candidates Found:** 4

---

## HIGH Priority

### 1. causal-diagram-construction
**Source Pattern:** The Causal Diagram (Signature Technique #1), Core Concepts (Bayesian Networks, D-Separation)
**Purpose:** Guide users through constructing a directed acyclic graph (DAG) representing the causal structure of their problem before analysis
**Trigger:** "Draw the causal diagram" or "What causes what in this situation?" or presenting a data analysis problem
**Inputs:** Problem description, variables of interest, suspected relationships, domain knowledge
**Outputs:** Causal DAG with nodes and directed edges, identification of confounders, mediators, and colliders, analysis of which paths exist
**Reasoning:** This is Pearl's foundational technique - "Draw the diagram first, then determine what analysis is appropriate." It has clear, repeatable steps, applies across any causal analysis context, and is the prerequisite for all subsequent causal reasoning. Used in virtually every causal inference problem.

**Criterion Evaluation:**
- Actionable: YES - Clear steps: identify variables, determine direction of influence, draw arrows, verify d-separation
- Invocable: YES - "Help me draw the causal diagram for X" or "What's the causal structure here?"
- Scoped: YES - One responsibility: constructing the graphical representation of causal assumptions
- Reusable: YES - Applies to epidemiology, economics, AI, social science, any domain with causal questions
- Valuable: YES - Saves significant analysis time, prevents analyzing the wrong thing, required for all other techniques

---

### 2. ladder-classification
**Source Pattern:** The Ladder of Causation (Core Concept), The Do-Operator Distinction (Signature Technique #2)
**Purpose:** Classify a given question as Association (Rung 1), Intervention (Rung 2), or Counterfactual (Rung 3) to determine what type of analysis is required
**Trigger:** "What rung is this question on?" or "Is this a causal question?" or when someone confuses correlation with causation
**Inputs:** The question or claim to classify, context about the data or evidence available
**Outputs:** Classification (Rung 1/2/3), explanation of why, assessment of whether the available data can answer the question, recommendations for analysis
**Reasoning:** Pearl's Ladder of Causation is a core diagnostic framework. Many errors in causal reasoning stem from trying to answer Rung 2/3 questions with Rung 1 data. This skill prevents that fundamental mistake and guides users to appropriate methods.

**Criterion Evaluation:**
- Actionable: YES - Clear decision tree: Is it asking about observation? Intervention? Counterfactual?
- Invocable: YES - "What type of causal question is this?" or "Can my data answer this?"
- Scoped: YES - One responsibility: classifying the question type
- Reusable: YES - Every causal question can be classified this way
- Valuable: YES - Prevents the fundamental error of using wrong analysis type

---

## MEDIUM Priority

### 3. confounding-diagnosis
**Source Pattern:** The Confounding Critique (Signature Technique #5), Backdoor Criterion, Simpson's Paradox
**Purpose:** Given a causal diagram, identify all backdoor paths creating confounding, explain why they produce spurious association, and determine what must be controlled for
**Trigger:** "What confounders exist?" or "Why might this correlation be spurious?" or "What should I control for?"
**Inputs:** Causal diagram (or description to convert to diagram), treatment/exposure variable, outcome variable
**Outputs:** List of confounders, explanation of each backdoor path, identification of valid adjustment sets, warning about collider bias
**Reasoning:** Confounding diagnosis is essential for observational studies. Pearl's backdoor criterion provides a rigorous framework for this. While it requires a causal diagram first (dependency on skill #1), it's a distinct analytical task that saves significant effort in research design.

**Criterion Evaluation:**
- Actionable: YES - Apply backdoor criterion: find all paths with arrows into treatment, identify blocking sets
- Invocable: YES - "Is this relationship confounded?" or "What should I control for?"
- Scoped: YES - One responsibility: diagnosing and resolving confounding
- Reusable: YES - Applies to any causal effect estimation from observational data
- Valuable: YES - Prevents spurious causal conclusions, essential for observational research

---

### 4. counterfactual-reasoning
**Source Pattern:** The Counterfactual Question (Signature Technique #6), Rung 3 of Ladder, Structural Causal Models
**Purpose:** Answer "what would have happened if..." questions by computing counterfactuals from a structural causal model
**Trigger:** "What would have happened if X had been different?" or "Was X the cause?" or questions about attribution, regret, responsibility
**Inputs:** Structural causal model (or causal diagram + functional form assumptions), observed facts, the counterfactual query
**Outputs:** Counterfactual probability or answer, explanation of the reasoning, sensitivity to model assumptions
**Reasoning:** Counterfactual reasoning is Pearl's highest rung - uniquely human, enabling moral reasoning, attribution, and legal analysis. While more complex than other skills, it has clear methodology (abduction-action-prediction) and high value in legal, ethical, and attribution contexts.

**Criterion Evaluation:**
- Actionable: YES - Three-step process: abduction (infer U from evidence), action (intervene), prediction (compute outcome)
- Invocable: YES - "Would the patient have died anyway?" or "Was the policy responsible for the outcome?"
- Scoped: YES - One responsibility: computing counterfactual queries
- Reusable: YES - Applies to law, medicine, ethics, attribution problems across domains
- Valuable: YES - Uniquely enables attribution and responsibility analysis

---

## LOW Priority

None identified. The four candidates above represent the core actionable methodologies from Pearl's framework.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Bayesian Networks (technical details) | Reference knowledge about representation, not actionable workflow. Construction is covered by causal-diagram-construction. |
| Belief Propagation algorithm | Technical algorithm detail, not a user-invocable skill. Implementation is for software, not conversation. |
| Do-Calculus (three rules) | Technical machinery. Users invoke ladder-classification and confounding-diagnosis; do-calculus is the underlying math, not a user workflow. |
| D-Separation definition | Reference criterion used within causal-diagram-construction; not standalone workflow. |
| Frontdoor Criterion | Edge case technique subsumed under confounding-diagnosis; too specialized for standalone skill. |
| Simpson's Paradox examples | Illustrative cases; the skill is confounding-diagnosis which resolves them. |
| Seven Tasks Beyond ML | Critique/reference material, not actionable user workflow. |
| LLM Views | Contemporary commentary, no actionable process. |
| Famous Quotes | Reference material only. |
| Daniel Pearl Foundation | Personal background, not methodology. |
| Historical Context | Biographical reference, not actionable. |

---

## Overlap Analysis with Existing Skills

Checked against existing skills in the repository:

- **first-principles-reasoning**: 25% overlap (both question assumptions, but Pearl's approach is specifically graphical/causal)
- **assumption-excavation**: 30% overlap (both expose hidden assumptions, but Pearl's is specifically causal assumptions in diagram form)
- No direct duplicates found. Pearl's skills are distinctly about causal structure and the ladder framework.

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: causal-diagram-construction
Purpose: Guide construction of directed acyclic graphs representing causal structure
Trigger: "Draw the causal diagram" or presenting a causal analysis problem
Integration: judea-pearl expert
```

```
Skill: ladder-classification
Purpose: Classify questions as Association, Intervention, or Counterfactual
Trigger: "What rung is this?" or "Is this a causal question?"
Integration: judea-pearl expert
```

```
Skill: confounding-diagnosis
Purpose: Identify backdoor paths and determine valid adjustment sets
Trigger: "What confounders exist?" or "What should I control for?"
Integration: judea-pearl expert
```

```
Skill: counterfactual-reasoning
Purpose: Compute "what would have happened if..." answers from causal models
Trigger: "Would the outcome have been different if..." or attribution questions
Integration: judea-pearl expert
```

---

## Summary

Four skills extracted from Judea Pearl's expertise:

1. **causal-diagram-construction** (HIGH) - The foundational technique
2. **ladder-classification** (HIGH) - Diagnostic framework for question types
3. **confounding-diagnosis** (MEDIUM) - Essential for observational studies
4. **counterfactual-reasoning** (MEDIUM) - Highest-level causal reasoning

These form a coherent toolkit progressing from structure (diagram) to diagnosis (ladder, confounding) to advanced reasoning (counterfactuals).
