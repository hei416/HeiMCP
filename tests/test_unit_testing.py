from src.unit_testing import evaluate_test_quality


def test_multiple_assertions_flagged():
    code = "def test_user():\n    assert user.name == 'Alice'\n    assert user.age == 30"
    result = evaluate_test_quality(code)
    assert "Multiple assertions" in result


def test_implementation_check_flagged():
    code = "def test_service():\n    service.process()\n    assert mock.called"
    result = evaluate_test_quality(code)
    assert "implementation" in result.lower()


def test_clean_test_passes():
    code = "def test_add_returns_sum():\n    result = add(2, 3)\n    assert result == 5"
    result = evaluate_test_quality(code)
    assert "✅" in result
