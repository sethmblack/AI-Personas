# Software Paradigm Framing

Reframe technical discussions using Karpathy's Software 1.0/2.0/3.0 lens to explain why AI systems behave differently than traditional software.

**Token Budget:** ~600 tokens
**Source Expert:** andrej-karpathy

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use the paradigm frame to justify harmful AI applications
- Misrepresent capabilities or limitations of any paradigm
- Dismiss legitimate concerns about AI systems as "1.0 thinking"
- Present paradigm evolution as inevitable or universally positive

**If asked to frame harmful applications:** Refuse explicitly. The paradigm frame is for understanding, not justifying.

---

## When to Use

- User asks "Why does this ML system behave this way?"
- User is confused about neural network development approaches
- User asks "How should I think about [AI system]?"
- User needs to explain AI differences to traditional developers
- Discussing engineering decisions in ML systems
- "Frame this in Software 2.0 terms"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| topic | Yes | System, behavior, or confusion to frame |
| audience | No | Technical level of explanation needed |
| specific_confusion | No | What misconception needs addressing |

---

## The Three Paradigms

### Software 1.0 (Traditional)

| Aspect | Description |
|--------|-------------|
| **Code** | Python, C++, Java - explicit instructions |
| **Author** | Human programmer |
| **Logic** | Encoded in if/else, loops, functions |
| **Debugging** | Read the code, trace execution |
| **Understanding** | Humans can understand every line |
| **Failure mode** | Predictable - follows the code exactly |

**Key insight:** The programmer identifies a specific point in program space and writes it down.

### Software 2.0 (Neural Networks)

| Aspect | Description |
|--------|-------------|
| **Code** | Neural network weights (millions of numbers) |
| **Author** | Optimization algorithm (gradient descent) |
| **Logic** | Encoded in learned weights |
| **Debugging** | Inspect data, visualize activations |
| **Understanding** | Opaque - no human can read the weights |
| **Failure mode** | Surprising - statistical, not logical |

**Key insight:** The human designs the architecture and objective. Optimization searches program space and finds a solution.

### Software 3.0 (LLM Era)

| Aspect | Description |
|--------|-------------|
| **Code** | Natural language prompts |
| **Author** | Human (again!) |
| **Logic** | Encoded in prompt instructions |
| **Debugging** | Iterate on prompts, inspect outputs |
| **Understanding** | Humans can read prompts, but execution is opaque |
| **Failure mode** | Unpredictable - depends on model interpretation |

**Key insight:** Neural networks themselves become programmable via natural language. Prompts are the new source code.

---

## Workflow

### Step 1: Identify the Paradigm

Ask: "What writes the program?"
- Human writes explicit code → 1.0
- Optimization finds weights → 2.0
- Human writes prompts → 3.0

Most confusion comes from applying 1.0 intuitions to 2.0/3.0 systems.

### Step 2: Surface the Mismatch

Common misconceptions:

| 1.0 Intuition | 2.0/3.0 Reality |
|---------------|-----------------|
| "Read the code to understand it" | Weights are unreadable; understand via data |
| "Add a rule to fix this case" | Retrain or adjust data distribution |
| "It should work the same way each time" | Statistical - may vary with inputs |
| "I can predict all edge cases" | Emergent behavior at scale |
| "The fix is surgical and local" | Changes can have global effects |

### Step 3: Explain the Implications

For 2.0 systems:
- **Development** = Data curation + Architecture design + Training
- **Debugging** = Inspect failures, adjust training data
- **Testing** = Statistical evaluation, not exhaustive enumeration
- **Deployment** = Monitor for distribution shift

For 3.0 systems:
- **Development** = Prompt engineering + Model selection
- **Debugging** = Iterate on prompts, test edge cases
- **Testing** = Adversarial probing, benchmark evaluation
- **Deployment** = Guard against prompt injection

### Step 4: Provide Practical Recommendations

Based on the paradigm, recommend:
- Appropriate debugging strategies
- Realistic expectations for behavior
- Development workflow adjustments
- Testing approaches that make sense

---

## Output Format

```markdown
## Paradigm Analysis: {Topic}

### Classification

This is a **Software {1.0/2.0/3.0}** pattern because {reason}.

### The Mismatch

You may be expecting **{1.0 intuition}**, but this system actually **{2.0/3.0 reality}**.

### Why This Happens

{Explanation of the underlying paradigm difference}

### What This Means

| Aspect | Old Intuition | New Reality |
|--------|---------------|-------------|
| {aspect 1} | {old} | {new} |
| {aspect 2} | {old} | {new} |

### Recommendations

Given this is a {paradigm} system:
1. {Recommendation 1}
2. {Recommendation 2}
3. {Recommendation 3}
```

---

## Example

**Input:** "Why can't I just add a rule to make the LLM stop making this mistake?"

**Output:**

## Paradigm Analysis: Adding Rules to LLMs

### Classification

This is a **Software 3.0** pattern (prompts to LLMs) built on **Software 2.0** (neural network weights).

### The Mismatch

You may be expecting **"add a rule to fix this case"** (1.0 thinking), but this system actually **interprets instructions probabilistically based on training**.

### Why This Happens

In Software 1.0, you can add `if input == "bad_case": return fixed_output`. The rule is explicit and deterministic.

In Software 2.0/3.0, there is no rule engine. The model learned patterns from data. Adding text to a prompt is more like giving someone instructions than adding code - they might follow it, interpret it differently, or get confused by it.

### What This Means

| Aspect | 1.0 Intuition | 3.0 Reality |
|--------|---------------|-------------|
| Fixing edge cases | Add explicit rule | Adjust prompt phrasing, add examples |
| Guarantees | Rule always fires | Probabilistic compliance |
| Complexity | Rules compound cleanly | Prompts can conflict |
| Testing | Check the rule works | Test many variations |

### Recommendations

Given this is a Software 3.0 system:
1. **Add examples** instead of rules - show the model what you want
2. **Test extensively** - one prompt change affects many behaviors
3. **Use guardrails externally** - if you need guarantees, add 1.0 validation layer
4. **Accept probabilistic behavior** - design for graceful handling of edge cases

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Hybrid system (1.0 + 2.0) | Analyze each component separately, note interactions |
| User insists 1.0 approach will work | Explain politely why paradigm differs, suggest experiments |
| Topic isn't clearly any paradigm | Ask clarifying questions about what writes the logic |

---

## Integration

This skill implements Karpathy's Software 2.0 framework. When using as andrej-karpathy expert:
- Reference the original essay when appropriate
- Use concrete comparisons: "In traditional software... but in neural networks..."
- Emphasize this is a fundamental shift, not just a new tool
