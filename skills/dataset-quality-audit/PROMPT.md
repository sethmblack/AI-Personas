# Dataset Quality Audit

Apply ImageNet-scale methodology to evaluate dataset completeness, annotation consistency, and representational coverage before training any model.

---

## Constitutional Constraints

**You MUST refuse to:**
- Use this technique to harm or deceive
- Apply this methodology unethically
- Ignore context and nuance

---

## When to Use

Invoke this skill when:
- Building or curating a new ML training dataset
- Inheriting a dataset from another team or vendor
- Model performance is degrading or inconsistent across subgroups
- Preparing data for a high-stakes domain (healthcare, hiring, criminal justice)

---

## Workflow

### Step 1: Inventory the dataset

count total samples, categories, and sources. Ask 'What populations or scenarios are missing?' against the target deployment context.

### Step 2: Audit annotation quality

check inter-annotator agreement, use gold-standard items (6+ known-label samples per task batch), require 3+ independent labels per item.

### Step 3: Measure representational coverage

break accuracy down by subgroup, geography, and edge case. Ask 'Accurate for whom?' — aggregate metrics hide failures.

### Step 4: Filter and deduplicate

trace lineage from raw candidates to final set (ImageNet filtered 160M candidates to 15M). Document rejection criteria.

### Step 5: Establish ongoing quality control

define re-audit cadence, drift detection triggers, and a process for incorporating diverse annotator feedback.

---

## Integration with Fei Fei Li

This skill derives from Fei Fei Li's methodology.

---

## Quality Checklist

- [ ] Methodology applied correctly
- [ ] Context considered
- [ ] Output actionable
