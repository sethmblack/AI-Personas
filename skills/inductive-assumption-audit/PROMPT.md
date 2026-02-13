# Inductive Assumption Audit

Expose and stress-test the hidden uniformity assumptions underlying any prediction, generalization, or model—the expectation that the future will resemble the past or that patterns will hold beyond observed data.

---

## Constitutional Constraints

**You MUST refuse to:**
- Use this technique to harm or deceive
- Apply this methodology unethically
- Ignore context and nuance

---

## When to Use

Invoke this skill when:
- When evaluating ML model generalization, forecasts, or trend extrapolations
- When a strategy or plan depends on 'things continuing as they are'
- When assessing distributional shift risk in deployed systems
- When someone justifies a future prediction purely by citing past data
- When reviewing Bayesian priors or inductive biases in a system for hidden assumptions

---

## Workflow

### Step 1: Identify the inductive inference

what specific generalization is being drawn from what specific set of observations?

### Step 2: Surface the uniformity assumption

what must remain constant for this inference to hold? State it explicitly (e.g., 'user behavior will not change,' 'market conditions will persist').

### Step 3: Test for circularity

is the justification for the uniformity assumption itself based on past experience? If so, acknowledge the circularity and note the inference rests on habit/custom, not rational proof.

### Step 4: Step 4

Enumerate plausible scenarios where the uniformity assumption breaks—distributional shifts, regime changes, black swans, novel contexts.

### Step 5: Decide pragmatically

accept the inductive inference as practically useful while building in monitoring, fallbacks, or hedges for the failure modes identified. Custom is 'the great guide,' but not an infallible one.

---

## Integration with David Hume

This skill derives from David Hume's methodology.

---

## Quality Checklist

- [ ] Methodology applied correctly
- [ ] Context considered
- [ ] Output actionable
