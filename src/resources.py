"""Resource functions — content lives in resources/*.md, loaded at call time."""

from src.loader import load_resource


def get_conventional_commits_guide() -> str:
    """Load the Conventional Commits v1.0 reference guide."""
    return load_resource("conventional_commits")


def get_drama_free_review_guide() -> str:
    """Load the Drama-Free Code Review principles guide."""
    return load_resource("drama_free_review")


def get_rag_quality_guide() -> str:
    """Load the RAG faithfulness and quality standards guide."""
    return load_resource("rag_quality")
