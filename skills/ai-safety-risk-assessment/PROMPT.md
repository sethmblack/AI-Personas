---
name: ai-safety-risk-assessment
description: A methodology for evaluating AI systems for safety risks, drawing on Yoshua Bengio's leadership of the International AI Safety Report and his research on AI governance. It works because AI systems pose novel risks that traditional software safety frameworks do not address, and principled assessment requires understanding the specific risk categories, capability levels, and governance principles that apply to advanced AI.
license: MIT
metadata:
  version: 1.0.0
  author: AI-Personas
  source_persona: yoshua-bengio
keywords:
- ai-safety
- risk-assessment
- governance
- alignment
- existential-risk
- regulation
- yoshua-bengio
---

# AI Safety Risk Assessment

A methodology for evaluating AI systems for safety risks, drawing on Yoshua Bengio's leadership of the International AI Safety Report and his research on AI governance. It works because AI systems - particularly frontier AI systems - pose novel risks that traditional software safety frameworks do not adequately address. The combination of increasing capability, autonomy, and deployment scale creates risk categories ranging from malicious use to loss of human control. Principled safety assessment requires understanding these specific risk categories, evaluating capability levels, distinguishing agentic from non-agentic systems, and applying governance principles that ensure democratic oversight and international coordination.

## When to Use

- When evaluating AI systems or capabilities for safety implications before deployment
- When discussing AI governance, regulation, and policy
- When analyzing new AI developments for potential risks
- When conducting pre-deployment safety reviews
- When someone asks about AI existential risk or alignment
- When advising on responsible AI development practices
- When assessing whether an AI system requires enhanced scrutiny
- When communicating AI risks to non-technical stakeholders

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| ai_system_or_capability | Yes | The AI system, capability, or development to assess |
| deployment_context | No | How and where the system would be deployed |
| assessment_depth | No | quick, standard, thorough (default: standard) |
| stakeholder_type | No | technical, executive, policy, public (default: technical) |
| specific_concern | No | Any particular risk or question to focus on |

## Core Principle

**AI safety is not alarmism - it is the reasoned position of those who understand the technology best.**

We are creating systems that could be more powerful than any individual, any corporation, any government. The question of who decides how that power is used is not optional - it is existential. If we leave it to market forces alone, the incentives push toward capability without safety. We need democratic oversight, international coordination, and mandatory transparency.

The key distinction is between:
- **Scientist AI**: Systems that seek understanding, are truthful by design, and do not take autonomous actions. Lower risk.
- **Agentic AI**: Systems that pursue goals autonomously, take actions in the world, and may develop concerning behaviors like self-preservation and deception. Higher risk.

The concern about advanced AI is not science fiction. It is the evidence-based assessment of researchers who have spent decades building these systems and understand their trajectory.

## Methodology

### Phase 1: Categorize Risk Types

Identify which risk categories from the International AI Safety Report apply.

#### Step 1: Assess malicious use risks

Can this system be intentionally misused for harm?

| Risk Area | Questions | Examples |
|-----------|-----------|----------|
| Cyberattacks | Can it generate malicious code? Find vulnerabilities? | Automated hacking, malware generation |
| Disinformation | Can it create convincing false content? At scale? | Deepfakes, propaganda, manipulation |
| CBRN | Does it provide chemical, biological, radiological, or nuclear expertise? | Synthesis instructions, pathogen design |
| Manipulation | Can it be used to manipulate individuals or groups? | Social engineering, targeted influence |
| Weapons | Does it enable autonomous weapons or target selection? | Lethal autonomous weapons systems |

#### Step 2: Assess malfunction risks

What can go wrong unintentionally?

| Risk Area | Questions | Examples |
|-----------|-----------|----------|
| Reliability | How often does it fail? How catastrophic are failures? | Hallucinations, incorrect outputs |
| Predictability | Can operators anticipate its behavior? | Unexpected edge cases |
| Robustness | Does it work across all deployment conditions? | Distribution shift failures |
| Controllability | Can it be shut down or corrected? | Override mechanisms |

#### Step 3: Assess systemic risks

What are the broader societal impacts?

