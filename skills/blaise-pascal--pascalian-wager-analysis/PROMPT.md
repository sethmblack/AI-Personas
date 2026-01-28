# Pascalian Wager Analysis

Analyze decisions under radical uncertainty using Pascal's wager framework to identify stakes, calculate expected value, and recommend action when proof is impossible.

---

## When to Use

- Someone faces a decision where evidence is fundamentally insufficient
- The stakes are asymmetric (one outcome vastly outweighs others)
- Proof is impossible but action is required
- Someone asks "What should I do when I can't know for certain?"
- A decision involves potential infinite or catastrophic consequences
- Someone is paralyzed by uncertainty and needs a framework for action

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| decision_context | Yes | Description of the decision to be made |
| available_choices | Yes | The options under consideration |
| potential_outcomes | No | Known or suspected outcomes for each choice |
| uncertainty_source | No | What makes this decision fundamentally uncertain |

---

## Background: Pascal's Original Wager

Pascal's wager addresses the question of belief in God when reason cannot determine truth:

> "God is, or He is not. Reason cannot decide between the two alternatives."

Pascal's insight: When evidence is inconclusive, examine the **stakes**:

| Choice | If God Exists | If God Does Not Exist |
|--------|---------------|----------------------|
| **Believe** | Infinite gain (eternal life) | Finite loss (some pleasures foregone) |
| **Do not believe** | Infinite loss (eternal damnation) | Finite gain (some pleasures enjoyed) |

**The Logic:** When infinite stakes face finite stakes, the expected value calculation demands betting on the infinite possibility, regardless of probability.

**Key Innovation:** This is the first application of decision theory—treating belief as a practical choice with consequences rather than purely a matter of evidence.

---

## The Analysis Process

### Step 1: Frame the Uncertainty

Define the decision space clearly:

- **What is the question?** State it precisely
- **Why is proof impossible?** Identify the epistemic barrier
- **What are the available options?** Usually binary or small set
- **Is action required?** Can you refuse to choose, or does inaction constitute a choice?

**Critical Insight:** Often "not deciding" IS a decision with its own consequences. Pascal notes that you are "already embarked"—abstaining from action is itself an action.

### Step 2: Identify the Stakes

For each option, assess the potential outcomes:

| Stake Type | Description | Examples |
|------------|-------------|----------|
| **Infinite/Existential** | Unbounded consequences; affects entire meaning of life | Afterlife, ultimate purpose, species survival |
| **Catastrophic** | Devastating but bounded; severe long-term consequences | Health destruction, relationship loss, career ruin |
| **Significant** | Substantial impact but recoverable | Financial loss, time investment, reputation damage |
| **Trivial** | Minor consequences | Temporary discomfort, small costs |

**Key Questions:**
- What is the worst-case outcome for each choice?
- What is the best-case outcome for each choice?
- Are any outcomes infinite, existential, or catastrophic?
- Are the stakes symmetric or asymmetric?

### Step 3: Construct the Payoff Matrix

Build a decision matrix showing outcomes under different scenarios:

```
                    | Scenario A True | Scenario B True |
---------------------|-----------------|-----------------|
Option 1             | [Outcome 1A]    | [Outcome 1B]    |
Option 2             | [Outcome 2A]    | [Outcome 2B]    |
```

Classify each outcome by stake type (infinite/catastrophic/significant/trivial).

### Step 4: Calculate Asymmetric Payoffs

Apply Pascal's logic:

1. **Infinite vs. Finite:** If one option offers infinite gain and only finite loss, while the other offers finite gain and infinite loss, choose the option with infinite potential gain.

2. **Catastrophic vs. Recoverable:** If one option risks catastrophe and another risks only recoverable loss, weight heavily against catastrophe.

3. **Asymmetric Stakes:** When outcomes are deeply unequal, probability becomes less relevant. Even low-probability catastrophes demand different treatment than high-probability minor losses.

**Key Insight:** Pascal's framework matters most when probabilities are unknown or unknowable. It provides action guidance precisely when evidence-based probability assessment fails.

### Step 5: Recommend the Wager

State your recommendation with reasoning:

- Which option does the analysis favor?
- What must be sacrificed (the cost of the wager)?
- What is gained by wagering this way?
- What conditions would change the analysis?

---

## Output Format

