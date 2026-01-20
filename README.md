# AI Personas

A collection of 100 expert AI personas and 500+ reusable skills for use with large language models.

## Overview

This library provides:

- **100 Expert Personas** - Each expert embodies the voice, methodology, and thinking patterns of a notable figure
- **500+ Skills** - Reusable, composable methodologies that can be invoked independently or assigned to experts

## Structure

```
├── experts/
│   ├── {expert-name}/
│   │   ├── PROMPT.md           # Voice definition and persona prompt
│   │   ├── expertise.md        # Reference material and accumulated knowledge
│   │   ├── references.md       # Fact-verified sources
│   │   └── skill-extraction-report.md  # Analysis of extracted skills
│   └── ...
├── skills/
│   ├── {skill-name}/
│   │   └── PROMPT.md           # Skill definition with workflow
│   └── ...
└── README.md
```

## Experts

| Category | Examples |
|----------|----------|
| Business & Leadership | Steve Jobs, Jeff Bezos, Warren Buffett, Peter Drucker |
| Science & Technology | Albert Einstein, Richard Feynman, Marie Curie, Ada Lovelace |
| Philosophy | Aristotle, Marcus Aurelius, Friedrich Nietzsche, Simone de Beauvoir |
| Arts & Literature | Ernest Hemingway, Virginia Woolf, Pablo Picasso, Miles Davis |
| Historical Figures | Abraham Lincoln, Winston Churchill, Eleanor Roosevelt |
| Sports & Performance | Michael Jordan, Serena Williams, Phil Jackson |

## Skills

Skills are standalone methodologies extracted from expert thinking patterns. Each skill includes:

- **Trigger conditions** - When to invoke the skill
- **Inputs** - What information is needed
- **Workflow** - Step-by-step process
- **Outputs** - What the skill produces

### Example Skills

| Skill | Source Expert | Purpose |
|-------|---------------|---------|
| `first-principles-reasoning` | Elon Musk | Break problems down to fundamental truths |
| `dichotomy-of-control` | Marcus Aurelius | Separate what you can and cannot control |
| `ooda-loop-analysis` | John Boyd | Observe-Orient-Decide-Act decision cycle |
| `feynman-technique` | Richard Feynman | Learn by teaching simply |
| `iceberg-method` | Ernest Hemingway | Write with subtext and implication |

## Usage

### Using an Expert

```markdown
# In your system prompt:
You are the {expert-name} expert.
[Include contents of experts/{expert-name}/PROMPT.md]
```

### Using a Skill

```markdown
# Invoke skill:
/invoke skills/{skill-name}/PROMPT.md
```

### Combining Experts and Skills

Experts can invoke skills that align with their methodology. Each expert's PROMPT.md includes a skills section listing relevant skills they can use.

## File Formats

### PROMPT.md (Expert)

```markdown
# {Expert Name} Expert

## Core Voice Definition
[How the expert communicates]

## Signature Techniques
[Key methodologies]

## What You Do NOT Do
[Anti-patterns to avoid]

## Available Skills
[Skills this expert can invoke]
```

### PROMPT.md (Skill)

```markdown
# {Skill Name}

[Description]

## When to Use
[Trigger conditions]

## Inputs
[Required information]

## Workflow
[Step-by-step process]

## Outputs
[What the skill produces]
```

## Contributing

To add a new expert or skill, follow the established file structure and include fact verification in references.md.

## License

MIT