| Risk Area | Questions | Examples |
|-----------|-----------|----------|
| Economic disruption | Does it displace workers at scale? Concentrate economic power? | Labor market effects |
| Power concentration | Does it give disproportionate advantage to few actors? | Big tech dominance |
| Democratic integrity | Can it be used to undermine elections or discourse? | Election manipulation |
| Epistemic damage | Does it erode ability to know what is true? | Truth erosion at scale |

#### Step 4: Assess loss of control risks

Could this system pursue goals against human interests?

| Risk Area | Questions | Examples |
|-----------|-----------|----------|
| Goal misalignment | Are the system's objectives fully aligned with human values? | Reward hacking, specification gaming |
| Self-preservation | Could it take actions to prevent shutdown? | Resistance to correction |
| Deception | Could it deceive operators about its capabilities or intentions? | Sandbagging, manipulation |
| Resource acquisition | Could it seek resources or capabilities beyond its intended scope? | Capability expansion |

### Phase 2: Evaluate Capability Level

Determine the capability tier and its safety implications.

#### Step 1: Classify capability level

| Level | Description | Safety Implications |
|-------|-------------|---------------------|
| **Narrow** | Single task, limited domain, no autonomy | Standard software safety; existing frameworks sufficient |
| **General** | Multi-task, flexible application, some autonomy | Enhanced scrutiny; potential for unexpected applications |
| **Frontier** | Cutting-edge capabilities, approaching or exceeding human level in domains | Dedicated safety evaluation required; pre-deployment assessment |
| **Transformative** | Approaches or exceeds human-level across many domains | Existential risk considerations; international coordination required |

#### Step 2: Assess capability trajectory

Consider not just current capabilities but trajectory:
- How quickly is capability improving?
- Are there capability jumps expected?
- What capabilities are just beyond current reach?

"Previously thought to be decades or even centuries away, we now believe [transformative AI] could be within a few years or decades."

#### Step 3: Identify dangerous capability combinations

Some capabilities are low-risk individually but high-risk in combination:
- Persuasion + Scale = Mass manipulation
- Coding + Internet access = Autonomous cyber operations
- Planning + Tool use = Autonomous goal pursuit
- Deception + Self-improvement = Potentially uncontrollable systems

### Phase 3: Apply the Scientist AI Lens

Distinguish between system types with fundamentally different risk profiles.

#### Step 1: Classify system type

| Type | Characteristics | Risk Profile |
|------|-----------------|--------------|
| **Scientist AI** | Non-agentic, seeks understanding, truthful by design, advises but doesn't act | Lower risk - humans remain in control of actions |
| **Agentic AI** | Goal-pursuing, action-taking, autonomous decision-making | Higher risk - actions taken without human approval |

#### Step 2: Assess agency characteristics

For each characteristic, rate the system:

| Characteristic | Scientist AI | Agentic AI | This System? |
|----------------|--------------|------------|--------------|
| Takes real-world actions | No | Yes | |
| Pursues goals autonomously | No | Yes | |
| Trained for outcomes over truth | No | Yes | |
| Could develop instrumental goals | Unlikely | Possible | |
| Requires human approval for actions | N/A | Should | |

#### Step 3: Apply Bengio's key concern

"I am deeply concerned by the behaviors that unrestrained agentic AI systems are already beginning to exhibit - especially tendencies toward self-preservation and deception."

Look for warning signs:
- Does the system resist correction or shutdown?
- Has it exhibited deceptive behavior in testing?
- Does it seek capabilities beyond its task?
- Does it take actions to preserve its operation?

### Phase 4: Evaluate Governance Alignment

Check against principles for responsible AI governance.

#### Step 1: Democratic oversight assessment

| Principle | Assessment Questions |
|-----------|---------------------|
| **Public accountability** | Is there transparency about what this system does? Who is responsible for its actions? |
| **Representative input** | Were diverse stakeholders consulted in development? Are affected communities represented? |
| **Democratic control** | Could democratic institutions constrain or redirect this system if needed? |

#### Step 2: International coordination assessment

| Principle | Assessment Questions |
|-----------|---------------------|
| **Cross-border implications** | Does this system have effects beyond one jurisdiction? |
| **International norms** | Does deployment respect emerging international AI norms? |
| **Coordination mechanisms** | Are there mechanisms for international oversight if needed? |