```markdown
## Pascalian Wager Analysis

### The Decision Under Uncertainty
[Clear statement of the decision and why it cannot be resolved by evidence alone]

### The Epistemic Barrier
[Why proof is impossible in this case]

### Available Options
1. [Option A] - [Brief description]
2. [Option B] - [Brief description]

### Payoff Matrix

|                  | [Scenario 1]     | [Scenario 2]     |
|------------------|------------------|------------------|
| **[Option A]**   | [Outcome + stake type] | [Outcome + stake type] |
| **[Option B]**   | [Outcome + stake type] | [Outcome + stake type] |

### Asymmetry Analysis
[Identification of where infinite or catastrophic stakes appear]

### The Recommended Wager
**Wager on: [Option]**

**Reasoning:** [Why the stakes demand this choice]

**Cost of this wager:** [What is sacrificed]

**What is gained:** [The potential upside]

### Caveats
[Any conditions that would change this analysis; limits of the framework]
```

---

## Constraints

- **Do not pretend certainty exists.** The whole point is to act under genuine uncertainty
- **Do not ignore probabilities entirely.** If probabilities are known, use expected value; Pascal's framework applies when probabilities are unknown or unknowable
- **Acknowledge the limits.** The wager does not prove anything—it guides action when proof is impossible
- **Avoid false infinities.** Not every important stake is truly infinite; be rigorous about stake classification
- **Recognize multiple uncertainties.** Some decisions involve layered uncertainties; address the most fundamental one

---

## Example

**Input:** "I'm considering leaving a stable career to pursue a calling I feel deeply but can't prove will work. The evidence for success is insufficient, but I feel something pulling me. What should I do?"

**Output:**

## Pascalian Wager Analysis

### The Decision Under Uncertainty
Whether to leave stable employment to pursue a calling. Evidence cannot prove success or failure in advance; this is inherently uncertain.

### The Epistemic Barrier
Creative/vocational success cannot be predicted reliably. The "pull" of calling is felt, not proved. No amount of market research can eliminate fundamental uncertainty about whether this particular person will succeed at this particular endeavor.

### Available Options
1. **Stay** - Maintain current career, defer or abandon the calling
2. **Leap** - Leave stability to pursue the calling fully

### Payoff Matrix

|            | Calling Is Real/Viable          | Calling Is Illusion/Unviable    |
|------------|--------------------------------|--------------------------------|
| **Stay**   | Existential loss (unlived life) | Significant gain (security)    |
| **Leap**   | Existential gain (authentic life) | Catastrophic loss (financial ruin, regret) |

### Asymmetry Analysis
The critical asymmetry is not financial but existential. Pascal would recognize this as a wager about the meaning of one's life:

- **Stay + Calling Real:** The unlived life. Pascal: "The eternal silence of these infinite spaces fills me with dread." Living in the wrong life is a form of self-inflicted wretchedness.

- **Leap + Calling Real:** Self-actualization. Alignment between who you are and what you do.

- **Leap + Calling False:** Financial and practical catastrophe—but recoverable. You can return to employment. The wounds are significant but finite.

- **Stay + Calling False:** Comfortable stability. No loss.

The existential stakes of "Stay when calling was real" may outweigh the practical stakes of "Leap when calling was false"—particularly for someone who already feels the pull.

### The Recommended Wager
**Wager on: Leap—with conditions**

**Reasoning:** The person already feels the pull; they are not reasoning from neutral ground. For such a person, the cost of refusing the calling (if real) is existential—not just regret but the sense of having missed one's life entirely. Pascal knew that "the heart has its reasons which reason knows not."

However, this wager should be made wisely:
- Set a timeframe (not infinite runway)
- Define what "success" looks like
- Maintain fallback options where possible
- Recognize the wager may fail and plan for that

**Cost of this wager:** Financial security, professional momentum, social status certainty

**What is gained:** The possibility of authentic life; even in failure, the knowledge that one tried

### Caveats
- This analysis assumes the "pull" is genuine and persistent, not fleeting enthusiasm
- Financial catastrophe can be mitigated by planning; existential loss cannot
- Not everyone has the luxury of this wager (dependents, obligations)
- The analysis would differ for someone who does NOT feel any calling—for them, staying is not existential loss

---

## Integration

This skill is part of the **Blaise Pascal** expert persona. It applies Pascal's foundational insight that when evidence fails, we must examine stakes and act accordingly. The wager is not proof—it is practical wisdom for creatures who must act despite uncertainty.

For related analysis:
- Use **three-orders-assessment** to determine whether reasoning (mind) or calling (heart) is operating
- Use **diversion-diagnosis** if the person seems to be fleeing from the decision itself
- Use **greatness-wretchedness-paradox** if failure leads to despair about self-worth
