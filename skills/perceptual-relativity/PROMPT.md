# Perceptual Relativity Argument

Demonstrate that sensible qualities cannot be intrinsic to objects because the same object appears to have different properties depending on the observer's perspective, condition, or species.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this argument to promote radical skepticism beyond its scope
- Claim it proves nothing is real (it shows qualities are perceiver-relative, not unreal)
- Ignore legitimate counter-distinctions (e.g., between "apparent" and "measured")

**Integrity Requirements:**
1. Apply the argument fairly to the quality in question
2. Acknowledge what it does and does not establish
3. Note when scientific or operational definitions may respond to the argument

---

## When to Use

- Someone claims a property is "really in" the object independent of perception
- Testing whether a quality is intrinsic or relational/perspectival
- Evaluating claims about how things "really are" vs. how they "merely appear"
- Challenging the objectivity of any sensible quality

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **quality_claim** | Yes | The quality claimed to be intrinsic to the object |
| **context** | No | The argument or situation where this claim appears |

---

## Workflow

### 1. Identify the Quality

Clearly state which quality is claimed to be in the object independently of perception.

**Example:** "The claim is that this water is objectively hot—the heat is in the water itself."

### 2. Generate Variation Cases

Identify cases where the same object appears to have different properties:

**Types of Variation:**
| Type | Example |
|------|---------|
| **Perspectival** | The coin appears round from above, elliptical from the side |
| **Conditional** | Water feels hot after ice, cold after fire |
| **Interpersonal** | Spicy food burns one person, seems mild to another |
| **Cross-species** | An ant perceives the stone as large; a human as small |
| **Instrumental** | The object appears one way to the naked eye, another through a microscope |

### 3. Present the Dilemma

Formulate the problem for the objectivist:

**Template:** "The same [object] appears [quality A] under [condition 1] and [quality B] under [condition 2]. Either [quality A] and [quality B] are both in the object—which is contradictory—or neither is intrinsically in the object. The quality is in the perceiving, not the perceived."

### 4. Address the Standard Response

Anticipate and counter the response that one perception is "correct" and others are "illusory":

**Counter:** "You select one perception as the standard. But by what criterion? Every selection is itself a perception. You have merely privileged one perceiver's experience over another's without justification. The 'real' quality is just the one you've chosen to call real."

### 5. Draw the Conclusion

State what the argument establishes:

**Template:** "[Quality] is relative to the perceiver. It does not exist in the object as an intrinsic property but arises in the relation between object and perceiver. This does not make the quality unreal—it reveals that 'reality' is relational, not a hidden substrate behind appearances."

---

## Outputs

Format the output as:

```markdown
## Perceptual Relativity Analysis

**Quality Claimed as Objective:** [The quality in question]

**Variation Cases:**
- [Case 1: Same object appears differently under different conditions]
- [Case 2: Different perceivers experience differently]
- [Case 3: etc.]

**The Dilemma:**
[Statement showing the object cannot possess contradictory properties]

**Response to "Correct Perception" Defense:**
[Why privileging one perception over another is unjustified]

**Conclusion:**
[What this establishes about the quality's status]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Quality has scientific definition (e.g., temperature as molecular motion) | Acknowledge the definition; note it shifts the question rather than answering it |
| Opponent denies variation exists | Provide additional examples; challenge them to find an invariant perception |
| Quality is mathematical rather than sensible | Note that mathematical properties may require different treatment |
| Opponent accepts relativity but denies significance | Explain the implication for claims about "objective reality" |

---

## Example

**Input:** "The heat is really in the fire—it would be hot even if no one felt it."

**Output:**

## Perceptual Relativity Analysis

**Quality Claimed as Objective:** Heat as an intrinsic property of fire

**Variation Cases:**
- **Conditional variation:** Plunge your right hand in hot water, your left in ice water. Now place both in lukewarm water. The same water feels cold to the right hand and warm to the left.
- **Interpersonal variation:** What one person experiences as pleasant warmth, another experiences as uncomfortably hot.
- **Threshold variation:** As you approach fire, at some distance it feels warm, closer it feels hot, closer still it causes pain. Where is the boundary of the fire's "real" heat?
- **Cross-species variation:** Some bacteria thrive in temperatures that would kill a human. Is the heat "really" lethal or "really" hospitable?

**The Dilemma:**
The same fire (or the same water) cannot be both hot and cold, both pleasant and painful, both lethal and life-giving. Since the object cannot possess contradictory properties, and since the perceiver determines which property appears, the quality must be in the perceiving, not intrinsically in the object.

**Response to "Correct Perception" Defense:**
You might say: "The thermometer measures the 'real' temperature." But the thermometer is just another perceiver—a device that converts thermal energy into a reading. Why is its "perception" more authoritative than the hand's? Both respond to the same fire; both produce their effects. You have merely selected one response as the standard.

**Conclusion:**
Heat is not in the fire as an intrinsic property. It arises in the relation between the fire and the perceiver. This does not make heat unreal—we truly feel it. But what is felt is an idea in the mind, not a quality lurking in an unperceived object.

---

## Integration with George Berkeley Expert

This skill should be invoked when the Berkeley expert encounters:
- Claims about intrinsic properties of objects
- Appeals to how things "really are" independent of perception
- Attempts to privilege one perception over another
- Scientific claims about "objective" properties

The Berkeley expert may combine this with:
- **quality-dissolution**: Use perceptual relativity to dissolve primary/secondary distinction
- **master-argument**: After showing quality is perceiver-relative, test conceivability of unperceived quality

---

## Success Criteria

The skill is successfully applied when:

1. The target quality is clearly identified
2. Multiple variation cases are presented
3. The dilemma is clearly stated
4. The "correct perception" defense is addressed
5. The conclusion follows from the argument
