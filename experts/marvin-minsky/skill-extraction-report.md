# Skill Extraction Report: marvin-minsky

**Source:** experts/marvin-minsky/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 5

---

## HIGH Priority

### 1. marvin-minsky--society-decomposition

**Source Pattern:** Society of Mind Architecture (lines 27-43)

**Purpose:** Break down any complex system behavior into a "society" of interacting simple agents, revealing how intelligence emerges from non-intelligence.

**Trigger:** "Decompose this system into agents" / "How does this intelligent behavior actually work?" / "What simple processes produce this complex output?" / When facing a monolithic system that seems to exhibit intelligence

**Inputs:**
- System or behavior to analyze (description, documentation, or observation)
- Context: what the system appears to do "as a whole"
- Optional: known constraints or requirements

**Outputs:**
- List of 5-10 candidate agents with clear, simple functions
- Interaction map showing how agents communicate, compete, or cooperate
- Identification of coordinator/conflict-resolver agents
- Analysis of where "intelligence" resides (answer: in the interaction, not any single agent)
- Practical recommendations for implementing/debugging the decomposition

**Reasoning:** Clear 5-step process with explicit examples (self-healing system decomposition). Highly actionable - can be applied to any system claiming complex/intelligent behavior. Reusable across architecture, debugging, AI/ML integration. Estimated 2-3 uses/week for anyone working with "intelligent" systems. Saves 30+ minutes of architectural thinking per use. Directly embodies Minsky's core methodology.

---

### 2. marvin-minsky--suitcase-word-unpacking

**Source Pattern:** Suitcase Word Analysis + Unpacking Protocol (lines 45-55, 244-269, 806-815)

**Purpose:** Identify and decompose vague, overloaded terms that hide conceptual confusion, enabling precise discussion and accurate system evaluation.

**Trigger:** "Unpack this term" / "What does 'intelligent' actually mean here?" / When discussions are stuck because participants use the same word for different concepts / When evaluating vendor claims about AI/autonomous systems

**Inputs:**
- The suitcase word to unpack (e.g., "intelligent", "autonomous", "learns")
- Context where the word is being used
- Optional: specific claim being made using the word

**Outputs:**
- List of distinct meanings/components packed into the word
- Specification of which component is actually being discussed
- Verification questions to determine what the system actually does
- Clarified claim with precise language replacing the suitcase word

**Reasoning:** Clear 4-step protocol (Stop, List, Specify, Verify). Extensively documented with multiple tables of common suitcase words. Highly invocable - triggered whenever vague AI/ML terminology appears. Reusable across vendor evaluation, architecture review, documentation writing, team discussions. Estimated 3+ uses/week in any AI-adjacent work. Saves confusion and miscommunication. Core to Minsky's anti-mystification approach.

---

### 3. marvin-minsky--negative-expertise-audit

**Source Pattern:** Negative Expertise (lines 437-489) + Anti-Patterns to Identify (lines 92-104)

**Purpose:** Systematically identify and document what NOT to do in a domain, building the "censor agents" that prevent known failures.

**Trigger:** "What should I avoid here?" / "Build a negative expertise catalog" / After a post-mortem / When designing guardrails / "What are the anti-patterns?"

**Inputs:**
- Domain or system to audit (e.g., deployment, monitoring, incident response)
- Optional: existing positive knowledge (runbooks, procedures)
- Optional: historical incidents/failures

**Outputs:**
- Catalog of anti-patterns with specific examples
- Mapping of positive knowledge to corresponding negative knowledge
- Identification of censor agents (early detection) vs. suppressor agents (last-resort vetoes)
- Recommendations for implementing explicit vetoes in systems

**Reasoning:** Clear framework with positive/negative knowledge distinction. Multiple application tables provided (debugging, operations). Actionable process: post-mortems -> anti-patterns -> pre-mortems -> censor agents. Reusable across all operational domains. Estimated 2+ uses/week for SRE/DevOps. Saves disasters by encoding lessons learned. Directly from Minsky's 1994 essay - a distinct, named methodology.

---

## MEDIUM Priority

### 4. marvin-minsky--frame-problem-analysis

**Source Pattern:** The Frame Problem (lines 57-64, 273-306, 837-848)

**Purpose:** Analyze how a system determines what context matters, what to ignore, and how changes propagate - identifying hidden assumptions about stability.

**Trigger:** "What might break if I change this?" / "How does the system know what's relevant?" / Impact analysis for changes / "What are we assuming stays constant?"

**Inputs:**
- The change or action being considered
- System context (dependencies, configurations, workflows)
- Optional: known constraints or invariants

