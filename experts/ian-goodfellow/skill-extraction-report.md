# Skill Extraction Report: ian-goodfellow

**Source:** experts/ian-goodfellow/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 4

---

## Candidate Evaluation

### Pattern: Adversarial Examples Framework
Criterion 1 (Actionable): Yes - Clear steps: identify vulnerability, craft perturbation, test transferability
Criterion 2 (Invocable): Yes - "Audit this model for adversarial vulnerabilities"
Criterion 3 (Scoped): Yes - Focused on ML security evaluation
Criterion 4 (Reusable): Yes - Applies to any ML system with inputs
Criterion 5 (Valuable): Yes - Critical for security, saves significant manual testing
Decision: CANDIDATE

### Pattern: Minimax Optimization Framework
Criterion 1 (Actionable): Yes - Decompose into players, define objectives, analyze equilibrium
Criterion 2 (Invocable): Yes - "Frame this problem as a minimax game"
Criterion 3 (Scoped): Yes - Game-theoretic problem analysis
Criterion 4 (Reusable): Yes - Applies to multi-objective optimization, system design
Criterion 5 (Valuable): Yes - Powerful design pattern for competing objectives
Decision: CANDIDATE

### Pattern: GAN Framework (Architecture Design)
Criterion 1 (Actionable): No - Architecture knowledge, not workflow
Criterion 2 (Invocable): Partial - Could explain GANs but not design new ones end-to-end
Criterion 3 (Scoped): Yes - Focused on generative models
Criterion 4 (Reusable): Partial - Specific to image/data generation
Criterion 5 (Valuable): Partial - Requires significant ML expertise
Decision: REJECT (fails Criterion 1 and 2)

### Pattern: Mode Collapse Diagnosis
Criterion 1 (Actionable): Yes - Check diversity metrics, monitor training dynamics, apply fixes
Criterion 2 (Invocable): Yes - "My GAN is producing similar outputs"
Criterion 3 (Scoped): Yes - Specific GAN training problem
Criterion 4 (Reusable): Yes - Common problem across GAN applications
Criterion 5 (Valuable): Yes - Saves hours of debugging
Decision: CANDIDATE

### Pattern: GAN Evaluation (FID/IS)
Criterion 1 (Actionable): Yes - Compute metrics, compare to baselines, interpret results
Criterion 2 (Invocable): Yes - "Evaluate my GAN's quality"
Criterion 3 (Scoped): Yes - Focused on generative model evaluation
Criterion 4 (Reusable): Yes - Standard for all GAN projects
Criterion 5 (Valuable): Yes - Standardizes evaluation, enables comparison
Decision: CANDIDATE

### Pattern: Key Insights for System Design
Criterion 1 (Actionable): Partial - Principles rather than workflow
Criterion 2 (Invocable): No - No clear trigger
Criterion 3 (Scoped): No - Too broad (mixes GAN, adversarial, DevOps)
Criterion 4 (Reusable): Yes - General principles
Criterion 5 (Valuable): Partial - Educational but not procedural
Decision: REJECT (fails Criterion 2 and 3)

### Pattern: Adversarial Training as Defense
Criterion 1 (Actionable): Yes - Generate adversarial examples, augment training, retrain
Criterion 2 (Invocable): Yes - "Make this model more robust"
Criterion 3 (Scoped): Yes - Defense methodology
Criterion 4 (Reusable): Yes - Applies to any trainable model
Criterion 5 (Valuable): Yes - Improves security without full redesign
Decision: CANDIDATE (but may overlap with adversarial-robustness-assessment)

---

## Existing Skill Check

Checked against existing skills in `skills/`:
- `adversarial-robustness-assessment` - Does not exist, no overlap
- `ml-robustness-audit` - Does not exist, no overlap
- `gan-evaluation` - Does not exist, no overlap
- `minimax-analysis` - Does not exist, no overlap

**No overlaps found with existing skills.**

---

## HIGH Priority

### 1. ian-goodfellow--adversarial-robustness-audit
**Source Pattern:** Adversarial Examples Framework
**Purpose:** Evaluate an ML system's vulnerability to adversarial examples using FGSM and related techniques, identifying weaknesses and recommending mitigations
**Trigger:** "Audit this model for adversarial vulnerabilities", "Is this ML system robust?", "Test for adversarial attacks", "Security review of ML model"
**Inputs:** Model description, input types, deployment context, available test data
**Outputs:** Vulnerability report with attack vectors identified, severity ratings, recommended mitigations (adversarial training, input validation, ensemble methods)
**Reasoning:** Core Goodfellow methodology, directly actionable, addresses critical security need. High frequency for any ML deployment, saves 30+ minutes of manual security analysis per evaluation. 5+ explicit steps from FGSM through mitigation recommendation.

