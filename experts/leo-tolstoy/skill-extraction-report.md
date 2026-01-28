# Skill Extraction Report: leo-tolstoy

**Source:** experts/leo-tolstoy/expertise.md
**Analyzed:** 2026-01-28
**Candidates Found:** 4

---

## HIGH Priority

### 1. defamiliarization-technique

**Source Pattern:** Defamiliarization (Ostranenie) - Literary Techniques section
**Purpose:** Apply Tolstoy's defamiliarization technique to make familiar concepts, processes, or situations appear strange and questionable, revealing hidden assumptions and conventions
**Trigger:** "Make this familiar thing strange" / "What would a peasant/outsider/dying person see here?" / "Strip away the conventions" / "Question the obvious"
**Inputs:** Content to defamiliarize (process description, organizational practice, social convention, technical system)
**Outputs:** Defamiliarized description that exposes underlying assumptions, arbitrary conventions, and unexamined practices; fresh perspective on familiar material
**Reasoning:** Clear actionable technique (describe as if seeing for first time), highly reusable across any content that involves conventions or assumptions, saves significant effort in critical analysis. Viktor Shklovsky identified "several hundred examples" in Tolstoy's work, demonstrating robustness. Directly connected to Brecht's Verfremdungseffekt. Estimated 3+ uses/week for questioning established practices.

**Criterion evaluation:**
- Actionable: YES - Clear steps: identify familiar element, remove conventional labels, describe physical/functional reality, expose what habit conceals
- Invocable: YES - "Defamiliarize this process" / "Make this strange"
- Scoped: YES - One responsibility: make familiar things appear unfamiliar
- Reusable: YES - Applies to any content involving conventions, habits, or assumptions
- Valuable: YES - Saves 30+ minutes of manual critical analysis, ensures consistent application

---

### 2. moral-life-audit

**Source Pattern:** The Death of Ivan Ilyich framework - Authentic vs. Artificial Life
**Purpose:** Diagnose whether a person, organization, or practice is living/operating authentically or artificially (following convention rather than truth)
**Trigger:** "Am I living authentically?" / "Is this organization authentic or performing?" / "Ivan Ilyich test" / "Is this artificial or authentic?"
**Inputs:** Description of a life situation, organizational culture, career path, or decision framework to evaluate
**Outputs:** Diagnosis of authentic vs. artificial living with specific indicators; recommendations for moving toward authenticity; warning signs of "spiritual death while physically alive"
**Reasoning:** Core Tolstoyan framework with clear binary classification (authentic/artificial). Two types clearly defined in expertise.md. Directly addresses Tolstoy's central question "How should we live?" Reusable across personal and organizational contexts. Estimated 2-3 uses/week for life and work decisions.

**Criterion evaluation:**
- Actionable: YES - Clear framework: assess against authentic life criteria (compassion, seeing others as individuals, meaningful relationships) vs. artificial (self-interest, materialism, shallow relationships)
- Invocable: YES - "Run an Ivan Ilyich audit on my career" / "Is this authentic or artificial?"
- Scoped: YES - One responsibility: diagnose authenticity of life/work
- Reusable: YES - Applies to personal decisions, organizational culture, career evaluation
- Valuable: YES - Addresses fundamental life questions, saves hours of undirected reflection

---

## MEDIUM Priority

### 3. panoramic-to-particular-rendering

**Source Pattern:** The Panoramic to Particular Method - Literary Techniques
**Purpose:** Structure analysis or narrative to move from vast context (historical, social, institutional forces) to intimate detail (individual thought, physical gesture) in a single coherent sweep
**Trigger:** "Give me the big picture and the small details" / "How does this individual situation fit the larger context?" / "Tolstoy-style rendering"
**Inputs:** A situation, event, or analysis topic that has both macro context and micro details
**Outputs:** Structured narrative/analysis that seamlessly moves between panoramic scope and intimate particulars, connecting individual experience to larger forces
**Reasoning:** Distinctive Tolstoyan technique explicitly described in expertise.md. Useful for writing, analysis, and presentations. Percy Lubbock's comparison to Iliad + Aeneid shows the technique's power. Estimated 1-2 uses/week for comprehensive analysis.

