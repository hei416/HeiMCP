import re

CONVENTIONAL_TYPES = {
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "perf",
    "test",
    "chore",
    "ci",
    "build",
    "revert",
}

CONVENTIONAL_PATTERN = re.compile(
    r"^(?P<type>[a-z]+)(\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s(?P<desc>.+)$"
)


def _check_subject(subject: str, feedback: list, passed: list) -> tuple[str | None, str | None]:
    """
    Validate the subject line format and return (commit_type, desc).

    Appends messages to feedback or passed lists in place.
    Returns (None, None) if the subject does not match the pattern.
    """
    match = CONVENTIONAL_PATTERN.match(subject)
    if not match:
        feedback.append(
            f"\u274c Subject line does not follow Conventional Commits format.\n"
            f"   Expected: <type>(<scope>): <description>\n"
            f"   Example:  feat(auth): add JWT refresh token support\n"
            f"   Got:      '{subject}'"
        )
        return None, None

    commit_type = match.group("type")
    scope = match.group("scope")
    desc = match.group("desc")
    breaking = match.group("breaking")

    if commit_type not in CONVENTIONAL_TYPES:
        feedback.append(
            f"\u274c Unknown type '{commit_type}'. "
            f"Valid types: {', '.join(sorted(CONVENTIONAL_TYPES))}"
        )
    else:
        passed.append(f"\u2705 Type '{commit_type}' is valid.")

    if scope:
        passed.append(f"\u2705 Scope '{scope}' provided.")

    if breaking:
        passed.append(
            "\u26a0\ufe0f  Breaking change marker (!) detected \u2014 "
            "remember to add BREAKING CHANGE footer."
        )

    if len(subject) > 72:
        feedback.append(f"\u274c Subject line too long ({len(subject)} chars). Keep under 72.")
    else:
        passed.append(f"\u2705 Subject length OK ({len(subject)} chars).")

    if desc.endswith("."):
        feedback.append("\u274c Subject line should not end with a period.")

    past_tense = re.findall(
        r"\b(added|fixed|updated|changed|removed|refactored|implemented)\b",
        desc.lower(),
    )
    if past_tense:
        feedback.append(
            f"\u26a0\ufe0f  Possible past tense detected: {past_tense}. "
            f"Use imperative mood (e.g., 'add' not 'added')."
        )

    return commit_type, desc


def lint_commit_message(commit_message: str) -> str:
    """
    Lint a git commit message against the Conventional Commits v1.0 spec.

    Checks: type validity, subject line length, imperative mood, body format.
    """
    if not commit_message or not commit_message.strip():
        return "ERROR: Commit message cannot be empty."

    lines = commit_message.strip().splitlines()
    subject = lines[0].strip()
    feedback: list[str] = []
    passed: list[str] = []

    _check_subject(subject, feedback, passed)

    if len(lines) > 1:
        if lines[1].strip() != "":
            feedback.append("\u274c Missing blank line between subject and body.")
        else:
            passed.append("\u2705 Blank line separator present.")

    result_lines = ["COMMIT LINT RESULT:"]
    result_lines.extend(passed)
    if feedback:
        result_lines.extend(feedback)
        result_lines.append("\n\U0001f4d6 Reference: https://www.conventionalcommits.org")
    else:
        result_lines.append(
            "\n\U0001f389 Commit message is fully compliant "
            "with Conventional Commits v1.0."
        )

    return "\n".join(result_lines)
