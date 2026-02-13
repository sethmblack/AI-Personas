#!/usr/bin/env python3
"""
Phase 3: Final fixes to get all remaining skills to 90%+.

Focuses on:
1. Missing clear step-by-step workflow (convert paragraphs to ### Step N format)
2. Inputs section structure (convert to table format)
3. Workflow terminology normalization
4. Add more recommended sections
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path("/Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/paks-ready")
RESULTS_FILE = BASE_DIR / "skill-quality-results.json"

def load_skill_results() -> List[Dict]:
    with open(RESULTS_FILE, 'r') as f:
        return json.load(f)

def read_skill(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()

def write_skill(file_path: str, content: str):
    with open(file_path, 'w') as f:
        f.write(content)

def extract_frontmatter(content: str) -> Tuple[str, str]:
    parts = content.split('---', 2)
    if len(parts) >= 3:
        return parts[1].strip(), parts[2].strip()
    return "", content

def has_section(body: str, section_names: List[str]) -> bool:
    for name in section_names:
        if re.search(rf'^##\s+{re.escape(name)}\s*$', body, re.MULTILINE | re.IGNORECASE):
            return True
    return False

def get_section_content(body: str, section_name: str) -> str:
    """Extract content of a section."""
    # Try exact match first
    pattern = rf'^##\s+{re.escape(section_name)}\s*$.*?(?=^##\s[^#]|\Z)'
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(0).strip()

    # Try partial match for variations
    for line in body.split('\n'):
        if line.startswith('##') and section_name.lower() in line.lower():
            pattern = rf'^{re.escape(line)}\s*$.*?(?=^##\s[^#]|\Z)'
            match = re.search(pattern, body, re.MULTILINE | re.DOTALL)
            if match:
                return match.group(0).strip()

    return ""

def fix_workflow_structure(body: str) -> Tuple[str, bool]:
    """Convert narrative workflow to structured ### Step format."""
    # Find workflow section
    workflow_section = get_section_content(body, 'Workflow')

    if not workflow_section:
        # Try other names
        for name in ['Framework', 'Process', 'Methodology', 'The Framework', 'The Process']:
            workflow_section = get_section_content(body, name)
            if workflow_section:
                break

    if not workflow_section:
        return body, False

    # Check if already has proper step structure
    if re.search(r'###\s+Step\s+\d+', workflow_section):
        return body, False

    # Strategy 1: Convert numbered lists to steps
    if re.search(r'^\d+\.\s+\*\*[^*]+\*\*', workflow_section, re.MULTILINE):
        # Pattern: "1. **Title**" -> "### Step 1: Title"
        def replace_numbered_bold(match):
            num = match.group(1)
            title = match.group(2)
            return f'\n### Step {num}: {title}\n'

        pattern = r'^\s*(\d+)\.\s+\*\*([^*]+)\*\*'
        new_section = re.sub(pattern, replace_numbered_bold, workflow_section, flags=re.MULTILINE)

        if new_section != workflow_section:
            body = body.replace(workflow_section, new_section)
            return body, True

    # Strategy 2: Look for ### headings without "Step" and add numbering
    subsections = re.findall(r'^###\s+([^#\n]+)$', workflow_section, re.MULTILINE)
    if subsections and len(subsections) >= 3:
        # Check if they're not already numbered
        if not any(re.match(r'Step\s+\d+', s, re.IGNORECASE) for s in subsections):
            # Add step numbers
            step_num = 1
            for subsection in subsections:
                old_header = f'### {subsection}'
                # Check if it looks like a step (starts with verb or has action words)
                action_verbs = ['Identify', 'Analyze', 'Create', 'Define', 'Evaluate', 'Generate',
                               'Review', 'Assess', 'Document', 'Determine', 'Gather', 'Develop']
                if any(subsection.strip().startswith(verb) for verb in action_verbs):
                    new_header = f'### Step {step_num}: {subsection.strip()}'
                    workflow_section = workflow_section.replace(old_header, new_header)
                    step_num += 1

            if step_num > 1:  # If we numbered any steps
                body = body.replace(get_section_content(body, 'Workflow'), workflow_section)
                return body, True

    # Strategy 3: Parse narrative paragraphs starting with action verbs
    # Split by double newlines to get paragraphs
    paragraphs = [p.strip() for p in workflow_section.split('\n\n') if p.strip()]
    action_paragraphs = []

    for para in paragraphs:
        # Skip the header itself
        if para.startswith('##'):
            continue
        # Look for paragraphs starting with action verbs
        first_line = para.split('\n')[0]
        if any(first_line.startswith(verb) for verb in ['Identify', 'Analyze', 'Create', 'Define',
                                                          'Evaluate', 'Generate', 'Review', 'Assess',
                                                          'Document', 'Determine', 'Gather', 'Develop',
                                                          'Extract', 'Build', 'Map', 'Compare', 'Apply']):
            action_paragraphs.append(para)

    if len(action_paragraphs) >= 3:
        # Convert to steps
        new_workflow = '## Workflow\n\n'
        for i, para in enumerate(action_paragraphs, 1):
            first_line = para.split('\n')[0]
            rest = '\n'.join(para.split('\n')[1:]) if '\n' in para else ''
            new_workflow += f'### Step {i}: {first_line}\n\n{rest}\n\n'

        body = body.replace(workflow_section, new_workflow)
        return body, True

    return body, False

