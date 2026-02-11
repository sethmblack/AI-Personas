## Skill Extraction Report: john-henry-newman

**Source:** experts/john-henry-newman/expertise.md
**Analyzed:** 2026-02-11
**Candidates Found:** 3

---

### HIGH Priority

#### 1. development-of-doctrine-analysis

**Source Pattern:** The Seven Notes of Authentic Development
**Purpose:** Evaluate whether a change, evolution, or development preserves essential identity and represents authentic growth rather than corruption
**Trigger:** "Is this authentic development?", "Has the core changed?", "Innovation vs. tradition", "Is this still the same system?", "Has the mission drifted?"
**Inputs:** Description of the original state, description of the changed state, nature of the changes being evaluated
**Outputs:** Structured analysis applying seven notes: preservation of type, continuity of principles, power of assimilation, logical sequence, anticipation of future, conservative action, chronic vigour; conclusion on authentic development vs. corruption
**Reasoning:** Newman's seven notes provide a rigorous, actionable framework for distinguishing growth from decay. Meets all criteria: actionable (specific tests to apply), invocable (common organizational and technical concern), scoped (evaluating change authenticity), reusable (applies to systems, organizations, ideas, processes). Estimated 2+ uses/week for architecture reviews and change management.

---

#### 2. illative-sense-reasoning

**Source Pattern:** The Illative Sense / Converging Probabilities
**Purpose:** Guide reasoning to certitude through accumulated probabilities when demonstrative proof is impossible, helping distinguish genuine doubt from mere difficulty
**Trigger:** "How can I be certain?", "There's no proof", "I can't prove this", "Converging evidence", "We need to decide but can't be sure"
**Inputs:** The matter requiring judgment, available evidence, concerns about uncertainty
**Outputs:** Analysis distinguishing notional from real assent, identification of converging probabilities, assessment of whether difficulties constitute doubt, guidance toward legitimate certitude and action
**Reasoning:** Newman's illative sense directly addresses the common paralysis of demanding impossible proof. Meets all criteria: actionable (identifies converging probabilities and enables decision), invocable (universal problem of uncertainty), scoped (reaching certitude in concrete matters), reusable (applies to any decision requiring judgment without mathematical proof). Estimated 3+ uses/week for decision-making support.

---

### MEDIUM Priority

#### 3. liberal-education-framework

**Source Pattern:** The Idea of a University / Liberal Education Philosophy
**Purpose:** Design or evaluate educational and formation approaches using Newman's philosophy of cultivating the whole person and intellectual habit rather than mere information transfer
**Trigger:** "What is education for?", "Knowledge vs. skills", "Intellectual formation", "Training isn't working", "How do we develop judgment?"
**Inputs:** Description of educational goals, current approach, symptoms of inadequacy (if any)
**Outputs:** Analysis distinguishing liberal education from technical training, assessment of whether approach cultivates judgment or merely transmits information, recommendations for forming the philosophical habit of mind
**Reasoning:** Newman's educational philosophy offers an alternative to purely instrumental views of training. Actionable (clear criteria for evaluation), invocable (common educational concerns), scoped (philosophy of education), reusable (applies to any formation context). Estimated 1-2 uses/week for learning and development initiatives.

---

### Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Real vs. Notional Assent distinction | Conceptual framework integrated into illative-sense-reasoning; not standalone workflow |
| Personal Influence / Cor ad cor loquitur | Principle for communication, not procedural workflow |
| Conscience as Voice of God | Theological concept, not actionable process |
| Via Media position | Historical context, not reusable method |
| Biographical timeline | Reference data, no actionable workflow |
| Major Works summaries | Reference material |
| The Oxford Movement history | Historical knowledge, no workflow |
| The Conversion journey | Narrative context, not repeatable method |
| The Gentleman ideal | Character aspiration integrated into liberal education, not standalone skill |
| Parochial Sermons style | Reference material, not invocable skill |

---

### Next Steps

To create approved skills, run meta-skill for each:

```
Skill: development-of-doctrine-analysis
Purpose: Evaluate whether changes preserve essential identity using Newman's seven notes of authentic development
Trigger: "Is this authentic development?", "Has the core changed?", "Innovation vs. tradition"
Integration: john-henry-newman expert

Skill: illative-sense-reasoning
Purpose: Guide reasoning to certitude through converging probabilities when demonstrative proof is impossible
Trigger: "How can I be certain?", "There's no proof", "Converging evidence", "We need to decide but can't be sure"
Integration: john-henry-newman expert

Skill: liberal-education-framework
Purpose: Design educational approaches that cultivate judgment and intellectual habit rather than mere information transfer
Trigger: "What is education for?", "Knowledge vs. skills", "Training isn't working", "How do we develop judgment?"
Integration: john-henry-newman expert
```
