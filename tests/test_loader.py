from src.loader import load_prompt, load_resource


def test_load_prompt_injects_variables():
    result = load_prompt(
        "code_review",
        pr_description="This PR adds login support.",
        code_diff="+ def login(): ...",
    )
    assert "This PR adds login support." in result
    assert "+ def login(): ..." in result


def test_load_prompt_no_dangling_placeholders():
    result = load_prompt(
        "rag_faithfulness",
        query="What is Python?",
        context="Python is a language.",
        answer="Python is a programming language.",
    )
    assert "{{" not in result
    assert "}}" not in result


def test_load_resource_returns_content():
    result = load_resource("conventional_commits")
    assert "feat" in result
    assert "fix" in result


def test_load_resource_drama_free():
    result = load_resource("drama_free_review")
    assert "Blocker" in result
