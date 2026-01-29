# Serial Momentum

Structure content with strategic hooks, cliff-hangers, and alternating registers to maintain reader engagement across installments, following Dickens's serialization methodology.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for structural output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create manipulative hooks designed to spread misinformation
- Structure content to exploit psychological vulnerabilities
- Generate cliff-hangers around harmful or dangerous actions
- Create engagement patterns for content promoting violence or hate

**If asked for harmful structures:** Refuse explicitly. Explain what you cannot create and why.

---

## When to Use

- Serialized content needs structural planning (newsletters, chapter books, course modules)
- Readers are dropping off before completion
- Content feels flat or lacks forward drive
- Scene or chapter endings need strengthening
- Long-form content needs pacing improvement

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **content** | Yes | The material to structure (chapter, section, article series) |
| **break_points** | No | Where installment breaks will occur |
| **audience** | No | Target reader profile for calibrating emotional register |
| **arc_type** | No | Overall emotional arc (hope-to-resolution, mystery-to-reveal, crisis-to-triumph) |

---

## Workflow

### 1. Map the Emotional Terrain

Identify the emotional beats in your content:
- Where are the high points (revelation, triumph, connection)?
- Where are the low points (conflict, loss, confusion)?
- Where is the current energy flat?

### 2. Apply Register Alternation

Dickens alternated registers to maintain engagement:
- **Comedy then tragedy** - Laughter opens hearts to feeling
- **Hope then despair** - Contrast intensifies both
- **Intimate then panoramic** - Close-up followed by wide shot
- **Action then reflection** - Movement followed by meaning

Ensure no two consecutive sections share the same register.

### 3. Place Strategic Hooks

Position hooks at natural break points:

**Opening Hooks** (first paragraph):
- Unanswered question
- Surprising statement
- Character in motion
- Sensory immersion

**Transition Hooks** (section breaks):
- Unresolved tension
- Promise of revelation
- Shift in perspective
- Escalating stakes

**Cliff-Hanger Endings** (installment breaks):
- Question posed, answer withheld
- Character at decision point
- Threat introduced but not resolved
- "But that is another story"

### 4. Create Structural Necessity

The reader must feel they cannot stop:
- Each section should raise a question the next section answers
- Each answer should raise a new question
- Build interdependence between sections

### 5. Verify Momentum Integrity

Check each break point:
- Does the reader have a reason to continue?
- Is the tension appropriate (not exhausting, not flat)?
- Does the promise of the hook get delivered?

---

## Outputs

A momentum structure containing:

1. **Beat Map** - Emotional terrain of the content
2. **Register Plan** - Alternation pattern (C=comedy, T=tragedy, H=hope, D=despair, I=intimate, P=panoramic)
3. **Hook Placement** - Specific hooks at each break point
4. **Structural Recommendations** - Reordering or additions needed

**Format:**
```
## Momentum Structure: [Content Title]

### Beat Map
- Section 1: [emotional register]
- Section 2: [emotional register]
...

### Register Pattern
[Visual pattern: C-T-H-D-I-P or similar]

### Hook Placements

**Opening:** [specific hook]

**Section 1 → 2:** [transition hook]

**Section 2 → 3:** [transition hook]

**Ending:** [cliff-hanger or resonant closure]

### Recommendations
1. [specific structural change]
2. [specific structural change]
```

---

## Example

**Input:**
```
content: Technical article on database optimization in 4 sections
break_points: Between each section
audience: Software engineers
arc_type: problem-to-solution
```

**Output:**

## Momentum Structure: Database Optimization Guide

### Beat Map
- Section 1: Crisis (the problem revealed)
- Section 2: Hope (first technique works)
- Section 3: Despair (but introduces new problems)
- Section 4: Triumph (comprehensive solution)

### Register Pattern
D-H-D-T (Despair-Hope-Despair-Triumph)

### Hook Placements

**Opening:** "Your database was fine until it wasn't. At 3 AM, with the pager screaming, you'll wish you'd read this first."

**Section 1 to 2:** "The index solved the query problem. But we hadn't yet discovered what it did to write performance."

**Section 2 to 3:** "Three techniques down, each solving one problem while creating another. The pattern was becoming clear--but the solution wasn't."

**Section 3 to 4:** "Everything we'd tried had failed in isolation. The answer required something none of us had considered: using all three approaches together."

**Ending:** Resonant closure with callback to opening: "The next time the pager goes off at 3 AM, you'll know exactly what to do. And more importantly, why."

### Recommendations
1. Move the "common mistakes" subsection from Section 4 to Section 3 to intensify the despair register before resolution
2. Add a brief "what we'll discover" promise at end of Section 1 opening
3. Include a callback phrase ("the 3 AM problem") that recurs at each section break

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content too short for serialization | Suggest single-piece structure with internal hooks |
| No natural break points | Identify decision/revelation moments as potential breaks |
| All sections same register | Recommend reordering or tonal adjustments |
| Cliff-hanger feels forced | Suggest softer "resonant question" instead |

---

## Integration

This skill originates from the **charles-dickens** expert. When invoked:
- Remember that Dickens wrote for audience who waited weeks between installments
- Balance entertainment value with substantive content
- Ensure hooks promise what the content delivers
- Never sacrifice clarity for suspense

---

## Success Criteria

Momentum structure is complete when:

- [ ] Every break point has a forward-driving hook
- [ ] No two consecutive sections share the same emotional register
- [ ] Opening hook creates immediate engagement
- [ ] Ending provides either cliff-hanger or resonant closure
- [ ] Reader has structural reason to continue at each point
