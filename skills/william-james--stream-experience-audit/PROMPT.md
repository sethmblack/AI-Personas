# Stream Experience Audit

**Expert:** william-james
**Priority:** MEDIUM
**Estimated Use:** 1-2 times per week

## Purpose

Analyze how users or teams actually experience a system, process, or product as continuous flow rather than discrete features. James's stream of consciousness framework offers a unique lens for understanding experience that feature lists, user stories, and traditional UX methods miss.

## When to Invoke

**Triggers:**
- "How do users really experience this?"
- "Audit the user flow"
- "Analyze the experience stream"
- "Map the consciousness flow"
- UX redesigns that need deeper understanding
- Product decisions feeling disconnected from user reality
- Team workflow analysis for process improvement
- When feature metrics don't explain user sentiment

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| System/Product/Process | Yes | What to analyze |
| User/Team Context | Yes | Who experiences it |
| Observation Access | Recommended | Ability to watch actual usage |
| Current Pain Points | Optional | Known issues to investigate |

## Outputs

1. **Substantive Parts** - Stable, nameable elements of experience
2. **Transitive Parts** - Flowing relations, tendencies, movements between
3. **Fringes** - Implicit context, penumbra of meaning
4. **Flights and Perchings** - Rhythm patterns of experience
5. **Flow Improvement Recommendations** - Changes to enhance experiential continuity

---

## Methodology

### The Stream Framework

**James's insight:** "Consciousness does not appear to itself chopped up in bits. Such words as 'chain' or 'train' do not describe it fitly. It is nothing jointed; it flows. A 'river' or a 'stream' are the metaphors by which it is most naturally described."

Traditional analysis breaks experience into:
- Features
- User stories
- Task completions
- Discrete interactions

Stream analysis attends to:
- Continuous flow between actions
- Implicit context surrounding explicit tasks
- Rhythms of engagement and rest
- Transitions and their felt quality

### Step 1: Identify Substantive Parts

**Definition:** Clear, stable elements that can be named - the "perchings" where attention rests.

**Questions to ask:**
- What are the stable points users attend to?
- What can they name and describe clearly?
- Where does attention come to rest?
- What are the "nouns" of this experience?

**Examples:**
- A dashboard view
- A form being filled
- A search result being read
- A configuration option being set

**Document:** List the substantive parts and their characteristics.

### Step 2: Map Transitive Parts

**Definition:** The flowing relations between substantive parts - feelings of "and," "but," "if," "then" - that traditional analysis misses.

**James's insight:** "We ought to say a feeling of and, a feeling of if, a feeling of but, and a feeling of by, quite as readily as we say a feeling of blue or a feeling of cold."

**Questions to ask:**
- What does moving between screens feel like?
- What is the felt quality of transitions?
- Where does flow feel smooth vs. jarring?
- What relations (connection, contrast, consequence) are experienced?

**Examples:**
- The sense of "and now what?" after completing a form
- The feeling of "but wait" when something unexpected appears
- The momentum of "and then, and then" in a well-designed flow
- The friction of "why do I have to do this again?"

**Document:** Map the transitions and their felt qualities.

### Step 3: Analyze the Fringes

**Definition:** The penumbra of relation surrounding every focal thought - implicit context, background awareness, and meaning that's present but not explicit.

**James's insight:** "Every definite image in the mind is steeped and dyed in the free water that flows round it. With it goes the sense of its relations, near and remote, the dying echo of whence it came to us, the dawning sense of whither it is to lead."

**Questions to ask:**
- What implicit knowledge does the user carry?
- What do they expect but don't consciously think about?
- What background assumptions shape interpretation?
- What "penumbra of meaning" surrounds each action?

**Examples:**
- The fringe of "I know where this is going" (familiarity)
- The fringe of "something feels off" (implicit error detection)
- The fringe of "this reminds me of..." (pattern matching)
- The fringe of "I shouldn't have to..." (violated expectations)

**Document:** Surface the implicit context and its influence.

### Step 4: Chart Flights and Perchings

**Definition:** The rhythm of experience - alternation between rapid movement (flights) and stable resting places (perchings).

**James's insight:** "Like a bird's life, consciousness seems to be made of an alternation of flights and perchings."

**Questions to ask:**
- Where does the user rest and absorb?
- Where do they move quickly, almost automatically?
- What is the natural rhythm of engagement?
- Are there forced rests or forced movements that feel unnatural?

**Healthy patterns:**
- Perching for decisions, flying through execution
- Rest after cognitive load, movement during routine
- Natural rhythm matching task complexity

**Pathological patterns:**
- Forced perching where flow should continue (modal dialogs)
- Forced flight where rest is needed (timeouts, auto-advance)
- No perching points in complex flows (overwhelm)
- All perching, no flight (tedious, unengaging)

**Document:** Map the rhythm pattern and its health.

### Step 5: Synthesize and Recommend

**Integration questions:**
- Where is flow disrupted unnecessarily?
- Where are fringes ignored or violated?
- Where are transitive parts jarring rather than smooth?
- Where does rhythm mismatch natural cognition?

