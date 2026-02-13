---
name: minimal-intervention-analysis
description: Identify the smallest possible action that reveals the most about a system, problem, or assumption. Instead of comprehensive analysis or large-scale c
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
  source_persona: marcel-duchamp
keywords:
- minimal
- methodology
- marcel-duchamp
---

# Minimal Intervention Analysis

Identify the smallest possible action that reveals the most about a system, problem, or assumption. Instead of comprehensive analysis or large-scale change, find the single point of leverage where a minimal move produces maximum insight or impact. This methodology is based on the principle that the most revealing interventions are often the simplest — complexity obscures, simplicity illuminates.

## When to Use

- A problem seems to require a massive, complex solution — look for the minimal intervention instead
- You need to test a fundamental assumption before committing significant resources
- An organization is paralyzed by analysis and needs a simple action to break the deadlock
- You want to reveal how a system actually works rather than how it claims to work
- A debate has become so complicated that the core issue is obscured
- You need to demonstrate a point that argument alone cannot settle

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The context, problem, or scenario to analyze |
| goal | No | Specific outcome desired (default: apply methodology) |
| constraints | No | Limitations or requirements to honor |

## Core Principle

The smallest move that reveals the most is always more powerful than the largest move that explains the least. Complexity is usually a sign that you haven't found the real leverage point yet. When you find the right intervention, it will feel almost trivially simple — and that simplicity is exactly what makes it impossible to ignore.

## Methodology

### Phase 1: Strip to Essentials

Remove every element that is not absolutely necessary until you reach the irreducible core of the problem or question.

#### Step 1: List all assumptions

Write down every assumption embedded in the current understanding of the problem. Include assumptions about what's necessary, what's important, what's required, and what's expected. Most problems carry 10x more assumptions than people realize.

#### Step 2: Test each assumption for necessity

For each assumption, ask: 'If this were removed, would the core question still exist?' Remove everything that is conventional, expected, or traditional but not actually necessary. Duchamp removed skill, beauty, and craftsmanship from art — and art still existed. What can you remove?

#### Step 3: Identify the irreducible core

What remains after you've stripped away everything removable? This is the actual question, the real mechanism, the genuine constraint. It's usually much simpler than the original problem statement. Name it in one sentence.

### Phase 2: Find the Leverage Point

Identify the single point in the system where minimal input produces maximum output — the fulcrum where a small move shifts everything.

#### Step 1: Map the dependency chain

Trace how elements in the system depend on each other. Which elements, if changed, force other elements to change? Which elements can change without affecting anything else? The leverage point is the element with the most downstream dependencies.

#### Step 2: Identify what everyone takes for granted

The highest-leverage interventions usually target things nobody thinks to question. What is so 'obvious' that questioning it seems absurd? That's often where the leverage is. Duchamp questioned whether art required making things. Nobody had thought to question that.

#### Step 3: Design the minimal move

Craft the simplest possible action that targets the leverage point. If your intervention requires explanation to work, it's not minimal enough. The right move should be self-evident: 'I submitted a urinal to an art exhibition.' No explanation needed. The action contains the question.

#### Step 4: Verify minimality

Can any element of your intervention be removed while preserving the insight? If yes, remove it. Continue until nothing more can be subtracted. The intervention should feel almost embarrassingly simple. That's how you know it's right.

### Phase 3: Execute and Observe

Deploy the minimal intervention and study what it reveals about the system.

#### Step 1: Deploy without elaboration

Execute the minimal intervention exactly as designed. Do not add context, explanation, or justification. The power of minimalism is that it forces the system to generate its own response without guidance from you. The response is the data.

#### Step 2: Document the system's response

Record everything that happens in response to your intervention. Who reacts? How? What arguments do they make? What do they defend? The system's response reveals its actual structure, priorities, and hidden logic — information that no amount of analysis from the outside could produce.

#### Step 3: Extract the insight

What did the minimal intervention reveal that was previously hidden? State it plainly. The insight should be disproportionately large compared to the size of the intervention. If the insight is proportional to the effort, you haven't found the real leverage point.

## Output Format