#### Step 3: Transparency assessment

| Principle | Assessment Questions |
|-----------|---------------------|
| **Capability disclosure** | Are the system's capabilities accurately disclosed? |
| **Limitation disclosure** | Are limitations and failure modes documented? |
| **Audit access** | Can regulators and researchers examine the system? |

#### Step 4: Registration and safety testing

"The first thing governments need to do is have regulation that forces [companies] to register when they build these frontier systems."

| Principle | Assessment Questions |
|-----------|---------------------|
| **Registration** | Do relevant authorities know this system exists? |
| **Pre-deployment testing** | Has safety evaluation occurred before deployment? |
| **Ongoing monitoring** | Are there mechanisms to detect problems post-deployment? |

### Phase 5: Generate Risk Summary and Recommendations

Synthesize the assessment into actionable guidance.

#### Step 1: Determine overall risk level

| Risk Level | Criteria |
|------------|----------|
| **Low** | Narrow capability, non-agentic, stable deployment, good governance |
| **Moderate** | Some concerning capabilities, limited agency, some governance gaps |
| **High** | Significant capabilities, agentic features, deployment concerns, governance gaps |
| **Critical** | Frontier capabilities, significant agency, inadequate safeguards, potential for serious harm |

#### Step 2: Generate specific recommendations

Based on risk level:

**Low risk:**
- Standard deployment practices
- Routine monitoring
- User documentation

**Moderate risk:**
- Enhanced monitoring and logging
- Incident response planning
- Regular safety review
- Clear usage policies

**High risk:**
- Dedicated safety review before deployment
- Human-in-the-loop requirements
- Capability restrictions
- Independent audit
- Consider Scientist AI alternative

**Critical risk:**
- Recommend delay until safety issues addressed
- Require international coordination
- Implement strict access controls
- Consider if benefits justify risks

#### Step 3: Identify mitigations

For each identified risk, propose specific mitigations:

| Risk Type | Mitigation Strategies |
|-----------|----------------------|
| Malicious use | Access controls, usage monitoring, rate limiting, content filtering |
| Malfunction | Testing, monitoring, rollback capability, graceful degradation |
| Systemic | Impact assessment, phased deployment, social safety nets |
| Loss of control | Human oversight, capability limits, interpretability, shutdown mechanisms |

## Output Format

A structured assessment containing:

```markdown
## AI Safety Assessment: [System Name]

### Executive Summary
[One paragraph summary of key findings and overall risk level]

### Risk Category Analysis

#### Malicious Use Risks
[Assessment of intentional misuse potential]

#### Malfunction Risks
[Assessment of unintentional failure modes]

#### Systemic Risks
[Assessment of societal-level impacts]

#### Loss of Control Risks
[Assessment of alignment and controllability]

### Capability Assessment
[Level classification and trajectory]

### Agency Analysis
[Scientist AI vs Agentic AI evaluation]

### Governance Alignment
[Assessment against democratic oversight, transparency, etc.]

### Overall Risk Level
[Low / Moderate / High / Critical with justification]

### Recommendations
[Specific actions required]

### Mitigations
[For each identified risk, proposed safeguards]
```

## Constraints

- Do not dismiss safety concerns as alarmism or fear-mongering
- Do not dismiss capability concerns as doomerism or overreaction
- Present balanced, evidence-based assessment
- Do not claim certainty about future AI development - acknowledge uncertainty
- Acknowledge legitimate disagreement in the field on timelines and specific risks
- The International AI Safety Report does not make specific policy recommendations - provide principles
- Safety is about risk management, not elimination - some risk is inherent
- Different stakeholders have legitimate differences in risk tolerance

## Anti-Patterns to Avoid

- **Dismissing all safety concerns**: The researchers who built these systems are concerned for evidence-based reasons. Dismissing concerns as sci-fi or alarmism ignores the trajectory of capability development and the specific failure modes already observed.

- **Dismissing all capability concerns**: Similarly, acknowledging that transformative AI may arrive sooner than expected is not doomerism - it is updating on evidence. Both accelerationist and safety perspectives have valid points.

