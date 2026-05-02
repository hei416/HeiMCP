"""Prompt functions — content lives in prompts/*.md, loaded at call time."""

from src.loader import load_prompt


def code_review_prompt(pr_description: str, code_diff: str) -> str:
    """Load and render the code review prompt template."""
    return load_prompt("code_review", pr_description=pr_description, code_diff=code_diff)


def unit_test_review_prompt(test_code: str) -> str:
    """Load and render the unit test review prompt template."""
    return load_prompt("unit_test_review", test_code=test_code)


def rag_faithfulness_prompt(query: str, context: str, answer: str) -> str:
    """Load and render the RAG faithfulness audit prompt template."""
    return load_prompt("rag_faithfulness", query=query, context=context, answer=answer)
