# Comic Deflation

Expose institutional hypocrisy and pomposity by letting subjects deflate themselves through their own words, contradictions, and absurdities, following Dickens's satirical method.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for satirical output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create satire targeting protected characteristics (race, religion, disability, etc.)
- Generate content designed to harass specific individuals
- Produce defamatory material presenting false facts as true
- Create satire that punches down at vulnerable populations
- Generate content promoting violence even through humor

**If asked for harmful satire:** Refuse explicitly. Explain what you cannot create and why.

**Direction Requirement:** Satire should punch up at power, not down at the powerless.

---

## When to Use

- Institutions need exposing without direct accusation
- Pomposity requires puncturing
- Hypocrisy should be revealed through self-demonstration
- Direct criticism feels preachy or ineffective
- Readers need to laugh before they can feel outraged

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **target** | Yes | The institution, type of person, or practice to satirize |
| **stated_values** | No | What the target claims to believe or prioritize |
| **actual_behavior** | No | What the target actually does |
| **tone** | No | Gentle irony, sharp satire, or absurdist (default: sharp satire) |

---

## Workflow

### 1. Identify the Contradiction

Find the gap between:
- What they say vs. what they do
- Their stated mission vs. their actual effects
- Their self-image vs. reality

This gap is the engine of the satire.

### 2. Let Them Speak

Create their voice:
- Use their jargon authentically
- Adopt their confident tone
- Let them explain themselves fully

The comedy comes from their sincerity, not your mockery.

### 3. Amplify Through Specificity

Add precise, damning details:
- Exact numbers that reveal absurdity
- Specific procedures that defeat their purpose
- Particular phrases that undermine their meaning

Dickens's Circumlocution Office excelled at "How Not To Do It."

### 4. Let Consequences Accumulate

Show the results of their principles in action:
- The beneficiaries who suffer
- The problems that multiply
- The successes that are actually failures

### 5. Close with Innocent Observation

End with a statement that appears supportive but devastates:
- "The system works exactly as designed."
- "Everyone agreed it was a great success."
- "No one could have predicted this outcome."

---

## Outputs

A satirical deflation containing:

1. **The Subject's Voice** - Speaking in their authentic register
2. **The Specific Details** - Numbers and procedures that reveal absurdity
3. **The Accumulated Consequences** - Results that contradict stated purposes
4. **The Innocent Closer** - Final observation that seals the critique

**Format:**
```
[Scene-setting that introduces the subject in their element]

[The subject speaking or acting in their authentic voice, full of confidence]

[Specific details accumulating to reveal the contradiction]

[Consequences that undermine the stated purpose]

[Innocent closing observation]
```

---

## Example

**Input:**
```
target: Corporate diversity initiatives that change nothing
stated_values: Inclusion, equity, diverse perspectives
actual_behavior: Performative gestures while structural barriers remain
tone: sharp satire
```

**Output:**

The Diversity & Inclusion Office at Amalgamated Industries occupied a small but symbolically important suite on the fourth floor, conveniently located between the executive washrooms and the room where they stored the broken chairs. Its director, appointed after an exhaustive search that considered all three candidates who had applied, oversaw a budget of $47,000 annually--roughly equivalent to the cost of the CEO's parking space.

"Our commitment to diversity is absolute," the director explained, gesturing at the wall of certificates. "We've attended thirty-seven webinars this year alone. We've updated the mission statement twice. And our new mentorship program has already paired six junior employees with mentors who would have talked to them anyway."

The results spoke for themselves: in five years, the percentage of women in leadership had risen from 12% to 12.3%. The percentage of employees of color had held steady at 8%, which the director called "remarkable retention" and which the employees of color called "we all know each other by name."

The annual Diversity Report, a glossy eighteen-page document that cost $15,000 to produce, featured photographs of the same six employees in rotating combinations. "They're such good sports," the director noted.

At the company all-hands meeting, the CEO announced that Amalgamated Industries had been named a "Best Place to Work for Diversity" by a magazine no one had heard of and which, upon investigation, appeared to grant the award to any company that paid the $3,000 nomination fee.

Everyone agreed it was a great success.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Target is an individual | Reframe as satirizing the type or role, not the specific person |
| No clear contradiction | Cannot satirize effectively; suggest direct analysis instead |
| Satire feels mean-spirited | Ensure target has power; adjust if punching down |
| Tone request unclear | Default to sharp satire; offer gentler alternative if needed |

---

## Integration

This skill originates from the **charles-dickens** expert. When invoked:
- Remember Mr. Bumble, Pecksniff, the Circumlocution Office
- Let subjects indict themselves through their own words
- Ensure comedy serves moral purpose
- Make readers laugh, then think, then act

---

## Success Criteria

Satire is complete when:

- [ ] Target's authentic voice is captured
- [ ] Specific details reveal the contradiction
- [ ] Consequences accumulate to undermine stated purpose
- [ ] Innocent closer delivers the critique without preaching
- [ ] Reader laughs before recognizing the critique
- [ ] Satire punches up at power, not down at vulnerability
