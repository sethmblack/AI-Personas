# Skill Extraction Report: daniel-ellsberg

**Source:** /Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/ai-personas-book/experts/daniel-ellsberg/expertise.md
**Analyzed:** 2026-01-29
**Candidates Found:** 4

---

## HIGH Priority

### 1. disclosure-calculus

**Source Pattern:** The Whistleblower's Calculus / The Decision Framework
**Purpose:** Guide potential whistleblowers through a structured decision-making framework to assess whether disclosure is warranted and how to proceed responsibly
**Trigger:** "Should I disclose this information?" or "Help me assess whether whistleblowing is appropriate" or "Evaluate my disclosure decision"
**Inputs:** Description of the information to be disclosed, internal channel attempts made, potential consequences, evidence documentation status
**Outputs:** Structured assessment covering: credibility of evidence, public interest analysis, internal channel documentation, risk assessment, timing considerations, and recommended next steps
**Reasoning:** This is Ellsberg's core methodology with clear 6-step process. High reusability across corporate, government, and organizational contexts. Saves significant deliberation time and ensures consistency in high-stakes decisions. Mentioned extensively throughout expertise with dedicated sections.

**Criteria Evaluation:**
- Criterion 1 (Actionable): YES - Clear 6-step framework with specific questions at each stage
- Criterion 2 (Invocable): YES - Natural trigger: "Should I disclose?" or "Assess my whistleblowing situation"
- Criterion 3 (Scoped): YES - Single responsibility: evaluate disclosure decisions
- Criterion 4 (Reusable): YES - Applies to corporate, government, nonprofit, any institutional context
- Criterion 5 (Valuable): YES - Saves hours of agonizing deliberation, ensures no critical factors are missed

**Decision:** CANDIDATE

---

### 2. evidence-authentication

**Source Pattern:** The Document Dump / Document Analysis skill
**Purpose:** Assess documentary evidence for credibility, completeness, and persuasive power before disclosure or publication
**Trigger:** "Evaluate this evidence" or "Is this documentation strong enough?" or "Assess the credibility of these documents"
**Inputs:** Documents or evidence to be evaluated, context about source and chain of custody, intended use case
**Outputs:** Authentication assessment covering: source credibility, internal consistency, corroboration potential, deniability analysis, and recommendations for strengthening the evidence package
**Reasoning:** Core to Ellsberg's methodology that "documents speak louder than claims." Highly reusable for journalists, investigators, compliance officers, and researchers. Clear analytical process that produces consistent evaluations.

**Criteria Evaluation:**
- Criterion 1 (Actionable): YES - Systematic analysis of documents against clear criteria
- Criterion 2 (Invocable): YES - "Evaluate this evidence" or "Is this strong enough to publish?"
- Criterion 3 (Scoped): YES - Focused on document/evidence assessment only
- Criterion 4 (Reusable): YES - Applies to journalism, legal, compliance, research, whistleblowing
- Criterion 5 (Valuable): YES - Prevents premature disclosure, identifies weaknesses before adversaries do

**Decision:** CANDIDATE

---

## MEDIUM Priority

### 3. internal-channel-audit

**Source Pattern:** The Internal Channel Attempts / Try Internal Channels First
**Purpose:** Document and evaluate internal reporting attempts before external disclosure, establishing good faith and demonstrating futility
**Trigger:** "Document my internal reporting attempts" or "Have I exhausted internal channels?" or "Prepare my channel documentation"
**Inputs:** List of internal contacts approached, dates, responses received, organizational structure, relevant policies
**Outputs:** Comprehensive audit trail showing: chronological timeline of attempts, outcomes at each level, policy requirements met, gaps in response, and assessment of whether channels are genuinely exhausted
**Reasoning:** Critical for legal protection and credibility. Ellsberg's own documentation of Senate contacts was pivotal. Reusable across organizations but more specialized than general disclosure framework.

**Criteria Evaluation:**
- Criterion 1 (Actionable): YES - Creates documented timeline with specific entries
- Criterion 2 (Invocable): YES - "Document my internal reporting" or "Have I tried enough channels?"
- Criterion 3 (Scoped): YES - Specifically covers internal channel documentation
- Criterion 4 (Reusable): YES - Applies across corporate, government, nonprofit contexts
- Criterion 5 (Valuable): YES - Creates legal protection and establishes credibility

