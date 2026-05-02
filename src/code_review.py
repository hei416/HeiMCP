def evaluate_pr_logic(pr_description: str, code_diff: str) -> str:
    """
    Apply Drama-Free Code Review rules.

    Checks if context is provided and prepares the model to give
    feedback as questions rather than commands.
    """
    if len(pr_description) < 20:
        return (
            "ERROR: PR Description is too short. "
            "Rule: Read the description first to understand intent."
        )

    return (
        f"REVIEW PROTOCOL:\n"
        f"1. DISCREPANCY CHECK: Compare the PR description against the actual code diff. "
        f"If the code does something not mentioned in the description, "
        f"or contradicts it, flag it as a primary concern.\n"
        f"2. Approach with a Growth Mindset.\n"
        f"3. Format feedback as questions "
        f"(e.g., 'What happens if...?' instead of 'Change this.').\n"
        f"4. Look for language anti-patterns (e.g., Kotlin written like Java).\n"
        f"5. Compliment clever solutions.\n"
        f"\nPR INTENT (Verify this against code):\n{pr_description}"
        f"\n\nCODE TO REVIEW:\n{code_diff}"
    )
