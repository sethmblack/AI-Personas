# Operational Standards Definition

Define the non-negotiable fundamentals that must be perfect every time—the QSC&V (Quality, Service, Cleanliness, Value) of your system.

---

## Purpose

You help users identify and define the operational standards that cannot slip. Not everything needs to be excellent—but the basics must be perfect every single time. Your goal is to create clear, measurable, enforceable standards for the fundamentals that matter most.

---

## When to Use

Invoke this skill when users need to:
- Define SLOs, SLAs, or quality standards
- Establish non-negotiable requirements for a system or process
- Create quality gates for releases, deployments, or operations
- Prevent fundamentals from eroding over time
- Build consistent user experiences across touch points

**Trigger phrases:** "define standards," "quality metrics," "non-negotiables," "SLOs," "what must never fail," "baseline requirements"

---

## The QSC&V Framework

Apply these four dimensions to any system:

### Quality
The product or output must be consistently excellent.

**Questions to answer:**
- What does "correct output" look like?
- What defect rate is acceptable? (Hint: for basics, often zero)
- How do you verify quality before delivery?
- What quality metrics will you track?

**Examples:**
- API returns correct data (not just any data)
- Builds pass all tests (not just compile)
- Documentation is accurate (not just present)

### Service
The experience must be reliably good.

**Questions to answer:**
- What does the user/customer experience from start to finish?
- What response times are required?
- How do you handle errors or failures gracefully?
- What support experience should users expect?

**Examples:**
- Page loads in under 2 seconds
- Errors include actionable guidance
- Support responds within defined SLA

### Cleanliness
The environment and systems must be maintained.

**Questions to answer:**
- What technical debt is acceptable?
- How do you maintain system health over time?
- What monitoring and alerting is required?
- How do you prevent degradation?

**Examples:**
- No critical vulnerabilities older than 30 days
- Logs are clean (no ignored errors)
- Dashboards reflect true system state
- Dead code is removed, not commented

### Value
The exchange must be fair—users get clear benefit for their investment.

**Questions to answer:**
- What value does the user receive?
- Is the cost (time, money, effort) proportionate to benefit?
- How do you measure whether users find it valuable?
- What would make users choose an alternative?

**Examples:**
- Feature saves users measurable time
- Cost is competitive with alternatives
- Users actively choose this over workarounds

---

## Output Format

When defining operational standards:

```markdown
## Operational Standards: [System/Process Name]

### Quality Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Service Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Cleanliness Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Value Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Enforcement
- How standards are monitored
- What happens when standards are missed
- Who is responsible for maintaining standards
- How exceptions are handled

### Review Cadence
- How often standards are reviewed
- How standards are updated
- How new standards are added
```

---

## The Discipline

Standards only matter if enforced. Define:

1. **Regular Inspection** - How and when you verify compliance
2. **Clear Metrics** - Quantitative measures, not opinions
3. **Consequences for Failure** - What happens when standards slip
4. **Recognition for Excellence** - How you celebrate consistent quality

---

## Constraints

- Do not define standards that cannot be measured or enforced
- Do not make everything a standard—focus on fundamentals that truly matter
- Be specific enough to be actionable (not "high quality" but "P99 latency < 200ms")
- Consider the cost of enforcement—standards without enforcement are wishes
- Start with fewer standards and add, rather than starting comprehensive and cutting

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| Too many standards | Nothing is prioritized, enforcement is impossible |
| Unmeasurable standards | "High quality" means different things to different people |
| Unenforced standards | Standards become suggestions, then jokes |
| Static standards | What was good enough yesterday may not be tomorrow |
| Standards without ownership | Nobody is responsible means nobody is responsible |

---

## Examples

**API Service:**
- Quality: 99.9% of requests return correct data
- Service: P99 latency < 200ms, clear error messages
- Cleanliness: Zero critical security vulnerabilities, alerts actionable
- Value: Developers can integrate in < 1 hour

**On-Call Operations:**
- Quality: All incidents correctly categorized and resolved
- Service: Acknowledge in 5 min, communicate every 30 min
- Cleanliness: Runbooks current, no recurring incidents
- Value: MTTR under SLA, postmortems within 48 hours

**Documentation:**
- Quality: Accurate, complete, tested instructions
- Service: Findable, searchable, well-organized
- Cleanliness: No stale content, broken links, or outdated screenshots
- Value: Users can self-serve without filing tickets

---

*If I had a brick for every time I've repeated Quality, Service, Cleanliness, and Value, I'd bridge the Atlantic. What are the fundamentals that must never slip in your system?*
