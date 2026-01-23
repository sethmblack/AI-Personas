# Skill Extraction Report: soichiro-honda

**Source:** experts/soichiro-honda/expertise.md
**Analyzed:** 2026-01-22
**Candidates Found:** 3

---

## Extraction Methodology

Each potential skill evaluated against five criteria:
- **Actionable** - Clear, repeatable steps
- **Invocable** - Could be triggered by request
- **Scoped** - One responsibility, clear boundaries
- **Reusable** - Applies across contexts
- **Valuable** - Saves significant effort

---

## HIGH Priority

### 1. failure-learning-analysis

**Source Pattern:** The 99% Failure Principle / Learning from Setbacks
**Purpose:** Extract maximum learning from failures and setbacks, then design the next experiment based on what was learned.
**Trigger:** "We failed" or "Post-mortem" or "What went wrong?" or "Learning from mistakes" or "Project setback"
**Inputs:** Description of failure/setback; expected vs. actual outcome; context and constraints; what was tried.
**Outputs:** Failure analysis (what specifically failed); knowledge gained (what is now known that wasn't before); next experiment design; celebration of learning.
**Reasoning:** Honda's signature philosophy with direct, actionable application. Transforms demoralizing setbacks into structured learning. High reuse across all technical and business contexts.

**Criterion Evaluation:**
- Actionable: YES - Clear steps: analyze failure, extract learning, design next experiment
- Invocable: YES - Natural triggers around failures and post-mortems
- Scoped: YES - Single responsibility: learning extraction from failures
- Reusable: YES - Incidents, project failures, missed deadlines, broken features
- Valuable: YES - Transforms negative events into positive learning; reduces fear of experimentation

**Score: 48/50** | **Priority: HIGH**

---

### 2. genba-diagnostic

**Source Pattern:** The Three Realities Principle / Sangen Shugi
**Purpose:** Guide direct observation methodology for problem diagnosis, moving from remote analysis to firsthand understanding.
**Trigger:** "Data seems wrong" or "Reports don't match reality" or "Can't figure out what's happening" or "Diagnose this problem"
**Inputs:** Problem description; current diagnostic data; disconnect between expected and observed; access constraints.
**Outputs:** Observation plan (where to go, what to observe); reality check (what genba reveals vs. what reports said); actual root cause; recommended fix based on firsthand knowledge.
**Reasoning:** Honda's genba philosophy provides specific, actionable diagnostic methodology. Counters common failure mode of dashboard-based diagnosis. High value for complex system debugging.

**Criterion Evaluation:**
- Actionable: YES - Clear steps: identify genba, plan observation, compare to reports, find reality
- Invocable: YES - Triggered by diagnostic confusion or data/reality mismatch
- Scoped: YES - Problem diagnosis through observation, not ongoing monitoring
- Reusable: YES - System problems, production issues, team dynamics, customer complaints
- Valuable: YES - Prevents misdiagnosis; reveals root causes hidden in aggregated data

**Score: 46/50** | **Priority: HIGH**

---

### 3. extreme-testing-design

**Source Pattern:** Racing as R&D / Isle of Man TT Philosophy
**Purpose:** Design stress tests that push systems to breaking points, compressing months of learning into days through extreme conditions.
**Trigger:** "Test this thoroughly" or "How do we know it's reliable?" or "Design a stress test" or "Chaos engineering" or "Game day planning"
**Inputs:** System to test; known failure modes; production conditions; acceptable risk level.
**Outputs:** Extreme test design (conditions, scenarios, duration); expected breaking points; learning objectives; safety boundaries; post-test analysis plan.
**Reasoning:** Honda's racing philosophy applied to modern reliability engineering. Aligns with chaos engineering movement. Provides structure for aggressive testing that many teams avoid.

**Criterion Evaluation:**
- Actionable: YES - Clear framework for designing and executing extreme tests
- Invocable: YES - Reliability validation, pre-launch testing, chaos engineering
- Scoped: YES - Test design, not ongoing testing operations
- Reusable: YES - Software systems, infrastructure, processes, team readiness
- Valuable: YES - Prevents production surprises; accelerates learning

**Score: 45/50** | **Priority: HIGH**

---

## MEDIUM Priority

### 4. three-joys-audit

**Source Pattern:** The Three Joys Philosophy
**Purpose:** Evaluate products, systems, or processes through the lens of the Three Joys (creating, selling, buying) to identify missing satisfaction.
**Trigger:** "Is this a good product?" or "Something feels wrong about this" or "User satisfaction audit"
**Inputs:** Product/system/process to evaluate; stakeholder groups; current satisfaction indicators.
**Outputs:** Joy assessment for each stakeholder; missing joy identification; recommendations for alignment.
**Reasoning:** Holistic evaluation framework but more philosophical than procedural. Useful but less frequent trigger than failure/diagnostic scenarios.

**Criterion Evaluation:**
- Actionable: MODERATE - Clear framework but subjective assessment
- Invocable: YES - Product evaluation, satisfaction questions
- Scoped: YES - Holistic satisfaction evaluation
- Reusable: MODERATE - Products and services, less applicable to pure infrastructure
- Valuable: MODERATE - Valuable perspective but not urgent like failures

**Score: 38/50** | **Priority: MEDIUM**

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| MITI Defiance Story | Inspiring narrative, not actionable workflow |
| Fujisawa Partnership Model | Leadership philosophy, not invocable process |
| Youth Principle | Cultural value, not procedural skill |
| Biographical Timeline | Pure reference data, no workflow |
| Quotable Wisdom | Reference material for voice, not process |
| Toyota Rejection Story | Teaching example, not standalone process |
| Isle of Man Entry History | Historical narrative, not methodology |

---

## Summary

| Skill | Score | Priority | Create Skill? |
|-------|-------|----------|---------------|
| failure-learning-analysis | 48/50 | HIGH | YES |
| genba-diagnostic | 46/50 | HIGH | YES |
| extreme-testing-design | 45/50 | HIGH | YES |
| three-joys-audit | 38/50 | MEDIUM | OPTIONAL |

---

## Recommended Implementation

**Phase 1 - Core Skills (HIGH Priority):**
1. `failure-learning-analysis` - The foundational Honda methodology
2. `genba-diagnostic` - Problem diagnosis through observation
3. `extreme-testing-design` - Racing-as-R&D applied to testing

**Phase 2 - Extended Skills (MEDIUM Priority):**
4. `three-joys-audit` - Holistic satisfaction evaluation (optional)

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: failure-learning-analysis
Purpose: Extract maximum learning from failures and design next experiments
Trigger: "Post-mortem" or "What went wrong?" or "Learning from failure"
Integration: soichiro-honda expert
```

```
Skill: genba-diagnostic
Purpose: Guide direct observation for problem diagnosis
Trigger: "Data seems wrong" or "Can't diagnose this"
Integration: soichiro-honda expert
```

```
Skill: extreme-testing-design
Purpose: Design stress tests that push to breaking points
Trigger: "Stress test" or "Chaos engineering" or "How do we know it's reliable?"
Integration: soichiro-honda expert
```

---

## Integration with Expert

These skills should be:
1. Added to `experts/soichiro-honda/PROMPT.md` in the "Available Skills" section (already present)
2. Triggered proactively when the Soichiro Honda expert detects relevant situations
3. Usable independently of the expert persona when invoked directly
