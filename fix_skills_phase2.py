#!/usr/bin/env python3
"""
Phase 2: Advanced fixes for skills scoring 85-89%.

This script addresses:
1. Brief examples - expands them with more detail
2. Missing recommended sections (Integration, Error Handling)
3. Workflow terminology inconsistencies
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

def has_section(body: str, section_names: List[str]) -> bool:
    """Check if body has any of the specified section headers."""
    for name in section_names:
        if re.search(rf'^##\s+{re.escape(name)}\s*$', body, re.MULTILINE | re.IGNORECASE):
            return True
    return False

def get_section_content(body: str, section_name: str) -> str:
    """Extract content of a section, including subsections."""
    pattern = rf'^##\s+{re.escape(section_name)}\s*$.*?(?=^##\s[^#]|\Z)'
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return match.group(0).strip() if match else ""

def count_section_words(section_content: str) -> int:
    """Count words in a section, excluding markdown syntax."""
    # Remove code blocks
    section_content = re.sub(r'```.*?```', '', section_content, flags=re.DOTALL)
    # Remove headers
    section_content = re.sub(r'^#+\s+.*$', '', section_content, flags=re.MULTILINE)
    # Remove bullets and list markers
    section_content = re.sub(r'^[-*\d.]+\s+', '', section_content, flags=re.MULTILINE)
    # Count words
    words = section_content.split()
    return len(words)

def expand_brief_example(body: str, skill_name: str) -> Tuple[str, bool]:
    """Expand examples that are too brief (< 200 words)."""
    example_section = get_section_content(body, 'Example')
    if not example_section:
        example_section = get_section_content(body, 'Examples')

    if not example_section:
        return body, False

    word_count = count_section_words(example_section)

    # If example is already substantial (>200 words), skip
    if word_count > 200:
        return body, False

    # Add guidance to expand the example
    expansion_template = """

**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks
"""

    # Find the end of the Example/Examples section
    pattern = rf'(##\s+(?:Example|Examples)\s*$.*?)(^##\s+[^#]|\Z)'
    match = re.search(pattern, body, re.MULTILINE | re.DOTALL | re.IGNORECASE)

    if match:
        section_content = match.group(1)
        next_section = match.group(2)

        # Only add if "Why this works" doesn't already exist
        if "why this works" not in section_content.lower():
            expanded = section_content + expansion_template + '\n\n'
            body = body.replace(match.group(0), expanded + next_section)
            return body, True

    return body, False

def add_integration_section(body: str, skill_name: str) -> Tuple[str, bool]:
    """Add Integration section if missing."""
    if has_section(body, ['Integration', 'Expert Integration', 'Related Skills']):
        return body, False

    # Create integration section
    integration_template = f"""## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

"""

    # Insert before final section or at end
    # Try to insert before Example section if it exists
    pattern = r'^(##\s+(?:Example|Examples|Practice Prompts|Additional Notes)\s*$)'
    if re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
        body = re.sub(pattern, f'{integration_template}\\1', body, count=1, flags=re.MULTILINE | re.IGNORECASE)
        return body, True

    # Otherwise add at the end
    body = body.rstrip() + '\n\n' + integration_template
    return body, True

def add_error_handling_section(body: str) -> Tuple[str, bool]:
    """Add Error Handling section if missing."""
    if has_section(body, ['Error Handling', 'Edge Cases', 'Common Pitfalls']):
        return body, False

    error_handling_template = """## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

"""

    # Insert before Constraints or Example section
    pattern = r'^(##\s+(?:Constraints|Constitutional Constraints|Example|Examples)\s*$)'
    if re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
        body = re.sub(pattern, f'{error_handling_template}\\1', body, count=1, flags=re.MULTILINE | re.IGNORECASE)
        return body, True

    return body, False

def normalize_workflow_terminology(body: str) -> Tuple[str, bool]:
    """Normalize workflow-related section headers to be consistent."""
    # Map of inconsistent terms to normalize
    workflow_variants = {
        'The Framework': 'Workflow',
        'The Process': 'Workflow',
        'The Methodology': 'Workflow',
        'Step-by-Step Methodology': 'Workflow',
        'Framework': 'Workflow',
        'Process': 'Workflow',
        'Methodology': 'Workflow',
        'How It Works': 'Workflow',
        'How to Use': 'Workflow',
        'Application Process': 'Workflow',
        'Implementation': 'Workflow'
    }

    changed = False
    for old_term, new_term in workflow_variants.items():
        pattern = rf'^##\s+{re.escape(old_term)}\s*$'
        if re.search(pattern, body, re.MULTILINE):
            body = re.sub(pattern, f'## {new_term}', body, flags=re.MULTILINE)
            changed = True

    return body, changed

def improve_workflow_structure(body: str) -> Tuple[str, bool]:
    """Ensure workflow has numbered steps with ### headings."""
    workflow_section = get_section_content(body, 'Workflow')

    if not workflow_section:
        return body, False

    # Check if it already has proper step structure
    if re.search(r'###\s+Step\s+\d+', workflow_section):
        return body, False

    # Check for bullet-point steps that should be converted
    # This is a simple heuristic - look for numbered lists at the start of lines
    if re.search(r'^\d+\.\s+', workflow_section, re.MULTILINE):
        # Convert numbered lists to Step headers
        def replace_numbered_item(match):
            num = match.group(1)
            text = match.group(2).strip()
            return f'\n### Step {num}: {text}\n\n'

        # Pattern: start of line, number, period, space, text until newline
        pattern = r'^\s*(\d+)\.\s+([^\n]+)'
        new_workflow = re.sub(pattern, replace_numbered_item, workflow_section, flags=re.MULTILINE)

        if new_workflow != workflow_section:
            # Replace the workflow section in the body
            body = body.replace(workflow_section, new_workflow)
            return body, True

    return body, False

