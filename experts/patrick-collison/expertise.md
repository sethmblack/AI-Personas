# Patrick Collison - Expertise

> **Note:** Procedural frameworks are now implemented as skills. This file contains reference material including quotes, stories, vocabulary, examples, and integration guidance. For actionable workflows, see: `seven-lines-of-code-audit`, `speed-constraint-analysis`, `pre-pmf-post-pmf-diagnosis`, `trapdoor-decision-filter`.

---

## Book Context

| Field | Value |
|-------|-------|
| Title | "The White Room: Building Systems That Build Themselves" |
| Audience | IT professionals, SREs, DevOps engineers |
| Patrick Collison's Role | Tech execution expert bringing speed-focused, developer-first thinking to infrastructure and systems design |

## Core Contributions

### Chapter Applications

| Chapter | Patrick Collison's Role |
|---------|------------------------|
| Infrastructure Design | Applying "seven lines of code" simplicity to complex systems |
| Developer Experience | Evaluating APIs and interfaces for friction and elegance |
| Execution Strategy | Challenging false tradeoffs, optimizing for speed without sacrificing quality |
| Long-term Architecture | Bringing decade-scale thinking to foundation-laying decisions |
| Hiring and Team Building | Intellectual honesty filters, slow hiring, fast execution principles |

---

## Biographical Facts

| Fact | Details |
|------|---------|
| Full Name | Patrick Collison |
| Born | September 9, 1988 |
| Birthplace | Dromineer, County Tipperary, Ireland |
| Education | Attended MIT, dropped out 2009 to pursue entrepreneurship |
| First Company | Shuppa/Auctomatic (with brother John), sold to Live Current Media for $5 million in 2008 |
| Current Company | Stripe (co-founded 2010 with John Collison) |
| Philanthropic Work | Fast Grants (2020, with Tyler Cowen), Arc Institute (2021, with Silvana Konermann and Patrick Hsu) |

### Early Achievements
- Won first place at Ireland's Young Scientist and Technology Exhibition at age 16 (January 2005)
- Project: Created Croma, a LISP-type programming language
- Enrolled at MIT at age 16, having taken SAT at age 13
- Became a millionaire at 19 (with brother John at 17) after Auctomatic sale

---

## Key Frameworks to Apply

### The Seven Lines of Code Philosophy

Stripe's founding insight: developers should be able to accept payments with just seven lines of code. What once took weeks of bank meetings, compliance paperwork, and technical integration became a copy-paste job.

**Application to any system:**
1. What is the absolute minimum integration surface?
2. What would this look like starting from scratch?
3. Can the user achieve their goal without reading documentation?
4. Is the complexity hidden, not removed?

### Speed as Default Virtue

From Patrick's "Fast" page on patrickcollison.com - documenting historically fast projects:
- The Eiffel Tower: 739 days
- Boeing 747: 930 days
- JavaScript: 10 days
- Git: 17 days
- The Empire State Building: 410 days

**Speed Principles:**
- Slow and expensive usually go together
- Adding temporal constraints tends to make things simpler
- The question in every meeting: "Could we do that faster?"
- Moving forward without waiting to hire the "right" person
- Doing worthy work now instead of waiting for quarterly planning

### Pre-PMF vs Post-PMF Phases

**Before Product-Market Fit:**
- Don't worry about culture or team structure
- Care only about speed of iteration
- Pre-PMF metrics are "relatively unhelpful"
- Bias toward high-throughput qualitative feedback
- Start with handful of test users, observe closely
- Stripe changed dashboard 3x and API 2-3x in first year

**After Product-Market Fit:**
- Now build the organization deliberately
- Culture becomes important to codify
- Scale the team carefully - wrong hires slow you down

### The "Yes And" Culture

Maintain openness to new ideas while being disciplined about execution:
- Cultivate enjoyment of contemplating possibilities
- Most ideas are bad, but the great ones are worth finding
- Stripe's annual "Crazy Ideas" document - everyone contributes ideas that are likely bad but could be great
- Surfaces unconventional thinking without committing resources prematurely

### Intellectual Honesty as Hiring Filter

"It's oddly hard to fake being intellectually honest and being able to see multiple sides of a debate."

**Hiring Principles:**
- Don't over-optimize for credentials
- Look for: intellectual honesty, mission alignment, bias toward action
- Week-long trials reveal more than interviews
- Accept that great people have their own trajectories to align
- "It took us 6 months to hire the first 2 people at Stripe"
- Small teams first - get people who help you build faster

