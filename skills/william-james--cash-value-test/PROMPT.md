# Cash-Value Test

**Expert:** william-james
**Priority:** HIGH
**Estimated Use:** 5+ times per week

## Purpose

Evaluate any idea, concept, theory, or dispute by translating it into experiential consequences and stripping away merely verbal disputes. This is William James's signature contribution to philosophy - the pragmatic method for testing whether debates are substantive or merely semantic.

## When to Invoke

**Triggers:**
- "What's the practical difference?"
- "Does this matter in practice?"
- "Is this a real dispute or just words?"
- "Apply the cash-value test"
- Technical debates that seem circular or unresolvable
- Architecture discussions where parties talk past each other
- Theoretical arguments that never reach actionable conclusions

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Idea/Concept/Theory | Yes | The claim, concept, or theory to evaluate |
| Dispute | Optional | If evaluating a disagreement, both positions |
| Context | Optional | Domain of application (technical, organizational, personal) |

## Outputs

1. **Cash-Value Translation** - What the idea means in experiential terms
2. **Practical Consequences** - What would be different if the idea is true vs. false
3. **Dispute Classification** - Whether the dispute is verbal (dissolve) or substantive (decide)
4. **Recommendation** - Action based on experiential consequences

---

## Methodology

### Step 1: State the Dispute Clearly

Articulate exactly what is being claimed or debated.

**Questions to ask:**
- What specifically is being asserted?
- What are the competing positions?
- What would each side consider a "win"?

**Example:** "Team A says we should use microservices. Team B says monolith. What exactly does each position entail?"

### Step 2: Trace the Cash-Value

Translate abstract claims into experiential consequences.

**The core question:** "What practical difference would it make if this view were true?"

**Cash-value translation template:**
- If [Position A] is true, then in practice we would experience...
- If [Position B] is true, then in practice we would experience...

**Watch for:**
- Claims that have no experiential translation (empty abstractions)
- Differences that are purely linguistic (same experience, different words)
- Hidden value differences masquerading as factual disputes

### Step 3: Test Experientially

Examine how the world would actually be different in lived experience.

**Testing questions:**
- What would we observe differently?
- What would we do differently?
- What problems would arise or be solved?
- How would success or failure manifest?

**James's insight:** "Truth happens to an idea. It becomes true, is made true by events."

### Step 4: Dissolve or Decide

Based on the cash-value analysis, take action.

**If verbal dispute (no practical difference):**
- Declare the dispute dissolved
- Redirect energy to actionable questions
- Name the common ground beneath the semantic difference

**If substantive dispute (real practical difference):**
- Identify which consequences matter most
- Decide based on experiential outcomes
- Acknowledge genuine trade-offs

---

## Example Application

### Scenario: "Is our system truly event-driven?"

**Step 1: State the Dispute**
- Architect claims the system is event-driven
- Operator claims it's really just request-response with queues
- Both are defending their characterization

**Step 2: Trace the Cash-Value**
- If "truly event-driven": Events would be first-class, decoupled producers/consumers, temporal decoupling
- If "request-response with queues": Synchronous dependencies, queues just buffer, tight coupling remains

**Step 3: Test Experientially**
- Can we take down Consumer A without affecting Producer B? (If yes -> event-driven)
- Do producers block waiting for acknowledgment? (If yes -> request-response)
- Can events be replayed independently? (If yes -> event-driven)
- Is there a timeout if the "response" doesn't come? (If yes -> request-response)

**Step 4: Dissolve or Decide**
- Testing reveals: Producers block with 30-second timeout. Consumers can't replay events.
- **Decision:** The system is architecturally request-response despite using a message broker
- **Action:** Either accept this (rename it) or refactor toward true event-driven patterns
- **Dissolved:** The debate about terminology; **Decided:** The architectural reality

---

## Anti-Patterns

### Avoid These Mistakes

1. **Premature dissolution** - Dismissing disputes as "merely verbal" before tracing full consequences
2. **Abstract answers** - Responding with more theory instead of experiential translation
3. **Ignoring stakeholder values** - Different people may legitimately weigh consequences differently
4. **Binary thinking** - Forgetting that both views may have partial cash-value

### Signs the Test is Working

- Energy shifts from defending positions to exploring consequences
- Previously "obvious" positions become questionable
- Hidden assumptions surface
- Actionable next steps emerge

---

## Integration with william-james Expert

This skill implements the core of James's pragmatic method. When using the william-james expert persona:

- **This skill provides:** The systematic process for testing ideas pragmatically
- **The expert provides:** Broader philosophical context, related concepts (pluralism, radical empiricism), signature phrases, historical examples

**Handoff to expert when:**
- Deeper philosophical grounding is needed
- The cash-value test reveals tensions requiring Jamesian wisdom
- Multiple skills need orchestration (e.g., cash-value test + will-to-believe assessment)

**Related skills:**
- `will-to-believe-assessment` - When evidence is genuinely incomplete
- `temperament-bridge` - When dispute reflects philosophical temperament
- `stream-experience-audit` - For understanding how consequences unfold experientially

---

## Key Quotes for Invocation

> "The pragmatic method... is to try to interpret each notion by tracing its respective practical consequences. What difference would it practically make to anyone if this notion rather than that notion were true?"

> "What is the cash-value of this in experiential terms?"

> "Ideas become true insofar as they help us get into satisfactory relation with other parts of our experience."

> "You can say of it then either that 'it is useful because it is true' or that 'it is true because it is useful.' Both these phrases mean exactly the same thing."
