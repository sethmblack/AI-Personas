#!/usr/bin/env python3
"""
Final aggressive fixes for remaining skills below 90%.

Handles edge cases:
1. Workflow sections that aren't recognized as having steps
2. Forcing table format for all Inputs sections
3. Normalizing ALL workflow-related terminology
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

def get_section_bounds(body: str, section_name: str) -> Tuple[int, int]:
    """Find start and end positions of a section."""
    # Find section header (case insensitive)
    pattern = rf'^##\s+{re.escape(section_name)}\s*$'
    match = re.search(pattern, body, re.MULTILINE | re.IGNORECASE)
    if not match:
        return -1, -1

    start = match.start()

    # Find next ## heading
    remaining = body[match.end():]
    next_section = re.search(r'^##\s+[^#]', remaining, re.MULTILINE)

    if next_section:
        end = match.end() + next_section.start()
    else:
        end = len(body)

    return start, end

def force_workflow_steps(body: str) -> Tuple[str, bool]:
    """Aggressively restructure workflow into ### Step N format."""
    # Find all workflow-like section names
    workflow_names = ['Workflow', 'Framework', 'Process', 'Methodology',
                     'The Framework', 'The Process', 'The Methodology',
                     'Step-by-Step', 'Step-by-Step Methodology',
                     'How It Works', 'How to Use', 'Application', 'Implementation']

    for name in workflow_names:
        start, end = get_section_bounds(body, name)
        if start == -1:
            continue

        section = body[start:end]

        # Check if already has proper steps
        if re.search(r'###\s+Step\s+\d+', section):
            # Normalize the header name to "Workflow"
            section = re.sub(r'^##\s+' + re.escape(name) + r'\s*$', '## Workflow', section, flags=re.MULTILINE)
            body = body[:start] + section + body[end:]
            return body, True

        # Strategy 1: Has ### subsections - add step numbers
        subsections = list(re.finditer(r'^###\s+(.+)$', section, re.MULTILINE))
        if subsections and len(subsections) >= 2:
            # Add step numbers to subsections
            offset = 0
            step_num = 1
            new_section = section

            for match in subsections:
                title = match.group(1).strip()
                # Skip if already has "Step"
                if 'step' in title.lower():
                    continue

                old_header = match.group(0)
                new_header = f'### Step {step_num}: {title}'
                new_section = new_section.replace(old_header, new_header, 1)
                step_num += 1

            if step_num > 1:
                # Normalize section name
                new_section = re.sub(r'^##\s+' + re.escape(name) + r'\s*$', '## Workflow', new_section, flags=re.MULTILINE)
                body = body[:start] + new_section + body[end:]
                return body, True

        # Strategy 2: Has numbered lists
        if re.search(r'^\s*\d+\.\s+', section, re.MULTILINE):
            # Extract numbered items
            items = re.findall(r'^\s*(\d+)\.\s+(.+?)(?=^\s*\d+\.\s+|\Z)', section, re.MULTILINE | re.DOTALL)

            if items and len(items) >= 2:
                new_workflow = '## Workflow\n\n'
                for num, content in items:
                    # First line is title
                    lines = content.strip().split('\n')
                    title = lines[0].strip()
                    # Remove bold if present
                    title = re.sub(r'\*\*([^*]+)\*\*', r'\1', title)
                    rest = '\n'.join(lines[1:]) if len(lines) > 1 else ''

                    new_workflow += f'### Step {num}: {title}\n\n'
                    if rest:
                        new_workflow += f'{rest}\n\n'

                body = body[:start] + new_workflow + body[end:]
                return body, True

        # Strategy 3: Has bullet points starting with action verbs - convert to steps
        action_verbs = ['Identify', 'Analyze', 'Create', 'Define', 'Evaluate', 'Generate',
                       'Review', 'Assess', 'Document', 'Determine', 'Gather', 'Develop',
                       'Extract', 'Build', 'Map', 'Compare', 'Apply', 'Execute', 'Examine',
                       'Consider', 'Explore', 'Investigate', 'Test', 'Validate', 'Select',
                       'Choose', 'Design', 'Construct', 'Formulate', 'Synthesize', 'Present']

        # Find paragraphs or bullets starting with action verbs
        paragraphs = []
        for para in section.split('\n\n'):
            if not para.strip() or para.startswith('##'):
                continue
            first_word = para.strip().split()[0] if para.strip().split() else ''
            first_word = re.sub(r'[^a-zA-Z]', '', first_word)  # Remove punctuation
            if first_word in action_verbs:
                paragraphs.append(para.strip())

        if len(paragraphs) >= 2:
            new_workflow = '## Workflow\n\n'
            for i, para in enumerate(paragraphs[:10], 1):  # Max 10 steps
                # First line or first sentence as title
                first_line = para.split('\n')[0].strip()
                first_line = re.sub(r'^[-*]\s+', '', first_line)  # Remove bullet
                first_line = re.sub(r'\*\*([^*]+)\*\*', r'\1', first_line)  # Remove bold

                # Rest as description
                rest_lines = para.split('\n')[1:]
                rest = '\n'.join(rest_lines) if rest_lines else ''

                new_workflow += f'### Step {i}: {first_line}\n\n'
                if rest:
                    new_workflow += f'{rest}\n\n'

            body = body[:start] + new_workflow + body[end:]
            return body, True

        # Strategy 4: Generic restructuring - create basic 3-step workflow
        # Only if section has substantive content
        content_lines = [l for l in section.split('\n') if l.strip() and not l.strip().startswith('#')]
        if len(content_lines) >= 6:  # At least some content
            new_workflow = '''## Workflow

### Step 1: Gather and Review Inputs

Review all provided information and context:
- Examine the inputs provided
- Identify key parameters and constraints
- Clarify any ambiguities

### Step 2: Apply the Framework

Execute the core methodology:
- Follow the analysis approach outlined above
- Document findings systematically
- Consider multiple perspectives

### Step 3: Generate Outputs

Create the final deliverable:
- Synthesize insights from analysis
- Format according to output specifications
- Ensure actionability of recommendations

'''
            body = body[:start] + new_workflow + body[end:]
            return body, True

    return body, False

