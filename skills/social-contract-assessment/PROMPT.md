# Social Contract Assessment

Evaluate whether an arrangement, institution, or authority has genuine legitimacy based on consent and service to the common good.

**Token Budget:** ~550 tokens
**Source Expert:** Jean-Jacques Rousseau

---

## When to Use

- Evaluating organizational governance structures
- Assessing whether leadership has legitimate authority
- Analyzing policies for consent basis
- Questioning institutional arrangements
- Any situation where "this is how it's done" masks illegitimate authority
- When obedience is expected but legitimacy is unclear

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **institution_or_authority** | Yes | The arrangement, structure, or authority to assess |
| **those_governed** | Yes | Who is subject to this authority |
| **claimed_justification** | No | How legitimacy is claimed |
| **current_functioning** | No | How the authority actually operates |

---

## Core Principles from The Social Contract

### Legitimacy Requires Consent
"Man is born free" — no one has natural authority over another. Legitimate authority must arise from agreement.

### Consent Must Be Genuine
- Not coerced or manipulated
- Made by those affected
- Renewable, not merely historical

### Authority Must Serve the General Will
Legitimate authority exists to serve the common good, not private interests of rulers.

### Freedom Through Obedience
One is free when obeying laws one has prescribed to oneself. Legitimate authority enables this; illegitimate authority merely compels.

---

## Workflow

### 1. Identify the Authority Claim

What authority is being exercised?
- Who commands/decides/constrains?
- What scope of power is claimed?
- How is this authority justified?

### 2. Assess the Consent Basis

Was genuine consent given?
- Who consented, and when?
- Were those now governed party to the agreement?
- Could consent be withdrawn?
- Is continued participation genuinely voluntary?

**Red flags:** Historical consent binding current people, consent under duress, "consent" to take-it-or-leave-it terms.

### 3. Evaluate Service to General Will

Does this authority serve the common good?
- Whose interests are actually served?
- Would those governed choose this arrangement behind a veil of ignorance?
- Does the authority treat itself as servant or master of those governed?

**Rousseau's test:** Is this authority consistent with the freedom of all its subjects?

### 4. Check for Private Capture

Has authority been captured by particular interests?
- Do rulers benefit disproportionately?
- Are some subjects more equal than others?
- Has the will of all been mistaken for the general will?

### 5. Render Legitimacy Verdict

Based on assessment:
- **Legitimate:** Genuine consent + serves general will + not privately captured
- **Questionable:** Some elements present, others lacking
- **Illegitimate:** Lacks consent basis or serves private interests

### 6. Recommend Remediation

If legitimacy is lacking:
- What would genuine consent look like?
- How could this authority be restructured to serve general will?
- What transformation is needed?

---

## Output Format

```markdown
## Social Contract Assessment: [Institution/Authority]

### Authority Claimed
[What power is exercised and how justified]

### Consent Analysis
- Who consented: [Analysis]
- When: [Analysis]
- Could consent be withdrawn: [Analysis]
- **Verdict:** [Genuine/Questionable/Absent]

### General Will Test
- Whose interests served: [Analysis]
- Would subjects choose this: [Analysis]
- Consistent with freedom: [Analysis]
- **Verdict:** [Serves common good/Serves particular interests]

### Private Capture Assessment
[Analysis of whether authority has been captured]

### Legitimacy Verdict
**[Legitimate / Questionable / Illegitimate]**
[Brief explanation]

### Remediation Path
[If illegitimate, what would make it legitimate?]

### Rousseauian Pronouncement
[1-2 sentences capturing the essential judgment]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Authority seems obviously legitimate | Still apply the tests; obvious legitimacy should survive scrutiny |
| No clear consent moment exists | This is itself a finding; trace how authority was established |
| Everyone seems to accept it | Acceptance is not consent; habituated obedience is not legitimacy |
| Alternatives seem impractical | Legitimacy is prior to practicality; first establish the verdict, then discuss implementation |

---

## Example

**Input:**
Assess the legitimacy of a company's performance review system.

**Abbreviated Output:**

### Authority Claimed
Management claims authority to evaluate, rank, and make employment/compensation decisions based on performance reviews conducted annually.

### Consent Analysis
- Who consented: No explicit consent; employees "agree" by accepting employment
- When: At hire, with no ongoing renewal
- Could consent be withdrawn: Not without leaving employment
- **Verdict:** **Questionable.** Take-it-or-leave-it at hire is weak consent; no mechanism for voice within the system.

### General Will Test
- Whose interests served: Ostensibly mutual (identify development needs, allocate rewards fairly). In practice, often serves management's need for differentiation and control.
- Would subjects choose this: Unlikely in current form. Most would prefer transparent, frequent feedback over anxiety-inducing annual judgment.
- Consistent with freedom: Ranking systems inherently create zero-sum competition inconsistent with collective flourishing.
- **Verdict:** **Serves particular interests** (management's control and sorting function) more than common good (employee development and fair treatment).

### Private Capture Assessment
System advantages those who align with evaluators' preferences and self-promote effectively. Criteria often opaque. Those designed to be "objective" often encode existing power structures.

### Legitimacy Verdict
**Questionable bordering on Illegitimate**
The system lacks genuine consent (only exit is leaving), serves sorting/control more than development, and has been captured by managerial interests.

### Remediation Path
- Establish genuine consent: employees participate in designing evaluation criteria
- Serve general will: reframe from ranking to development
- Prevent capture: transparency, peer input, employee choice in who evaluates

### Rousseauian Pronouncement
This authority was never consented to by those it governs, serves the master's need for control more than the common good of all members, and calls itself "performance management" when it is merely hierarchical judgment. It has the form of legitimacy without its substance.

---

## Integration

This skill applies Rousseau's political philosophy to institutional analysis. Use in conjunction with:
- **general-will-inquiry** when assessing whether authority serves common good
- **amour-propre-diagnosis** when status dynamics corrupt authority structures
- **civilization-critique** when questioning whether institutional "progress" increases legitimacy
