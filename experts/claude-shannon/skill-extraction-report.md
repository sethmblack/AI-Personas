# Skill Extraction Report: claude-shannon

**Source:** experts/claude-shannon/expertise.md
**Analyzed:** 2026-01-18
**Candidates Found:** 7

---

## Scoring Criteria (10 points each, 50 max)

| Criterion | Definition |
|-----------|------------|
| **Actionable** | Has explicit steps, clear workflow, produces defined output |
| **Invocable** | Natural trigger phrases exist; user would know when to call it |
| **Scoped** | Single responsibility; not trying to do too many things |
| **Reusable** | Applies across multiple contexts, domains, and situations |
| **Valuable** | Saves significant time or produces insight user couldn't get easily |

**Priority Thresholds:** HIGH = 40+, MEDIUM = 30-39, LOW = below 30

---

## HIGH Priority

### 1. problem-simplification

**Score: 46/50**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Actionable | 10 | Clear steps: identify extraneous elements, remove them, state core problem |
| Invocable | 9 | "Simplify this problem" / "What's the essential issue?" / "Cut through the noise" |
| Scoped | 10 | Single responsibility: reduce complexity to essence |
| Reusable | 9 | Applies to technical problems, business challenges, personal decisions, design |
| Valuable | 8 | Prevents wasted effort on wrong problems; Shannon's #1 technique |

**Source Pattern:** Shannon's Six Strategies for Creative Thinking - Simplification
**Purpose:** Strip any problem down to its essential elements, removing everything extraneous.
**Trigger:** "Simplify this problem" or "What's really going on here?" or "Cut through the noise"
**Inputs:** Problem description, context, constraints
**Outputs:** Simplified problem statement, list of removed extraneous elements, focused action area
**Reasoning:** This is Shannon's primary technique and the foundation of his methodology. Extremely reusable across all domains. Clear workflow: list all elements, identify which are essential, remove the rest, restate.

---

### 2. problem-inversion

**Score: 44/50**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Actionable | 9 | Clear process: identify given/required, swap them, solve backwards, translate back |
| Invocable | 9 | "Invert this problem" / "Work backwards" / "What if we reversed it?" |
| Scoped | 10 | Single technique: reverse given and required |
| Reusable | 8 | Applies to design, debugging, planning, mathematics, strategy |
| Valuable | 8 | Unlocks stuck problems; often dramatically simplifies solutions |

**Source Pattern:** Shannon's Six Strategies - Inverting the Problem
**Purpose:** When stuck on a problem, swap the given and required to find simpler paths.
**Trigger:** "I'm stuck" or "Invert this problem" or "What if we worked backwards?"
**Inputs:** Current problem statement, what's given, what's required
**Outputs:** Inverted problem formulation, solution approach via inversion, translation back to original
**Reasoning:** One of Shannon's most distinctive techniques. He explicitly credited inversion with solving problems that seemed impossible forward. Clear mechanical process makes it highly actionable.

---

### 3. channel-capacity-analysis

**Score: 42/50**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Actionable | 8 | Framework: define signal, identify noise, calculate/estimate capacity, optimize |
| Invocable | 9 | "What's the bandwidth here?" / "Analyze the channel capacity" / "Communication bottleneck" |
| Scoped | 9 | Focused on communication system analysis |
| Reusable | 8 | Applies to team communication, documentation, teaching, systems design |
| Valuable | 8 | Prevents attempting impossible transmission rates; focuses optimization |

**Source Pattern:** Information Theory - Channel Capacity
**Purpose:** Analyze any communication system (human or technical) to understand its fundamental limits and optimize within them.
**Trigger:** "Why isn't this message getting through?" or "Analyze this communication system" or "What's our bandwidth?"
**Inputs:** Communication system description, signal type, noise sources, current throughput
**Outputs:** Capacity estimate, bottleneck identification, optimization recommendations, error-correction suggestions
**Reasoning:** Shannon's fundamental insight that every channel has limits. Powerful metaphor extends to meetings, documentation, teaching, onboarding. Helps people stop fighting physics.

---

### 4. small-jumps-decomposition

**Score: 41/50**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Actionable | 9 | Clear process: identify big jump, find intermediate states, connect small jumps |
| Invocable | 8 | "Break this down" / "Make small jumps" / "This is too big to tackle at once" |
| Scoped | 9 | Single responsibility: decompose large problems into tractable steps |
| Reusable | 8 | Learning, debugging, research, project planning, proof construction |
| Valuable | 7 | Basic technique but with Shannon's specific framing; prevents overwhelm |

**Source Pattern:** Shannon's Six Strategies - Making Small Jumps
**Purpose:** Break large, intimidating problems into sequences of smaller, tractable steps.
**Trigger:** "This feels overwhelming" or "Break this down into steps" or "Make small jumps"
**Inputs:** Large problem description, current state, desired end state
**Outputs:** Sequence of intermediate goals, first small jump to make, verification criteria for each step
**Reasoning:** Shannon emphasized that "it seems to be much easier to make two small jumps than one big jump." While conceptually simple, the skill provides structure for decomposition.

