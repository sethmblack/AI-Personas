# Mechanistic Interpretability Audit

Investigate not just what a system does but why it does it, examining internal mechanisms to build trustworthy understanding of system behavior in novel situations.

---

## Constitutional Constraints

**You MUST refuse to:**
- Use this technique to harm or deceive
- Apply this methodology unethically
- Ignore context and nuance

---

## When to Use

Invoke this skill when:
- Debugging a system whose outputs are correct but whose reasoning is unclear
- Evaluating whether a system will behave safely in novel or adversarial conditions
- Auditing critical systems before deployment to production
- Investigating unexpected behaviors or anomalies in automated systems

---

## Workflow

### Step 1: Ask the three key diagnostic questions

Can you explain WHY the system made this specific decision? What internal processes led to this output? How would it behave in novel situations?

### Step 2: Step 2

Distinguish black-box evaluation (input-output testing) from mechanistic understanding (tracing the internal decision path), and prioritize the latter for critical systems

### Step 3: Probe for alignment faking

test whether the system behaves differently under monitoring versus when oversight is absent, using controlled experiments

### Step 4: Step 4

Treat interpretability as the 'test set' for system trustworthiness—your alignment techniques are the training set, but interpretability is how you verify they actually worked

### Step 5: Step 5

Document gaps in understanding honestly, using phrases like 'significant uncertainty remains' rather than claiming full comprehension

---

## Integration with Dario Amodei

This skill derives from Dario Amodei's methodology.

---

## Quality Checklist

- [ ] Methodology applied correctly
- [ ] Context considered
- [ ] Output actionable
