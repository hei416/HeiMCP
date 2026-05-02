"""Resource functions — content lives in resources/*.md, loaded at call time."""

from src.loader import load_resource


def get_conventional_commits_guide() -> str:
    return load_resource("conventional_commits")


def get_drama_free_review_guide() -> str:
    return load_resource("drama_free_review")


def get_rag_quality_guide() -> str:
    return load_resource("rag_quality")