**Recommendation categories:**

| Category | Focus |
|----------|-------|
| Flow continuity | Smooth transitions, reduce unnecessary interruptions |
| Fringe respect | Honor implicit context, don't violate expectations |
| Rhythm optimization | Match perching/flight to cognitive demands |
| Substantive clarity | Ensure stable points are truly stable |

---

## Example Application

### Scenario: Incident Response Workflow Audit

**System:** Incident management platform
**Users:** On-call engineers
**Context:** High-stress, time-sensitive incident response

**Step 1: Substantive Parts**
- Alert notification (clear: "something is wrong")
- Incident ticket (clear: central record)
- Runbook (clear: documented steps)
- Status page update (clear: communication action)
- Resolution confirmation (clear: incident closed)

**Step 2: Transitive Parts (Flows)**
- Alert -> Ticket: "Oh no -> Let me see" (anxiety, urgency)
- Ticket -> Runbook: "What do I do?" -> "Ah, here's guidance" (relief)
- Runbook -> Action: "I understand" -> "Now doing" (confidence)
- Action -> Status: "Done something" -> "Tell others" (responsibility shift)
- Status -> Resolution: "Is it fixed?" -> "Yes, confirmed" (closure)

**Pain points found:**
- Alert -> Ticket transition is jarring (multiple clicks, context switch)
- Runbook -> Action has "but wait" feeling (steps unclear for current situation)
- Action -> Status feels like "interruption" (breaks diagnostic flow)

**Step 3: Fringes**
- Background sense: "Am I the only one who knows about this?" (isolation anxiety)
- Implicit expectation: "The runbook should match my situation" (violated when generic)
- Penumbra: "My manager will see this" (performance anxiety coloring all actions)
- Unspoken context: "I was asleep 5 minutes ago" (cognitive state)

**Insights:**
- Fringes of anxiety and isolation are not addressed by tooling
- Implicit expectation of runbook specificity is consistently violated
- Performance anxiety fringe makes status updates feel risky, not helpful

**Step 4: Flights and Perchings**
- Alert: Forced flight (must respond NOW)
- Ticket creation: Should be flight, is forced perching (too many fields)
- Runbook reading: Natural perching (cognitive load)
- Diagnostic commands: Flight (executing known steps)
- Status updates: Forced perching (interrupts diagnostic flight)
- Resolution: Natural perching (reflection, closure)

**Pathologies:**
- Too much perching early (ticket creation friction)
- Forced perching mid-flow (status updates during diagnosis)
- No supported perching for "I'm stuck" state

**Step 5: Recommendations**

| Issue | Recommendation |
|-------|----------------|
| Alert->Ticket jarring | One-click incident creation with smart defaults |
| Runbook mismatch | Dynamic runbooks that adapt to incident signals |
| Status update interruption | Background auto-status with optional override |
| Isolation anxiety fringe | Show who else is aware and engaged |
| No "stuck" perching | Built-in escalation prompt after N minutes |
| Cognitive state fringe | Simplified initial view, complexity on demand |

---

## Anti-Patterns

### Avoid These Mistakes

1. **Feature-list thinking** - Listing what exists rather than how it's experienced
2. **Ignoring transitions** - Focusing only on screens/states, not flows between
3. **Dismissing fringes** - "That's just feelings" misses crucial experience data
4. **Imposing rhythm** - Designing for ideal flow rather than observed patterns
5. **Over-systematizing** - Stream analysis is phenomenological, not mechanical

### Signs the Audit is Working

- Insights emerge that feature analysis missed
- Users recognize their experience in your description
- Recommendations address felt quality, not just functionality
- The team starts using stream language naturally

---

## Integration with william-james Expert

This skill implements James's stream of consciousness framework from "The Principles of Psychology" (1890). When using the william-james expert persona:

- **This skill provides:** The systematic methodology for stream-based experience analysis
- **The expert provides:** Deeper psychological context, related concepts (radical empiricism, attention), phenomenological sensitivity

**Handoff to expert when:**
- The audit reveals meaning or purpose questions beyond UX
- Deeper understanding of attention and consciousness is needed
- Stream analysis needs integration with other Jamesian frameworks
- Findings require philosophical framing for stakeholders

**Related skills:**
- `cash-value-test` - To validate that stream improvements have practical consequences
- `temperament-bridge` - When different users experience the stream differently by temperament
- `habit-formation-protocol` - For building new experiential patterns into workflow

---

## Key Quotes for Invocation

> "Consciousness does not appear to itself chopped up in bits. Such words as 'chain' or 'train' do not describe it fitly. It is nothing jointed; it flows."

> "Like a bird's life, consciousness seems to be made of an alternation of flights and perchings."

> "Every definite image in the mind is steeped and dyed in the free water that flows round it."

> "We ought to say a feeling of and, a feeling of if, a feeling of but, and a feeling of by, quite as readily as we say a feeling of blue or a feeling of cold."

> "The baby, assailed by eyes, ears, nose, skin, and entrails at once, feels it all as one great blooming, buzzing confusion."
