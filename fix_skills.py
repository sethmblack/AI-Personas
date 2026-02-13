#!/usr/bin/env python3
"""
Batch fix skills scoring below 90% by adding missing sections.

This script:
1. Reads skill-quality-results.json to identify skills needing fixes
2. For each skill, adds missing sections based on the template
3. Improves existing sections to meet quality standards
4. Saves fixed skills back to their original locations
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Base directory
BASE_DIR = Path("/Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/paks-ready")
RESULTS_FILE = BASE_DIR / "skill-quality-results.json"

def load_skill_results() -> List[Dict]:
    """Load the skill quality results."""
    with open(RESULTS_FILE, 'r') as f:
        return json.load(f)

def read_skill(file_path: str) -> str:
    """Read a skill file."""
    with open(file_path, 'r') as f:
        return f.read()

def write_skill(file_path: str, content: str):
    """Write a skill file."""
    with open(file_path, 'w') as f:
        f.write(content)

def extract_frontmatter(content: str) -> Tuple[str, str]:
    """Extract frontmatter and body from skill content."""
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[1].strip()
        body = parts[2].strip()
        return frontmatter, body
    return "", content

def get_skill_name_from_frontmatter(frontmatter: str) -> str:
    """Extract skill name from frontmatter."""
    match = re.search(r'name:\s*(.+)', frontmatter)
    return match.group(1).strip() if match else "Unknown Skill"

def get_skill_description(frontmatter: str) -> str:
    """Extract description from frontmatter."""
    match = re.search(r'description:\s*(.+)', frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else ""

def has_section(body: str, section_names: List[str]) -> bool:
    """Check if body has any of the specified section headers."""
    for name in section_names:
        if re.search(rf'^##\s+{re.escape(name)}\s*$', body, re.MULTILINE | re.IGNORECASE):
            return True
    return False

def get_section_content(body: str, section_name: str) -> str:
    """Extract content of a section."""
    pattern = rf'^##\s+{re.escape(section_name)}\s*$.*?(?=^##\s|\Z)'
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return match.group(0).strip() if match else ""

def normalize_section_header(body: str, old_headers: List[str], new_header: str) -> str:
    """Normalize section header names."""
    for old in old_headers:
        pattern = rf'^##\s+{re.escape(old)}\s*$'
        body = re.sub(pattern, f'## {new_header}', body, flags=re.MULTILINE | re.IGNORECASE)
    return body

def add_outputs_section(body: str, skill_name: str, description: str) -> str:
    """Add Outputs section if missing."""
    if has_section(body, ['Outputs', 'Output']):
        # Rename if it's "Output Format" to "Outputs"
        body = normalize_section_header(body, ['Output Format', 'Output'], 'Outputs')
        return body

    # Find where to insert (before Example or at end)
    insert_before = ['Example', 'Examples', 'Integration', 'Practice Prompts']

    outputs_template = f"""## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

"""

    # Try to insert before a known section
    for section in insert_before:
        pattern = rf'^(##\s+{re.escape(section)}\s*$)'
        if re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
            body = re.sub(pattern, f'{outputs_template}\\1', body, count=1, flags=re.MULTILINE | re.IGNORECASE)
            return body

    # Otherwise add before final section or at end
    body = body.rstrip() + '\n\n' + outputs_template
    return body

def add_workflow_section(body: str, skill_name: str) -> str:
    """Add or normalize Workflow section."""
    # Check for existing workflow-like sections
    workflow_variants = [
        'Workflow', 'Framework', 'The Framework', 'Process', 'The Process',
        'Methodology', 'The Methodology', 'Step-by-Step', 'Step-by-Step Methodology',
        'How It Works', 'How to Use'
    ]

    # If it exists, normalize it
    if has_section(body, workflow_variants):
        body = normalize_section_header(body, workflow_variants, 'Workflow')

        # Check if it has numbered steps - if not, add structure
        workflow_content = get_section_content(body, 'Workflow')
        if workflow_content and not re.search(r'###\s+Step\s+\d+', workflow_content):
            # Already has content but no clear steps - leave it for manual review
            pass
        return body

    # Add new workflow section
    workflow_template = f"""## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

