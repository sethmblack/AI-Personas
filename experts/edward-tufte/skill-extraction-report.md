# Skill Extraction Report: Edward Tufte

**Expert:** Edward Tufte
**Domain:** Data Visualization, Information Design & Visual Communication
**Extraction Date:** 2026-02-10

---

## Extracted Skills

### 1. data-ink-maximization
**Description:** Systematically remove non-data elements from graphics to maximize the ratio of data-ink to total ink.

**Validation:**
- [x] Actionable - Clear process: identify non-data ink, evaluate each element, remove or simplify
- [x] Invocable - User says "my chart is cluttered" or "how do I simplify this graphic"
- [x] Scoped - Focused specifically on ink/element reduction, not overall design
- [x] Reusable - Applies to any chart, graph, dashboard, or data display
- [x] Valuable - Directly improves clarity and information density

**Source Concepts:**
- Data-ink ratio formula
- Erase non-data-ink
- Erase redundant data-ink
- The shrink principle

---

### 2. small-multiples-design
**Description:** Design repeating visual structures that enable comparison across variables, time periods, or categories.

**Validation:**
- [x] Actionable - Clear methodology: identify comparison dimension, design base structure, repeat with variation
- [x] Invocable - User says "how do I show change over time" or "compare across categories"
- [x] Scoped - Specific to comparative visualization, not general chart design
- [x] Reusable - Applies to time series, geographic comparison, category analysis
- [x] Valuable - Reveals patterns impossible to see in single views

**Source Concepts:**
- Muybridge motion studies
- Once viewers understand one slice, they understand all
- Parallelism and repetition
- Multiples in space and time

---

### 3. chartjunk-detection
**Description:** Identify and evaluate decorative, non-informative, or information-obscuring elements in visualizations.

**Validation:**
- [x] Actionable - Checklist-based evaluation: 3D effects, gradients, moiré, heavy grids, decoration
- [x] Invocable - User says "is this graphic good" or "review my visualization"
- [x] Scoped - Focused on identification, not redesign (pairs with data-ink-maximization)
- [x] Reusable - Works on any visualization type
- [x] Valuable - Prevents common design mistakes, improves clarity

**Source Concepts:**
- Chartjunk definition
- Self-promoting graphics
- Moiré vibration
- Design variation vs. data variation

---

### 4. sparkline-integration
**Description:** Design and embed word-sized graphics within text, tables, and documents for contextual data display.

**Validation:**
- [x] Actionable - Design parameters: size, placement, context, data selection
- [x] Invocable - User says "inline data" or "embed graphics in text"
- [x] Scoped - Specific to small, embedded graphics
- [x] Reusable - Applies to reports, dashboards, medical records, financial documents
- [x] Valuable - Enables data density without disrupting reading flow

**Source Concepts:**
- Word-sized graphics
- Intense continuous time-series
- Graphics as words in a sentence
- High resolution in small space

---

### 5. graphical-integrity-audit
**Description:** Evaluate visualizations for truthful representation by calculating lie factors and checking for distortion.

**Validation:**
- [x] Actionable - Calculate lie factor, check axis scales, verify proportions
- [x] Invocable - User says "is this misleading" or "check my chart for accuracy"
- [x] Scoped - Focused on integrity/accuracy, not aesthetics
- [x] Reusable - Applies to any quantitative visualization
- [x] Valuable - Prevents misleading graphics, builds credibility

**Source Concepts:**
- Lie factor formula
- Six principles of graphical integrity
- Truncated axes
- Context and source verification

---

### 6. high-resolution-thinking
**Description:** Design dense, layered information displays that respect the viewer's intelligence and visual processing capacity.

**Validation:**
- [x] Actionable - Layer information, increase density, add micro/macro readings
- [x] Invocable - User says "they won't understand this" or "too complex to show"
- [x] Scoped - Focused on information density and layering strategy
- [x] Reusable - Applies to any complex information challenge
- [x] Valuable - Counters the tendency to oversimplify

**Source Concepts:**
- Escaping flatland
- Micro/macro readings
- No such thing as information overload
- Data density metrics

---

## Skills NOT Extracted

### "powerpoint-alternative-design"
**Reason:** Too broad. The principles (dense documents, integrated text/graphics) are better expressed through the other skills combined. Would overlap significantly with high-resolution-thinking and data-ink-maximization.

### "color-encoding"
**Reason:** Too narrow and technical. Color use is part of broader design decisions covered in other skills. Tufte's color principles are supporting concepts, not a standalone methodology.

### "presentation-design"
**Reason:** Overlaps with existing skills. Tufte's presentation guidance is essentially "don't use PowerPoint, use dense documents with good graphics"—which combines the other extracted skills.

---

## Skill Relationships

```
graphical-integrity-audit ─────► Verify before publishing
        ↑
        │
chartjunk-detection ──────────► Identify problems
        │
        ↓
data-ink-maximization ────────► Remove non-data elements
        │
        ├── small-multiples-design ──► Add comparative structure
        │
        └── sparkline-integration ───► Add embedded context

high-resolution-thinking ─────► Frame the overall approach
```

---

## Summary

| Skill | Primary Use Case | Tufte Concept |
|-------|------------------|---------------|
| data-ink-maximization | Decluttering graphics | Data-ink ratio |
| small-multiples-design | Showing comparison | Parallelism, repetition |
| chartjunk-detection | Evaluating graphics | Chartjunk identification |
| sparkline-integration | Inline data display | Word-sized graphics |
| graphical-integrity-audit | Checking for lies | Lie factor, integrity |
| high-resolution-thinking | Complex information | Escaping flatland |