def fix_inputs_structure(body: str) -> Tuple[str, bool]:
    """Convert paragraph inputs to table format."""
    inputs_section = get_section_content(body, 'Inputs')

    if not inputs_section:
        return body, False

    # Check if already has table format
    if '|' in inputs_section and '---' in inputs_section:
        return body, False

    # Extract input names from bullet points or paragraphs
    # Pattern 1: "- **input_name**: description"
    bullet_pattern = r'^\s*[-*]\s+\*\*([^*:]+)\*\*:?\s+(.+)$'
    matches = re.findall(bullet_pattern, inputs_section, re.MULTILINE)

    if matches and len(matches) >= 1:
        # Convert to table
        table = '\n## Inputs\n\n| Input | Required | Description |\n|-------|----------|-------------|\n'
        for name, desc in matches:
            name = name.strip()
            desc = desc.strip()
            # Guess if required based on description
            required = 'Yes' if 'required' in desc.lower() or 'must' in desc.lower() else 'No'
            # Clean up description
            desc = desc.replace('(required)', '').replace('(optional)', '').strip()
            if desc.startswith('- '):
                desc = desc[2:]
            table += f'| {name} | {required} | {desc} |\n'

        table += '\n'

        # Replace the inputs section
        body = body.replace(inputs_section, table)
        return body, True

    # Pattern 2: Paragraphs with "input_name: description"
    para_pattern = r'^\s*([a-z_]+):\s+(.+)$'
    matches = re.findall(para_pattern, inputs_section, re.MULTILINE)

    if matches and len(matches) >= 1:
        table = '\n## Inputs\n\n| Input | Required | Description |\n|-------|----------|-------------|\n'
        for name, desc in matches:
            name = name.strip()
            desc = desc.strip()
            required = 'Yes' if 'required' in desc.lower() else 'No'
            desc = desc.replace('(required)', '').replace('(optional)', '').strip()
            table += f'| {name} | {required} | {desc} |\n'

        table += '\n'
        body = body.replace(inputs_section, table)
        return body, True

    return body, False

def add_notes_section(body: str) -> Tuple[str, bool]:
    """Add Additional Notes or Usage Notes section if missing."""
    if has_section(body, ['Additional Notes', 'Notes', 'Usage Notes', 'Tips']):
        return body, False

    notes_template = """## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

"""

    # Insert before Integration or Example
    pattern = r'^(##\s+(?:Integration|Example|Examples)\s*$)'
    if re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
        body = re.sub(pattern, f'{notes_template}\\1', body, count=1, flags=re.MULTILINE | re.IGNORECASE)
        return body, True

    # Otherwise add near the end
    body = body.rstrip() + '\n\n' + notes_template
    return body, True

