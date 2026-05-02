"""Static knowledge resources exposed via MCP @resource decorators."""

CONVENTIONAL_COMMITS_GUIDE = """
# Conventional Commits v1.0 Quick Reference

Format: <type>(<scope>): <short description>

Types:
  feat     - A new feature
  fix      - A bug fix
  docs     - Documentation only changes
  style    - Formatting, missing semicolons (no logic change)
  refactor - Code change that is not a bug fix or feature
  perf     - Performance improvement
  test     - Adding or fixing tests
  chore    - Build process or tooling changes
  ci       - CI/CD configuration changes
  revert   - Reverting a previous commit

Rules:
  - Subject line max 72 characters
  - Use imperative mood: "add" not "added"
  - No period at end of subject
  - Blank line between subject and body
  - Breaking changes: add ! after type or BREAKING CHANGE: in footer

Examples:
  feat(auth): add OAuth2 login support
  fix(api): handle null response from payment gateway
  docs(readme): update installation steps
  feat!: remove deprecated /v1 endpoints
"""

DRAMA_FREE_REVIEW_GUIDE = """
# Drama-Free Code Review Principles

1. READ FIRST — understand the PR intent before reading code
2. DISCREPANCY CHECK — does the code match the description?
3. GROWTH MINDSET — assume the author had good reasons
4. ASK QUESTIONS — "What happens if...?" not "Change this."
5. CATEGORISE — [Blocker] / [Suggestion] / [Nit]
6. LANGUAGE IDIOMS — flag anti-patterns (e.g., Java-style Kotlin)
7. COMPLIMENT — explicitly acknowledge clever solutions

Blocker: Must be fixed before merge (correctness, security, data loss)
Suggestion: Should be addressed but won't block merge
Nit: Minor style preference — author's discretion
"""

RAG_QUALITY_GUIDE = """
# RAG Faithfulness Quality Standards

Faithfulness: Does the answer only contain claims supported by retrieved context?
Relevance: Does the answer address the original query?
Completeness: Does the answer cover all key points from the context?

Hallucination signals:
  - Specific numbers/dates not in context
  - Named entities not mentioned in context
  - Causal claims not supported by context
  - Confident assertions on absent information

Mitigation:
  - Re-rank retrieved chunks by semantic similarity
  - Ask LLM to cite specific context passages
  - Use NLI model (e.g., cross-encoder) for post-generation validation
  - Reduce temperature for factual queries
"""
