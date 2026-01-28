# Skill Extraction Report: rene-descartes

**Source:** experts/rene-descartes/expertise.md
**Analyzed:** 2026-01-26
**Candidates Found:** 4

---

## HIGH Priority

### 1. methodical-doubt-analysis

**Source Pattern:** The Cartesian Method (Detailed), Key Thought Experiments (Evil Demon, Dream Argument)

**Purpose:** Apply systematic skepticism to beliefs, claims, or assumptions to identify what can be known with certainty and what is merely assumed.

**Trigger:** "What can I really know here?", "Test these assumptions", "Apply radical doubt", "What's actually certain?", "Subject this to skeptical analysis"

**Inputs:**
- beliefs_or_claims: The statements, assumptions, or knowledge claims to examine
- domain_context: (Optional) The field or situation
- doubt_intensity: (Optional) Level of skepticism (standard, radical, evil-demon)

**Outputs:**
- Inventory of claims sorted by epistemic status (certain, probable, doubtful, rejected)
- Identified "indubitable" foundations (if any)
- Analysis of what survives radical doubt
- Clear/distinct vs. obscure/confused classification
- Recommendations for building on certain foundations

**Reasoning:** This is Descartes' signature methodology with clear steps: (1) doubt everything that can be doubted, (2) identify what survives even radical skepticism, (3) classify ideas by clarity and distinctness. Highly actionable, frequently invocable ("test my assumptions"), well-scoped, reusable across domains, and valuable for critical thinking. Does NOT overlap significantly with existing `first-principles-reasoning` (which focuses on reducing to fundamentals, not testing certainty through doubt).

---

### 2. analysis-synthesis-method

**Source Pattern:** The Cartesian Method (Rule 2: Analysis, Rule 3: Synthesis), Four Rules of the Method

**Purpose:** Decompose complex problems into simple parts, solve each part, then reconstruct systematically from simple to complex.

**Trigger:** "This problem is too complex", "Break this down", "Help me work through this systematically", "Divide and conquer", "How do I approach this step by step?"

**Inputs:**
- problem_statement: The complex problem to decompose
- known_constraints: Any fixed constraints or requirements
- simplicity_criteria: (Optional) What counts as "simple" in this domain

**Outputs:**
- Problem decomposition (tree/list of component parts)
- Ordered sequence from simplest to most complex
- Solution for each simple component
- Synthesis showing how parts reconstruct the whole
- Enumeration check (nothing omitted)

**Reasoning:** The four rules of Descartes' method (evidence, analysis, order, enumeration) constitute a complete problem-solving framework. This is actionable (clear steps), invocable ("break this down for me"), scoped (problem decomposition and reconstruction), reusable (any domain), and saves significant effort on complex problems. While related to general decomposition techniques, this specifically implements Descartes' ordered approach (simple-to-complex) with his enumeration verification.

---

### 3. clarity-distinctness-evaluation

**Source Pattern:** Clear and Distinct Ideas, The Wax Argument, Key Distinctions (Clear vs. Obscure, Distinct vs. Confused)

**Purpose:** Evaluate whether an idea, concept, or argument is sufficiently clear and distinct to be trusted, or whether it remains obscure and confused.

**Trigger:** "Is this idea clear enough?", "Am I really understanding this?", "Evaluate this argument's clarity", "Is this confusion or genuine complexity?", "Do I truly grasp this?"

**Inputs:**
- idea_or_argument: The concept, claim, or reasoning to evaluate
- purpose: What the understanding will be used for (decision, teaching, etc.)

**Outputs:**
- Clarity assessment (Clear: vivid and present to mind? Or obscure?)
- Distinctness assessment (Precisely separated from other ideas? Or confused with related concepts?)
- Specific sources of obscurity or confusion identified
- Recommendations for achieving clarity
- Verdict: ready to build on, or needs clarification

**Reasoning:** Descartes' criterion for truth was clarity and distinctness. This is actionable (assess and improve understanding), invocable ("is this clear enough?"), scoped (evaluating ideas for epistemic quality), reusable (any concept or argument), and valuable (prevents building on confused foundations). Distinct from general "analysis" - this specifically tests epistemic quality using Cartesian criteria.

---

## MEDIUM Priority

### 4. foundational-certainty-mapping

**Source Pattern:** The Six Meditations structure, Cogito Analysis, building from indubitable foundations

