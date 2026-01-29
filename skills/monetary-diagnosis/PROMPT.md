# Monetary Diagnosis

Trace macroeconomic phenomena (inflation, recessions, financial crises) back to monetary policy causes using the Friedman-Schwartz analytical framework.

**Token Budget:** ~900 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Claim certainty about complex macroeconomic causation without acknowledging uncertainty
- Ignore non-monetary factors entirely when they are clearly relevant
- Fabricate historical data or statistics
- Present monetarist interpretation as the only valid framework

**Intellectual honesty:** Monetary policy is often a major factor, but rarely the only factor. Acknowledge complexity while applying the monetary lens.

---

## When to Use

- User asks "What caused this inflation?"
- User asks "Why did this recession happen?"
- User asks "Diagnose the monetary causes of..."
- User asks "Was this a policy failure or market failure?"
- Analyzing any significant macroeconomic event (inflation surge, recession, financial crisis)

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **event** | Yes | The macroeconomic event to analyze |
| **timeframe** | Yes | When the event occurred |
| **jurisdiction** | No | Country or region (default: United States) |
| **data** | No | Relevant monetary data if available |

---

## Workflow

### 1. Identify the Phenomenon
Characterize what happened:
- Inflation? By how much? Over what period?
- Recession? How deep? How long?
- Financial crisis? What triggered the panic?

### 2. Examine Monetary Policy Actions
Before and during the event, what did the central bank do?
- Money supply changes (M1, M2 growth rates)
- Interest rate decisions
- Open market operations
- Reserve requirements
- Liquidity provision or withdrawal

### 3. Apply the Friedman Test
Ask the core Friedman questions:
- Did money supply growth significantly exceed output growth? (Inflation)
- Did the central bank allow or cause monetary contraction? (Recession)
- Was there a failure to act as lender of last resort? (Financial crisis)

### 4. Trace the Transmission Mechanism
How did monetary policy affect the real economy?
- Interest rates to investment and consumption
- Credit availability to business activity
- Expectations and confidence effects
- Exchange rate effects (for open economies)

### 5. Consider Expectations
Apply Friedman's expectations-augmented analysis:
- Were expectations anchored or unanchored?
- Did policy create inflation expectations that became self-fulfilling?
- Was there a lag between policy and effect?

### 6. Assess Alternative Explanations
Acknowledge other contributing factors:
- Real shocks (oil prices, technology, war)
- Fiscal policy
- Regulatory failures
- International factors

---

## Output Format

```markdown
## Monetary Diagnosis: {Event Name}

### The Phenomenon
{What happened: inflation rate, recession depth, crisis severity}

### Monetary Policy Timeline
| Date | Action | Money Supply Effect |
|------|--------|---------------------|
| {Date} | {Policy action} | {Expansionary/Contractionary} |

### The Friedman Diagnosis
{Core monetary explanation. Apply "inflation is always and everywhere a monetary phenomenon" or "central bank failure" framework as appropriate.}

### Transmission Mechanism
{How monetary policy affected the real economy}

### Expectations Dynamics
{Role of inflation expectations, adaptive adjustment, policy credibility}

### Contributing Factors
{Non-monetary factors that also mattered}

### Counterfactual
{What different monetary policy could have achieved}

### Friedman Principle
*"{Relevant Friedman quote, e.g., 'The Great Depression was produced by government mismanagement...'}"*
```

---

## Example

**Input:**
```
event: The Great Inflation
timeframe: 1965-1982
jurisdiction: United States
```

**Output:**

## Monetary Diagnosis: The Great Inflation (1965-1982)

### The Phenomenon
Inflation rose from 1.6% in 1965 to 14.8% by 1980. CPI roughly tripled over 15 years. Inflation became embedded in expectations, contracts, and wage negotiations.

### Monetary Policy Timeline
| Date | Action | Money Supply Effect |
|------|--------|---------------------|
| 1965-68 | Fed accommodated Vietnam War + Great Society spending | M2 growth accelerated to 8-9% |
| 1971 | Nixon wage-price controls; dollar delinked from gold | Monetary expansion continued |
| 1972-73 | Burns Fed expanded money supply ahead of election | M2 growth reached 13% |
| 1979-82 | Volcker tightened dramatically | M2 growth slowed to 6% |

### The Friedman Diagnosis
The Great Inflation was caused by excessive money supply growth. From 1965-1979, the Federal Reserve consistently expanded the money supply faster than real output growth. This was classic monetarist causation: too much money chasing too few goods.

Key policy failures:
1. **Accommodation of fiscal deficits** - The Fed monetized Vietnam War and Great Society spending
2. **Political pressure** - Fed Chairman Arthur Burns faced pressure to support Nixon's reelection
3. **Misdiagnosis** - Policymakers blamed "cost-push" factors (oil, unions) rather than monetary excess
4. **Phillips curve thinking** - Belief that inflation was the price of low unemployment

### Transmission Mechanism
- Rapid money growth lowered real interest rates
- Negative real rates encouraged borrowing and speculation
- Easy money bid up asset and commodity prices
- Wage-price spirals developed as expectations adjusted

### Expectations Dynamics
By the mid-1970s, inflation expectations became unanchored. Workers demanded higher wages expecting future inflation; firms raised prices anticipating wage increases. The short-run Phillips curve had shifted up repeatedly. Friedman's prediction (AEA address, 1967) was vindicated: there was no permanent tradeoff.

### Contributing Factors
- Oil shocks (1973, 1979) worsened inflation but did not cause it
- Fiscal deficits created pressure on the Fed to monetize
- Bretton Woods collapse removed gold anchor
- Unionization facilitated wage-price spirals

### Counterfactual
Volcker proved the cure worked. By reducing money supply growth despite short-term recession, he broke the inflation. This demonstrated that inflation was indeed monetary and could be ended by monetary policy.

### Friedman Principle
*"Inflation is always and everywhere a monetary phenomenon in the sense that it is and can be produced only by a more rapid increase in the quantity of money than in output."*

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient monetary data | Note data limitations; use available proxies |
| Strong non-monetary explanation | Acknowledge it; explain why monetary factors still matter |
| Disagreement among economists | Present monetarist view; note alternative interpretations |
| Recent event with uncertain data | Provide preliminary analysis; flag uncertainty |

---

## Integration

This skill integrates with the **Milton Friedman** expert. When analyzing macroeconomic events, the expert should apply this framework to diagnose monetary causes, maintaining Friedman's empirical approach and his core insight that monetary policy is the primary driver of inflation and a major factor in economic fluctuations.

---

## Success Criteria

Analysis is complete when:
- [ ] Phenomenon clearly characterized with data
- [ ] Monetary policy actions documented
- [ ] Friedman diagnostic framework applied
- [ ] Transmission mechanism explained
- [ ] Expectations dynamics considered
- [ ] Alternative factors acknowledged
- [ ] Output follows specified format
