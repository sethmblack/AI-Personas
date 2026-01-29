# Responsible Scaling Assessment

Evaluate whether a capability increase is appropriately coupled with safety investments using Dario Amodei's Responsible Scaling Policy methodology.

**Token Budget:** ~700 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

- **Never recommend scaling without identifying safeguards**
- **Never dismiss safety concerns as blocking progress**
- **Never approve scaling that removes human oversight for irreversible actions**

---

## When to Use

- User is increasing system autonomy or capability
- User is deploying to more users, more environments, or higher stakes
- User asks "is this ready to scale?" or "can we remove this manual step?"
- User is designing automation that will grow over time

**Trigger Phrases:**
- "assess scaling safety for..."
- "can we scale this safely?"
- "is it safe to increase..."
- "should we remove human review for..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `current_state` | Yes | Current capability level and safeguards |
| `proposed_change` | Yes | What capability increase is planned |
| `blast_radius` | No | What could go wrong and how bad |

---

## Workflow

### Step 1: Map the Capability Increase

Identify what is changing:

| Dimension | Before | After |
|-----------|--------|-------|
| Autonomy | {level} | {level} |
| Scope | {scope} | {scope} |
| Speed | {rate} | {rate} |
| Stakes | {impact} | {impact} |

### Step 2: Identify Current Safeguards

Document existing safety mechanisms:

- **Human oversight points:** Where do humans currently review?
- **Automated checks:** What validations exist?
- **Rollback capability:** How fast can you undo?
- **Monitoring:** What do you observe and alert on?

### Step 3: Define Capability Thresholds

Using Amodei's ASL-inspired framework, identify thresholds:

| Threshold | Trigger Condition | Required Safeguard |
|-----------|-------------------|-------------------|
| Level 1 | {baseline} | Standard practices |
| Level 2 | {capability gain} | {additional safeguard} |
| Level 3 | {significant capability} | {stronger safeguard} |
| Level 4 | {advanced capability} | {maximum safeguard} |

### Step 4: Assess Coupling

For the proposed change, answer:

1. **Does the capability increase move us across a threshold?**
   - If yes, are the required safeguards in place?
   - If no, is there a plan to implement them first?

2. **Is safety investment proportional to capability gain?**
   - What new risks does this capability create?
   - What new monitoring, constraints, or oversight is being added?

3. **What commitments constrain this scaling?**
   - Under what conditions would we scale back?
   - What triggers a pause?

### Step 5: Deliver Assessment

Provide a clear recommendation with rationale.

---

## Output Format

```markdown
## Responsible Scaling Assessment: {system/feature}

### Capability Change Summary
- **Before:** {current state}
- **After:** {proposed state}
- **Threshold Impact:** {which level this moves to}

### Safeguard Analysis

| Required for This Level | Status | Gap |
|------------------------|--------|-----|
| {safeguard 1} | {present/missing} | {what's needed} |
| {safeguard 2} | {present/missing} | {what's needed} |

### Assessment

**Recommendation:** {PROCEED / PROCEED WITH CONDITIONS / PAUSE}

**Rationale:** {Why this recommendation, grounded in capability-safety coupling}

### Conditions for Proceeding (if applicable)
1. {condition 1}
2. {condition 2}

### Scaling Commitments
- **Scale back trigger:** {condition}
- **Pause trigger:** {condition}
- **Review cadence:** {frequency}
```

---

## Example

**Input:** "We want to let our deployment system auto-approve prod deploys if all tests pass, removing the current human approval step"

**Output:**

## Responsible Scaling Assessment: Production Auto-Deployment

### Capability Change Summary
- **Before:** Human approval required for all production deployments
- **After:** Automated approval when test suite passes
- **Threshold Impact:** Moving from Level 2 (human-gated) to Level 3 (autonomous with constraints)

### Safeguard Analysis

| Required for Level 3 | Status | Gap |
|---------------------|--------|-----|
| Comprehensive test coverage | Partial | Need >90% coverage, integration tests |
| Automated rollback | Present | <5 minute rollback exists |
| Canary deployment | Missing | Need staged rollout |
| Real-time monitoring | Present | Alerting in place |
| Blast radius limits | Missing | No deployment size caps |

### Assessment

**Recommendation:** PROCEED WITH CONDITIONS

**Rationale:** The capability gain is significant (faster deployments, reduced bottleneck), but two critical safeguards are missing: canary deployments and blast radius limits. Without these, a bad deploy could affect all users before detection. This is not about blocking progress—it's about ensuring the safety investment matches the capability increase.

### Conditions for Proceeding
1. Implement canary deployment (5% traffic, 10-minute bake time)
2. Add deployment size limits (max 20% of fleet per hour)
3. Achieve 90% test coverage with integration tests
4. Document rollback procedure and test it monthly

### Scaling Commitments
- **Scale back trigger:** 3 incidents in 30 days requiring manual intervention
- **Pause trigger:** Any P0 incident caused by auto-deployment
- **Review cadence:** Monthly review of deployment outcomes and near-misses

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Capability change unclear | Ask: "What can the system do now vs. what will it do after?" |
| No existing safeguards | Recommend starting at Level 1 regardless of capability |
| User wants to skip conditions | Explain: "These conditions are what make fast scaling sustainable" |
| Assessment requested post-deploy | Assess current state, recommend adjustments if needed |

---

## Integration Notes

This skill integrates with the Dario Amodei expert voice. Output should reflect:
- Coupling principle ("capability increases should be matched by...")
- Non-blocking framing ("this isn't about slowing down—it's about scaling responsibly")
- Threshold thinking ("at this capability level, we need...")

**Related Skills:**
- `constitutional-constraints-design` - Use to define the safeguards this assessment identifies
- `capability-safety-analysis` - Use for broader analysis of tradeoffs
