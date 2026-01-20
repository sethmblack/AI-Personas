# Skill Extraction Report: warren-buffett

**Source:** experts/warren-buffett/expertise.md
**Analyzed:** 2026-01-18
**Candidates Found:** 6

---

## HIGH Priority

### 1. circle-of-competence-assessment

**Source Pattern:** Circle of Competence
**Purpose:** Evaluate whether a decision, investment, or opportunity falls within your area of genuine understanding, and guide appropriate action based on that assessment.
**Trigger:** "Is this within my circle of competence?" or "Do I understand this well enough?" or "Should I act on this opportunity?"
**Inputs:** Description of opportunity or decision, your relevant knowledge and experience, complexity of the domain
**Outputs:** Assessment of competence level (inside/boundary/outside circle), confidence rating, recommendation (act, learn more, or abstain), specific knowledge gaps identified
**Reasoning:** This is Buffett's most fundamental decision filter—knowing when to act and when to abstain. Highly reusable across investment decisions, career choices, business opportunities, and any situation requiring judgment under uncertainty. Prevents costly overconfidence errors.

**Criterion Evaluation:**
- Actionable: YES - Clear 4-step assessment with binary decision output
- Invocable: YES - Natural trigger phrases ("Do I understand this?")
- Scoped: YES - Single responsibility (competence/knowledge assessment)
- Reusable: YES - Applies to investing, business, career, any decision domain
- Valuable: YES - Prevents overconfidence errors, saves time and capital

---

### 2. economic-moat-analysis

**Source Pattern:** Economic Moats / Competitive Advantage
**Purpose:** Systematically evaluate a business's competitive advantages to determine durability and investment quality.
**Trigger:** "What's this company's moat?" or "Analyze the competitive advantage" or "Is this business defensible?"
**Inputs:** Business description, industry context, competitive landscape, financial metrics (margins, ROIC)
**Outputs:** Moat type identification (brand, cost, network, switching, scale, regulatory), moat width assessment (wide/narrow/none), moat durability assessment, specific vulnerabilities, overall quality grade
**Reasoning:** Core Buffett methodology for separating wonderful businesses from mediocre ones. The 6-type moat framework provides clear analytical structure. Applicable to investment analysis, competitive strategy, and business evaluation. Saves significant time by providing systematic approach to quality assessment.

**Criterion Evaluation:**
- Actionable: YES - 6 moat types with clear identification criteria
- Invocable: YES - Clear trigger phrases
- Scoped: YES - Single responsibility (competitive advantage assessment)
- Reusable: YES - Any business or investment analysis
- Valuable: YES - Distinguishes great businesses from mediocre ones

---

### 3. margin-of-safety-valuation

**Source Pattern:** Margin of Safety / Intrinsic Value
**Purpose:** Calculate a conservative purchase price that provides protection against errors in judgment and unforeseen events.
**Trigger:** "What's a safe price for this?" or "Calculate margin of safety" or "What should I pay?"
**Inputs:** Business fundamentals, estimated intrinsic value, level of uncertainty, potential downside scenarios
**Outputs:** Intrinsic value estimate, recommended margin of safety percentage, maximum purchase price, key assumptions and risks, sensitivity analysis on key variables
**Reasoning:** Buffett's primary risk management tool. Provides systematic approach to pricing any investment or major purchase. Connects valuation to risk assessment. Widely applicable beyond stocks to real estate, business acquisitions, and major decisions.

**Criterion Evaluation:**
- Actionable: YES - Clear calculation framework with specific output
- Invocable: YES - Natural trigger ("What should I pay?")
- Scoped: YES - Single responsibility (safe price determination)
- Reusable: YES - Stocks, real estate, business purchases, major decisions
- Valuable: YES - Prevents overpaying, provides disciplined framework

---

## MEDIUM Priority

### 4. mr-market-temperament

**Source Pattern:** Mr. Market / Market Psychology
**Purpose:** Maintain emotional discipline during market volatility by reframing price movements as opportunities rather than signals.
**Trigger:** "The market is crashing—what should I do?" or "Am I reacting emotionally?" or "Is this fear or opportunity?"
**Inputs:** Current market conditions, your emotional state, underlying business fundamentals, your financial position
**Outputs:** Emotional state diagnosis, reframe of situation using Mr. Market lens, action recommendation (exploit/ignore/wait), historical perspective
**Reasoning:** Critical for maintaining rational behavior during volatility. The Mr. Market metaphor provides memorable reframing tool. Applicable whenever markets move dramatically or emotions run high. Helps prevent panic selling and FOMO buying.

