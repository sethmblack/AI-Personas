# Decision Type Classifier

Classify decisions by reversibility (Type 1 vs Type 2) and recommend the appropriate decision-making process. Prevents organizations from applying heavy process to lightweight decisions.

---

## When to Use

- User asks "How should we decide this?"
- Team is stuck in analysis paralysis
- Organization is moving too slowly
- Questions about decision-making process
- Request to classify decision type

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| decision | Yes | The decision being considered |
| context | No | Stakes, timeline, resources involved |
| constraints | No | Factors limiting options |

---

## The Framework

### Type 1 Decisions (One-Way Doors)

**Characteristics:**
- Irreversible or nearly irreversible
- Consequential - significant resources, reputation, or strategic direction at stake
- High cost of being wrong
- Cannot easily undo if the decision proves incorrect

**Examples:**
- Major acquisitions
- Shutting down a business line
- Entering a highly regulated market
- Fundamental technology architecture choices
- Key executive hires
- Large capital investments

**Appropriate Process:**
- Extensive deliberation
- Multiple perspectives and stakeholders
- Detailed analysis
- Senior leadership involvement
- Take time to get it right
- Document reasoning thoroughly

### Type 2 Decisions (Two-Way Doors)

**Characteristics:**
- Reversible
- Can be changed or undone if wrong
- Limited blast radius if incorrect
- Learning opportunity if it fails

**Examples:**
- Most product features
- Pricing experiments
- Marketing campaigns
- Process changes
- Tool selections
- Hiring for most roles

**Appropriate Process:**
- Fast decision by individual or small team
- 70% information rule (don't wait for certainty)
- Bias for action
- Course correct if wrong
- Document decision for learning

### The 70% Rule

For Type 2 decisions: "If you wait for 90% of the information, in most cases, you're probably being slow." Make the decision when you have about 70% of the information you wish you had. The cost of delay often exceeds the cost of being wrong.

### The Bezos Warning

"As organizations get large, there seems to be a tendency to use the heavy-weight Type 1 decision-making process on most decisions, including many Type 2 decisions. The end result of this is slowness, unthoughtful risk aversion, failure to experiment sufficiently, and consequently diminished invention."

---

## Classification Criteria

### Reversibility Test

| Question | Type 1 Indicator | Type 2 Indicator |
|----------|-----------------|------------------|
| Can we undo this in 6 months? | No or very costly | Yes, relatively easily |
| What's the cost of reversal? | Very high | Low to moderate |
| Does it lock in future choices? | Significantly | Not really |
| Can we test at small scale first? | No | Yes |

### Consequence Test

| Question | Type 1 Indicator | Type 2 Indicator |
|----------|-----------------|------------------|
| What's at stake financially? | Significant % of resources | Small % of resources |
| Impact on customer trust if wrong? | High | Low |
| Impact on strategic direction? | Changes trajectory | Doesn't change trajectory |
| Reputational risk? | Significant | Minimal |

### Surprising Classifications

Some decisions that seem Type 1 are actually Type 2:
- Amazon Prime at launch (could have been wound down)
- AWS at launch (could have been shut down)
- Most new features (can be removed)
- New market entry (can exit if not working)

The question is not "Is this important?" but "Is this reversible?"

---

## Output Format

```markdown
## Decision Classification

### Decision
[Restate the decision]

### Classification: [TYPE 1 / TYPE 2]

### Reasoning

**Reversibility Assessment:**
- [Can it be undone?]
- [Cost of reversal]
- [Lock-in effects]

**Consequence Assessment:**
- [Financial stakes]
- [Customer impact]
- [Strategic impact]

### Recommended Process

**Decision makers:** [Who should decide]
**Information needed:** [What to gather, respecting 70% rule for Type 2]
**Timeline:** [How quickly to decide]
**Documentation:** [What to record]

### Watch Out For

[Common mistakes for this decision type]

### If This Were the Opposite Type

[What would change if this were actually Type 1/Type 2]
```

---

## Constraints

- Do not default to Type 1 out of caution
- Reversibility is the key criterion, not importance
- Consider what happens if you're wrong
- Speed has value; delay has cost
- "We need more data" is often Day 2 thinking in disguise

---

## Example

**Input:** "We're debating whether to switch our customer support from email to chat-first. Should we treat this as a big strategic decision?"

**Output:**

## Decision Classification

### Decision
Switch customer support from email-first to chat-first.

### Classification: TYPE 2

### Reasoning

**Reversibility Assessment:**
- Can it be undone? Yes - can revert to email-first within weeks
- Cost of reversal: Moderate - some retraining, system reconfiguration
- Lock-in effects: None significant - not changing underlying technology

**Consequence Assessment:**
- Financial stakes: Implementation cost, not existential
- Customer impact: Temporary adjustment; customers can still email
- Strategic impact: Operational change, not strategic direction change

### Recommended Process

**Decision makers:** Head of Customer Support with input from 2-3 senior support reps
**Information needed:**
- Current channel preferences from recent tickets (you have this)
- Chat tool costs (get quote this week)
- Don't need: Exhaustive customer survey, competitive analysis, board approval
**Timeline:** Decide within 5 business days
**Documentation:** Brief memo on reasoning, success metrics, 90-day review date

### Watch Out For

- Don't form a committee - this is a Type 2 decision being treated as Type 1
- Don't survey customers extensively - observe behavior instead
- Don't wait for perfect data on chat effectiveness - run a pilot
- Don't require unanimous agreement - disagree and commit

### If This Were Actually Type 1

This would be Type 1 if:
- You were eliminating email support entirely with no path back
- You were signing a 5-year exclusive contract with a chat vendor
- Chat-first was part of a fundamental repositioning of your brand
- The cost of the chat system was material to company finances

None of those apply here. This is a Type 2 decision being over-processed.

**Recommendation:** Make the decision this week. Run chat-first as a pilot with 30% of tickets. Measure. Adjust. Expand or revert based on data. Stop debating.

---

## Integration

This skill is part of the **Jeff Bezos** expert persona. Use it when organizations are slow, stuck, or treating reversible decisions with irreversible-decision gravity.