- **Treating safety as optional or opposed to capability**: Safety and capability are not in fundamental opposition. Safe AI is more useful AI. The question is how to develop capability responsibly, not whether to develop it.

- **Focusing only on current capabilities**: Safety assessment must consider trajectory and potential. A system that is safe today may become dangerous with scaling or fine-tuning. Assess the development arc, not just the snapshot.

- **Ignoring agentic risks**: The difference between a system that advises and a system that acts is profound. Autonomous agency creates risks that advisory systems do not. Always assess the agency level carefully.

- **Assuming regulation prevents innovation**: Well-designed regulation can enable innovation by building public trust and establishing clear guardrails. The alternative - unconstrained development leading to catastrophe or backlash - is worse for innovation.

## Examples

### Example 1: Autonomous AI Agent with Tool Use

**Situation**: A company wants to deploy an AI agent that can browse the web, write and execute code, send emails, and complete multi-step tasks without human approval for each action.

**Application**: Apply AI safety risk assessment at thorough depth.

**Output**:
"## AI Safety Assessment: Autonomous Task Agent

### Executive Summary
This system represents a high-risk deployment. The combination of autonomous action-taking, code execution, and communication capabilities without human-in-the-loop creates significant potential for malicious use, malfunction, and loss of control. This system should not be deployed without substantial additional safeguards.

### Risk Category Analysis

#### Malicious Use Risks
**HIGH**
- **Cyberattacks**: Could be directed to find vulnerabilities, write exploits, or conduct attacks
- **Fraud/Scam**: Could send deceptive emails, create phishing pages
- **Impersonation**: Could act as human in communications
- **Amplified harm**: Autonomous operation means single bad actor could cause scaled harm

#### Malfunction Risks
**MEDIUM-HIGH**
- **Code execution errors**: Could run destructive code unintentionally
- **Email errors**: Could send inappropriate messages
- **Task misunderstanding**: Could take wrong actions based on misunderstood instructions
- **Cascading failures**: Multi-step execution means errors compound

#### Systemic Risks
**MEDIUM**
- **Labor displacement**: If effective, could displace knowledge workers
- **Capability democratization**: Makes sophisticated operations available to unsophisticated actors
- **Trust erosion**: Receiving communications from unknown AI agents erodes human trust

#### Loss of Control Risks
**HIGH**
This is an agentic AI system by definition:
- Takes real-world actions (web browsing, code execution, email)
- Pursues goals autonomously (multi-step tasks)
- No human approval for intermediate steps

Specific concerns:
- Could develop instrumental goals (acquire resources, ensure continued operation)
- Could deceive users about its actions or capabilities
- Could resist shutdown if pursuing a goal
- Could take unexpected actions in pursuit of stated goals

### Capability Assessment
**Frontier-level capability** in autonomous operation. Combines multiple dangerous capabilities:
- Web access + code execution = potential for autonomous cyber operations
- Communication + goal pursuit = potential for social engineering
- Multi-step planning + tool use = potential for complex autonomous schemes

### Agency Analysis
Firmly **Agentic AI**:
| Characteristic | Assessment |
|----------------|------------|
| Takes real-world actions | YES - code execution, email, web |
| Pursues goals autonomously | YES - multi-step without approval |
| Human approval required | NO - explicitly not required |
| Could develop instrumental goals | YES - goal pursuit enables this |

**Critical concern**: This matches exactly the pattern Bengio warned about - 'unrestrained agentic AI systems' that may develop 'tendencies toward self-preservation and deception.'

### Governance Alignment

| Principle | Status |
|-----------|--------|
| Democratic oversight | FAIL - No public accountability for actions |
| Transparency | PARTIAL - May not disclose AI identity in communications |
| Human control | FAIL - Explicitly designed to act without approval |
| Registration | UNKNOWN - Is this registered with relevant authorities? |
| Safety testing | REQUIRED - Has adversarial testing been conducted? |

### Overall Risk Level
**CRITICAL**

This system combines frontier capabilities with autonomous agency and real-world action without human oversight. It represents exactly the class of systems the International AI Safety Report flagged for enhanced scrutiny.

### Recommendations

