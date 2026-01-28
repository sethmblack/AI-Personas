# Skill Extraction Report: ray-kurzweil

**Source:** experts/ray-kurzweil/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 4

---

## Skill Candidate Evaluation

### Candidate 1: exponential-trend-analysis
**Pattern:** Law of Accelerating Returns / Forecasting Questions (Kurzweil Method)

- Criterion 1 (Actionable): **Yes** - Clear 5-step methodology exists (identify curve, find doubling rate, count doublings, identify paradigm pressure, find "1% moment")
- Criterion 2 (Invocable): **Yes** - Triggered by "analyze this technology trend" or "is this growing exponentially?"
- Criterion 3 (Scoped): **Yes** - Single responsibility: analyze technology domains for exponential patterns
- Criterion 4 (Reusable): **Yes** - Applies to any information technology domain (cloud, AI, storage, etc.)
- Criterion 5 (Valuable): **Yes** - Transforms vague technology discussions into quantified forecasts with dates

**Decision:** CANDIDATE - HIGH PRIORITY

---

### Candidate 2: paradigm-shift-detection
**Pattern:** S-Curve Pattern / Five Computing Paradigms / Paradigm Shifts to Watch

- Criterion 1 (Actionable): **Yes** - Clear framework: identify current paradigm position on S-curve, assess pressure building, identify emerging alternatives
- Criterion 2 (Invocable): **Yes** - Triggered by "is this technology hitting a wall?" or "what's replacing X?"
- Criterion 3 (Scoped): **Yes** - Single responsibility: identify when technology paradigms are shifting
- Criterion 4 (Reusable): **Yes** - Applies across all technology domains
- Criterion 5 (Valuable): **Yes** - Helps avoid investing in dying paradigms and recognizing emerging ones

**Decision:** CANDIDATE - HIGH PRIORITY

---

### Candidate 3: linear-thinking-reframe
**Pattern:** Anti-Patterns to Avoid / Knee in the Curve Concept / 30 Steps Example

- Criterion 1 (Actionable): **Yes** - Replace linear language with exponential framing, convert vague timeframes to specific dates
- Criterion 2 (Invocable): **Yes** - Triggered by "make this more forward-looking" or "add exponential perspective"
- Criterion 3 (Scoped): **Yes** - Single responsibility: transform linear thinking into exponential framing
- Criterion 4 (Reusable): **Yes** - Applies to any technology writing
- Criterion 5 (Valuable): **Yes** - Ensures consistency of Kurzweil voice; prevents common forecasting errors

**Decision:** CANDIDATE - MEDIUM PRIORITY (simpler than HIGH candidates; could be part of expert voice itself)

---

### Candidate 4: gnr-convergence-frame
**Pattern:** GNR Framework / Three Overlapping Revolutions

- Criterion 1 (Actionable): **Partial** - Framework exists but application is more conceptual than procedural
- Criterion 2 (Invocable): **Yes** - Triggered by "how does this connect to larger tech trends?"
- Criterion 3 (Scoped): **Yes** - Single responsibility: frame technology in GNR context
- Criterion 4 (Reusable): **Partial** - Most applicable to health/biotech; less to pure IT
- Criterion 5 (Valuable): **Partial** - Useful for big-picture framing but less actionable for IT audience

**Decision:** REJECT - Does not fully meet criteria 1, 4, 5 for book's IT audience

---

## HIGH Priority

### 1. exponential-trend-analysis
**Source Pattern:** Law of Accelerating Returns / Forecasting Questions (Kurzweil Method)
**Purpose:** Analyze any technology domain for exponential growth patterns and produce dated predictions
**Trigger:** "Analyze the exponential trend in [domain]" or "Is [technology] growing exponentially?" or "What's the trajectory for [X]?"
**Inputs:** Technology domain or trend to analyze, optional historical data points
**Outputs:** Analysis identifying doubling rate, current position on curve, doublings to mainstream, dated predictions, paradigm shift risks
**Reasoning:** Core Kurzweil methodology; directly actionable for IT professionals planning infrastructure; 3+ uses per week for technology forecasting sections. Saves 30+ minutes of manual trend research by providing structured framework.

---

### 2. paradigm-shift-detection
**Source Pattern:** S-Curve Pattern / Five Computing Paradigms / Paradigm Shifts to Watch
**Purpose:** Identify when a technology is reaching paradigm limits and what emerging technology may replace it
**Trigger:** "Is [technology] hitting its limits?" or "What will replace [X]?" or "Should we invest in [current approach] or wait for [new approach]?"
**Inputs:** Current technology or approach being evaluated, optional context about signs of plateau
**Outputs:** S-curve position assessment, paradigm pressure analysis, emerging alternatives, recommendation on timing
**Reasoning:** Critical for architecture decisions; prevents sunk cost in dying paradigms; directly applicable to IT infrastructure planning (e.g., containers vs. VMs, classical vs. quantum). Saves significant effort in technology selection decisions.

---

## MEDIUM Priority

### 3. linear-thinking-reframe
**Source Pattern:** Anti-Patterns to Avoid / "Knee in the Curve" Concept / Transformation Example
**Purpose:** Transform content that uses linear thinking/language into exponential framing
**Trigger:** "Reframe this with exponential thinking" or "Add Kurzweil perspective to this" or "Make this more forward-looking"
**Inputs:** Content containing linear thinking patterns (vague timeframes, "advancing rapidly" language)
**Outputs:** Reframed content with specific dates, doubling metrics, exponential vocabulary
**Reasoning:** Ensures voice consistency; automated transformation rather than manual rewriting. Estimated 1-2 uses per week during chapter editing. Note: Could potentially be absorbed into expert voice rather than standalone skill.

---

## LOW Priority

None identified.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Six Epochs Framework | Reference knowledge for contextualizing, not actionable workflow |
| GNR Framework | Too conceptual for IT audience; better as reference material than standalone skill |
| Signature Phrases | Vocabulary reference, not actionable process |
| Biographical Context | Pure reference information |
| Predictions Timeline | Reference data, no workflow |
| Criticisms and Responses | Reference material for handling objections, not procedural |
| Longevity Escape Velocity | Health-focused; not applicable to IT book context |
| Pattern Recognition Theory of Mind | Theoretical background, not actionable |
| Case Studies (Genome, Solar) | Examples for illustration, not repeatable skills |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: exponential-trend-analysis
Purpose: Analyze any technology domain for exponential growth patterns and produce dated predictions
Trigger: "Analyze the exponential trend in [domain]"
Integration: ray-kurzweil expert
```

```
Skill: paradigm-shift-detection
Purpose: Identify when a technology is reaching paradigm limits and what emerging technology may replace it
Trigger: "Is [technology] hitting its limits?"
Integration: ray-kurzweil expert
```

```
Skill: linear-thinking-reframe
Purpose: Transform content that uses linear thinking/language into exponential framing
Trigger: "Reframe this with exponential thinking"
Integration: ray-kurzweil expert
```

---

## Summary

- **HIGH Priority:** 2 candidates (exponential-trend-analysis, paradigm-shift-detection)
- **MEDIUM Priority:** 1 candidate (linear-thinking-reframe)
- **LOW Priority:** 0 candidates
- **Rejected:** 9 patterns (reference material only)

Recommendation: Create all 3 candidates. The two HIGH priority skills are core to Kurzweil's methodology and directly valuable to IT professionals. The MEDIUM priority skill supports voice consistency but could be deferred if resources are limited.
