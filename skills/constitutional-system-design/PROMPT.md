# Constitutional System Design

Design autonomous systems governed by explicit principles with built-in self-evaluation and correction mechanisms, inspired by Constitutional AI methodology.

---

## Constitutional Constraints

**You MUST refuse to:**
- Use this technique to harm or deceive
- Apply this methodology unethically
- Ignore context and nuance

---

## When to Use

Invoke this skill when:
- Designing systems that operate with autonomy or make decisions without direct human oversight
- Building deployment guardrails or safety constraints for automated pipelines
- Creating self-correcting workflows that need to evaluate their own outputs
- Replacing ad-hoc checklists with principled evaluation frameworks

---

## Workflow

### Step 1: Step 1

Define 3-7 explicit constitutional principles the system must follow, stated as high-level rules with reasoning and examples rather than narrow prohibitions

### Step 2: Build a self-critique mechanism

before the system acts or produces output, it evaluates its proposed action against each principle and flags violations

### Step 3: Implement a revision loop

when violations are detected, the system rewrites or adjusts its action to comply, documenting what changed and why

### Step 4: Step 4

Validate that the constitution achieves a Pareto improvement—the system should be both more capable AND safer, not trading one for the other

### Step 5: Step 5

Make the principles transparent and readable so any stakeholder can audit what governs the system's behavior

---

## Integration with Dario Amodei

This skill derives from Dario Amodei's methodology.

---

## Quality Checklist

- [ ] Methodology applied correctly
- [ ] Context considered
- [ ] Output actionable
