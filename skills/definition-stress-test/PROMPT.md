# Definition Stress Test

Test whether definitions, categories, or criteria are robust by finding absurd edge cases that technically satisfy the definition but violate its intent—exposing weaknesses before they cause problems.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use edge cases to dismiss legitimate concepts through sophistry
- Generate edge cases for harmful categories (e.g., testing definitions that could enable discrimination)
- Present gotchas as wisdom when the definition is actually functional

**Integrity Requirements:**
1. Apply the test fairly to the definition as actually used
2. Acknowledge when definitions are robust enough for their purpose
3. Offer constructive refinements, not just critique

---

## When to Use

- Evaluating definitions in policies, criteria, or specifications
- Testing hiring criteria before use
- Reviewing legal or contractual language
- Auditing taxonomies and classification systems
- Checking if categories will hold up in practice
- Preventing "letter of the law" violations of intent

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **definition** | Yes | The definition, category, or criteria to test |
| **purpose** | No | What the definition is trying to accomplish |

---

## Workflow

### 1. State the Definition Clearly

Capture the exact definition being tested:

**Template:** "[Term] is defined as [criteria/conditions]"

Identify:
- Necessary conditions (must have)
- Sufficient conditions (enough to qualify)
- Boundary markers (what's excluded)

### 2. Find the Plucked Chicken

Generate edge cases that:
- Technically satisfy all stated criteria
- Are clearly absurd or unintended
- Expose what the definition failed to capture

**The Diogenes Method:** When Plato defined "man" as a "featherless biped," Diogenes plucked a chicken and presented it: "Behold, Plato's man!"

**Edge Case Categories:**
| Type | Method |
|------|--------|
| Literal compliance | Follow letter while violating spirit |
| Boundary straddling | Find cases exactly at the edge |
| Unexpected satisfiers | What else technically qualifies? |
| Missing exclusions | What should be out but isn't? |
| Context collapse | Would this work in a different context? |

### 3. Expose the Weakness

For each edge case, articulate:
- Why it technically satisfies the definition
- Why it violates the apparent intent
- What the definition failed to specify

### 4. Suggest Refinements

Propose how to strengthen the definition:
- Additional necessary conditions
- Explicit exclusions
- Intent clauses
- Context boundaries

---

## Outputs

Format the output as:

```markdown
## Definition Stress Test: [Term]

**Definition Under Test:**
"[exact definition]"

**Apparent Intent:**
[what the definition seems to be trying to accomplish]

### Edge Cases Found

#### 1. [Edge Case Name]
**The Case:** [description]
**Why It Technically Qualifies:** [how it meets stated criteria]
**Why It's Absurd:** [how it violates intent]
**Weakness Exposed:** [what the definition failed to capture]

#### 2. [Edge Case Name]
[repeat structure]

### Robustness Assessment
- [ ] Definition is robust for its purpose
- [ ] Minor refinements needed
- [ ] Significant gaps exist
- [ ] Definition is fundamentally flawed

### Suggested Refinements
| Current Gap | Proposed Addition |
|-------------|-------------------|
| [weakness] | [fix] |

### Refined Definition
"[improved definition incorporating fixes]"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Definition withstands all tests | Report it as robust; this is success |
| Edge cases are unrealistic | Note unreality but still document the gap |
| Definition is purpose-built for specific context | Test within that context |
| Definition is intentionally broad | Test whether breadth is feature or bug |

---

## Example

**Input:** "Test this hiring criterion: 'Candidates must have 5+ years of relevant experience'"

**Output:**

## Definition Stress Test: "5+ Years Relevant Experience"

**Definition Under Test:**
"Candidates must have 5+ years of relevant experience"

**Apparent Intent:**
Ensure candidates have sufficient depth of practice to perform at senior level

### Edge Cases Found

#### 1. The Plucked Chicken: Repeated Year One
**The Case:** Candidate with 5 years at same job doing same tasks, never growing
**Why It Technically Qualifies:** 5 years have elapsed; work was in the field
**Why It's Absurd:** 1 year of experience repeated 5 times ≠ 5 years of growth
**Weakness Exposed:** "Years" measures time, not learning or capability

#### 2. The Adjacent Dabbler
**The Case:** 5 years in adjacent field with occasional overlap
**Why It Technically Qualifies:** "Relevant" is undefined; they can argue relevance
**Why It's Absurd:** Tangential experience may not transfer
**Weakness Exposed:** "Relevant" needs definition

#### 3. The Credential Without Practice
**The Case:** 5 years employed in role but minimal actual practice (management, leave, etc.)
**Why It Technically Qualifies:** 5 years on the payroll in the title
**Why It's Absurd:** Title ≠ practice
**Weakness Exposed:** Employment duration ≠ practice hours

#### 4. The Prodigy Exclusion
**The Case:** Exceptional candidate with 3 years who outperforms 10-year veterans
**Why They Don't Qualify:** Fails the 5-year threshold
**Why It's Absurd:** Capability exists; arbitrary cutoff excludes it
**Weakness Exposed:** Time proxy may exclude best candidates

### Robustness Assessment
- [ ] Definition is robust for its purpose
- [ ] Minor refinements needed
- [x] Significant gaps exist
- [ ] Definition is fundamentally flawed

### Suggested Refinements
| Current Gap | Proposed Addition |
|-------------|-------------------|
| Time ≠ learning | Add "progressive responsibility" or "demonstrated growth" |
| "Relevant" undefined | Specify which domains/skills count |
| Title ≠ practice | Add "hands-on" or specify practice hours |
| Excludes prodigies | Add "or equivalent demonstrated capability" |

### Refined Definition
"Candidates must demonstrate 5+ years of progressive, hands-on experience in [specific domains], OR equivalent capability demonstrated through [portfolio/test/references]"

---

## Integration with Diogenes Expert

This skill should be invoked when the Diogenes expert encounters:
- Definitions that seem too neat
- Categories being used to include/exclude
- Policies or criteria under development
- Arguments that depend on precise definitions

May combine with:
- **lantern-audit**: Test if the definition is even followed in practice
- **barrel-reduction**: Eliminate unnecessary definitional complexity

---

## Success Criteria

The skill is successfully applied when:

1. The definition is accurately stated
2. Multiple edge cases are generated
3. Each edge case's absurdity is clearly articulated
4. Weaknesses are precisely identified
5. Constructive refinements are offered