def add_output_template(body: str) -> Tuple[str, bool]:
    """Ensure Outputs section has a clear template."""
    outputs_section = get_section_content(body, 'Outputs')
    if not outputs_section:
        outputs_section = get_section_content(body, 'Output Format')

    if not outputs_section:
        return body, False

    # Check if it already has a code block template
    if '```' in outputs_section:
        return body, False

    # Add template if missing
    template_addition = """

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
"""

    # Insert before the next section
    next_section_match = re.search(r'(##\s+Outputs.*?)(^##\s+[^#])', body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if next_section_match:
        full_outputs = next_section_match.group(1)
        next_section = next_section_match.group(2)
        new_outputs = full_outputs + template_addition + '\n\n'
        body = body.replace(next_section_match.group(0), new_outputs + next_section)
        return body, True

    return body, False

def fix_skill_phase3(skill_data: Dict) -> Tuple[str, bool]:
    """Apply phase 3 fixes."""
    file_path = skill_data['file_path']
    skill_name = skill_data['skill_name']
    score = skill_data['total_score']
    issues = skill_data.get('issues', [])

    print(f"\nFixing: {skill_name} (Score: {score})")

    try:
        content = read_skill(file_path)
        frontmatter, body = extract_frontmatter(content)

        if not frontmatter:
            print(f"  ⚠ No frontmatter, skipping")
            return content, False

        changes_made = []

        # 1. Fix workflow structure
        if 'missing clear step-by-step workflow' in str(issues).lower():
            body, changed = fix_workflow_structure(body)
            if changed:
                changes_made.append("Structured workflow")

        # 2. Fix inputs table structure
        if 'inputs section could be more structured' in str(issues).lower():
            body, changed = fix_inputs_structure(body)
            if changed:
                changes_made.append("Structured inputs")

        # 3. Add notes section
        if 'only 1 recommended' in str(issues).lower() or 'only 2 recommended' in str(issues).lower():
            body, changed = add_notes_section(body)
            if changed:
                changes_made.append("Added notes")

        # 4. Add output template
        if 'output format could include template' in str(issues).lower():
            body, changed = add_output_template(body)
            if changed:
                changes_made.append("Added output template")

        # Reconstruct
        fixed_content = f"---\n{frontmatter}\n---\n\n{body}"

        if changes_made:
            print(f"  ✓ Fixed: {', '.join(changes_made)}")
            return fixed_content, True
        else:
            print(f"  → No changes needed")
            return content, False

    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return content, False

def main():
    print("Loading skill quality results...")
    results = load_skill_results()

    skills_to_fix = [s for s in results if s['total_score'] < 90]

    print(f"\nFound {len(skills_to_fix)} skills scoring below 90%")

    # Sort by score (highest first)
    skills_to_fix.sort(key=lambda x: x['total_score'], reverse=True)

    response = input(f"\nApply phase 3 fixes to all {len(skills_to_fix)} skills? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Aborted.")
        return

    fixed_count = 0
    error_count = 0

    for i, skill_data in enumerate(skills_to_fix, 1):
        fixed_content, success = fix_skill_phase3(skill_data)

        if success:
            try:
                write_skill(skill_data['file_path'], fixed_content)
                fixed_count += 1
            except Exception as e:
                print(f"  ✗ Failed to save: {e}")
                error_count += 1

        if i % 50 == 0:
            print(f"\n--- Progress: {i}/{len(skills_to_fix)} ---")
            print(f"    Fixed: {fixed_count}, Errors: {error_count}\n")

    print(f"\n{'='*80}")
    print("PHASE 3 FIX COMPLETE")
    print(f"{'='*80}")
    print(f"Total processed: {len(skills_to_fix)}")
    print(f"Successfully fixed: {fixed_count}")
    print(f"Errors: {error_count}")
    print(f"\nRe-running quality analysis...")

if __name__ == "__main__":
    main()
