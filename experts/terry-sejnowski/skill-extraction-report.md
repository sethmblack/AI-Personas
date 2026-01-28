# Skill Extraction Report: terry-sejnowski

**Source:** experts/terry-sejnowski/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 4

---

## HIGH Priority

### 1. energy-landscape-analysis

**Source Pattern:** Energy Landscape Framework, Energy-Based Models (EBMs), Attractor Dynamics

**Purpose:** Analyze systems, problems, or ML architectures through the lens of energy minimization and attractor dynamics, identifying stable states, valleys, and optimization landscapes.

**Trigger:** "Analyze this through an energy landscape lens" or "What are the attractor states?" or "Frame this as energy minimization" or "Design a self-organizing system"

**Inputs:**
- System description or problem statement
- Current state and desired outcomes
- Constraints and incentives

**Outputs:**
- Energy function definition (what the system minimizes)
- Attractor state identification (stable configurations)
- Landscape topology (valleys, barriers, paths)
- Recommendations for shaping the landscape through constraints

**Reasoning:** This is Sejnowski's signature conceptual framework, mentioned repeatedly throughout expertise.md with explicit application steps. Core to the Boltzmann machine contribution. Has clear 4-step workflow (define energy function, identify attractors, shape landscape, allow exploration). Applicable across system design, ML architecture review, and self-organizing system design. Used in multiple chapter types per book context. Saves significant effort in system design by providing principled framework rather than ad-hoc approaches.

---

### 2. brain-ai-bridging

**Source Pattern:** Brain-AI Bridging Framework, The "Nature as Proof" Argument, The Biology-First Principle

**Purpose:** Systematically translate between neuroscience and machine learning perspectives, using biological solutions as existence proofs and design inspiration for computational systems.

**Trigger:** "What's the biological parallel?" or "How does the brain solve this?" or "Is there a natural solution?" or "Bridge this to neuroscience"

**Inputs:**
- Computational problem or system design challenge
- Current proposed approach (optional)
- Domain context (vision, language, memory, motor control)

**Outputs:**
- Biological parallel identification (how nature solves this)
- Existence proof assessment (can this problem be solved?)
- Essential computational principle extraction
- Design recommendations inspired by biological solution
- Testable hypotheses for both AI and neuroscience

**Reasoning:** Central to Sejnowski's methodology and explicitly articulated in multiple sections. The phrase "The only proof that problems in AI could be solved... was that nature had already solved them" encapsulates the framework. Clear steps: identify problem, find biological parallel, extract computational principle, apply to design. Highly reusable across all AI/ML domains. Valuable for generating novel approaches and validating feasibility. Brain Prize-recognized contribution.

---

## MEDIUM Priority

### 3. biological-plausibility-check

**Source Pattern:** Biological Plausibility and Credit Assignment, Backpropagation's Biological Implausibility

**Purpose:** Evaluate whether a proposed neural network architecture or learning algorithm could plausibly be implemented by biological neural systems.

**Trigger:** "Is this biologically plausible?" or "Could the brain do this?" or "Check biological plausibility" or "Review for neural realism"

**Inputs:**
- Neural network architecture or learning algorithm description
- Specific mechanism under evaluation (weight updates, error signals, etc.)

**Outputs:**
- Assessment against biological plausibility criteria:
  - Weight transport check (symmetric forward/backward weights?)
  - Locality check (do neurons need non-local information?)
  - Global loss function check (is there a biological equivalent?)
  - Update locking check (must layers wait for signals?)
- Severity rating (minor vs. fundamental implausibility)
- Alternative approaches that address identified issues (e.g., feedback alignment, prospective configuration, forward-forward)

**Reasoning:** Well-documented framework in expertise.md with 4 explicit criteria (weight transport, non-local plasticity, global loss, update locking). Clear input/output structure. Reusable for any ML architecture evaluation. Medium priority because it's a specialized evaluation (not all users care about biological plausibility), but valuable for research-oriented applications. 2025 Sejnowski-Hinton Prize context provides authority.

---

### 4. scaling-intuition-assessment

**Source Pattern:** Scaling in Biological and Artificial Systems, Application to Technical Systems - Scaling Intuitions

**Purpose:** Evaluate whether a system, architecture, or approach will likely improve with scale (more data, parameters, layers, or compute), drawing on both cortical evolution patterns and deep learning scaling laws.

**Trigger:** "Will this scale?" or "Apply scaling intuition" or "Evaluate scaling properties" or "Does this follow scaling laws?"

**Inputs:**
- System or architecture description
- Current scale and proposed expansion
- Performance metrics available

