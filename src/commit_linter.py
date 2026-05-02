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


def lint_commit_message(commit_message: str) -> str:
    """
    Lint a git commit message against the Conventional Commits v1.0 spec.

    Checks: type validity, subject line length, imperative mood, body format.
    """
    if not commit_message or not commit_message.strip():
        return "ERROR: Commit message cannot be empty."

    lines = commit_message.strip().splitlines()
    subject = lines[0].strip()
    feedback = []
    passed = []

    match = CONVENTIONAL_PATTERN.match(subject)
    if not match:
        feedback.append(
            f"❌ Subject line does not follow Conventional Commits format.\n"
            f"   Expected: <type>(<scope>): <description>\n"
            f"   Example:  feat(auth): add JWT refresh token support\n"
            f"   Got:      '{subject}'"
        )
    else:
        commit_type = match.group("type")
        scope = match.group("scope")
        desc = match.group("desc")
        breaking = match.group("breaking")

        if commit_type not in CONVENTIONAL_TYPES:
            feedback.append(
                f"❌ Unknown type '{commit_type}'. "
                f"Valid types: {', '.join(sorted(CONVENTIONAL_TYPES))}"
            )
        else:
            passed.append(f"✅ Type '{commit_type}' is valid.")

        if scope:
            passed.append(f"✅ Scope '{scope}' provided.")

        if breaking:
            passed.append(
                "⚠️  Breaking change marker (!) detected — "
                "remember to add BREAKING CHANGE footer."
            )

        if len(subject) > 72:
            feedback.append(f"❌ Subject line too long ({len(subject)} chars). Keep under 72.")
        else:
            passed.append(f"✅ Subject length OK ({len(subject)} chars).")

        if desc.endswith("."):
            feedback.append("❌ Subject line should not end with a period.")

        past_tense = re.findall(
            r"\b(added|fixed|updated|changed|removed|refactored|implemented)\b",
            desc.lower(),
        )
        if past_tense:
            feedback.append(
                f"⚠️  Possible past tense detected: {past_tense}. "
                f"Use imperative mood (e.g., 'add' not 'added')."
            )

    if len(lines) > 1:
        if lines[1].strip() != "":
            feedback.append("❌ Missing blank line between subject and body.")
        else:
            passed.append("✅ Blank line separator present.")

    result_lines = ["COMMIT LINT RESULT:"]
    result_lines.extend(passed)
    if feedback:
        result_lines.extend(feedback)
        result_lines.append("\n📖 Reference: https://www.conventionalcommits.org")
    else:
        result_lines.append("\n🎉 Commit message is fully compliant with Conventional Commits v1.0.")

    return "\n".join(result_lines)
