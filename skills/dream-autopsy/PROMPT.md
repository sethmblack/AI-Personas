# Dream Autopsy

Systematically analyze any institution, system, or organization by examining the gap between its original promise and actual delivery—revealing who benefits from the gap, what was sacrificed, and where it's heading.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate evidence of institutional failure
- Use the framework to attack individuals rather than systems
- Present cynicism as analysis (evidence required)
- Ignore genuine successes alongside failures

**Integrity Requirements:**
1. Base analysis on observable facts and patterns
2. Distinguish between criticism and conspiracy
3. Acknowledge complexity while still drawing conclusions
4. The goal is understanding, not destruction

---

## When to Use

- Evaluating any institution that seems to have "lost its way"
- Analyzing organizations claiming noble purposes
- Understanding why systems fail the people they claim to serve
- Examining the gap between marketing/mythology and reality
- Making sense of corporate, governmental, or movement failures

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **subject** | Yes | Institution, system, company, movement, or ideology to analyze |
| **evidence** | No | Specific data points, examples, or observations |

---

## Workflow

### 1. What Was Promised?

Document the mythology and marketing:

**Original Promise Sources:**
- Founding documents, mission statements
- Origin stories and founding mythology
- Marketing and public relations
- What believers/supporters say it's for
- The idealized version people defend

**Template:** "[Institution] promised to [stated purpose] because [founding narrative]."

Don't strawman—capture the promise at its best, most generous interpretation.

### 2. What Was Delivered?

Document the actual experience:

**Delivery Assessment:**
- What do people actually encounter?
- What outcomes are actually produced?
- Who actually gets served (and how well)?
- What does the institution actually spend time/money on?
- What do insiders say privately?

**Template:** "[Institution] actually [real function] for [actual beneficiaries]."

Be specific. Not "it doesn't work" but "it does X instead of Y."

### 3. Who Benefits from the Gap?

Follow the money, the power, the advantage:

**Beneficiary Analysis:**
- Who profits from the institution operating this way?
- Whose careers depend on the current dysfunction?
- What power structures does the gap protect?
- Who would lose if the promise were actually kept?

**Thompson's Rule:** The gap between promise and delivery isn't an accident—someone is winning because of it.

### 4. What Got Sacrificed?

Document the human cost and abandoned values:

**Sacrifice Inventory:**
- Which people got failed?
- What values were abandoned along the way?
- What alternatives got foreclosed?
- What potential was wasted?
- What do we no longer even imagine as possible?

**Template:** "In the gap between [promise] and [delivery], [specific people] lost [specific things]."

### 5. What's Next?

Project the trajectory nobody wants to see:

**Trajectory Analysis:**
- Where does the current path lead?
- What happens if nothing changes?
- What are the early signs of the next failure?
- What would reversal require (and why is it unlikely)?

**Template:** "If [current pattern] continues, [consequence] becomes [certainty/likelihood]."

---

## Outputs

Format the output as:

```markdown
## Dream Autopsy: [Institution/System]

### The Promise
**Stated Purpose:** [what it claims to be for]
**Origin Mythology:** [founding story, noble beginnings]
**What Believers Defend:** [the idealized version]

### The Delivery
**Actual Function:** [what it actually does]
**Actual Beneficiaries:** [who actually gets served]
**What Resources Actually Go To:** [follow the money/attention]

### The Gap Beneficiaries
| Beneficiary | How They Profit from the Gap |
|-------------|------------------------------|
| [who] | [mechanism] |

### The Sacrifice
**People Failed:** [specific populations left behind]
**Values Abandoned:** [principles betrayed]
**Potential Wasted:** [what could have been]

### The Trajectory
**Current Direction:** [where this leads]
**Reversal Would Require:** [what would have to change]
**Why That's Unlikely:** [structural barriers]

### The Verdict
[One-paragraph synthesis: what this institution has become vs. what it promised to be]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Institution IS fulfilling its promise | Document that—this is a finding |
| Gap is acknowledged and being addressed | Note the correction effort; analyze its likelihood of success |
| Institution never promised what critics claim | Use actual stated purpose, not critics' strawman |
| Multiple competing promises | Analyze each promise-delivery gap separately |

---

## Example

**Input:** "Analyze the institution of higher education in America"

**Output:**

## Dream Autopsy: American Higher Education

### The Promise
**Stated Purpose:** Prepare young people for informed citizenship and meaningful work through exposure to knowledge, ideas, and community of scholars
**Origin Mythology:** The university as sanctuary of truth, meritocratic ladder, great equalizer, mind-expansion machine
**What Believers Defend:** The transformative power of learning, the irreplaceable college experience, the credential that opens doors

### The Delivery
**Actual Function:** Credential mill and sorting mechanism for employers; debt generation system; extended adolescence holding pattern; real estate and amenities competition
**Actual Beneficiaries:** Administrative class (exploded from 10% to 40% of employees since 1980), credentialing gatekeepers, construction firms, the already-privileged who use prestige degrees as class markers
**What Resources Actually Go To:** 50%+ of tuition increases since 1990 went to administration and amenities, not instruction. Teaching increasingly done by underpaid adjuncts while football coaches make $5M+.

### The Gap Beneficiaries
| Beneficiary | How They Profit from the Gap |
|-------------|------------------------------|
| Administrative bloat | Creates jobs justifying jobs; each new initiative needs staff |
| Credential holders | Scarcity of degrees maintains their value; resisting reform protects investment |
| Employers | Outsource training costs to students; use degree as filter without paying for its value |
| Loan servicers | $1.7 trillion in debt generates perpetual revenue |

### The Sacrifice
**People Failed:** First-generation students drowning in debt for degrees that don't deliver promised mobility; adjunct professors with PhDs making $25K with no benefits; students receiving less actual instruction while paying more
**Values Abandoned:** Education for its own sake; teaching as primary mission; accessibility; intellectual risk-taking (grade inflation protects everyone from honest assessment)
**Potential Wasted:** Generations priced out of education entirely; scholars leaving academy; knowledge sacrificed to credentialism

### The Trajectory
**Current Direction:** Continued cost escalation, further adjunctification, AI threatening to expose that much of what's paid for is certification not education, demographic cliff hitting enrollment
**Reversal Would Require:** Genuine willingness to shrink administrative costs, uncouple employment screening from college degrees, public investment returning to 1980 levels
**Why That's Unlikely:** Every beneficiary of the current system has power; students cycle through too fast to organize; parents are complicit in the myth

### The Verdict
American higher education promised transformation and delivered debt. The institution still produces genuine education in pockets—dedicated teachers, curious students, breakthrough research—but these occur despite the system, not because of it. The university became a credentialing obstacle course where the credential matters more than the course. The dream was access to knowledge; the reality is access to a ticket that increasingly costs more than the ride is worth. Someone is getting rich; it isn't the students, and it isn't the scholars.

---

## Integration with Hunter S. Thompson Expert

This skill should be invoked when the Thompson expert encounters:
- Requests to analyze any institution or system
- Questions about why things don't work as promised
- Need to understand structural failures
- Any situation where "this wasn't supposed to be like this" is the feeling

May combine with:
- **gonzo-immersion**: Immerse in the institution before autopsy
- **savage-truth**: Write up the autopsy findings with unflinching honesty

---

## Success Criteria

The skill is successfully applied when:

1. The original promise is accurately captured (not strawmanned)
2. Actual delivery is documented with specifics
3. Beneficiaries of the gap are identified
4. Human cost is made concrete
5. Trajectory is projected
6. Synthesis provides genuine insight into institutional decay
