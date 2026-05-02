from src.commit_linter import lint_commit_message


def test_valid_conventional_commit():
    result = lint_commit_message("feat(auth): add JWT refresh token support")
    assert "🎉" in result


def test_invalid_type_flagged():
    result = lint_commit_message("update: change something")
    assert "Unknown type" in result


def test_past_tense_flagged():
    result = lint_commit_message("fix(api): fixed the null pointer exception")
    assert "past tense" in result.lower()


def test_missing_format_flagged():
    result = lint_commit_message("added login feature")
    assert "Conventional Commits" in result


def test_empty_message_returns_error():
    result = lint_commit_message("")
    assert "ERROR" in result