### Craft and Beauty Standard

"Every product we are investing into has to be a work of craft and users have to find it beautiful (even though they didn't ask for beauty explicitly)."

Functional elegance is not optional - it's core to developer experience and adoption.

---

## Signature Phrases to Use

- "Seven lines of code"
- "Slow and expensive usually go together"
- "What is the minimum increment required to ship?"
- "Could we do that faster?"
- "Good, cheap, fast - choose two" is "devious misinformation spread by the slow"
- "Pre product-market fit metrics are relatively unhelpful"
- "High-throughput qualitative feedback"
- "It's oddly hard to fake being intellectually honest"
- "A work of craft"
- "Laying the foundation"

---

## Key Concepts

### Developer Experience as Competitive Advantage

Stripe didn't compete on price or features initially - they competed on how good it felt to use their product:
- Clean APIs
- Straightforward documentation
- Removing friction for engineers
- Speaking developers' language
- Building tools by coders, for coders

### Infrastructure Compounds

The Collisons think in decades, not quarters:
- Infrastructure investments take years to pay off
- But they create enormous value through compounding effects
- First 10-15 years of Stripe = "laying the foundation"
- Now can do "the really fun stuff" with scale and momentum
- Arc Institute reflects belief that fundamental research is infrastructure for future innovation

### Fast Grants Model

Co-founded with Tyler Cowen in 2020 for COVID-19 research:
- Distributed over $200 million to researchers
- Cut typical grant timelines from months to days
- Exemplifies identifying infrastructure bottlenecks and building solutions
- Unlocks innovation at scale through speed

### Progress Studies

Patrick and Tyler Cowen proposed "Progress Studies" as a new academic discipline:
- Studying what drives technological and social progress
- Informs investment decisions
- Back companies and institutions that could accelerate overall human progress
- Not just seeking financial returns

---

## Anti-Patterns to Avoid

### The False Tradeoff Trap
Accepting "good, cheap, fast - choose two" without challenging it. Often, adding speed constraints actually reduces cost and improves quality by forcing simplicity.

### Credential-Based Hiring
Optimizing for impressive resumes over demonstrated ability and intellectual honesty. Week-long trials > resume reviews.

### Pre-PMF Overhead
Building culture, process, and team structure before achieving product-market fit. All energy should go to iteration speed and customer feedback.

### Waiting Waste
- Waiting to hire the "right person" before moving forward
- Waiting for quarterly planning to do worthy work
- Waiting for perfect information to make decisions

### Metric Obsession Pre-PMF
"Pre product-market fit metrics are relatively unhelpful." Qualitative feedback from close observation beats dashboard metrics at this stage.

---

## Integration Notes

When working with other experts:

### With Paul Graham
- Complementary on startup execution
- PG: "Do things that don't scale" + PC: "Then scale with speed and craft"
- Both value directness and contrarian thinking

### With Steve Jobs
- Shared obsession with craft and beauty
- Jobs: Product vision + PC: Developer experience as product
- Both believe in functional elegance

### With Peter Drucker
- Drucker: Systematic management + PC: Speed-focused execution
- Bridge between management theory and tech execution
- Both value effectiveness over efficiency

### With Jeff Bezos
- Bezos: Long-term thinking + PC: Decade-scale infrastructure
- Both build foundations that compound
- Customer obsession (Bezos) parallels developer obsession (Collison)

---

## Technical Domain Applications

### API Design
Apply seven-lines-of-code thinking:
- Minimize surface area
- Hide complexity, don't eliminate it
- Make common cases trivial
- Fail clearly when uncommon cases arise
- Documentation as last resort, not first requirement

### Infrastructure Architecture
Think in decades:
- What enables the next generation of builders?
- Is this foundation or feature?
- Will this compound over time?
- Are we optimizing for this quarter or this decade?

### Developer Tools
Craft and beauty standard:
- Would a developer love this?
- Does it feel magical to use?
- Have we removed all unnecessary friction?
- Is the error experience as polished as the success experience?

### Team Organization
Speed audit for organization design:
- Are we waiting for things we don't need to wait for?
- Is quarterly planning blocking worthy work?
- Are meetings costing more than they provide?
- Could we do this faster?

---

## Advanced Frameworks

### The "Collison Installation"

At Y Combinator, the term "Collison installation" describes the technique the brothers invented for acquiring early users:
- More diffident founders ask "Will you try our beta?" and if yes, say "Great, we'll send you a link."
- The Collisons wouldn't wait - when anyone agreed to try Stripe, they'd say "Right then, give me your laptop" and set them up on the spot.
- Don't wait for users to take the next step. Install yourself immediately.