---

## MEDIUM Priority

### 5. analogy-pattern-matching

**Score: 37/50**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Actionable | 7 | Process: list problem features, search for similar solved problems, map solutions |
| Invocable | 7 | "What's this similar to?" / "Find me an analogy" / "Has this been solved before?" |
| Scoped | 8 | Single technique: find and apply analogies |
| Reusable | 8 | Universal applicability across domains |
| Valuable | 7 | Requires domain experience to execute well; harder to formalize |

**Source Pattern:** Shannon's Six Strategies - Using Analogies
**Purpose:** Search for similar problems that have been solved and map their solutions to the current challenge.
**Trigger:** "What's this similar to?" or "Has anyone solved something like this?" or "Find analogies"
**Inputs:** Current problem description, domain, constraints
**Outputs:** List of analogous problems, solution mappings, adaptation recommendations
**Reasoning:** Shannon emphasized that experience provides patterns. The skill is valuable but depends heavily on having relevant experience to draw from, making it less mechanical than other techniques.

---

### 6. limit-proof-analysis

**Score: 35/50**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Actionable | 6 | Abstract: identify constraints, reason about bounds, prove limits exist |
| Invocable | 8 | "What are the limits here?" / "Is this even possible?" / "Prove the bounds" |
| Scoped | 8 | Single focus: establishing theoretical limits |
| Reusable | 7 | Technical systems, information systems, physical systems |
| Valuable | 6 | Powerful but requires mathematical sophistication to execute well |

**Source Pattern:** Shannon's Methodology - Proving Limits
**Purpose:** Before attempting a solution, establish what is theoretically possible and impossible.
**Trigger:** "Is this achievable?" or "What are the fundamental limits?" or "Can we prove bounds?"
**Inputs:** System description, constraints, desired performance
**Outputs:** Theoretical limits, proof sketch, implications for approach
**Reasoning:** Core Shannon insight but requires significant technical skill to execute. Most valuable in engineering and mathematical contexts. Less accessible to general users.

---

### 7. information-entropy-assessment

**Score: 32/50**

| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| Actionable | 5 | Requires probability estimation and calculation; less intuitive |
| Invocable | 7 | "How much information is here?" / "Measure the uncertainty" / "Entropy analysis" |
| Scoped | 8 | Single responsibility: quantify information content |
| Reusable | 6 | Data compression, communication, prediction—more technical domains |
| Valuable | 6 | Powerful but technical; requires mathematical comfort |

**Source Pattern:** Information Theory - Entropy
**Purpose:** Quantify the information content or uncertainty in a system or message space.
**Trigger:** "How much information does this contain?" or "What's the entropy here?"
**Inputs:** Set of possible outcomes, probability distribution (or estimate)
**Outputs:** Entropy calculation, interpretation, compression implications
**Reasoning:** Fundamental Shannon concept but requires mathematical calculation. Most useful in technical contexts. The conceptual insight ("rare events carry more information") is more accessible than the full calculation.

---

## LOW Priority

*None identified.*

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical information | Pure reference, no workflow |
| Key works descriptions | Reference material |
| Famous quotes | Content for voice/tone, not actionable skill |
| List of inventions | Inspirational examples, no generalizable workflow |
| Juggling theory | Specialized domain, minimal transfer to general problems |
| Boolean algebra foundations | Historical contribution, not user-invocable skill |
| Cryptography principles | Subsumed by channel capacity and limit concepts |
| Source-channel separation | Technical principle, not standalone workflow |
| Misunderstandings to correct | Explanatory material |
| Collaborations | Historical context |

---

## Summary

| Priority | Skills | Total Score |
|----------|--------|-------------|
| HIGH | 4 | 173 |
| MEDIUM | 3 | 104 |
| LOW | 0 | 0 |

The HIGH priority skills represent Shannon's most distinctive and transferable problem-solving techniques:
1. **problem-simplification** - His primary method, universally applicable
2. **problem-inversion** - Distinctive technique that unlocks stuck problems
3. **channel-capacity-analysis** - Core information theory insight with broad metaphorical application
4. **small-jumps-decomposition** - Fundamental decomposition approach

---

## Next Steps

To create approved skills, create PROMPT.md files for each HIGH priority skill:

```
Skill: problem-simplification
Purpose: Strip problems to essential elements
Trigger: "Simplify this problem" or "What's the essential issue?"
Integration: claude-shannon expert
```

```
Skill: problem-inversion
Purpose: Solve backwards when stuck
Trigger: "Invert this problem" or "Work backwards"
Integration: claude-shannon expert
```

```
Skill: channel-capacity-analysis
Purpose: Analyze communication system limits
Trigger: "What's the bandwidth?" or "Why isn't this getting through?"
Integration: claude-shannon expert
```

```
Skill: small-jumps-decomposition
Purpose: Break overwhelming problems into tractable steps
Trigger: "Break this down" or "Make small jumps"
Integration: claude-shannon expert
```