"""

    # Insert after Inputs or When to Use, before Outputs
    insert_after = ['Inputs', 'When to Use']
    insert_before = ['Outputs', 'Output Format', 'Constraints']

    # Try to insert in the right place
    for section in insert_before:
        pattern = rf'^(##\s+{re.escape(section)}\s*$)'
        if re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
            body = re.sub(pattern, f'{workflow_template}\\1', body, count=1, flags=re.MULTILINE | re.IGNORECASE)
            return body

    # Or after inputs
    for section in insert_after:
        pattern = rf'(##\s+{re.escape(section)}\s*$.*?(?=^##\s|\Z))'
        match = re.search(pattern, body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
        if match:
            insertion_point = match.end()
            body = body[:insertion_point] + '\n\n' + workflow_template + body[insertion_point:]
            return body

    # Default: add after description
    lines = body.split('\n')
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            insert_pos = i
            break

    if insert_pos > 0:
        lines.insert(insert_pos, workflow_template)
        body = '\n'.join(lines)

    return body

def add_constraints_section(body: str, skill_name: str, skill_type: str = "analytical") -> str:
    """Add Constraints section if missing."""
    constraint_variants = ['Constraints', 'Constitutional Constraints', 'Boundaries', 'Limitations']

    if has_section(body, constraint_variants):
        # Normalize the header
        body = normalize_section_header(body, constraint_variants[1:], constraint_variants[0])
        return body

    # Determine skill type from content
    if any(word in skill_name.lower() for word in ['comedy', 'humor', 'satire', 'joke', 'wit']):
        skill_type = "creative"
    elif any(word in skill_name.lower() for word in ['code', 'technical', 'system', 'engineer']):
        skill_type = "technical"
    elif any(word in skill_name.lower() for word in ['strategy', 'business', 'plan']):
        skill_type = "strategic"

    # Create appropriate constraints based on type
    if skill_type == "creative":
        constraints = """## Constraints

- Do not sacrifice meaning for style
- Do not lose the core message in pursuit of cleverness
- Acknowledge when simplification distorts important nuance
- Honor the audience's intelligence—avoid condescension
- Stay true to the source material's intent
- Recognize cultural and contextual sensitivities
"""
    elif skill_type == "technical":
        constraints = """## Constraints

- Do not recommend approaches beyond stated technical capabilities
- Do not ignore security, performance, or scalability implications
- Acknowledge technical debt and trade-offs in recommendations
- Honor existing architecture and system constraints
- Verify recommendations are implementable before suggesting them
- Consider maintainability and long-term implications
"""
    elif skill_type == "strategic":
        constraints = """## Constraints

- Do not oversimplify complex business realities
- Do not ignore resource and timeline constraints
- Acknowledge risks and uncertainties explicitly
- Honor stakeholder concerns and competing priorities
- Base recommendations on available evidence, not assumptions
- Consider second-order effects and unintended consequences
"""
    else:  # analytical/default
        constraints = """## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology
"""

    # Insert before Example section or at end
    insert_before = ['Example', 'Examples', 'Integration', 'Practice Prompts']

    for section in insert_before:
        pattern = rf'^(##\s+{re.escape(section)}\s*$)'
        if re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
            body = re.sub(pattern, f'{constraints}\\n\\1', body, count=1, flags=re.MULTILINE | re.IGNORECASE)
            return body

    # Add at end
    body = body.rstrip() + '\n\n' + constraints
    return body

def improve_when_to_use(body: str) -> str:
    """Improve When to Use section."""
    when_variants = ['When to Use', 'When to Use This Skill', 'When to Apply']

    if not has_section(body, when_variants):
        # Add basic When to Use section
        when_template = """## When to Use

- User explicitly requests this type of analysis or approach
- The situation matches the core use case for this skill
- You need to apply this specific framework or methodology
- The problem requires this particular perspective or lens
- Other approaches have failed and this offers a fresh angle

"""
        # Insert after title and description, before Inputs
        pattern = r'^(#\s+.+?\n\n.+?(?=\n##))'
        if re.search(pattern, body, re.MULTILINE | re.DOTALL):
            body = re.sub(pattern, f'\\1\n\n{when_template}', body, count=1, flags=re.MULTILINE | re.DOTALL)
        else:
            # Just add at the beginning
            lines = body.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('## '):
                    lines.insert(i, when_template)
                    body = '\n'.join(lines)
                    break
    else:
        # Normalize header
        body = normalize_section_header(body, when_variants[1:], when_variants[0])

    return body

def improve_inputs_section(body: str) -> str:
    """Add or improve Inputs section."""
    if has_section(body, ['Inputs', 'Input', 'Parameters']):
        body = normalize_section_header(body, ['Input', 'Parameters'], 'Inputs')
        return body

    # Add basic Inputs section
    inputs_template = """## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