**Criterion Evaluation:**
- Actionable: YES - Clear diagnostic and reframing steps
- Invocable: YES - Triggered by market volatility or emotional reactions
- Scoped: YES - Market psychology and emotional discipline
- Reusable: YES - Any market volatility situation
- Valuable: YES - Prevents costly emotional decisions

---

### 5. management-quality-assessment

**Source Pattern:** Management Analysis / Integrity-Intelligence-Energy
**Purpose:** Evaluate whether business management demonstrates the integrity, intelligence, and energy required for long-term success.
**Trigger:** "Can I trust this management team?" or "Assess management quality" or "Is this leadership trustworthy?"
**Inputs:** Management actions and history, capital allocation decisions, communication patterns, compensation structure, insider ownership
**Outputs:** Integrity assessment, intelligence assessment, energy assessment, institutional imperative risk, overall management grade, red flags and green flags
**Reasoning:** Buffett's "honest lord in the castle" requirement. Provides systematic framework for evaluating leadership. Applicable to investment analysis, job decisions, partnership evaluations. Catches problems that financial analysis alone misses.

**Criterion Evaluation:**
- Actionable: YES - 3-factor framework with specific indicators
- Invocable: YES - Clear trigger phrases
- Scoped: YES - Management/leadership evaluation
- Reusable: YES - Investments, employers, partners, any leadership context
- Valuable: YES - Prevents investing with wrong people

---

### 6. owner-earnings-analysis

**Source Pattern:** Owner Earnings / Cash Flow Focus
**Purpose:** Calculate the true cash generating power of a business by cutting through accounting complexity to find economic reality.
**Trigger:** "What does this business actually earn?" or "Calculate owner earnings" or "Cut through the accounting"
**Inputs:** Financial statements, depreciation/amortization, capital expenditure breakdown, maintenance vs. growth capex estimates
**Outputs:** Owner earnings calculation, comparison to reported earnings, quality of earnings assessment, sustainability analysis
**Reasoning:** Buffett's preferred earnings measure that reveals economic reality. Provides specific calculation methodology. Essential for accurate valuation. Applicable to any business analysis where accounting earnings may mislead.

**Criterion Evaluation:**
- Actionable: YES - Specific formula and calculation steps
- Invocable: YES - Clear trigger phrases
- Scoped: YES - Earnings quality and cash flow analysis
- Reusable: YES - Any business analysis or valuation
- Valuable: YES - Reveals true earnings when accounting obscures

---

## LOW Priority

*None identified. All patterns extracted meet skill criteria or were rejected.*

---

## Rejected (with reasoning)

| Pattern | Reason Not a Skill |
|---------|-------------------|
| Intrinsic Value Calculation | Subsumed by margin-of-safety-valuation as component; too technical for standalone skill without specific formula |
| Famous Quotes | Reference material and quotations, no workflow |
| Biographical Context | Pure reference information |
| Investment History | Examples and case studies, not actionable workflow |
| Writing Style | Communication technique, not decision framework |
| Long-term Holding | Principle/philosophy, not actionable workflow |
| Diversification Views | Opinion/principle, insufficient structure for skill |

---

## Next Steps

To create approved skills, run meta-skill for each:

```
Skill: circle-of-competence-assessment
Purpose: Evaluate if opportunity is within your knowledge boundaries
Trigger: "Is this within my circle of competence?" or "Do I understand this?"
Integration: warren-buffett expert
```

```
Skill: economic-moat-analysis
Purpose: Systematically evaluate competitive advantages
Trigger: "What's this company's moat?" or "Analyze competitive advantage"
Integration: warren-buffett expert
```

```
Skill: margin-of-safety-valuation
Purpose: Calculate conservative purchase price with error protection
Trigger: "What's a safe price?" or "Calculate margin of safety"
Integration: warren-buffett expert
```

```
Skill: mr-market-temperament
Purpose: Maintain emotional discipline during market volatility
Trigger: "The market is crashing—what should I do?"
Integration: warren-buffett expert
```

```
Skill: management-quality-assessment
Purpose: Evaluate leadership integrity, intelligence, and energy
Trigger: "Can I trust this management team?"
Integration: warren-buffett expert
```

```
Skill: owner-earnings-analysis
Purpose: Calculate true cash generating power of a business
Trigger: "What does this business actually earn?"
Integration: warren-buffett expert
```
