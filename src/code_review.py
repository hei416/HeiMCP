def evaluate_pr_logic(pr_description: str, code_diff: str) -> str:
    """
    Applies 'Drama-Free' Code Review rules. 
    Checks if context is provided and prepares the model to give feedback as questions.
    """
    if len(pr_description) < 20:
        return "ERROR: PR Description is too short. Rule: Read the description first to understand intent."
    
    return f"""
    REVIEW PROTOCOL:
    1. DISCREPANCY CHECK: Compare the PR description against the actual code diff. If the code does something not mentioned in the description, or contradicts it, flag it as a primary concern.
    2. Approach with a Growth Mindset.
    3. Format feedback as questions (e.g., 'What happens if...?' instead of 'Change this.').
    4. Look for language anti-patterns (e.g., Kotlin written like Java).
    5. Compliment clever solutions.
    
    PR INTENT (Verify this against code):
    {pr_description}

    CODE TO REVIEW:
    {code_diff}
    """