from fastmcp import FastMCP
from pydantic import BaseModel, Field

from src.code_review import evaluate_pr_logic
from src.commit_linter import lint_commit_message
from src.nn_architecture import check_architecture
from src.prompts import (
    code_review_prompt,
    rag_faithfulness_prompt,
    unit_test_review_prompt,
)
from src.rag_faithfulness import evaluate_faithfulness
from src.resources import (
    get_conventional_commits_guide,
    get_drama_free_review_guide,
    get_rag_quality_guide,
)
from src.unit_testing import evaluate_test_quality

# ── Server ─────────────────────────────────────────────────────────────
mcp = FastMCP(
    "HeiMCP",
    instructions=(
        "A Staff Engineer toolkit. Use skill_* tools for heuristic analysis, "
        "prompt_* prompts for LLM-guided deep reviews, and resource_* resources "
        "for reference guides."
    ),
)


# ── Pydantic Input Schemas ───────────────────────────────────────────────
class PRReviewInput(BaseModel):
    pr_description: str = Field(
        ...,
        min_length=20,
        description="PR intent, must be at least 20 chars",
    )
    code_diff: str = Field(..., min_length=1, description="The raw code diff")


class RAGInput(BaseModel):
    query: str = Field(..., min_length=5)
    retrieved_context: str = Field(..., min_length=10)
    generated_answer: str = Field(..., min_length=10)


# ── Tools ───────────────────────────────────────────────────────────────────
@mcp.tool()
async def skill_code_review_logic(input: PRReviewInput) -> str:
    """
    Drama-Free Code Review: checks PR description vs. actual diff,
    formats feedback as questions, flags language anti-patterns.
    """
    try:
        return evaluate_pr_logic(input.pr_description, input.code_diff)
    except Exception as e:
        return f"ERROR: Code review failed — {type(e).__name__}: {e}"


@mcp.tool()
async def skill_evaluate_unit_tests(test_code: str) -> str:
    """
    Evaluates unit tests: single assertion, behavioural vs implementation,
    and setup complexity checks.
    """
    if not test_code or not test_code.strip():
        return "ERROR: test_code cannot be empty."
    try:
        return evaluate_test_quality(test_code)
    except Exception as e:
        return f"ERROR: Unit test evaluation failed — {type(e).__name__}: {e}"


@mcp.tool()
async def skill_nn_architecture_check(layers_info: str) -> str:
    """
    Validates tensor shape flow through PyTorch Conv2d / ConvTranspose2d layers.
    Input: JSON string with 'input_shape' [C,H,W] and 'layers' list.
    """
    if not layers_info or not layers_info.strip():
        return "ERROR: layers_info cannot be empty. Provide a JSON string."
    try:
        return check_architecture(layers_info)
    except Exception as e:
        return f"ERROR: Architecture check failed — {type(e).__name__}: {e}"


@mcp.tool()
async def skill_rag_faithfulness_check(input: RAGInput) -> str:
    """
    Heuristic faithfulness checker for RAG pipelines.
    Detects hallucination risk by checking if answer claims are grounded
    in the retrieved context.
    """
    try:
        return evaluate_faithfulness(input.query, input.retrieved_context, input.generated_answer)
    except Exception as e:
        return f"ERROR: Faithfulness check failed — {type(e).__name__}: {e}"


@mcp.tool()
async def skill_lint_commit_message(commit_message: str) -> str:
    """
    Lints a git commit message against Conventional Commits v1.0 spec.
    """
    if not commit_message or not commit_message.strip():
        return "ERROR: commit_message cannot be empty."
    try:
        return lint_commit_message(commit_message)
    except Exception as e:
        return f"ERROR: Commit lint failed — {type(e).__name__}: {e}"


# ── Prompts (content from prompts/*.md) ─────────────────────────────────────
@mcp.prompt()
def prompt_code_review(pr_description: str, code_diff: str) -> str:
    """Deep LLM-guided code review using Drama-Free principles."""
    return code_review_prompt(pr_description, code_diff)


@mcp.prompt()
def prompt_unit_test_review(test_code: str) -> str:
    """Deep LLM-guided unit test quality review."""
    return unit_test_review_prompt(test_code)


@mcp.prompt()
def prompt_rag_faithfulness(query: str, context: str, answer: str) -> str:
    """Deep LLM-guided RAG faithfulness audit with claim-level grounding labels."""
    return rag_faithfulness_prompt(query, context, answer)


# ── Resources (content from resources/*.md) ────────────────────────────────
@mcp.resource("resource://guides/conventional-commits")
def resource_conventional_commits() -> str:
    """Conventional Commits v1.0 quick reference guide."""
    return get_conventional_commits_guide()


@mcp.resource("resource://guides/drama-free-review")
def resource_drama_free_review() -> str:
    """Drama-Free Code Review principles reference."""
    return get_drama_free_review_guide()


@mcp.resource("resource://guides/rag-quality")
def resource_rag_quality() -> str:
    """RAG faithfulness and quality standards guide."""
    return get_rag_quality_guide()


# ── Entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run()