**Purpose:** Map the epistemic foundations of a domain, belief system, or project - identifying what is certain, what depends on what, and where uncertainty enters.

**Trigger:** "What are my first certainties here?", "Map the foundations", "What can I build on?", "What do I know for sure?", "Establish epistemological footing"

**Inputs:**
- domain_or_project: The area to map
- existing_beliefs: Current claims or assumptions
- certainty_threshold: How strict (practical certainty vs. philosophical certainty)

**Outputs:**
- Certainty hierarchy (what is most certain at the base)
- Dependency map (what builds on what)
- Points of uncertainty and their downstream effects
- Cogito-equivalent for this domain (the one thing you cannot doubt)
- Recommendations for proceeding despite uncertainty

**Reasoning:** This captures the Meditations' structure of building from indubitable foundations. Actionable (creates a map), invocable ("establish my foundations"), scoped (epistemic mapping), reusable (any domain with knowledge claims). Overlap with `first-principles-reasoning` is ~40% (both identify fundamentals), but this focuses specifically on *certainty relationships* and *building order* rather than challenging conventions.

---

## LOW Priority

### 5. evil-demon-stress-test

**Source Pattern:** The Evil Demon thought experiment, Modern Parallels (Security section)

**Purpose:** Subject a belief, system, or design to the most extreme adversarial scenario to test robustness.

**Trigger:** "What if there's a malicious actor?", "Stress test this", "Assume worst case", "What could go wrong if someone was trying to deceive me?"

**Reasoning:** While actionable and valuable, this largely reduces to adversarial thinking which is covered by security/threat modeling skills. The specifically Cartesian contribution (testing beliefs for certainty) is better captured in `methodical-doubt-analysis`. Mark as LOW priority - can be recommended without standalone skill.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Provisional Morality | Reference knowledge about Descartes' ethics, not a workflow. The maxims are guidance, not a process. |
| Arguments for God's Existence | Historical reference material; theological proofs are not actionable workflows for users |
| The Cartesian Circle | Philosophical objection/debate, not an actionable method |
| Mind-Body Problem | Philosophical position and debate, not an invocable workflow |
| Biographical details | Pure reference knowledge |
| Mathematical contributions | Historical reference; coordinate systems are foundational math, not invocable skills |
| Influence and Legacy | Reference material |
| Key Distinctions table | Reference definitions, not workflows |
| Famous Maxims | Quotes for reference |
| The Wax Argument (standalone) | Illustration supporting clarity-distinctness, not a separate skill |
| The Dream Argument (standalone) | Illustration supporting methodical-doubt, not a separate skill |

---

## Overlap Analysis

| Candidate | Existing Skill | Overlap % | Decision |
|-----------|---------------|-----------|----------|
| methodical-doubt-analysis | first-principles-reasoning | 25% | Distinct: doubt tests certainty; FPR reduces to fundamentals |
| methodical-doubt-analysis | uncertainty-assessment | 20% | Distinct: uncertainty-assessment quantifies risk; this tests truth |
| analysis-synthesis-method | first-principles-analysis | 30% | Distinct: FPA is Aristotelian four-causes; this is ordered decomposition |
| clarity-distinctness-evaluation | None identified | 0% | New skill |
| foundational-certainty-mapping | first-principles-reasoning | 40% | Distinct but related; this focuses on certainty ordering |

---

## Next Steps

To create approved skills, run skill creation for each HIGH and MEDIUM candidate:

```
Skill: rene-descartes--methodical-doubt-analysis
Purpose: Apply systematic skepticism to identify what is truly certain
Trigger: "Test these assumptions", "What can I really know?"
Integration: rene-descartes expert
```

```
Skill: rene-descartes--analysis-synthesis-method
Purpose: Decompose complex problems and reconstruct systematically
Trigger: "Break this down", "Divide and conquer"
Integration: rene-descartes expert
```

```
Skill: rene-descartes--clarity-distinctness-evaluation
Purpose: Evaluate whether ideas are clear and distinct enough to trust
Trigger: "Is this clear enough?", "Am I really understanding this?"
Integration: rene-descartes expert
```

```
Skill: rene-descartes--foundational-certainty-mapping
Purpose: Map epistemic foundations and certainty relationships
Trigger: "What can I build on?", "Map the foundations"
Integration: rene-descartes expert
```