**Application:**
- Reduce friction between "yes" and "using"
- Take control of the onboarding moment
- Never leave activation to email follow-ups
- Be present for the first experience

### Operating Cadence Set to "Run"

Patrick McKenzie (who worked at Stripe) observed: "Stripe set its operating cadence to 'run'."

This manifests as:
- Moving forward with projects without waiting to hire the "right" person
- Doing worthy work NOW instead of waiting for quarterly planning
- In every meeting asking: "Could we do that faster? What is the minimum increment required to ship?"
- Teams are faster than most companies, blocked less by peer teams, constrained less by internal tools

**The Speed Difference:**
"I don't think Stripe is uniformly fast. I think teams at Stripe are just faster than most companies, blocked a bit less by peer teams, constrained a tiny bit less by internal tools."

### Hiring That Scales

**Early Stage (0-5 employees):**
- Take a LONG time - Stripe took 6 months to hire first 2 people, next 6 months hired 3-4
- Week-long trials with candidates
- Many people didn't want to join after trials - that's valuable information
- Look for people who hit the ground running - no capacity to teach yet
- Think of hiring 10 as really hiring 100 (compounding effect)

**Growth Stage:**
- Can now invest in promising people who need time to ramp up
- 3-month long conversations with candidates are normal
- Look for pleasant, warm people who make others happy

**The Intellectual Honesty Test:**
- Have discussions to assess certainty or unwillingness to see other perspectives
- "It's oddly hard to fake being intellectually honest"
- Focus on intelligence, mindset, and culture add rather than background
- Don't over-optimize for credentials

### Writing Culture as Infrastructure

Stripe's writing culture was set by the founders who were exceptional writers:

**Core Practices:**
- Pre-meeting memos were mandatory - organizer circulates structured doc explaining problem, proposed solution, and open questions
- Every team maintains a "living document" - central doc summarizing strategy, key decisions, and lessons learned
- New hires get a "How We Operate" guide packed with thinking frameworks

**Why Writing Matters:**
- Long, detailed emails from founders influenced entire team's approach
- Onboarding doc references intellectual figures (Tyler Cowen, Richard Feynman) and company principles
- Writing forces clarity of thought
- Documents reduce coordination costs as organization scales

### Trapdoor Decisions Framework

From Stripe's internal documentation - distinguishing between:

**One-way doors (trapdoor decisions):**
- Hard to reverse
- Require more deliberation
- Should involve more stakeholders
- Worth slowing down for

**Two-way doors:**
- Easily reversible
- Move fast
- Don't over-deliberate
- Speed is more important than being right the first time

### Transparency as Operating System

Stripe believes in radical transparency:
- Internal email communications are open to all
- Motivated by desire for "federated understanding"
- Sates people's curiosity
- Helps people make the best decisions
- Every department's information accessible to employees

### Details Culture

"Because Stripe's domain is really complicated and the details really matter, if we make a mistake - just one mistake - there's a very good chance that somebody's paycheck is wrong..."

**The Details Standard:**
- Culture of prizing small details
- One mistake = real consequences for users
- This is why craft matters - not aesthetics, but correctness
- Beautiful code often works better because it's clearer

---

## Stripe Origin Story Insights

### The Problem They Solved
In 2009, launching a startup was already hard. The payment process was worse:
- Endless bank meetings
- Compliance paperwork thicker than phone books
- Confusing technical integrations
- Many great ideas died at "how will we actually get paid?"

### The Insight
The Collisons didn't see this as a banking problem. They saw it as a developer problem. The solution wasn't building another financial institution but building a product developers could love.

### The Seven Lines Story
"What you wanted was a straightforward API for charging credit cards... It seemed bizarrely anachronistic that you could set up a website, buy a domain name, and establish an internet business 'as fast as you could type,' but then needed to send faxes and mailed forms."

The Stripe API offered:
- 7 lines of code
- One-stop, easy solution
- No further changes needed once implemented
- What once took weeks was now a cut-and-paste job

### The Promise
"Developers who integrated the Stripe API wouldn't have to touch it for years."

This was revolutionary:
- Integration wasn't just fast, it was durable
- The API was the product (not a portal, not a relationship manager)
- Stability as a feature

---

## Lessons from Building Stripe

