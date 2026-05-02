import re


def _extract_key_claims(answer: str) -> list[str]:
    """Split answer into sentence-level claims."""
    sentences = re.split(r"(?<=[.!?])\s+", answer.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 10]


def evaluate_faithfulness(query: str, retrieved_context: str, generated_answer: str) -> str:
    """
    Lightweight faithfulness checker for RAG pipelines.

    Detects hallucination risk by checking if answer claims are grounded
    in the retrieved context. Use as a heuristic pre-filter before
    expensive NLI model calls.
    """
    if not query or not retrieved_context or not generated_answer:
        return "ERROR: All three inputs (query, retrieved_context, generated_answer) are required."

    claims = _extract_key_claims(generated_answer)
    context_lower = retrieved_context.lower()
    feedback = []
    ungrounded = []

    for claim in claims:
        words = [w.lower() for w in re.findall(r"\b\w+\b", claim) if len(w) > 4]
        if not words:
            continue
        matched = sum(1 for w in words if w in context_lower)
        grounding_ratio = matched / len(words) if words else 1.0

        if grounding_ratio < 0.4:
            ungrounded.append(
                f"  ❌ Possibly hallucinated: '{claim[:80]}...' "
                f"(only {int(grounding_ratio * 100)}% terms in context)"
            )
        elif grounding_ratio < 0.7:
            feedback.append(
                f"  ⚠️  Weakly grounded: '{claim[:80]}...' "
                f"({int(grounding_ratio * 100)}% terms in context)"
            )

    query_keywords = [w.lower() for w in re.findall(r"\b\w+\b", query) if len(w) > 3]
    answer_lower = generated_answer.lower()
    addressed = sum(1 for kw in query_keywords if kw in answer_lower)
    if query_keywords and addressed / len(query_keywords) < 0.5:
        feedback.append("  ⚠️  Answer may not fully address the original query.")

    lines = [f"FAITHFULNESS REPORT — {len(claims)} claims checked:"]
    if ungrounded:
        lines.append(f"\nHALLUCINATION RISK ({len(ungrounded)} claim(s)):")
        lines.extend(ungrounded)
    if feedback:
        lines.append(f"\nWEAK GROUNDING ({len(feedback)} issue(s)):")
        lines.extend(feedback)
    if not ungrounded and not feedback:
        lines.append("✅ All claims appear grounded in the retrieved context.")
    else:
        lines.append(
            "\nRECOMMENDATION: Re-retrieve with broader query or "
            "ask the LLM to cite specific context passages."
        )

    return "\n".join(lines)
