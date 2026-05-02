"""Reusable MCP Prompt templates for HeiMCP."""


def code_review_prompt(pr_description: str, code_diff: str) -> str:
    return (
        f"You are a Staff Engineer conducting a Drama-Free code review.\n\n"
        f"PR INTENT:\n{pr_description}\n\n"
        f"CODE DIFF:\n{code_diff}\n\n"
        f"Review rules:\n"
        f"1. Compare PR intent to what the code actually does. Flag discrepancies first.\n"
        f"2. Ask questions instead of issuing commands (e.g., 'What happens if X is null?').\n"
        f"3. Highlight idiomatic improvements (language-specific anti-patterns).\n"
        f"4. Compliment clever solutions explicitly.\n"
        f"5. Categorise each comment: [Blocker] / [Suggestion] / [Nit]"
    )


def unit_test_review_prompt(test_code: str) -> str:
    return (
        f"You are a Staff Engineer reviewing unit tests for quality.\n\n"
        f"TEST CODE:\n{test_code}\n\n"
        f"Evaluate against these principles:\n"
        f"1. Single assertion per test — one failure = one root cause.\n"
        f"2. Behavioural, not implementation — test outputs, not internal calls.\n"
        f"3. Simple setup — complex fixtures should be extracted into helpers.\n"
        f"4. Descriptive test names — the name should explain the scenario."
    )


def rag_faithfulness_prompt(query: str, context: str, answer: str) -> str:
    return (
        f"You are a RAG quality auditor checking for hallucinations.\n\n"
        f"USER QUERY:\n{query}\n\n"
        f"RETRIEVED CONTEXT:\n{context}\n\n"
        f"GENERATED ANSWER:\n{answer}\n\n"
        f"Task: For each factual claim in the answer, identify whether it is:\n"
        f"  [GROUNDED] — directly supported by the context\n"
        f"  [INFERRED] — reasonably inferable from context\n"
        f"  [HALLUCINATED] — not supported or contradicts context\n"
        f"Output a structured list of claims with their grounding label."
    )
