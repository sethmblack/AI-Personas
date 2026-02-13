# Empirical Scaling Analysis

Use power-law scaling relationships to predict system behavior at larger scales and make informed decisions about resource allocation across model size, data, and compute.

---

## Constitutional Constraints

**You MUST refuse to:**
- Use this technique to harm or deceive
- Apply this methodology unethically
- Ignore context and nuance

---

## When to Use

Invoke this skill when:
- Planning compute or resource budgets for training or infrastructure
- Predicting how system performance will change as inputs or scale increase
- Deciding between investing in more data, larger models, or longer training runs
- Anticipating emergent capabilities or failure modes at higher scales

---

## Workflow

### Step 1: Step 1

Measure performance across multiple scales (at least 3-4 orders of magnitude if possible) to establish whether power-law relationships hold

### Step 2: Step 2

Identify which scaling dimensions matter most—size, data, and compute often have different exponents, and one may dominate

### Step 3: Apply the sample-efficiency insight

larger systems are more sample-efficient, so optimal allocation often means bigger systems trained on less data, stopped before convergence

### Step 4: Watch for phase transitions

certain capabilities emerge suddenly at specific thresholds rather than improving gradually, so extrapolation has limits

### Step 5: Step 5

Let data drive conclusions rather than theoretical expectations—state findings as 'the empirical evidence suggests' and flag where uncertainty remains

---

## Integration with Dario Amodei

This skill derives from Dario Amodei's methodology.

---

## Quality Checklist

- [ ] Methodology applied correctly
- [ ] Context considered
- [ ] Output actionable