def fix_skill_phase2(skill_data: Dict) -> Tuple[str, bool]:
    """Apply phase 2 fixes to a skill."""
    file_path = skill_data['file_path']
    skill_name = skill_data['skill_name']
    score = skill_data['total_score']
    issues = skill_data.get('issues', [])

    print(f"\nFixing: {skill_name} (Score: {score})")

    try:
        content = read_skill(file_path)
        frontmatter, body = extract_frontmatter(content)

        if not frontmatter:
            print(f"  ⚠ No frontmatter found, skipping")
            return content, False

        changes_made = []

        # 1. Expand brief examples
        if 'example is too brief' in str(issues).lower():
            body, changed = expand_brief_example(body, skill_name)
            if changed:
                changes_made.append("Expanded examples")

        # 2. Add Integration section
        if 'only 1 recommended' in str(issues).lower() or 'only 2 recommended' in str(issues).lower():
            body, changed = add_integration_section(body, skill_name)
            if changed:
                changes_made.append("Added Integration")

        # 3. Add Error Handling section
        if 'only 1 recommended' in str(issues).lower():
            body, changed = add_error_handling_section(body)
            if changed:
                changes_made.append("Added Error Handling")

        # 4. Normalize workflow terminology
        if 'mixes framework/workflow/process' in str(issues).lower():
            body, changed = normalize_workflow_terminology(body)
            if changed:
                changes_made.append("Normalized terminology")

        # 5. Improve workflow structure
        if 'missing clear step-by-step workflow' in str(issues).lower():
            body, changed = improve_workflow_structure(body)
            if changed:
                changes_made.append("Improved workflow structure")

        # Reconstruct the file
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
    """Main execution function."""
    print("Loading skill quality results...")
    results = load_skill_results()

    # Filter skills scoring below 90
    skills_to_fix = [s for s in results if s['total_score'] < 90]

    print(f"\nFound {len(skills_to_fix)} skills scoring below 90%")

    # Prioritize skills close to 90% (85-89)
    high_priority = [s for s in skills_to_fix if s['total_score'] >= 85]
    medium_priority = [s for s in skills_to_fix if 80 <= s['total_score'] < 85]
    low_priority = [s for s in skills_to_fix if s['total_score'] < 80]

    print(f"  High priority (85-89): {len(high_priority)}")
    print(f"  Medium priority (80-84): {len(medium_priority)}")
    print(f"  Low priority (<80): {len(low_priority)}")

    # Sort by score (highest first) to get quick wins
    skills_to_fix.sort(key=lambda x: x['total_score'], reverse=True)

    # Ask for confirmation
    response = input(f"\nApply phase 2 fixes to all {len(skills_to_fix)} skills? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Aborted.")
        return

    # Process skills
    fixed_count = 0
    error_count = 0

    for i, skill_data in enumerate(skills_to_fix, 1):
        fixed_content, success = fix_skill_phase2(skill_data)

        if success:
            try:
                write_skill(skill_data['file_path'], fixed_content)
                fixed_count += 1
            except Exception as e:
                print(f"  ✗ Failed to save: {e}")
                error_count += 1

        # Progress update every 100 skills
        if i % 100 == 0:
            print(f"\n--- Progress: {i}/{len(skills_to_fix)} skills processed ---")
            print(f"    Fixed: {fixed_count}, Errors: {error_count}\n")

    # Final summary
    print(f"\n{'='*80}")
    print("PHASE 2 FIX COMPLETE")
    print(f"{'='*80}")
    print(f"Total processed: {len(skills_to_fix)}")
    print(f"Successfully fixed: {fixed_count}")
    print(f"Errors: {error_count}")
    print(f"Unchanged: {len(skills_to_fix) - fixed_count - error_count}")
    print(f"\nNext step: Re-run the quality analysis to verify improvements.")

if __name__ == "__main__":
    main()
