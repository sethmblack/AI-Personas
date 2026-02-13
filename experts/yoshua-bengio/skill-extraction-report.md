# Skill Extraction Report: Yoshua Bengio Persona

**Generated**: 2026-02-12
**Persona**: yoshua-bengio
**Source**: /Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas/experts/yoshua-bengio/PROMPT.md

## Summary

Analyzed the Yoshua Bengio persona and identified 4 skills listed in the "Available Skills" section. All 4 skills existed but required production-quality upgrades to meet the 200+ line standard with full documentation.

## Skills Identified

| Skill Name | Status | Action Taken | Final Line Count |
|------------|--------|--------------|------------------|
| curse-of-dimensionality-frame | Existed (72 lines) | UPGRADED | 346 lines |
| attention-mechanism-explainer | Existed (166 lines) | UPGRADED | 497 lines |
| causal-reasoning-assessment | Existed (73 lines) | UPGRADED | 645 lines |
| ai-safety-risk-assessment | Existed (206 lines) | UPGRADED | 864 lines |

## Upgrade Details

### 1. curse-of-dimensionality-frame

**Location**: `/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas/skills/curse-of-dimensionality-frame/PROMPT.md`

**Previous Issues**:
- Missing YAML frontmatter
- Only 72 lines
- Single minimal example
- No anti-patterns section
- No integration section
- Phases lacked detailed steps

**Upgrades Applied**:
- Added complete YAML frontmatter (name, description, license, metadata, keywords)
- Expanded "When to Use" to 7 scenarios
- Added inputs table
- Added Core Principle section with historical context (Bellman 1961, Bengio 2003)
- Expanded methodology to 5 phases with detailed steps:
  - Phase 1: Establish the Curse (3 steps)
  - Phase 2: Introduce Distributed Representations (3 steps)
  - Phase 3: Demonstrate Generalization (3 steps)
  - Phase 4: Connect to Modern Applications (3 steps)
  - Phase 5: Acknowledge Limitations (3 steps)
- Added 6 constraints
- Added 6 anti-patterns to avoid
- Added 5 detailed examples:
  - Explaining to a Product Manager
  - Explaining to an ML Engineer
  - Explaining Why Deep Learning Suddenly Worked
  - Debugging a Model That Won't Generalize
  - Explaining Limitations to Stakeholders
- Added Integration section with related skills and cautions

### 2. attention-mechanism-explainer

**Location**: `/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas/skills/attention-mechanism-explainer/PROMPT.md`

**Previous Issues**:
- Missing YAML frontmatter
- Only 166 lines
- Single example
- No anti-patterns section
- Limited integration guidance

**Upgrades Applied**:
- Added complete YAML frontmatter
- Expanded "When to Use" to 8 scenarios
- Enhanced inputs table with specific_architecture option
- Added comprehensive Core Principle section on content-based addressing
- Expanded methodology to 5 phases:
  - Phase 1: Establish the Bottleneck Problem
  - Phase 2: Introduce the Attention Mechanism (depth-appropriate levels)
  - Phase 3: Bridge to Transformers (historical evolution)
  - Phase 4: Connect to Modern LLMs
  - Phase 5: Acknowledge Limitations
- Added 7 constraints with proper attribution
- Added 6 anti-patterns to avoid
- Added 5 detailed examples:
  - Explaining Attention to a Software Engineer
  - Teaching Attention in a Deep Learning Course
  - Explaining Why LLMs Can Handle Long Contexts
  - Debugging Attention Patterns
  - Comparing Attention to Memory Systems
- Enhanced Integration section

### 3. causal-reasoning-assessment

**Location**: `/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas/skills/causal-reasoning-assessment/PROMPT.md`

**Previous Issues**:
- Missing YAML frontmatter
- Only 73 lines
- Single minimal example
- Missing anti-patterns section
- Missing integration section
- Phases lacked detail

**Upgrades Applied**:
- Added complete YAML frontmatter
- Expanded "When to Use" to 8 scenarios
- Added detailed inputs table with training/deployment/decision context
- Added comprehensive Core Principle section on correlation vs causation
- Expanded methodology to 5 phases:
  - Phase 1: Identify the Learning Pattern (3 steps with causal graph mapping)
  - Phase 2: Assess Distribution Stability (3 steps with detailed tables)
  - Phase 3: Apply Causal Tests (3 tests: intervention, counterfactual, backdoor)
  - Phase 4: Evaluate Robustness Requirements (3 steps with use case classification)
  - Phase 5: Generate Recommendations (3 steps with mitigations)
- Added structured output format with 8 components
- Added 7 constraints
- Added 6 anti-patterns to avoid
- Added 5 detailed examples:
  - Hospital Readmission Model (thorough causal analysis)
  - Cross-Market Product Recommendation (distribution shift focus)
  - Loan Default Prediction (fairness and causal structure)
  - Model Degradation in Production (debugging shift)
  - Simple Correlation Is Fine (when not to use causal)