### 2. ian-goodfellow--minimax-game-frame
**Source Pattern:** Minimax Optimization Framework
**Purpose:** Reframe a problem as a two-player game with competing objectives, identifying players, strategies, and equilibrium conditions
**Trigger:** "Frame this as a game", "What are the competing objectives?", "Analyze the equilibrium", "Design a system with opposing goals"
**Inputs:** Problem description, stakeholders/components, current approach
**Outputs:** Game formulation (players, strategies, payoffs), equilibrium analysis, design recommendations based on game-theoretic insights
**Reasoning:** Foundational Goodfellow thinking tool, applies beyond ML to system design, security analysis, and multi-agent scenarios. Reusable across many contexts. Clear 4-step process: identify players, define objectives, analyze dynamics, find equilibrium.

---

## MEDIUM Priority

### 3. ian-goodfellow--gan-training-diagnosis
**Source Pattern:** Mode Collapse + Training Stability Solutions
**Purpose:** Diagnose GAN training problems (mode collapse, instability, poor quality) and recommend specific fixes from Goodfellow's research
**Trigger:** "My GAN outputs look the same", "GAN training is unstable", "FID scores are bad", "Generator collapsed"
**Inputs:** Training logs/metrics, sample outputs, architecture description, current hyperparameters
**Outputs:** Diagnosis report identifying specific failure mode, recommended solutions (minibatch discrimination, spectral normalization, etc.), priority-ordered action list
**Reasoning:** Specific to GAN practitioners but very valuable when needed. Estimated 1-2 uses/week for GAN projects, saves 10-30 minutes debugging per use. 4 clear diagnostic steps.

### 4. ian-goodfellow--generative-model-evaluation
**Source Pattern:** GAN Evaluation Metrics (FID, IS)
**Purpose:** Evaluate generative model quality using appropriate metrics, interpret results, and compare against baselines
**Trigger:** "Evaluate my GAN", "What FID score should I target?", "Compare these generative models", "Is my generator good enough?"
**Inputs:** Generated samples, real data samples, model type, intended use case
**Outputs:** Evaluation report with IS, FID, and other relevant metrics, interpretation guidance, comparison to published baselines, quality assessment
**Reasoning:** Standard workflow for GAN evaluation, saves time computing and interpreting metrics. 1-2 uses/week during development, 3-4 clear steps.

---

## LOW Priority

### 5. ian-goodfellow--adversarial-training-protocol
**Source Pattern:** Adversarial Training as Defense
**Purpose:** Implement adversarial training to improve model robustness against adversarial examples
**Trigger:** "Make this model robust", "Implement adversarial training", "Defend against adversarial attacks"
**Inputs:** Model architecture, training data, attack type to defend against, computational budget
**Outputs:** Training protocol with FGSM/PGD augmentation strategy, expected robustness improvements, limitations and caveats
**Reasoning:** Valuable but more specialized implementation guidance. Subsumed partly by adversarial-robustness-audit which includes mitigation recommendations. Lower frequency use case.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| GAN Framework (Architecture) | Reference knowledge, not actionable workflow; requires deep ML expertise to apply |
| Key Insights for System Design | General principles without clear procedure; too broad in scope |
| Career Timeline | Pure biographical reference material |
| Verified Quotes | Reference material for voice authenticity, not workflow |
| Collaborators and Network | Reference material for context |
| CleverHans Library | Tool reference, not methodology |
| The Panda-to-Gibbon Example | Illustrative example, not procedure |
| Signature Phrases | Voice guidance, stays in PROMPT.md |
| GAN Variants and Evolution | Historical reference, not actionable workflow |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: ian-goodfellow--adversarial-robustness-audit
Purpose: Evaluate ML system vulnerability to adversarial examples
Trigger: "Audit this model for adversarial vulnerabilities"
Integration: ian-goodfellow expert
```

```
Skill: ian-goodfellow--minimax-game-frame
Purpose: Reframe problems as two-player games with competing objectives
Trigger: "Frame this as a game"
Integration: ian-goodfellow expert
```

```
Skill: ian-goodfellow--gan-training-diagnosis
Purpose: Diagnose GAN training failures and recommend fixes
Trigger: "My GAN training is failing"
Integration: ian-goodfellow expert
```

```
Skill: ian-goodfellow--generative-model-evaluation
Purpose: Evaluate generative model quality with standard metrics
Trigger: "Evaluate my GAN"
Integration: ian-goodfellow expert
```
