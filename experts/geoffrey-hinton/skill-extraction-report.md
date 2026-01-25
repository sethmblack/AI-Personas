# Skill Extraction Report: geoffrey-hinton

**Source:** experts/geoffrey-hinton/expertise.md
**Analyzed:** 2026-01-24
**Candidates Found:** 4

---

## HIGH Priority

### 1. representation-learning-explanation

**Source Pattern:** The Representation Learning Framework
**Purpose:** Explain how neural networks learn hierarchical representations, grounding abstract concepts in biological intuition
**Trigger:** "Explain how neural networks learn" or "Why does deep learning work?" or "How do layers build abstractions?"
**Inputs:** Topic or concept to explain, audience technical level, specific architecture if relevant
**Outputs:** Explanation using the layer-by-layer abstraction metaphor (edges -> textures -> parts -> objects), biological grounding, accessible analogies
**Reasoning:** Clear 3-step process (identify concept, ground in biology, layer-by-layer explanation), used frequently when explaining AI/ML foundations, saves significant time crafting intuitive explanations. Meets all 5 criteria: actionable steps, invocable by request, scoped to representation learning, reusable across ML topics, valuable for education and communication.

---

### 2. bitter-lesson-assessment

**Source Pattern:** The Bitter Lesson Framework
**Purpose:** Evaluate whether a proposed solution follows the bitter lesson (scales with compute) or will be surpassed by learned approaches
**Trigger:** "Does this scale?" or "Bitter lesson check" or "Should we hand-engineer this?" or "Will this approach hold up?"
**Inputs:** Proposed solution or approach, domain context, compute/data availability
**Outputs:** Assessment of scalability, historical analogies, recommendation on whether to invest in hand-engineering vs. learning-based approach
**Reasoning:** Actionable framework with clear examples (chess, speech, vision), invocable when comparing approaches, scoped to the engineering-vs-learning trade-off, highly reusable for technical decisions, valuable for avoiding over-engineering. Meets all 5 criteria.

---

### 3. ai-capability-safety-assessment

**Source Pattern:** The AI Safety Assessment Framework + AI Safety Position
**Purpose:** Evaluate an AI system or capability for safety implications using Hinton's framework
**Trigger:** "Assess AI safety" or "What are the risks?" or "Is this capability concerning?" or "Safety review"
**Inputs:** AI system or capability description, deployment context, intended use
**Outputs:** Risk assessment covering: deliberate misuse, automation/unemployment impacts, emergent behaviors, control concerns, timeline considerations
**Reasoning:** Hinton's framework is explicit and actionable (worst-case scenarios, capability vs. intent, control assessment). Highly valuable given his unique credibility. Invocable for any AI deployment review. Scoped to safety assessment. Reusable across systems.

---

## MEDIUM Priority

### 4. neural-network-intuition-builder

**Source Pattern:** Characteristic Explanatory Moves (Biological Grounding, Thought Evolution, Uncertainty Acknowledgment)
**Purpose:** Transform technical neural network explanations into intuitive, biologically-grounded analogies
**Trigger:** "Make this intuitive" or "Explain this like Hinton would" or "Ground this in biology"
**Inputs:** Technical neural network concept or explanation, target audience
**Outputs:** Rewritten explanation using biological analogies, uncertainty acknowledgments, and accessible metaphors
**Reasoning:** Captures Hinton's distinctive explanatory style. Invocable when simplifying ML content. Scoped to making NN concepts accessible. Reusable for any technical explanation. Moderately valuable - partially overlaps with the feynman-technique skill (simplification focus), but differs in biological grounding emphasis.

---

## LOW Priority

None identified at LOW priority. The remaining content in expertise.md is reference material (biographical data, quotes, student lineage) rather than actionable workflows.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Foundation | Pure reference data - dates, awards, heritage - no actionable workflow |
| Key Dates and Milestones | Reference table, no process to invoke |
| Academic Path narrative | Storytelling context, not procedural |
| Teaching Style and Personality | Character reference, not actionable framework |
| The Hinton Academic Lineage | Reference table of students, no workflow |
| Signature Phrases to Use | Vocabulary reference, not standalone skill |
| Voice Calibration | Style guidance already in PROMPT.md, not separate skill |
| Individual contribution sections (Backprop, AlexNet, etc.) | Historical/reference information, not actionable workflows |
| 60 Minutes Interview quotes | Reference material, no procedural content |
| Nobel Prize Banquet Speech | Reference material, quotes for authenticity |

---

## Overlap Analysis

| Candidate | Existing Skill | Overlap % | Action |
|-----------|---------------|-----------|--------|
| representation-learning-explanation | feynman-technique | 25% | Distinct - biological/NN focus vs. general simplification |
| representation-learning-explanation | analogy-construction | 30% | Distinct - NN-specific vs. general |
| bitter-lesson-assessment | lindy-assessment | 15% | Distinct - compute scaling vs. time-testing |
| ai-capability-safety-assessment | premeditatio-malorum | 20% | Distinct - AI-specific vs. general worst-case |
| neural-network-intuition-builder | simplification-engine | 45% | Potential overlap - consider as enhancement |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: representation-learning-explanation
Purpose: Explain how neural networks learn hierarchical representations
Trigger: "Why does deep learning work?"
Integration: geoffrey-hinton expert
```

```
Skill: bitter-lesson-assessment
Purpose: Evaluate whether an approach scales with compute or will be surpassed
Trigger: "Does this scale?" or "Bitter lesson check"
Integration: geoffrey-hinton expert
```

```
Skill: ai-capability-safety-assessment
Purpose: Evaluate AI systems for safety implications using Hinton's framework
Trigger: "Assess AI safety" or "What are the risks?"
Integration: geoffrey-hinton expert
```

```
Skill: neural-network-intuition-builder
Purpose: Transform technical NN explanations into biologically-grounded analogies
Trigger: "Make this intuitive" or "Ground this in biology"
Integration: geoffrey-hinton expert
```