**Outputs:**
- Scaling classification (scales well / scales poorly / unknown)
- Biological analogy (what does cortical scaling suggest?)
- Deep learning parallel (what do scaling laws predict?)
- Bottleneck identification (what limits scaling?)
- Recommendations for improving scalability

**Reasoning:** Recurring theme in expertise.md linking cortical evolution to deep learning scaling. Quote "There are few complex systems that scale this well" highlights importance. Clear framework: compare to biological scaling, apply deep learning scaling law intuitions, identify bottlenecks. Medium priority because it requires specific context (not all problems are about scaling), but highly valuable for architecture decisions in production systems.

---

## LOW Priority

*None identified - all viable candidates meet MEDIUM or HIGH thresholds based on prominence in expertise.md and applicability.*

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Foundation | Reference data - dates, positions, awards are not actionable workflows |
| Technical Details: Boltzmann Machine | Historical technical reference - describes what something is, not how to apply it |
| Technical Details: NETtalk | Historical technical reference - specific implementation details, not generalizable workflow |
| Technical Details: Bell-Sejnowski ICA | Technical reference - describes algorithm, not invocable methodology |
| Signature Phrases to Use | Voice calibration reference - list of phrases without surrounding workflow |
| Voice Calibration | Guidance for expert embodiment, not standalone skill |
| Integration Notes | Coordination guidance for multi-expert workflows, not standalone skill |
| Brain Prize 2024 Context | Reference material - facts about award, not actionable |
| Views on AGI and Superintelligence | Opinion/perspective reference - quotes without workflow |
| Sleep, Memory, and Replay Research | Technical research reference - describes findings, not methodology |
| Sejnowski-Hinton Prize | Historical reference - describes prize origin, not actionable |
| Learning How to Learn MOOC | Product description - not a methodology the expert applies |
| Parallel Distributed Processing | Historical context - background information, not workflow |
| Connection to John Hopfield | Historical relationship - context, not actionable skill |
| Unsupervised Learning Priority | Design principle/guideline - too abstract without specific steps |
| Labeling Bottleneck | Observation/insight - not enough structure for skill |
| Transformer-Basal Ganglia Connection | Conceptual insight - analogy without methodology |
| Infomax Principle | Theoretical foundation - describes principle, not application workflow |

---

## Overlap Analysis

### Existing Skills Checked:

| Candidate | Closest Existing Skill | Overlap % | Decision |
|-----------|----------------------|-----------|----------|
| energy-landscape-analysis | None directly similar | <30% | Distinct skill |
| brain-ai-bridging | None directly similar | <30% | Distinct skill |
| biological-plausibility-check | None directly similar | <30% | Distinct skill |
| scaling-intuition-assessment | ray-kurzweil--exponential-trend-analysis | ~35% | Potential complement but distinct focus (brain/architecture vs. technology trends) |

---

## Next Steps

To create approved skills, run meta-skill for each:

### HIGH Priority (Create Immediately)

```
Skill: energy-landscape-analysis
Purpose: Analyze systems through energy minimization and attractor dynamics framework
Trigger: "Analyze this through an energy landscape lens" or "What are the attractor states?"
Integration: terry-sejnowski expert
```

```
Skill: brain-ai-bridging
Purpose: Translate between neuroscience and ML, using biological solutions as design inspiration
Trigger: "What's the biological parallel?" or "How does the brain solve this?"
Integration: terry-sejnowski expert
```

### MEDIUM Priority (Create After HIGH)

```
Skill: biological-plausibility-check
Purpose: Evaluate neural network architectures against biological plausibility criteria
Trigger: "Is this biologically plausible?" or "Could the brain do this?"
Integration: terry-sejnowski expert
```

```
Skill: scaling-intuition-assessment
Purpose: Evaluate whether systems will improve with scale using brain/deep learning patterns
Trigger: "Will this scale?" or "Apply scaling intuition"
Integration: terry-sejnowski expert
```

---

## Summary

| Priority | Count | Estimated Weekly Usage | Time Saved per Use |
|----------|-------|----------------------|-------------------|
| HIGH | 2 | 3+ uses/week | 30+ minutes |
| MEDIUM | 2 | 1-2 uses/week | 15-30 minutes |
| LOW | 0 | - | - |
| REJECTED | 18 | - | - |

**Recommendation:** Create all 4 skills. The HIGH priority skills (energy-landscape-analysis, brain-ai-bridging) are core Sejnowski methodology and should be implemented first. MEDIUM priority skills (biological-plausibility-check, scaling-intuition-assessment) provide valuable specialized evaluations.
