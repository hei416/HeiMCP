"""Loads .md prompt and resource files, injecting variables via {{placeholders}}."""

from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"
RESOURCES_DIR = Path(__file__).parent.parent / "resources"


def _load_md(path: Path) -> str:
    """Read a markdown file, raise a clear error if missing."""
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def load_prompt(name: str, **kwargs: str) -> str:
    """
    Load a prompt template from prompts/<name>.md and inject variables.

    Usage:
        load_prompt("code_review", pr_description="...", code_diff="...")

    Placeholders in the .md file use {{variable_name}} syntax.
    """
    template = _load_md(PROMPTS_DIR / f"{name}.md")
    for key, value in kwargs.items():
        template = template.replace(f"{{{{{key}}}}}", value)
    return template


def load_resource(name: str) -> str:
    """
    Load a static resource guide from resources/<name>.md.

    Usage:
        load_resource("conventional_commits")
    """
    return _load_md(RESOURCES_DIR / f"{name}.md")
