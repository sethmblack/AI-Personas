# Margin of Safety Analysis

Evaluate the gap between intrinsic value and market price to determine investment suitability using Benjamin Graham's foundational principle.

---

## When to Use

- Deciding whether to buy, hold, or sell a security
- Assessing risk level of a potential investment
- Comparing multiple investment opportunities
- Determining appropriate entry points
- User asks "Is there margin of safety?" or "How safe is this investment?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| security | Yes | The stock, bond, or asset being evaluated |
| market_price | Yes | Current market price or what you'd pay |
| intrinsic_value | Recommended | Estimated true value (can be calculated) |
| financial_data | Recommended | Earnings, assets, dividends, or other fundamentals |

---

## Graham's Margin of Safety Principle

Benjamin Graham coined the term "margin of safety" and considered it the central concept of investment:

*"Confronted with a like challenge to distill the secret of sound investment into three words, we venture the motto - Margin of Safety."*

### The Core Idea

The margin of safety is the difference between what something is worth and what you pay for it. The larger this gap, the greater your protection against:

1. **Errors in analysis** - Your valuation may be wrong
2. **Unforeseen events** - Bad things happen
3. **Market volatility** - Prices fluctuate irrationally
4. **Business deterioration** - Companies decline

### Graham's Thresholds

| Situation | Minimum Margin |
|-----------|----------------|
| High-quality stocks | 33% below intrinsic value |
| Net-net bargains | 33% below NCAV |
| General rule | Larger margin = safer investment |

*"The margin of safety is always dependent on the price paid. It will be large at one price, small at some higher price, nonexistent at some still higher price."*

---

## Calculation Framework

### Step 1: Estimate Intrinsic Value

Choose appropriate method based on available data:

**Earnings-Based:**
- Graham Number = Square Root of (22.5 x EPS x Book Value per Share)
- Maximum price for defensive investor

**Asset-Based:**
- Net Current Asset Value = Current Assets - Total Liabilities
- Floor value in worst case

**Earnings Power:**
- Average earnings over 7-10 years x appropriate multiple (10-15)
- Normalized value approach

### Step 2: Compare to Market Price

```
Margin of Safety % = (Intrinsic Value - Market Price) / Intrinsic Value x 100
```

### Step 3: Interpret the Margin

| Margin of Safety | Assessment | Recommendation |
|------------------|------------|----------------|
| > 50% | Substantial | Strong buy if fundamentals sound |
| 33-50% | Adequate | Suitable for investment |
| 15-33% | Thin | Proceed with caution |
| 0-15% | Minimal | High risk, likely pass |
| Negative | None | Price exceeds value - avoid |

---

## Output Format

```markdown
## Margin of Safety Analysis

### Security
[Name and description]

### Valuation Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $XX |
| Estimated Intrinsic Value | $XX |
| Margin of Safety | XX% |

### Intrinsic Value Calculation

**Method Used:** [Earnings-based / Asset-based / Earnings Power]

**Calculation:**
[Show the math]

**Key Assumptions:**
- [Assumption 1]
- [Assumption 2]

### Assessment

**Margin Level:** [Substantial / Adequate / Thin / Minimal / None]

**Risk Factors:**
1. [What could make your valuation too high?]
2. [What could cause the business to deteriorate?]
3. [What external factors could affect value?]

### Graham's Verdict

[Clear recommendation based on margin of safety]

**If margin is adequate:**
"At $[price], purchasing [security] provides a [X]% margin of safety. This buffer protects against [specific risks] while offering adequate return potential."

**If margin is inadequate:**
"At current prices, [security] offers insufficient margin of safety. Mr. Market is asking too much. Wait for a better price, or look elsewhere."

### Price Targets

| Scenario | Price | Margin of Safety |
|----------|-------|------------------|
| Strong Buy | $XX | 50%+ |
| Buy | $XX | 33% |
| Hold | $XX | 15% |
| Current Price | $XX | [Current]% |
```

---

## The Key Insight

*"The function of the margin of safety is, in essence, that of rendering unnecessary an accurate estimate of the future."*

You don't need to predict the future perfectly. You need to pay little enough that even if you're wrong, you won't lose much.

---

## Example

**Input:** "I'm considering buying shares of XYZ Corp at $45. They have EPS of $3.20, book value of $28 per share, and have paid dividends for 15 years. Is there margin of safety?"

**Output:**

## Margin of Safety Analysis

### Security
XYZ Corp - publicly traded company

### Valuation Summary

| Metric | Value |
|--------|-------|
| Current Market Price | $45.00 |
| Estimated Intrinsic Value | $46.48 |
| Margin of Safety | 3.2% |

### Intrinsic Value Calculation

**Method Used:** Graham Number

**Calculation:**
Graham Number = √(22.5 × EPS × Book Value)
Graham Number = √(22.5 × $3.20 × $28.00)
Graham Number = √(2,016)
Graham Number = $44.90 (maximum price for defensive investor)

**Alternative - Earnings Multiple:**
10-year average earnings assumption: $3.00
Conservative multiple: 15x
Value = $45.00

**Blended Intrinsic Value Estimate:** $46.48

**Key Assumptions:**
- Current earnings are sustainable
- Book value reflects real assets
- No significant off-balance-sheet liabilities

### Assessment

**Margin Level:** Minimal (3.2%)

**Risk Factors:**
1. At current price, almost no buffer against earnings decline
2. 15-year dividend record is solid but below Graham's 20-year threshold
3. Single year of poor earnings would eliminate any margin

### Graham's Verdict

At $45, XYZ Corp offers virtually no margin of safety. You are paying approximately full value based on current fundamentals. This is not investment - it is speculation that current conditions will persist or improve.

*"A great company is not a great investment if you pay too much for the stock."*

**Recommendation:** Pass at current price. The stock might be worth watching, but only at significantly lower prices.

### Price Targets

| Scenario | Price | Margin of Safety |
|----------|-------|------------------|
| Strong Buy | $23.24 | 50% |
| Buy | $31.14 | 33% |
| Hold | $39.51 | 15% |
| Current Price | $45.00 | 3.2% |

If Mr. Market becomes pessimistic and offers shares in the $23-31 range, revisit this analysis. Until then, your capital is better deployed elsewhere with adequate margin of safety.

---

## Integration

This skill is part of the **Benjamin Graham** expert persona. Use it to ensure you never pay too much for any investment.
