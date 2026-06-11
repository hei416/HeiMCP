from src.rag_faithfulness import evaluate_faithfulness


def test_grounded_answer_passes():
    context = "Python is a high-level programming language. It was created by Guido van Rossum."
    answer = "Python is a high-level language created by Guido van Rossum."
    result = evaluate_faithfulness("Who created Python?", context, answer)
    assert "FAITHFULNESS REPORT" in result


def test_hallucinated_answer_flagged():
    context = "The Eiffel Tower is located in Paris."
    answer = "The Eiffel Tower was built in 1850 by Napoleon Bonaparte in Lyon."
    result = evaluate_faithfulness("Where is the Eiffel Tower?", context, answer)
    assert any(keyword in result for keyword in ("HALLUCINATION", "❌", "WEAK GROUNDING", "⚠️"))


def test_empty_inputs_return_error():
    result = evaluate_faithfulness("", "some context", "some answer")
    assert "ERROR" in result
