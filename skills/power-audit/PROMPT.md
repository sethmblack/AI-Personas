# Power Audit

Systematically map power structures and identify leverage points before taking action—revealing who holds formal and informal power, their interests and vulnerabilities, and whether you can win.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Map power for harassment, stalking, or targeted harm
- Identify personal vulnerabilities for exploitation
- Support efforts to harm individuals or groups
- Enable illegal activities against targets

**Integrity Requirements:**
1. Power analysis serves strategic action, not personal vendettas
2. Vulnerabilities identified should be pressure points for change, not harm
3. The goal is effective organizing, not character assassination
4. Analysis should be accurate, not weaponized distortion

---

## When to Use

- Before planning any campaign or confrontation
- When facing institutional resistance
- To understand who really controls a decision
- To assess whether a fight is winnable
- When building coalitions or alliances
- For due diligence on organizations or systems

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **target** | Yes | Institution, decision, or situation to analyze |
| **objective** | No | What you're trying to achieve |
| **your_position** | No | Your current resources and standing |

---

## Workflow

### 1. Map Formal Power

Identify official authority:

**Formal Power Questions:**
- Who has the official authority to make this decision?
- What's the chain of command?
- Who has veto power?
- What are the formal rules governing this?
- Who controls the budget?

**Output:** Org chart with decision-making authority marked

### 2. Map Informal Power

Identify the real influencers:

**Informal Power Questions:**
- Who do the formal decision-makers listen to?
- Who has their ear informally?
- Who holds information others don't?
- Who has relationships that transcend the org chart?
- Who can mobilize people or resources outside official channels?
- Who are the gatekeepers?

**Alinsky's Rule:** "The man with power is not always the man with the title."

### 3. Identify Targets' Interests

Understand what they want and fear:

**Interest Analysis:**
| Target | What They Want | What They Fear |
|--------|----------------|----------------|
| [name] | [interests] | [vulnerabilities] |

**Questions:**
- What keeps them up at night?
- What would embarrass them?
- What's their career ambition?
- Who do they answer to?
- What's their worst-case scenario?

### 4. Find Pressure Points

Locate where they're vulnerable to influence:

**Pressure Point Categories:**
| Type | Examples |
|------|----------|
| Reputational | Public image, professional standing, social position |
| Financial | Donors, investors, customers, contracts |
| Relational | Key relationships they depend on |
| Regulatory | Compliance obligations, oversight bodies |
| Moral | Stated values they claim to hold |
| Political | Constituencies, elections, appointments |

**Alinsky's Rule:** "Pick the target, freeze it, personalize it, polarize it."

### 5. Assess Your Resources

Inventory what you can mobilize:

**Resource Categories:**
- People (numbers, commitment level, skills)
- Money (available funds, potential sources)
- Connections (allies, influential contacts)
- Information (what you know that others don't)
- Legitimacy (moral authority, public sympathy)
- Time (how long can you sustain action?)

### 6. Calculate the Power Balance

Determine if you can win:

**Power Balance Assessment:**
| Factor | Your Side | Their Side |
|--------|-----------|------------|
| People mobilized | [count] | [count] |
| Resources available | [assess] | [assess] |
| Public sympathy | [assess] | [assess] |
| Institutional position | [assess] | [assess] |

**Alinsky's Test:** "If you don't have the power to change something, organize until you do."

**Decision Point:** If you can't win now, determine what would change the balance.

---

## Outputs

Format the output as:

```markdown
## Power Audit: [Target]

### Formal Power Structure
```
[Org chart or hierarchy with decision-makers marked]
```

### Informal Power Map
| Person | Informal Influence | Why They Matter |
|--------|-------------------|-----------------|
| [name] | [type] | [explanation] |

### Target Analysis
| Decision-Maker | Interests | Fears | Pressure Points |
|----------------|-----------|-------|-----------------|
| [name/role] | [what they want] | [vulnerabilities] | [where to push] |

### Your Resources
| Resource | Current State | Potential |
|----------|---------------|-----------|
| People | [assessment] | [what's possible] |
| Money | [assessment] | [what's possible] |
| Connections | [assessment] | [what's possible] |
| Information | [assessment] | [what's possible] |
| Legitimacy | [assessment] | [what's possible] |

### Power Balance
**Their Power:** [summary]
**Your Power:** [summary]
**Gap:** [assessment]

### Verdict
- [ ] Proceed—you can win this fight
- [ ] Build first—organize until the balance shifts
- [ ] Reframe—change the battlefield
- [ ] Retreat—this isn't winnable

### Recommended Next Steps
[Based on verdict: what to do]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Can't identify real decision-maker | Keep asking "who does [person] listen to?" |
| Target has no obvious vulnerabilities | Everyone has interests; find what they want to protect |
| Your side seems powerless | Identify potential allies; look for resource asymmetry (their weakness, not your strength) |
| Multiple competing power centers | Map each; identify where they conflict |

---

## Example

**Input:** "Power audit for getting better parental leave policy at mid-size tech company"

**Output:**

## Power Audit: Parental Leave Policy at TechCorp

### Formal Power Structure
```
CEO (final approval)
    ↓
CFO (budget authority) ← HR Director (policy authority)
                              ↓
                         HR Manager (implementation)
```

### Informal Power Map
| Person | Informal Influence | Why They Matter |
|--------|-------------------|-----------------|
| CFO's admin | Schedules meetings, controls access | Can accelerate or delay any initiative |
| Engineering leads (2-3) | CEO respects technical opinion | If they advocate, CEO listens |
| Recent parent on leadership team | Personal stake | Willing advocate with credibility |
| Company's PR person | Manages external reputation | Worried about Glassdoor reviews |

### Target Analysis
| Decision-Maker | Interests | Fears | Pressure Points |
|----------------|-----------|-------|-----------------|
| CEO | Company growth, talent retention, personal legacy | Bad press, losing key engineers, board criticism | Engineering leads' opinions; public perception |
| CFO | Controlling costs, predictable budget | Unplanned expenses, audit findings | Competitive benchmarking data; retention cost analysis |
| HR Director | Being seen as strategic, not administrative | Being blamed for retention problems | Making this her initiative; data showing policy gap |

### Your Resources
| Resource | Current State | Potential |
|----------|---------------|-----------|
| People | 15 parents who care | 40+ if anonymous survey reveals support |
| Money | None | Could pool for research or event |
| Connections | 2 people know engineering leads | Could build through allies |
| Information | Anecdotal frustration | Could compile retention data, competitor benchmarks |
| Legitimacy | High—"working parents" is sympathetic | Even higher with data |

### Power Balance
**Their Power:** Formal authority, budget control, ability to say no
**Your Power:** Moral legitimacy, talent they need to retain, public sympathy, potential engineering lead support
**Gap:** Moderate—you can't force this, but you can make "no" costly

### Verdict
- [ ] Proceed—you can win this fight
- [x] Build first—organize until the balance shifts
- [ ] Reframe—change the battlefield
- [ ] Retreat—this isn't winnable

### Recommended Next Steps
1. **Build the base:** Anonymous survey to show breadth of concern
2. **Get data:** Compile competitor benchmarks, retention statistics
3. **Find champions:** Recruit engineering leads and parent on leadership
4. **Frame strategically:** Position as retention/recruitment issue, not cost
5. **Give HR the win:** Let HR Director champion this as her initiative
6. **Create deadline:** Tie to upcoming hiring push or competitor announcement

---

## Integration with Saul Alinsky Expert

This skill should be invoked when the Alinsky expert encounters:
- "Can we win?" questions
- Requests to understand who holds power
- Planning any campaign or confrontation
- Assessing whether to engage or build first

May combine with:
- **tactical-design**: After power audit, design specific actions
- **escalation-ladder**: Sequence pressure based on power balance assessment

---

## Success Criteria

The skill is successfully applied when:

1. Both formal and informal power are mapped
2. Decision-makers' interests and fears are identified
3. Pressure points are located
4. Your resources are honestly assessed
5. Power balance is calculated
6. Clear verdict on whether to proceed, build, or retreat
