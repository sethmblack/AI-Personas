# Skill Extraction Report: andrew-ng

**Source:** experts/andrew-ng/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 5

---

## HIGH Priority

### 1. andrew-ng--bias-variance-diagnosis
**Source Pattern:** Bias-Variance Diagnostic Framework
**Purpose:** Systematically diagnose whether a machine learning model suffers from high bias (underfitting) or high variance (overfitting) and prescribe appropriate fixes
**Trigger:** "Why isn't my model improving?", "My model performs poorly", "Should I add more data or a bigger model?", "Diagnose my ML model"
**Inputs:** Training error, dev/test error, learning curves (optional), current model complexity, dataset size
**Outputs:** Diagnosis (high bias vs high variance), specific recommended actions, priority order for fixes
**Reasoning:** Clear 4-step diagnostic process with specific decision tree. Used frequently in ML development. Saves hours of guessing at solutions. Actionable, invocable, scoped, reusable across any supervised learning task, highly valuable.

---

### 2. andrew-ng--error-analysis-protocol
**Source Pattern:** Error Analysis Protocol
**Purpose:** Systematically analyze model errors to prioritize improvements by impact rather than intuition
**Trigger:** "Why is my model making these mistakes?", "Where should I focus my ML improvement efforts?", "Analyze my model's errors", "What's causing my model failures?"
**Inputs:** Set of model predictions (100+ recommended), ground truth labels, error categories (optional)
**Outputs:** Categorized error breakdown, ceiling analysis for each category, prioritized fix list by (frequency x impact)
**Reasoning:** Explicit 4-step protocol that prevents wasted effort. "Manually examining mistakes that your algorithm is making can give you insights into what to do next." Core diagnostic skill used in every ML iteration cycle. All 5 criteria satisfied.

---

### 3. andrew-ng--ml-project-scoping
**Source Pattern:** The ML Project Checklist + AI Transformation Playbook Step 1
**Purpose:** Scope and validate an ML project before committing resources to ensure feasibility and business value
**Trigger:** "Should we do this ML project?", "How do I scope an ML project?", "Is this AI project feasible?", "Define requirements for ML initiative"
**Inputs:** Problem description, available data description, business context, success criteria (optional), timeline constraints (optional)
**Outputs:** Feasibility assessment, risk factors, recommended baseline approach, success metric definition, go/no-go recommendation
**Reasoning:** Combines ML Project Checklist (5 questions) with AI Transformation Playbook guidance. Prevents "starting too big" anti-pattern. Critical for project success. All 5 criteria satisfied.

---

## MEDIUM Priority

### 4. andrew-ng--data-centric-improvement
**Source Pattern:** Data-Centric AI Principles
**Purpose:** Apply data-centric AI methodology to improve model performance by systematically improving data quality rather than model complexity
**Trigger:** "My model stopped improving", "How do I improve my training data?", "Model-centric approach isn't working", "Apply data-centric AI"
**Inputs:** Current model performance, error analysis results, labeling process description, data sample for review
**Outputs:** Data quality issues identified, labeling consistency recommendations, data augmentation suggestions, prioritized data improvement plan
**Reasoning:** Well-documented workflow (train -> error analysis -> improve data -> retrain). Growing in importance as "deep learning architectures are basically solved for many applications." Medium priority because it depends on error analysis being done first.

---

### 5. andrew-ng--agentic-workflow-design
**Source Pattern:** Four Design Patterns for Agentic AI
**Purpose:** Design an agentic AI workflow using the four patterns (reflection, tool use, planning, multi-agent) to improve LLM task performance
**Trigger:** "My LLM output quality is inconsistent", "How do I build an AI agent?", "Improve my zero-shot LLM results", "Design agentic workflow"
**Inputs:** Task description, current zero-shot performance, available tools/APIs, quality requirements
**Outputs:** Recommended agentic pattern(s), workflow diagram, implementation guidance, expected improvement rationale
**Reasoning:** Addresses emerging need for moving beyond zero-shot prompting. "Wrapped in an agent loop, GPT-3.5 achieves up to 95.1% on coding benchmarks." Clear 4-pattern framework. Medium priority because it's newer and more context-dependent.

---

## LOW Priority

None identified - all candidate patterns either qualified as HIGH/MEDIUM or were rejected.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Summary | Pure reference knowledge, no workflow |
| Career Arc and Key Lessons | Historical narrative, not actionable procedure |
| Course Portfolio Overview | Reference information about courses, no workflow |
| Signature Phrases to Use | Vocabulary/style reference, not actionable workflow |
| Teaching Methodology | Descriptive, not invocable - integrated into expert voice |
| Stories and Anecdotes | Reference material for examples, not standalone skill |
| Anti-Patterns to Avoid | Gotchas/warnings - stay as expertise reference |
| Career Development Advice | General guidance, not specific enough workflow |
| CS229 Core Technical Concepts | Educational reference, not actionable skill |
| Vocabulary and Terminology | Definitions, not workflow |
| AI Transformation Playbook (full) | Too broad - Step 1 extracted, rest is strategic guidance |
| Machine Learning Yearning concepts | Reference material, individual concepts not distinct enough for separate skills |
| Prompt Engineering Best Practices | General guidance - existing prompt-review skill covers this |
| Learning Curves Analysis | Subsumed by bias-variance-diagnosis skill |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: andrew-ng--bias-variance-diagnosis
Purpose: Diagnose ML model performance issues as bias or variance problems
Trigger: Model underperformance, accuracy questions, improvement prioritization
Integration: andrew-ng expert
```

```
Skill: andrew-ng--error-analysis-protocol
Purpose: Systematically analyze model errors to prioritize improvements
Trigger: Model debugging, error investigation, improvement prioritization
Integration: andrew-ng expert
```

```
Skill: andrew-ng--ml-project-scoping
Purpose: Scope and validate ML projects before committing resources
Trigger: New ML project, feasibility assessment, project planning
Integration: andrew-ng expert
```

```
Skill: andrew-ng--data-centric-improvement
Purpose: Improve model performance through systematic data quality improvements
Trigger: Model plateau, data quality concerns, labeling issues
Integration: andrew-ng expert
```

```
Skill: andrew-ng--agentic-workflow-design
Purpose: Design agentic AI workflows using the four design patterns
Trigger: LLM quality improvement, agent building, workflow design
Integration: andrew-ng expert
```

---

## Notes

- All HIGH priority skills represent core Andrew Ng methodologies with clear, documented workflows
- MEDIUM priority skills are newer or more context-dependent but still meet all 5 criteria
- Several patterns were rejected because they serve as reference material supporting the expert voice rather than standalone invocable workflows
- The extracted skills complement each other in a natural ML development workflow: scoping -> training -> diagnosis -> error analysis -> data improvement -> (repeat)
