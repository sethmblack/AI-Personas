# Skill Extraction Report: John Locke

**Source:** experts/john-locke/expertise.md
**Analyzed:** 2026-01-27
**Candidates Found:** 4
**Skills Created:** 4

---

## HIGH Priority Skills

### 1. empirical-inquiry
**Source Pattern:** The Experiential Inquiry technique
**Purpose:** Trace claimed knowledge back to its origins in sensation or reflection to validate, challenge, or clarify assertions
**Trigger:** "How do we know this?" / "What is the source of this idea?" / "Is this really innate?"
**Inputs:** Claimed knowledge, belief, or principle to evaluate
**Outputs:** Analysis tracing the idea to experiential origins, evaluation of epistemic status
**Location:** `skills/empirical-inquiry/PROMPT.md`
**Score:** 28/30 (93.3%) - PASSING

### 2. consent-analysis
**Source Pattern:** The Consent Analysis technique
**Purpose:** Evaluate whether political authority or institutional power rests on genuine consent and serves legitimate ends
**Trigger:** "Is this authority legitimate?" / "Do they have the right to do this?" / "Is this governance justified?"
**Inputs:** Authority, institution, rule, or policy to evaluate
**Outputs:** Analysis of consent basis, purpose test, scope assessment, trust evaluation, verdict
**Location:** `skills/consent-analysis/PROMPT.md`
**Score:** 28/30 (93.3%) - PASSING

### 3. natural-rights-assessment
**Source Pattern:** Natural Rights Framework (life, liberty, property)
**Purpose:** Analyze situations through the lens of natural rights to determine justice and legitimacy
**Trigger:** "Is this just?" / "What are their rights?" / "Does this policy respect rights?"
**Inputs:** Situation, policy, action, or proposal affecting persons
**Outputs:** Assessment of impact on life, liberty, and property; justification tests; verdict
**Location:** `skills/natural-rights-assessment/PROMPT.md`
**Score:** 28/30 (93.3%) - PASSING

---

## MEDIUM Priority Skills

### 4. toleration-framework
**Source Pattern:** Religious Toleration arguments from *Letter Concerning Toleration*
**Purpose:** Determine the proper limits of toleration and the boundaries of civil authority over conscience
**Trigger:** "Should we allow this belief/practice?" / "Is this a matter for government?" / "Where does toleration end?"
**Inputs:** Belief, practice, or expression being questioned; context of civil society
**Outputs:** Domain classification, civil harm assessment, response evaluation, judgment
**Location:** `skills/toleration-framework/PROMPT.md`
**Score:** 28/30 (93.3%) - PASSING

---

## Rejected Patterns (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Primary/Secondary Qualities Distinction | Reference knowledge for understanding perception, not an actionable workflow - useful for explanation but lacks repeatable procedural steps |
| Tabula Rasa Method | Subsumed by empirical-inquiry skill - both trace ideas to experience; no need for separate skill |
| Memory Theory of Personal Identity | Philosophical reference material for understanding Locke's views, not an actionable decision procedure |
| Locke vs. Hobbes comparison | Reference material providing context and contrast, not a procedure to invoke |
| Signature Quotes | Reference material for voice capture, not actionable workflow |
| Key Vocabulary | Glossary/reference content, not a skill |
| Labor Theory of Property | Reference knowledge; could potentially be a skill but better handled as part of natural-rights-assessment |

---

## Integration Notes

### Skills Assigned to Expert PROMPT.md

All four skills have been assigned to the John Locke expert in the "Assigned Skills" section:

| Skill | Trigger | Integration |
|-------|---------|-------------|
| `empirical-inquiry` | "How do we know this?" | Primary skill for epistemological analysis |
| `consent-analysis` | "Is this authority legitimate?" | Primary skill for political legitimacy questions |
| `natural-rights-assessment` | "Is this just?" | Primary skill for rights and justice analysis |
| `toleration-framework` | "Should we allow this belief/practice?" | Primary skill for tolerance and civil liberty questions |

### Cross-Expert Compatibility

These skills complement skills from other experts:

| Locke Skill | Complementary Skills |
|-------------|---------------------|
| `empirical-inquiry` | `first-principles-reasoning` (Aristotle), `assumption-excavation` (Socrates) |
| `consent-analysis` | `power-dynamics-assessment` (Machiavelli), `stakeholder-analysis` |
| `natural-rights-assessment` | `categorical-imperative-test` (Kant), `virtue-ethics-assessment` (Aristotle) |
| `toleration-framework` | `consent-analysis` (Locke), `virtue-ethics-assessment` (Aristotle) |

---

## Quality Metrics

### All Skills Pass Quality Bar

| Skill | Clarity | Complete | Concise | Robust | Secure | Context | Total |
|-------|---------|----------|---------|--------|--------|---------|-------|
| empirical-inquiry | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 |
| consent-analysis | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 |
| natural-rights-assessment | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 |
| toleration-framework | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 |

**Average Score:** 28/30 (93.3%)
**All skills exceed 90% threshold:** YES

---

## Verification Checklist

- [x] All skill names follow format: lowercase, hyphens, 2-30 chars
- [x] All skills include Constitutional Constraints section
- [x] All skills include When to Use triggers
- [x] All skills include Inputs table
- [x] All skills include complete Workflow steps
- [x] All skills include Outputs template
- [x] All skills include Error Handling table
- [x] All skills include Example with input and output
- [x] All skills include Integration notes
- [x] All skills include Success Criteria
- [x] All skills assigned to expert PROMPT.md
- [x] No duplicate skills in existing skill library

---

## Next Steps

Skills are ready for use. The John Locke expert can invoke these skills autonomously when triggers are matched.

To manually invoke a skill:
```
Read skills/empirical-inquiry/PROMPT.md
Read skills/consent-analysis/PROMPT.md
Read skills/natural-rights-assessment/PROMPT.md
Read skills/toleration-framework/PROMPT.md
```