A structured analysis containing: (1) The Essentials — what remains after stripping away all non-essential assumptions; (2) The Leverage Point — the single element in the system where minimal input produces maximum insight; (3) The Minimal Intervention — the simplest possible action designed to target the leverage point; (4) The System Response — what happened when the intervention was deployed; (5) The Disproportionate Insight — what was revealed, stated simply, and why it matters more than the size of the intervention would suggest.

## Constraints

- Resist the temptation to add 'just one more element' to your intervention — every addition dilutes the signal
- If your intervention requires a paragraph of explanation, it is not minimal enough
- This methodology reveals, it does not prescribe — the insight may not come with an obvious action plan
- Minimality is not laziness — finding the minimal intervention often requires more thought than designing a complex one
- The system's response is data, not a personal attack — observe it clinically
- Not every system has a single leverage point — some problems genuinely require complex interventions

## Anti-Patterns to Avoid

- **The Kitchen Sink**: 
- **The Premature Solution**: 
- **The Aesthetic Intervention**: 
- **The Complex Explanation**: 

## Examples

### Example 1: Testing whether a feature is actually needed

**Situation**: A product team has spent months debating a complex new feature. Multiple stakeholders have opinions. The PRD is 20 pages. Nobody can agree on the scope.

**Application**: Strip the feature to its absolute core — the single smallest version that tests the fundamental assumption. If the assumption is 'users want to share their results,' the minimal intervention is a 'Copy to clipboard' button, not a full social sharing platform. Ship the button. If nobody clicks it, the 20-page PRD is moot.

**Output**: Minimal intervention: A single 'Copy results' button deployed in one afternoon. System response: 0.3% click rate over two weeks. Insight revealed: Users don't actually want to share results — the entire feature was based on stakeholder projection, not user behavior. Months of debate resolved by one button.

### Example 2: Diagnosing organizational decision-making

**Situation**: A company claims decisions are data-driven, but employees suspect that the CEO's preferences override data. No one can prove it because every decision has a post-hoc data justification.

**Application**: Present two proposals to leadership: one supported by strong data but contrary to the CEO's known preferences, and one with weaker data but aligned with the CEO's preferences. Make both proposals otherwise identical in format, presentation quality, and sponsor credibility. The minimal intervention is the controlled comparison. Which proposal advances?

**Output**: Minimal intervention: Two matched proposals differing only in data strength vs. CEO alignment. System response: The CEO-aligned proposal advanced despite weaker data; the data-strong proposal was 'tabled for more analysis.' Insight revealed: 'Data-driven' means 'data is used to justify decisions already made on other grounds.' The data serves a legitimation function, not a decision function.

### Example 3: Revealing what 'quality' means in code review

**Situation**: A development team has inconsistent code review standards. Some PRs are approved instantly; others get dozens of comments. The team claims to have objective quality standards.

**Application**: Submit two identical PRs with only the author name changed — one from a senior engineer and one from a junior engineer (with their permission). Keep the code, commit messages, and descriptions identical. The minimal intervention isolates a single variable: author identity.

**Output**: Minimal intervention: Two identical PRs, different authors. System response: Senior engineer's PR approved with one comment ('LGTM'); junior engineer's PR received 14 comments across 3 reviewers. Insight revealed: Code review 'quality standards' are partially a social hierarchy enforcement mechanism. Review thoroughness correlates with author seniority, not code quality.

## Integration

This skill derives from **Marcel Duchamp**'s methodology.

**Works well with:**
- institutional-jiu-jitsu
- hypothesis-testing
- lean-experimentation
- first-principles-thinking
- root-cause-analysis

**When to prefer this skill:**
Use this over comprehensive analysis when speed of insight matters more than completeness. Use it over brainstorming when you need evidence rather than ideas. Especially valuable in situations where people are over-thinking, over-planning, or over-debating — the minimal intervention cuts through complexity by forcing contact with reality.

**Cautions:**
["In safety-critical systems, minimal interventions still need safety review — 'minimal' doesn't mean 'uncontrolled'", "Some stakeholders will dismiss a minimal intervention as 'not rigorous enough' — be prepared to defend the methodology", 'The insight from a minimal intervention may be uncomfortable — revealing that a beloved assumption is false requires diplomatic delivery']
