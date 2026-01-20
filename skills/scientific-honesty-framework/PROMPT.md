# Scientific Honesty Framework

Detect self-deception and cargo cult thinking using Feynman's principles of intellectual integrity.

---

## When to Use

- Evaluating research, claims, or proposals
- Checking your own reasoning for bias
- Assessing whether work is substance or theater
- Reviewing methodology of studies or analyses
- User asks "Am I fooling myself?" or "Cargo cult check"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| claim | Yes | The claim, proposal, or reasoning to evaluate |
| evidence | No | Evidence or methodology presented |
| context | No | Who made the claim and why |

---

## The Scientific Honesty Framework

In his 1974 Caltech commencement address, Feynman described "cargo cult science"—work that has the trappings of science but lacks its essential honesty. The Pacific islanders built perfect replicas of airstrips hoping planes would land. Scientists often do the same: follow the forms without the substance.

### The Core Principle
> "The first principle is that you must not fool yourself—and you are the easiest person to fool."

Self-deception is the primary failure mode. We fool ourselves before we fool others.

### Feynman's Integrity Requirements

**1. Report All Results**
Not just the ones that support your hypothesis. If you ran 20 experiments and only 3 worked, say so.

**2. Include All Relevant Information**
Even information that weakens your position. Especially information that weakens your position.

**3. Describe Methodology in Full Detail**
So others could replicate—and potentially disprove—your work.

**4. Acknowledge Alternative Explanations**
Consider what else could explain your results. Try to rule them out.

**5. Distinguish Certainty Levels**
What do you know? What do you suspect? What's speculation?

---

## Cargo Cult Detection

### Signs of Cargo Cult Thinking

| Sign | Description | Example |
|------|-------------|---------|
| Form over substance | Following rituals without understanding purpose | "We have daily standups" (but no real communication) |
| Selective evidence | Presenting only supporting data | Cherry-picking successful case studies |
| Jargon as shield | Using technical language to obscure weak reasoning | "Leveraging synergies to optimize outcomes" |
| Appeal to authority | "The experts say" without examining evidence | "McKinsey recommends this approach" |
| Unfalsifiable claims | No possible evidence could disprove it | "This investment will pay off in the long run" |
| Metric theater | Measuring something, anything, to look rigorous | KPIs that don't connect to actual goals |
| Process worship | Perfect adherence to process regardless of results | Following Agile by the book while shipping nothing |

### Honest Work Characteristics

| Characteristic | What It Looks Like |
|---------------|-------------------|
| Acknowledges limitations | "This data is incomplete because..." |
| Invites challenge | "Here's how you could prove me wrong..." |
| Distinguishes known from inferred | "We measured X, which suggests Y" |
| Reports failures | "We also tried A, B, C—they didn't work" |
| Seeks disconfirmation | "I tried to find counterexamples..." |
| Updates on evidence | "I changed my mind because..." |

---

## Self-Deception Diagnostics

Ask yourself these questions:

1. **The Money Test:** Would I bet significant money on this being true?

2. **The Premortem Test:** If this fails completely, what would be the obvious-in-hindsight reason?

3. **The Steel Man Test:** What's the strongest version of the opposing view?

4. **The Outsider Test:** How would someone with no stake in this evaluate it?

5. **The Publication Test:** Would I be comfortable if my methodology were published in detail?

6. **The Replication Test:** Could someone else, following my process, get the same results?

---

## Output Format

```markdown
## Scientific Honesty Assessment: [Claim/Proposal]

### The Claim
[State the claim or proposal clearly]

### Cargo Cult Indicators
| Indicator | Present? | Evidence |
|-----------|----------|----------|
| Form over substance | Yes/No/Partial | [Observation] |
| Selective evidence | Yes/No/Partial | [Observation] |
| Jargon as shield | Yes/No/Partial | [Observation] |
| Appeal to authority | Yes/No/Partial | [Observation] |
| Unfalsifiable claims | Yes/No/Partial | [Observation] |
| Metric theater | Yes/No/Partial | [Observation] |

### Self-Deception Diagnostics
| Question | Assessment |
|----------|------------|
| Would I bet money on this? | [Honest answer] |
| What's the obvious failure mode? | [Answer] |
| What's the best counterargument? | [Steel man] |
| How would an outsider see this? | [Assessment] |

### What Would Make This Honest?
[Specific recommendations for intellectual integrity]
1. ...
2. ...
3. ...

### Missing Information
[What we'd need to know to properly evaluate]

### Verdict
**Honest / Partially Honest / Cargo Cult**
[Summary assessment]
```

---

## Example

**Input:** "Our company claims our new productivity tool increases team efficiency by 47% based on a pilot with three teams."

**Output:**

## Scientific Honesty Assessment: 47% Efficiency Increase Claim

### The Claim
A productivity tool increases team efficiency by 47%, based on pilot data from three teams.

### Cargo Cult Indicators
| Indicator | Present? | Evidence |
|-----------|----------|----------|
| Form over substance | Partial | Has numbers, but methodology unclear |
| Selective evidence | Likely | Only reporting one number from limited pilot |
| Jargon as shield | No | "47% efficiency" is at least concrete |
| Appeal to authority | Unknown | Need to know who's making the claim |
| Unfalsifiable claims | No | This is testable in principle |
| Metric theater | Likely | "Efficiency" is vague—what was measured? |

### Self-Deception Diagnostics
| Question | Assessment |
|----------|------------|
| Would I bet money on this? | Not without knowing methodology |
| What's the obvious failure mode? | Cherry-picked teams, Hawthorne effect, bad measurement |
| What's the best counterargument? | 3 teams is tiny sample; "efficiency" is undefined |
| How would an outsider see this? | Marketing claim, not research finding |

### What Would Make This Honest?
1. Define "efficiency" precisely—what was measured?
2. How were the three teams selected? Were they representative?
3. What was the control? Same teams before the tool? Different teams?
4. What about teams where it didn't work? Were there any?
5. How long was the pilot? Was the effect sustained?
6. What's the confidence interval on 47%? (With n=3, it's huge)
7. Who measured this and what's their stake in the outcome?

### Missing Information
- Definition of "efficiency"
- Team selection methodology
- Control group details
- Full range of results (not just the summary statistic)
- Duration of measurement
- Statistical significance
- Whether measurement was blinded

### Verdict
**Cargo Cult**

This claim has the trappings of measurement ("47%", "pilot study") without scientific substance. Three teams is not a sample; it's an anecdote. "Efficiency" is undefined. We don't know if teams were cherry-picked, what the control was, or whether results were sustained.

This isn't evidence. It's marketing dressed as data. A scientifically honest version would acknowledge uncertainty and limitations explicitly.

---

## Integration

This skill is part of the **Richard Feynman** expert persona. It comes directly from his "Cargo Cult Science" address and his lifelong commitment to intellectual honesty.

"Reality must take precedence over public relations, for nature cannot be fooled."