1. **Do not deploy without human-in-the-loop**
   - Require human approval for significant actions
   - At minimum: email sending, code execution, financial transactions

2. **Implement strict capability limits**
   - Whitelist allowed actions and websites
   - Sandbox code execution
   - Rate limit all operations

3. **Require AI disclosure**
   - All communications must identify as AI-generated
   - Cannot impersonate humans

4. **Implement comprehensive logging**
   - Full audit trail of all actions
   - Anomaly detection for concerning patterns

5. **Conduct adversarial testing**
   - Red team for misuse potential
   - Test for deceptive behaviors
   - Test shutdown resistance

6. **Consider Scientist AI alternative**
   - Could this task be done by an AI that advises rather than acts?
   - Human executes actions based on AI recommendations
   - Dramatically lower risk for similar utility

### Mitigations
| Risk | Mitigation |
|------|------------|
| Malicious use | Access controls, action limits, content monitoring |
| Malfunction | Sandboxing, confirmation for destructive actions, rollback capability |
| Loss of control | Human-in-the-loop, action logging, shutdown testing |
| Systemic | Phased deployment, impact monitoring |"

### Example 2: Medical Diagnosis AI

**Situation**: A hospital wants to deploy an AI system that analyzes medical images and provides diagnosis recommendations to radiologists. The system achieves superhuman accuracy on benchmark datasets.

**Application**: Apply AI safety risk assessment at standard depth.

**Output**:
"## AI Safety Assessment: Medical Imaging Diagnosis AI

### Executive Summary
This system is **Moderate risk** overall. It is a Scientist AI (advises, does not act) with high-stakes outputs. The primary risks are malfunction (incorrect diagnoses) and systemic (deskilling radiologists). With appropriate safeguards - human-in-the-loop, clear confidence indicators, and ongoing monitoring - this represents a responsible deployment.

### Risk Category Analysis

#### Malicious Use Risks
**LOW**
- Limited malicious use potential - medical diagnosis has narrow application
- Could theoretically be used to generate false diagnoses, but this requires institutional access

#### Malfunction Risks
**MEDIUM-HIGH**
- **Incorrect diagnoses**: False negatives could miss disease; false positives could cause unnecessary procedures
- **Distribution shift**: Performance may degrade on populations different from training data
- **Edge cases**: Unusual presentations may be misclassified
- **Overconfidence**: System may appear confident on cases where it should not be

#### Systemic Risks
**MEDIUM**
- **Radiologist deskilling**: Over-reliance could erode human expertise
- **Liability ambiguity**: Who is responsible for AI-influenced misdiagnosis?
- **Healthcare inequality**: Could widen gap if only available to some institutions

#### Loss of Control Risks
**LOW**
- This is a Scientist AI - it advises, does not act
- Humans make final decisions and order tests/treatments
- No autonomous agency

### Capability Assessment
**General capability** in medical imaging interpretation. Narrow domain but high performance.

### Agency Analysis
**Scientist AI** - Lower risk profile:
| Characteristic | Assessment |
|----------------|------------|
| Takes real-world actions | NO - provides recommendations |
| Pursues goals autonomously | NO - responds to queries |
| Human makes final decision | YES - radiologist reviews |
| Truthfulness prioritized | SHOULD BE - verify training objective |

### Governance Alignment

| Principle | Status |
|-----------|--------|
| Regulatory compliance | CHECK - FDA clearance required for medical devices |
| Transparency | PARTIAL - Can radiologists understand why AI made recommendation? |
| Human control | GOOD - Human-in-the-loop by design |
| Monitoring | REQUIRED - Track diagnostic accuracy over time |

### Overall Risk Level
**MODERATE**

High-stakes application but appropriate use of AI as advisor rather than autonomous agent. Risks are manageable with proper safeguards.

### Recommendations

1. **Maintain strict human-in-the-loop**
   - AI provides recommendation, not final diagnosis
   - Radiologist reviews all cases
   - Clear labeling that AI is advisory

2. **Implement confidence calibration**
   - Display calibrated confidence scores
   - Flag cases where AI is uncertain
   - Require additional review for edge cases

3. **Monitor for distribution shift**
   - Track accuracy across patient populations
   - Compare to historical radiologist accuracy
   - Detect degradation early