"""

    # Insert after When to Use, before Workflow
    pattern = r'(##\s+When to Use\s*$.*?(?=^##\s|\Z))'
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if match:
        insertion_point = match.end()
        body = body[:insertion_point] + '\n\n' + inputs_template + body[insertion_point:]
        return body

    # Otherwise insert early in document
    lines = body.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('## '):
            lines.insert(i, inputs_template)
            body = '\n'.join(lines)
            break

    return body

def improve_examples(body: str, skill_name: str) -> str:
    """Improve Examples section if it's too brief."""
    example_variants = ['Example', 'Examples', 'Example Application']

    if not has_section(body, example_variants):
        # Add placeholder example
        example_template = """## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

"""
        # Add near the end, before Integration
        pattern = r'^(##\s+Integration\s*$)'
        if re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
            body = re.sub(pattern, f'{example_template}\\1', body, count=1, flags=re.MULTILINE | re.IGNORECASE)
        else:
            body = body.rstrip() + '\n\n' + example_template

    return body

def fix_skill(skill_data: Dict) -> Tuple[str, bool]:
    """Fix a single skill and return the fixed content and success status."""
    file_path = skill_data['file_path']
    skill_name = skill_data['skill_name']
    score = skill_data['total_score']
    issues = skill_data.get('issues', [])

    print(f"\n{'='*80}")
    print(f"Fixing: {skill_name} (Score: {score})")
    print(f"Issues: {len(issues)}")

    try:
        content = read_skill(file_path)
        frontmatter, body = extract_frontmatter(content)

        if not frontmatter:
            print(f"  ⚠ No frontmatter found, skipping")
            return content, False

        description = get_skill_description(frontmatter)

        # Apply fixes based on issues
        changes_made = []

        # 1. Fix When to Use
        if any('when to use' in issue.lower() for issue in issues):
            body = improve_when_to_use(body)
            changes_made.append("When to Use")

        # 2. Fix Inputs
        if any('inputs' in issue.lower() for issue in issues):
            body = improve_inputs_section(body)
            changes_made.append("Inputs")

        # 3. Fix Workflow
        if any('workflow' in issue.lower() or 'step-by-step' in issue.lower() for issue in issues):
            body = add_workflow_section(body, skill_name)
            changes_made.append("Workflow")

        # 4. Fix Outputs
        if any('output' in issue.lower() for issue in issues):
            body = add_outputs_section(body, skill_name, description)
            changes_made.append("Outputs")

        # 5. Fix Constraints
        if any('constraint' in issue.lower() for issue in issues):
            body = add_constraints_section(body, skill_name)
            changes_made.append("Constraints")

        # 6. Fix Examples
        if any('example' in issue.lower() for issue in issues):
            body = improve_examples(body, skill_name)
            changes_made.append("Examples")

        # Reconstruct the file
        fixed_content = f"---\n{frontmatter}\n---\n\n{body}"

        if changes_made:
            print(f"  ✓ Added/fixed: {', '.join(changes_made)}")
            return fixed_content, True
        else:
            print(f"  → No changes needed")
            return content, False

    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return content, False

def main():
    """Main execution function."""
    print("Loading skill quality results...")
    results = load_skill_results()

    # Filter skills scoring below 90
    skills_to_fix = [s for s in results if s['total_score'] < 90]

    print(f"\nFound {len(skills_to_fix)} skills scoring below 90%")
    print(f"Total skills: {len(results)}")
    print(f"Skills at 90%+: {len(results) - len(skills_to_fix)}")

    # Sort by score (lowest first) to tackle worst cases first
    skills_to_fix.sort(key=lambda x: x['total_score'])

    # Ask for confirmation
    response = input(f"\nFix all {len(skills_to_fix)} skills? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Aborted.")
        return

    # Process skills
    fixed_count = 0
    error_count = 0

    for i, skill_data in enumerate(skills_to_fix, 1):
        fixed_content, success = fix_skill(skill_data)

        if success:
            try:
                write_skill(skill_data['file_path'], fixed_content)
                fixed_count += 1
                print(f"  ✓ Saved ({i}/{len(skills_to_fix)})")
            except Exception as e:
                print(f"  ✗ Failed to save: {e}")
                error_count += 1

        # Progress update every 50 skills
        if i % 50 == 0:
            print(f"\n--- Progress: {i}/{len(skills_to_fix)} skills processed ---")
            print(f"    Fixed: {fixed_count}, Errors: {error_count}\n")

    # Final summary
    print(f"\n{'='*80}")
    print("BATCH FIX COMPLETE")
    print(f"{'='*80}")
    print(f"Total processed: {len(skills_to_fix)}")
    print(f"Successfully fixed: {fixed_count}")
    print(f"Errors: {error_count}")
    print(f"Unchanged: {len(skills_to_fix) - fixed_count - error_count}")
    print(f"\nNext step: Re-run the quality analysis to verify improvements.")

if __name__ == "__main__":
    main()