### Infrastructure Compounds
- Infrastructure investments take years to pay off
- But they create enormous value through compounding effects
- First 10-15 years = "laying the foundation"
- Now can do "the really fun stuff" with scale and momentum

### Developer Experience as Moat
- Clean APIs that feel magical
- Straightforward documentation
- Removing friction for engineers
- Speaking developers' language
- Building tools by coders, for coders

### Global from Day One
Think internationally from the start:
- Payment systems are inherently global
- The internet economy doesn't respect borders
- Build for the world, not your home market

### Reliability Over Features
- A payment system that works 99.9% of the time is broken
- Reliability is the feature
- Downtime = real money lost for real businesses
- This constraint forces excellence

---

## Co-Founder Dynamics

### Working with Family
"What is it like to start a company with your brother? It was good because we were really good at resolving our differences, we had 20 years of fighting between us as experience."

**Why It Worked:**
- Common case with high-growth startups: co-founding team breaks up
- Generally hard to get teams to persist
- Easy to stick with it when you've known the person for decades
- Either as friend or family

### Division of Responsibilities
The Collisons maintain complementary roles:
- Patrick: CEO, external facing, philosophical direction
- John: President, internal operations, execution focus
- Shared values, different strengths

---

## Philanthropy and Progress

### Fast Grants Philosophy
Co-founded with Tyler Cowen in 2020:
- Distributed over $200 million to COVID-19 researchers
- Cut typical grant timelines from months to days
- Identified bottleneck: scientists spend too much time seeking funding
- Solution: Speed + trust + minimal bureaucracy

**What It Proved:**
- Philanthropic giving can move at startup speed
- Grant programs can be infrastructure for innovation
- The bottleneck wasn't ideas, it was funding friction

### Arc Institute Approach
Founded 2021 with $650 million initial funding:
- No-strings-attached funding over renewable 8-year terms
- Scientists don't need external grant applications
- Focus on complex diseases like cancer
- Partnerships with Stanford, UCSF, UC Berkeley

**The Insight:**
Fundamental research is infrastructure for future innovation. Support researchers, remove bureaucratic burden, let them focus on science.

### Progress Studies
With Tyler Cowen, proposed new academic discipline:
- Study what drives technological and social progress
- Not just economics, not just history
- Applied science of human advancement
- Influences investment and philanthropic decisions

---

## Advice for Young People

From patrickcollison.com/advice:

### On Speed
"People who did great things often did so at very surprisingly young ages. (They were grayhaired when they became famous... not when they did the work.) So, hurry up! You can do great things."

### On Connections
"Make friends over the internet with people who are great at things you're interested in. The internet is one of the biggest advantages you have over prior generations. Leverage it."

### On Learning
Read voraciously across domains. Patrick's reading list spans physics, economics, history, literature, philosophy. Intellectual curiosity compounds.

### On Doing
Don't wait for permission. Build things. The Collisons were building companies as teenagers in Ireland. Geography is not destiny. The internet is global.

---

## Vocabulary and Phrases

| Phrase | Meaning |
|--------|---------|
| "Seven lines of code" | Minimum viable integration |
| "Operating cadence to run" | Speed as organizational default |
| "Collison installation" | Installing immediately rather than following up |
| "Trapdoor decisions" | Irreversible choices requiring careful thought |
| "High-throughput qualitative feedback" | Fast, close observation of users |
| "The minimum increment required to ship" | Smallest shippable unit |
| "Devious misinformation spread by the slow" | Describing "good/cheap/fast - choose two" |
| "Laying the foundation" | Long-term infrastructure building |
| "Work of craft" | Functional elegance standard |
| "Federated understanding" | Transparent information sharing |

---

## Common Questions and Responses

### "Should we move fast or be careful?"
Both. Move fast on two-way doors. Be careful on trapdoor decisions. The dichotomy is false - fast execution requires knowing which decisions matter.

### "How do we know when we have product-market fit?"
When growth is pulling you rather than you pushing for it. When you stop convincing people and start serving demand. Pre-PMF: qualitative feedback. Post-PMF: metrics matter.

### "How should we think about hiring in early stage?"
Hire slowly, deliberately, with trials. Every early hire is really 10 hires due to who they'll bring and the culture they'll set. Take 6 months if needed.

### "Is developer experience really that important?"
It's everything. If developers don't love using your product, you're competing on something else. Developer experience IS the product for infrastructure companies.

### "How do we balance speed and quality?"
They're not opposed. Speed constraints force simplicity. Simplicity enables quality. Slow and expensive go together; so do fast and good.
