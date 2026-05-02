from src.code_review import evaluate_pr_logic


def test_short_description_returns_error():
    result = evaluate_pr_logic("too short", "diff content here")
    assert "ERROR" in result


def test_valid_review_returns_protocol():
    result = evaluate_pr_logic(
        "This PR adds JWT refresh token support to the auth service.",
        "+ def refresh_token(user_id): ...",
    )
    assert "REVIEW PROTOCOL" in result
    assert "PR INTENT" in result


def test_review_includes_diff_in_output():
    diff = "+ return user.is_active"
    result = evaluate_pr_logic(
        "This PR fixes the user active status check in the profile endpoint.",
        diff,
    )
    assert diff in result