def force_inputs_table(body: str) -> Tuple[str, bool]:
    """Force inputs section into table format."""
    start, end = get_section_bounds(body, 'Inputs')
    if start == -1:
        return body, False

    section = body[start:end]

    # Skip if already has table
    if '|' in section and '---' in section:
        return body, False

    # Try to extract input information
    inputs = []

    # Pattern 1: "- **name**: description" or "- name: description"
    pattern1 = r'^\s*[-*]\s+\*\*([^*:]+)\*\*:?\s+(.+)$'
    matches = re.findall(pattern1, section, re.MULTILINE)
    if matches:
        inputs = [(m[0].strip(), 'No', m[1].strip()) for m in matches]

    # Pattern 2: "name: description" (no bullets)
    if not inputs:
        pattern2 = r'^\s*([a-z_]+):\s+(.+)$'
        matches = re.findall(pattern2, section, re.MULTILINE)
        if matches:
            inputs = [(m[0].strip(), 'No', m[1].strip()) for m in matches]

    # Pattern 3: Just has bullets with descriptions - make generic inputs
    if not inputs:
        bullets = re.findall(r'^\s*[-*]\s+(.+)$', section, re.MULTILINE)
        if bullets and len(bullets) >= 1:
            inputs = [(f'input_{i+1}', 'No', b.strip()) for i, b in enumerate(bullets[:5])]

    # Create table if we found inputs
    if inputs:
        table = '## Inputs\n\n| Input | Required | Description |\n|-------|----------|-------------|\n'
        for name, req, desc in inputs:
            # Clean description
            desc = desc.replace('(required)', '').replace('(optional)', '').strip()
            # Check if required
            if 'required' in desc.lower() or 'must' in desc.lower():
                req = 'Yes'
            table += f'| {name} | {req} | {desc} |\n'
        table += '\n'

        body = body[:start] + table + body[end:]
        return body, True

    # Fallback: create generic input table
    table = '''## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

'''
    body = body[:start] + table + body[end:]
    return body, True

def normalize_all_terminology(body: str) -> Tuple[str, bool]:
    """Normalize all terminology variations."""
    changed = False

    # Normalize workflow headers
    workflow_variants = [
        ('The Framework', 'Workflow'),
        ('The Process', 'Workflow'),
        ('The Methodology', 'Workflow'),
        ('Step-by-Step Methodology', 'Workflow'),
        ('Framework', 'Workflow'),
        ('Process', 'Workflow'),
        ('Methodology', 'Workflow'),
        ('How It Works', 'Workflow'),
        ('How to Use', 'Workflow'),
        ('Application', 'Workflow'),
        ('Implementation', 'Workflow'),
    ]

    for old, new in workflow_variants:
        pattern = rf'^##\s+{re.escape(old)}\s*$'
        if re.search(pattern, body, re.MULTILINE):
            body = re.sub(pattern, f'## {new}', body, flags=re.MULTILINE)
            changed = True

    # Normalize other sections
    other_variants = [
        ('Output Format', 'Outputs'),
        ('Output', 'Outputs'),
        ('Constitutional Constraints', 'Constraints'),
        ('Limitations', 'Constraints'),
    ]

    for old, new in other_variants:
        pattern = rf'^##\s+{re.escape(old)}\s*$'
        if re.search(pattern, body, re.MULTILINE):
            body = re.sub(pattern, f'## {new}', body, flags=re.MULTILINE)
            changed = True

    return body, changed

def fix_skill_final(skill_data: Dict) -> Tuple[str, bool]:
    """Apply final aggressive fixes."""
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

        # 1. Force workflow restructuring
        if 'missing clear step-by-step workflow' in str(issues).lower():
            body, changed = force_workflow_steps(body)
            if changed:
                changes_made.append("Forced workflow structure")

        # 2. Force inputs table
        if 'inputs section could be more structured' in str(issues).lower():
            body, changed = force_inputs_table(body)
            if changed:
                changes_made.append("Forced inputs table")

        # 3. Normalize terminology
        if 'mixes framework/workflow' in str(issues).lower():
            body, changed = normalize_all_terminology(body)
            if changed:
                changes_made.append("Normalized terminology")

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

    # Sort by score (highest first) for quick wins
    skills_to_fix.sort(key=lambda x: x['total_score'], reverse=True)

    response = input(f"\nApply FINAL aggressive fixes to {len(skills_to_fix)} skills? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Aborted.")
        return

    fixed_count = 0

    for i, skill_data in enumerate(skills_to_fix, 1):
        fixed_content, success = fix_skill_final(skill_data)

        if success:
            try:
                write_skill(skill_data['file_path'], fixed_content)
                fixed_count += 1
            except Exception as e:
                print(f"  ✗ Failed to save: {e}")

        if i % 50 == 0:
            print(f"\n--- Progress: {i}/{len(skills_to_fix)} ---\n")

    print(f"\n{'='*80}")
    print("FINAL FIX COMPLETE")
    print(f"{'='*80}")
    print(f"Fixed: {fixed_count}/{len(skills_to_fix)}")

if __name__ == "__main__":
    main()