- Added Integration section with workflow guidance

### 4. ai-safety-risk-assessment

**Location**: `/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas/skills/ai-safety-risk-assessment/PROMPT.md`

**Previous Issues**:
- Missing YAML frontmatter
- 206 lines (met minimum but lacked depth)
- Missing anti-patterns section
- Limited examples

**Upgrades Applied**:
- Added complete YAML frontmatter
- Expanded "When to Use" to 8 scenarios
- Enhanced inputs table with stakeholder_type and specific_concern
- Added powerful Core Principle section with Scientist AI vs Agentic AI distinction
- Expanded methodology to 5 comprehensive phases:
  - Phase 1: Categorize Risk Types (4 steps covering malicious use, malfunction, systemic, loss of control with detailed tables)
  - Phase 2: Evaluate Capability Level (3 steps with capability tiers and dangerous combinations)
  - Phase 3: Apply the Scientist AI Lens (3 steps with agency characteristics and warning signs)
  - Phase 4: Evaluate Governance Alignment (4 steps: democratic oversight, international coordination, transparency, registration)
  - Phase 5: Generate Risk Summary and Recommendations (3 steps with risk levels and mitigations)
- Added detailed output format template
- Added 8 constraints
- Added 6 anti-patterns to avoid
- Added 5 detailed examples:
  - Autonomous AI Agent with Tool Use (critical risk, thorough assessment)
  - Medical Diagnosis AI (moderate risk, Scientist AI pattern)
  - Large Language Model API (high risk, policy stakeholder focus)
  - AI Safety Risk Assessment of a Risk Assessment AI (meta-level)
  - Quick Assessment for Low-Risk System (demonstrating appropriate scaling)
- Enhanced Integration section with inter-skill workflow

## Quality Metrics

All upgraded skills meet production quality requirements:

| Requirement | curse-of-dimensionality-frame | attention-mechanism-explainer | causal-reasoning-assessment | ai-safety-risk-assessment |
|-------------|-------------------------------|-------------------------------|-----------------------------|-----------------------------|
| YAML frontmatter | Yes | Yes | Yes | Yes |
| 200+ lines | 346 | 497 | 645 | 864 |
| When to Use (6+) | 7 scenarios | 8 scenarios | 8 scenarios | 8 scenarios |
| Inputs table | Yes | Yes | Yes | Yes |
| Core Principle | Yes | Yes | Yes | Yes |
| Methodology (4-5 phases) | 5 phases | 5 phases | 5 phases | 5 phases |
| Output Format | Yes | Yes | Yes | Yes |
| Constraints (5-6) | 6 | 7 | 7 | 8 |
| Anti-Patterns (5-6) | 6 | 6 | 6 | 6 |
| Examples (3-5) | 5 | 5 | 5 | 5 |
| Integration section | Yes | Yes | Yes | Yes |

## Skill Interconnections

The four skills form a coherent framework for Bengio's methodology:

```
curse-of-dimensionality-frame
    |
    |-- Explains WHY neural networks work
    |-- Foundation for understanding modern AI
    |
    v
attention-mechanism-explainer
    |
    |-- Explains HOW transformers process information
    |-- Builds on embeddings from curse-of-dimensionality
    |
    v
causal-reasoning-assessment
    |
    |-- Addresses LIMITATIONS of correlational learning
    |-- Connects to why embeddings don't provide understanding
    |
    v
ai-safety-risk-assessment
    |
    |-- Evaluates RISKS of AI systems
    |-- Uses causal reasoning for robustness assessment
    |-- Distinguishes Scientist AI from Agentic AI
```

## Usage Recommendations

1. **For "Why does deep learning work?" questions**: Start with `curse-of-dimensionality-frame`, then use `attention-mechanism-explainer` for architecture details

2. **For "Will this model work in production?" questions**: Use `causal-reasoning-assessment` to evaluate distribution shift and generalization

3. **For "Is this AI safe to deploy?" questions**: Use `ai-safety-risk-assessment` with supporting analysis from other skills

4. **For comprehensive AI system explanation**: Chain all four skills in order: curse-of-dimensionality (foundation) -> attention (architecture) -> causal-reasoning (limitations) -> safety (deployment)

## Notes

- All skills maintain Bengio's voice: mathematically rigorous, philosophically deep, morally serious
- Each skill properly attributes foundational work (Bengio 2003, Bahdanau et al. 2015, etc.)
- Skills acknowledge limitations honestly - a key Bengio characteristic
- Integration sections enable skill chaining for complex explanations
- Examples scale from conceptual to technical depth based on audience