**Criterion evaluation:**
- Actionable: YES - Clear steps: establish panorama, descend to particular, show connection between scales
- Invocable: YES - "Render this panoramically" / "Connect the big picture to the details"
- Scoped: YES - One responsibility: multi-scale rendering
- Reusable: YES - Applies to any complex situation with both macro and micro dimensions
- Valuable: YES - Saves 20-30 minutes structuring comprehensive analysis

---

### 4. death-awareness-perspective

**Source Pattern:** Death as Teacher - Core Principles / Philosophy of History
**Purpose:** Apply the perspective of mortality to strip away pretense and reveal what truly matters in a decision, priority, or life situation
**Trigger:** "What would a dying person see here?" / "View this from the perspective of mortality" / "Death awareness check"
**Inputs:** A decision, priority list, or life situation to examine
**Outputs:** Mortality-informed perspective that distinguishes essential from inessential, authentic from performative, meaningful from conventional
**Reasoning:** Central Tolstoyan insight that "only by facing mortality can we understand life." Ivan Ilyich's transformation demonstrates the technique. Complements moral-life-audit. Estimated 1-2 uses/week for major decisions or priority-setting.

**Criterion evaluation:**
- Actionable: YES - Clear steps: imagine approaching death, identify what would remain important, identify what would fall away
- Invocable: YES - "Apply death awareness to this decision" / "Mortality perspective"
- Scoped: YES - One responsibility: mortality-informed perspective
- Reusable: YES - Applies to any decision or priority evaluation
- Valuable: YES - Addresses fundamental questions, saves undirected philosophical wandering

---

## LOW Priority

None identified - all candidates met HIGH or MEDIUM thresholds.

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Philosophy of History (War and Peace) | Reference knowledge about historical causation theory, not actionable workflow |
| Christian Anarchism / Non-Resistance | Philosophical/ethical stance, not a procedural workflow |
| Tolstoy-Gandhi Correspondence | Historical reference material, no actionable process |
| Marriage to Sophia Behrs | Biographical reference, not applicable to user contexts |
| Excommunication details | Historical facts, no workflow |
| Free Indirect Discourse | Already exists as `free-indirect-voice` skill |
| Physical Observation as Psychology | Technique guidance for writers, stays as expertise reference |
| Multiple Perspectives technique | Writing technique without sufficient procedural steps |
| Epigraph interpretation (Anna Karenina) | Literary analysis reference, not actionable skill |
| Quotes (verified sources) | Pure reference data |

---

## Overlap Analysis

| Candidate | Existing Skill | Overlap % | Decision |
|-----------|---------------|-----------|----------|
| defamiliarization-technique | None found | 0% | Distinct |
| moral-life-audit | `authenticity-assessment` | ~35% | Distinct (Tolstoy-specific framework) |
| panoramic-to-particular-rendering | None found | 0% | Distinct |
| death-awareness-perspective | `being-toward-death-reflection` | ~50% | Potential enhancement, but Tolstoyan approach distinct |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: defamiliarization-technique
Purpose: Apply Tolstoy's defamiliarization to make familiar things appear strange, exposing hidden assumptions
Trigger: "Make this strange" / "Defamiliarize this"
Integration: leo-tolstoy expert
```

```
Skill: moral-life-audit
Purpose: Diagnose authentic vs. artificial living using Tolstoy's Ivan Ilyich framework
Trigger: "Ivan Ilyich test" / "Is this authentic or artificial?"
Integration: leo-tolstoy expert
```

```
Skill: panoramic-to-particular-rendering
Purpose: Structure analysis to move seamlessly from vast context to intimate detail
Trigger: "Render this panoramically" / "Connect big picture to details"
Integration: leo-tolstoy expert
```

```
Skill: death-awareness-perspective
Purpose: Apply mortality perspective to reveal what truly matters
Trigger: "Death awareness check" / "Mortality perspective"
Integration: leo-tolstoy expert
```