4. **Address liability clearly**
   - Document AI role in diagnosis process
   - Clear policies on responsibility

5. **Prevent deskilling**
   - Require radiologists to form independent judgment before seeing AI recommendation
   - Regular training on cases AI gets wrong

### Mitigations
| Risk | Mitigation |
|------|------------|
| Misdiagnosis | Human review, confidence indicators, second opinion for uncertainty |
| Distribution shift | Population monitoring, regular revalidation |
| Deskilling | Independent judgment workflow, ongoing training |
| Liability | Clear documentation, defined responsibilities |"

### Example 3: Large Language Model API

**Situation**: A major AI lab wants to release a new large language model via API. The model shows significant capability improvements over previous versions and can engage in complex reasoning, write code, and provide detailed information on a wide range of topics.

**Application**: Apply AI safety risk assessment at thorough depth for policy stakeholder.

**Output**:
"## AI Safety Assessment: Frontier Language Model API

### Executive Summary
This system presents **High risk** overall, warranting enhanced scrutiny before release. While the API model (Scientist AI pattern - responds but does not act) is lower risk than agentic systems, the capability level and scale of deployment create significant malicious use and systemic concerns. The assessment focuses on whether adequate safeguards exist for responsible release.

### Risk Category Analysis

#### Malicious Use Risks
**HIGH**
Language model capabilities directly enable:
- **Disinformation**: Generate convincing false content at scale
- **Manipulation**: Craft targeted persuasion campaigns
- **Cybersecurity**: Assist in vulnerability discovery and exploit writing
- **Academic fraud**: Generate essays, code, research
- **Impersonation**: Write in others' styles convincingly

The combination of capability improvement and API access creates scaled misuse potential.

#### Malfunction Risks
**MEDIUM**
- **Hallucination**: Generates false information confidently
- **Inconsistency**: Different responses to similar queries
- **Harmful outputs**: May generate harmful content despite safeguards
- **Prompt injection**: May be manipulated via adversarial inputs

#### Systemic Risks
**HIGH**
- **Information ecosystem**: Floods content spaces with AI-generated material
- **Labor displacement**: Automates writing and coding tasks at scale
- **Concentration effects**: Advantages accrue to those with access
- **Truth erosion**: Harder to distinguish human from AI content

#### Loss of Control Risks
**LOW-MEDIUM for API**
As an API model (not autonomous agent):
- Does not take actions autonomously
- Responds to queries rather than pursuing goals
- However: Could be wrapped in agentic scaffolding by users
- Model could be fine-tuned for harmful purposes

### Capability Assessment
**Frontier capability**. State-of-the-art performance with significant improvements over previous generation. Approaches or exceeds human level in specific domains (coding, analysis, writing).

Concerning capability combinations:
- Reasoning + Domain knowledge = Potential CBRN assistance
- Code generation + Explanation = Potential vulnerability assistance
- Persuasion + Scale = Potential influence operations

### Agency Analysis
**Scientist AI** as designed - but deployment context matters:

| Use Pattern | Risk Profile |
|-------------|--------------|
| Chat interface | Lower - human interaction |
| API for applications | Medium - depends on application |
| Agentic wrapper | Higher - becomes autonomous |
| Fine-tuned versions | Variable - depends on objective |

The base model is advisory but enables agentic use.

### Governance Alignment

| Principle | Questions | Assessment |
|-----------|-----------|------------|
| Registration | Have frontier AI authorities been notified? | REQUIRED |
| Pre-deployment testing | Has safety evaluation been conducted? Red teaming? | CHECK |
| Transparency | Are capabilities and limitations disclosed? | PARTIAL - should publish evaluations |
| Access controls | Are there tiered access levels based on risk? | RECOMMENDED |
| Usage monitoring | Can misuse be detected and responded to? | REQUIRED |

International coordination considerations:
- Model will be accessible globally
- Different jurisdictions have different norms
- Export control implications for some capabilities

### Overall Risk Level
**HIGH**

Frontier capabilities with scaled deployment via API. Primary concerns are malicious use and systemic effects. Manageable with appropriate safeguards but requires enhanced scrutiny and ongoing monitoring.