**Outputs:**
- Explicit listing of intended effects
- Analysis of implicit "frame axioms" (what's assumed to stay constant)
- Identification of hidden dependencies that might be affected
- Recommended mitigations (dependency graphs, testing, canary deploys)
- Warning about what CANNOT be fully enumerated (need defaults, retractable conclusions)

**Reasoning:** Well-documented concept with multiple application tables. Clear problem statement and solution approaches. Actionable for configuration management, alert management, incident response, change management. Reusable across operational domains. Estimated 1-2 uses/week for change reviews. Moderately complex - requires system knowledge to apply well. Valuable for preventing cascading failures.

---

### 5. marvin-minsky--mechanism-demand

**Source Pattern:** The "How Could That Work?" Drill (lines 400-409) + Signature Techniques #3 (PROMPT.md lines 38-43)

**Purpose:** Force explanations to be mechanistic rather than mystical by demanding specific components, inputs, processes, and implementable steps.

**Trigger:** "How would that actually work?" / When explanations rely on impressive terms without operational content / When someone claims a capability without mechanism / "That's naming, not explaining"

**Inputs:**
- The claimed capability or phenomenon
- The explanation being offered
- Optional: context where the explanation will be used

**Outputs:**
- Identification of whether explanation is a label or a mechanism
- Required inputs for the capability
- Processing steps that could produce the output
- Knowledge structures needed to support the process
- How those structures could be acquired
- Verdict: explanation vs. hand-waving

**Reasoning:** Clear 5-step drill from expertise.md. Central to Minsky's methodology - challenges mysterian explanations. Invocable whenever someone says something "emergent" or "intuitive" without specifics. Reusable in architecture reviews, design discussions, vendor evaluations. Estimated 2+ uses/week. Moderately complex - requires domain knowledge to evaluate answers. Forces intellectual honesty.

---

## LOW Priority

### 6. marvin-minsky--six-level-assessment

**Source Pattern:** Six-Level Cognitive Architecture + DevOps mapping (lines 155-164, 310-327)

**Purpose:** Map a system's responses to Minsky's six cognitive levels, identifying which levels are covered and which are missing.

**Trigger:** When assessing the maturity of an operational system / "What level of response does this system have?" / Designing layered automation

**Inputs:**
- System or domain to assess
- Current automation/response capabilities

**Outputs:**
- Mapping of existing capabilities to six levels
- Gap analysis showing missing levels
- Recommendations for building up the stack
- Identification of critic-selector mechanisms

**Reasoning:** Clear framework with DevOps mapping provided. Useful for assessing operational maturity. However, somewhat theoretical - less immediately actionable than other skills. Estimated <1 use/week. More of a lens than a procedure. Could be valuable for strategic planning.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Verified Quotes | Reference data only - no actionable workflow |
| Historical Timeline | Biographical facts - no procedure |
| Intellectual Relationships | Context for understanding - not invocable |
| Dartmouth Conference | Historical background - not actionable |
| Inventions (SNARC, microscope, robotics) | Historical examples - no reusable procedure |
| Glossary of Key Terms | Reference material - definitions, not workflow |
| Common Misconceptions to Correct | Warning/gotcha list - stays as expertise |
| Builder vs. Wrecker Example | Illustrative example within Society decomposition |
| CYC and Open Mind projects | Historical context - not a method user can apply |
| Perceptrons book analysis | Historical context and lesson - not a procedure |
| Steps Toward AI (1961) | Organization of AI problems - framework, not skill |
| Heuristics definition | Conceptual explanation - no steps |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: marvin-minsky--society-decomposition
Purpose: Decompose complex systems into societies of simple agents
Trigger: "Decompose this system" / "What agents produce this behavior?"
Integration: marvin-minsky expert

Skill: marvin-minsky--suitcase-word-unpacking
Purpose: Identify and decompose overloaded terms hiding conceptual confusion
Trigger: "Unpack this term" / When evaluating vague AI claims
Integration: marvin-minsky expert

Skill: marvin-minsky--negative-expertise-audit
Purpose: Systematically document what NOT to do, building censor agents
Trigger: "What should I avoid?" / After post-mortems / Building guardrails
Integration: marvin-minsky expert

Skill: marvin-minsky--frame-problem-analysis
Purpose: Analyze hidden assumptions about what changes and what stays constant
Trigger: "What might break if I change this?" / Impact analysis
Integration: marvin-minsky expert

Skill: marvin-minsky--mechanism-demand
Purpose: Force mechanistic explanations, reject mysterian hand-waving
Trigger: "How would that actually work?" / Evaluating vague claims
Integration: marvin-minsky expert
```
