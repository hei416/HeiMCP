import re

def evaluate_test_quality(test_code: str) -> str:
    """
    Evaluates unit tests based on the 'Right Way' principles.
    """
    feedback = []
    
    # Rule: Single Assertion per Test
    assertions = len(re.findall(r"assert", test_code))
    if assertions > 1:
        feedback.append("- Violation: Multiple assertions found. Goal: One assertion per test for specific CI failures.")

    # Rule: Simple Setup / Extraction
    if len(test_code.splitlines()) > 25 and "def" not in test_code: 
        feedback.append("- Suggestion: Setup looks complex. Extract factories or 'Given' steps into helper functions.")

    # Rule: Behavior vs Implementation
    if "verify(" in test_code or ".called" in test_code:
        feedback.append("- Caution: You are verifying function calls (implementation). Ensure you are testing the behavioral output instead.")

    if not feedback:
        return "✅ Test suite follows Staff Engineer standards: Isolated, Behavioral, and Specific."
    
    return "UNIT TEST FEEDBACK:\n" + "\n".join(feedback)