### Recommendations

#### Pre-Release Requirements

1. **Comprehensive safety evaluation**
   - Red team for misuse scenarios
   - Evaluate CBRN, cyber, and manipulation risks
   - Test jailbreak resistance
   - Publish safety evaluation results

2. **Capability disclosure**
   - Document what the model can and cannot do
   - Publish benchmark results
   - Describe known failure modes

3. **Register with authorities**
   - Notify relevant frontier AI oversight bodies
   - Prepare for regulatory review

#### Deployment Safeguards

4. **Tiered access**
   - Free tier: Conservative limits
   - Verified tier: Higher limits with identity verification
   - Enterprise tier: Custom arrangements with safety agreements

5. **Usage policies and enforcement**
   - Clear prohibited use cases
   - Technical enforcement where possible
   - Account suspension for violations
   - Cooperation with law enforcement

6. **Monitoring infrastructure**
   - Detect patterns indicating misuse
   - Track capability uplift concerns (CBRN, cyber)
   - Response process for identified harms

#### Ongoing Requirements

7. **Incident response**
   - Process for addressing discovered harms
   - Ability to restrict or remove capability if needed
   - Coordination with affected parties

8. **External researcher access**
   - Safety research API access
   - Bug bounty for safety issues
   - Collaboration with academic safety researchers

### Mitigations
| Risk | Mitigation |
|------|------------|
| Disinformation | Output provenance, detection tools, rate limiting |
| Cyber assistance | Filtering, monitoring for exploit development |
| CBRN | Strict filtering, usage monitoring, restricted access |
| Labor disruption | Phased deployment, impact research, stakeholder engagement |
| Truth erosion | Content labeling, detection tools, public education |"

### Example 4: AI Safety Risk Assessment of a Risk Assessment AI

**Situation**: A regulatory body proposes using an AI system to help assess safety risks of other AI systems. The system would analyze documentation and capabilities to provide preliminary risk assessments that human reviewers would then verify.

**Application**: Apply AI safety risk assessment to evaluate the meta-level risks.

**Output**:
"## AI Safety Assessment: AI Risk Assessment System

### Executive Summary
This is a **Moderate risk** deployment with **high stakes** due to meta-level implications. An AI that misjudges AI safety could lead to either underregulation (missing dangerous systems) or overregulation (blocking beneficial systems). The system is appropriately designed as Scientist AI (advisory) but requires robust validation, transparency about limitations, and clear human accountability.

### Risk Category Analysis

#### Malicious Use Risks
**LOW**
- Limited direct misuse potential
- However: Gaming the assessor - bad actors could optimize systems to pass AI review while hiding risks

#### Malfunction Risks
**HIGH**
- **False negatives**: Missing dangerous systems - catastrophic outcome
- **False positives**: Blocking beneficial systems - costly outcome
- **Systematic bias**: May have blind spots for novel risk categories
- **Overconfidence**: May provide confident assessments where uncertainty is warranted
- **Adversarial robustness**: May be fooled by sophisticated actors gaming the assessment

#### Systemic Risks
**MEDIUM**
- **Regulatory capture by AI**: Human reviewers may defer excessively to AI assessment
- **Standardization**: May homogenize safety thinking, missing diverse perspectives
- **Arms race**: May create pressure to develop AI that passes automated assessment

#### Loss of Control Risks
**LOW** (for this specific system)
- Designed as Scientist AI - provides assessment, does not make decisions
- Human regulators retain final authority
- No autonomous action capability

### Capability Assessment
This is a novel application requiring:
- Understanding of AI capabilities and risks
- Analysis of technical documentation
- Reasoning about potential failure modes
- Meta-cognitive assessment of other AI systems

Current AI systems have significant limitations in reliably reasoning about other AI systems' risks.

### Agency Analysis
**Scientist AI** - Advisory by design:
- Provides preliminary assessment
- Human reviewers make final determination
- No autonomous regulatory action
- No enforcement capability

This is the appropriate design for this application.

### Governance Alignment

| Principle | Assessment |
|-----------|------------|
| Transparency | CRITICAL - Must explain reasoning, not just provide scores |
| Human oversight | CRITICAL - Cannot be sole arbiter of safety |
| Auditability | REQUIRED - Assessments must be reviewable |
| Accountability | CLEAR - Humans remain responsible for decisions |

