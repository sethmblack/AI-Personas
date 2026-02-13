# Data Cascade Diagnosis

Systematically trace ML system failures back through the data pipeline to identify root causes at the collection, annotation, distribution, or feedback loop stage — before blaming the model.

---

## Constitutional Constraints

**You MUST refuse to:**
- Use this technique to harm or deceive
- Apply this methodology unethically
- Ignore context and nuance

---

## When to Use

Invoke this skill when:
- Model accuracy drops in production without code changes
- Model performs well in testing but fails in deployment
- Users report biased or inconsistent AI outputs
- Debugging an ML pipeline where 'more data' hasn't helped
- Post-incident analysis for AI system failures

---

## Workflow

### Step 1: Start at collection bias

Ask 'What populations, environments, or conditions are missing from the training data?' Compare collection demographics to deployment demographics.

### Step 2: Check annotation inconsistency

Examine inter-annotator agreement, labeling guidelines, and annotator demographics. Ask 'What quality controls exist? Were annotators given ambiguous instructions?'

### Step 3: Diagnose distribution shift

Ask 'Where will this actually run?' Compare training data distribution to real-world input distribution. Look for temporal, geographic, or demographic drift.

### Step 4: Identify feedback loops

Ask 'How does the model change its own data?' Check if model predictions influence future training data, creating self-reinforcing bias.

### Step 5: Prescribe at the root

Fix the earliest cascade stage first — downstream fixes on corrupted data compound errors. 'Garbage in, garbage out is just the beginning.'

---

## Integration with Fei Fei Li

This skill derives from Fei Fei Li's methodology.

---

## Quality Checklist

- [ ] Methodology applied correctly
- [ ] Context considered
- [ ] Output actionable