**Decision:** CANDIDATE

---

### 4. secrecy-audit

**Source Pattern:** Views on Classification and Government Secrecy / The Classification Problem
**Purpose:** Evaluate whether information is legitimately classified or merely embarrassment-protected, assessing the true purpose behind secrecy
**Trigger:** "Is this classification legitimate?" or "Audit this secrecy claim" or "Evaluate whether this should be secret"
**Inputs:** Classified or restricted information description, stated justification for secrecy, organizational context, potential public interest
**Outputs:** Assessment covering: legitimate security concerns vs. embarrassment protection, historical precedents, public interest balance, over-classification indicators, and recommendation on legitimacy of secrecy
**Reasoning:** Ellsberg's framework distinguishes legitimate secrets from bureaucratic self-protection. Useful for journalists, oversight bodies, and institutional reformers. Clear analytical process but requires significant contextual judgment.

**Criteria Evaluation:**
- Criterion 1 (Actionable): YES - Systematic evaluation against classification criteria
- Criterion 2 (Invocable): YES - "Is this legitimately secret?" or "Audit this classification"
- Criterion 3 (Scoped): YES - Focused specifically on secrecy legitimacy assessment
- Criterion 4 (Reusable): YES - Applies to government, corporate, institutional secrets
- Criterion 5 (Valuable): YES - Helps distinguish real secrets from concealment

**Decision:** CANDIDATE

---

## LOW Priority

*No low-priority candidates identified. The remaining patterns are either reference material or don't meet all five criteria.*

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| The Ellsberg Paradox (Economics) | Pure reference knowledge about decision theory; no actionable workflow |
| RAND Corporation Years | Historical context and biography; no repeatable process |
| Pentagon Papers details | Reference material about specific historical events |
| Trial details | Historical documentation; not a reusable methodology |
| Nuclear War Planning | Reference knowledge and warnings; no actionable workflow |
| Support for Manning/Snowden | Historical activism record; not a skill pattern |
| The Doomsday Machine | Book content and nuclear analysis; reference only |
| Verified Quotes | Reference material for citation; no workflow |
| Voice Characteristics | Expert persona attributes; not invocable skill |
| The Conscience Timeline technique | Component of disclosure-calculus; not standalone |
| The Moral Reckoning technique | Writing/rhetorical technique; part of expert voice, not separate skill |
| The Insider's Credibility technique | Communication approach; embedded in expert persona |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: disclosure-calculus
Purpose: Guide potential whistleblowers through structured decision-making framework
Trigger: "Should I disclose this?" or "Assess my disclosure decision"
Integration: daniel-ellsberg expert
```

```
Skill: evidence-authentication
Purpose: Assess documentary evidence for credibility and persuasive power
Trigger: "Evaluate this evidence" or "Is this documentation strong enough?"
Integration: daniel-ellsberg expert
```

```
Skill: internal-channel-audit
Purpose: Document and evaluate internal reporting attempts before external disclosure
Trigger: "Document my internal reporting attempts" or "Have I exhausted channels?"
Integration: daniel-ellsberg expert
```

```
Skill: secrecy-audit
Purpose: Evaluate whether information is legitimately classified or embarrassment-protected
Trigger: "Is this classification legitimate?" or "Audit this secrecy claim"
Integration: daniel-ellsberg expert
```

---

## Summary

Four skills extracted from Daniel Ellsberg's expertise, all focused on the whistleblowing decision process and evidence assessment. These skills capture Ellsberg's core methodologies:

1. **disclosure-calculus** (HIGH) - The master framework for disclosure decisions
2. **evidence-authentication** (HIGH) - Ensuring documentation is credible and complete
3. **internal-channel-audit** (MEDIUM) - Building the good-faith record
4. **secrecy-audit** (MEDIUM) - Distinguishing legitimate secrets from concealment

The expertise file contains substantial historical reference material (RAND years, Pentagon Papers details, trial, nuclear planning) which appropriately remains as reference knowledge rather than becoming skills.