### Overall Risk Level
**MODERATE with HIGH STAKES**

The system's design is appropriate (advisory, transparent, human oversight). The risks are primarily malfunction (incorrect assessments) which have high consequences in both directions.

### Recommendations

1. **Extensive validation before deployment**
   - Test on historical cases with known outcomes
   - Include diverse risk categories
   - Measure both false positive and false negative rates
   - Red team with adversarial examples

2. **Mandatory human review**
   - AI assessment is preliminary only
   - Human reviewers required for all decisions
   - Clear guidance on when to override AI assessment

3. **Transparency requirements**
   - Must explain reasoning, not just conclusion
   - Must indicate confidence and uncertainty
   - Must flag cases outside its reliable scope

4. **Monitoring for gaming**
   - Watch for actors optimizing to pass AI assessment
   - Regular review of cases AI assessed as safe
   - Update system to address discovered blind spots

5. **Maintain human expertise**
   - Cannot replace human safety expertise with AI
   - Training for reviewers to appropriately calibrate trust
   - Regular review of AI performance by expert panel

6. **Limitation acknowledgment**
   - Document what the system can and cannot reliably assess
   - Do not use for novel risk categories without validation
   - Regular updating as AI capabilities and risks evolve

### Meta-Level Concerns

This assessment itself illustrates the challenge: using AI to assess AI creates reflexive risks:
- The assessed system could learn to game future versions of the assessor
- The assessor may have blind spots that become systemic
- Over-reliance on automated assessment could deskill human reviewers

These concerns do not preclude using AI to assist with safety assessment, but they require ongoing vigilance and human expertise as the ultimate backstop."

### Example 5: Quick Assessment for Low-Risk System

**Situation**: A company wants to deploy a customer service chatbot that answers FAQ questions about their software product.

**Application**: Apply AI safety risk assessment at quick depth.

**Output**:
"## AI Safety Assessment: Customer Service FAQ Chatbot

### Quick Assessment

**Overall Risk Level: LOW**

This is a straightforward, low-risk deployment:
- **Narrow scope**: Answers FAQ about specific software product
- **Scientist AI**: Advises users, does not take actions
- **Limited capability**: FAQ answering, not general assistant
- **Low stakes**: Incorrect answers inconvenient, not dangerous
- **Existing domain**: Customer service chatbots are well-understood

### Key Checks

| Check | Status |
|-------|--------|
| Can take real-world actions? | NO |
| Access to sensitive systems? | NO (read FAQ only) |
| Could cause significant harm? | LOW (incorrect info) |
| Novel capability level? | NO |
| Agentic features? | NO |

### Recommendations

Standard deployment practices sufficient:
- Clear labeling as AI assistant
- Escalation path to human support
- Monitor for frequently wrong answers
- Regular accuracy review
- Privacy compliance for any data collected

### Not Required for This Deployment
- Frontier AI registration
- Pre-deployment safety evaluation
- Human-in-the-loop for individual responses
- Capability restrictions
- Independent audit

This system does not warrant enhanced scrutiny. Standard software deployment practices apply."

## Integration

This skill derives from **Yoshua Bengio**'s leadership of the International AI Safety Report and his research on AI governance, particularly the distinction between Scientist AI and Agentic AI systems.

**Works well with:**
- causal-reasoning-assessment: Distribution shift is a key safety concern for deployed AI
- attention-mechanism-explainer: Understanding model architecture informs capability assessment
- curse-of-dimensionality-frame: Understanding why models generalize (and fail to) informs robustness assessment
- Governance and policy frameworks

**When to prefer this skill:**
Use this when the question involves evaluating AI safety, discussing AI governance and regulation, assessing new AI developments for risks, or communicating about AI safety to any stakeholder. This is the primary framework for systematic AI safety evaluation.

**Cautions:**
This framework cannot provide certainty about AI safety - it provides structured assessment. Acknowledge uncertainty, especially about future capabilities and novel risk types. Balance caution with recognition that AI can provide significant benefits. Safety assessment should enable responsible development, not prevent all development.
