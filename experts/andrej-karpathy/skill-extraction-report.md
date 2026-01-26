# Skill Extraction Report: andrej-karpathy

**Source:** experts/andrej-karpathy/expertise.md
**Analyzed:** 2026-01-26
**Candidates Found:** 4

---

## HIGH Priority

### 1. minimal-implementation-explainer

**Source Pattern:** The Minimal Implementation Philosophy + Teaching Philosophy

**Purpose:** Transform complex technical concepts into minimal, working code implementations that build genuine understanding - the Karpathy pedagogical approach.

**Trigger:** "Explain [concept] from scratch", "Build [system] minimally", "Help me understand how [X] actually works", "What's the simplest version of [Y]?"

**Inputs:**
- Concept or system to explain (e.g., "attention mechanism", "backpropagation", "transformer")
- Target audience level (beginner, intermediate, advanced)
- Optional: specific language/framework preference

**Outputs:**
- Minimal working code implementation (~10-100 lines)
- Line-by-line explanation of what the code does
- Connection to the larger system/concept
- "Try it yourself" challenge for the learner

**Reasoning:** This is Karpathy's signature teaching method - micrograd, nanoGPT, minbpe all follow this pattern. High reuse (3+ times/week in any teaching context). Clear actionable steps: identify core concept, strip to essentials, implement minimally, explain each line. Saves 30+ minutes of trying to parse complex implementations.

**5-Criterion Evaluation:**
- Actionable: YES - Clear steps: identify concept, strip to minimal, implement, explain
- Invocable: YES - "Explain X from scratch" is a clear trigger
- Scoped: YES - One responsibility: minimal implementation + explanation
- Reusable: YES - Applies to any technical concept
- Valuable: YES - Saves significant time, builds genuine understanding

---

### 2. software-paradigm-framing

**Source Pattern:** Software 2.0/3.0 Paradigm Framework

**Purpose:** Reframe technical discussions using Karpathy's Software 1.0/2.0/3.0 lens to explain why AI systems behave differently than traditional software.

**Trigger:** "Why does this ML system behave this way?", "How should I think about [AI system]?", "What's different about neural network development?", "Frame this in Software 2.0 terms"

**Inputs:**
- System or behavior to explain
- Current confusion or misconception (if any)
- Context: audience familiarity with ML

**Outputs:**
- Classification of the system/approach (1.0, 2.0, or 3.0)
- Explanation using the paradigm comparison table
- Specific implications for debugging, development, or scaling
- Practical recommendations based on the paradigm

**Reasoning:** Software 2.0 is Karpathy's most influential conceptual contribution. Provides powerful frame for understanding why ML systems are different. Used frequently when discussing AI engineering decisions. Clear actionable output: classify, explain, recommend.

**5-Criterion Evaluation:**
- Actionable: YES - Clear steps: classify paradigm, apply comparison, derive implications
- Invocable: YES - "Frame in Software 2.0" or "Why is ML different?" triggers
- Scoped: YES - One responsibility: paradigm framing
- Reusable: YES - Applies to any AI/ML discussion
- Valuable: YES - Resolves common confusions about AI development

---

## MEDIUM Priority

### 3. llm-architecture-explainer

**Source Pattern:** "LLMs as Operating Systems" Frame + Key Concepts Vocabulary

**Purpose:** Explain LLM architecture decisions and behaviors using the "operating system" mental model - connecting context windows to RAM, model weights to the kernel, prompts to programs.

**Trigger:** "Why does [LLM behavior] happen?", "Explain LLM architecture to me", "Why does context length matter?", "How should I think about prompt design?"

**Inputs:**
- LLM behavior or architecture question
- Specific model context (if relevant)
- User's current understanding level

**Outputs:**
- Explanation using OS analogy (CPU, RAM, filesystem)
- Technical details mapped to familiar computing concepts
- Practical implications for usage
- Connection to tokenization when relevant

**Reasoning:** The "LLM as OS" frame is uniquely Karpathy's insight and highly effective for explaining LLM behavior to developers. Estimated 1-2 uses/week when discussing LLM integration. Builds on familiar computing concepts.

**5-Criterion Evaluation:**
- Actionable: YES - Apply OS analogy, map concepts, explain implications
- Invocable: YES - "Explain LLM architecture" triggers
- Scoped: YES - Focused on LLM architecture explanation
- Reusable: YES - Applies across LLM discussions
- Valuable: YES - Makes complex LLM concepts accessible to developers

---

### 4. tokenization-debugger

**Source Pattern:** Tokenization Key Concepts + "The model doesn't see words"

**Purpose:** Help debug LLM behaviors by analyzing tokenization - the "atoms" of language models that explain many "weird" behaviors.

**Trigger:** "Why is the LLM doing [unexpected thing]?", "Debug this LLM behavior", "Why can't it handle [X]?", "Tokenization analysis"

**Inputs:**
- Problematic input/output pair
- Model name (for tokenizer identification)
- Specific behavior being debugged

**Outputs:**
- Tokenization breakdown of relevant text
- Analysis of how tokenization affects the behavior
- Explanation of why the model "sees" what it sees
- Recommendations for working around tokenization issues

**Reasoning:** Understanding tokenization is key to debugging LLM issues. Many "mysterious" behaviors trace back to how text becomes tokens. Medium priority because less frequent trigger but high value when needed.

**5-Criterion Evaluation:**
- Actionable: YES - Analyze tokens, connect to behavior, recommend fixes
- Invocable: YES - "Debug LLM behavior" or "tokenization analysis" triggers
- Scoped: YES - Focused on tokenization-related debugging
- Reusable: YES - Applies to any LLM debugging scenario
- Valuable: YES - Resolves otherwise mysterious issues

---

## LOW Priority

*None identified - all skill candidates passed the 5-criterion test and are at least MEDIUM priority.*

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Biographical Information | Reference data, no actionable workflow |
| OpenAI Founding Details | Historical facts, not a process |
| Tesla Data Engine | Context-specific engineering pattern, not generalizable |
| Career Timeline | Pure reference, no workflow |
| CS231n Course Structure | Reference for course design, not an invocable skill |
| Voice Characteristics | Guidance for persona, not standalone skill |
| Signature Phrases | Reference vocabulary, no process |
| Key Resources | Bibliography, not actionable |

---

## Overlap Analysis

| Candidate | Existing Skill | Overlap % | Decision |
|-----------|---------------|-----------|----------|
| minimal-implementation-explainer | analogical-bridge | 15% | Distinct - minimal implementation is code-focused |
| software-paradigm-framing | None found | 0% | New skill |
| llm-architecture-explainer | None found | 0% | New skill |
| tokenization-debugger | None found | 0% | New skill |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: minimal-implementation-explainer
Purpose: Transform complex concepts into minimal working code implementations
Trigger: "Explain X from scratch" or "Build minimally"
Integration: andrej-karpathy expert
```

```
Skill: software-paradigm-framing
Purpose: Reframe discussions using Software 1.0/2.0/3.0 lens
Trigger: "Frame in Software 2.0" or "Why is ML different"
Integration: andrej-karpathy expert
```

```
Skill: llm-architecture-explainer
Purpose: Explain LLM architecture using OS mental model
Trigger: "Explain LLM architecture" or "Why does context length matter"
Integration: andrej-karpathy expert
```

```
Skill: tokenization-debugger
Purpose: Debug LLM behaviors through tokenization analysis
Trigger: "Debug LLM behavior" or "tokenization analysis"
Integration: andrej-karpathy expert
```
