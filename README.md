# HeiMCP — Staff Engineer Skills as MCP Tools

A FastMCP toolkit that encodes opinionated engineering quality rules as LLM-callable tools, prompts, and resources.

## What Makes It Different

Unlike generic MCP integrations (GitHub, Slack, Notion), HeiMCP provides an **opinionated engineering quality layer** — each tool embeds a specific, named framework rather than wrapping a raw API.

## Tools

| Tool | Description |
|---|---|
| `skill_code_review_logic` | Drama-Free code review: checks PR intent vs. diff |
| `skill_evaluate_unit_tests` | Behavioural unit test quality checker |
| `skill_nn_architecture_check` | PyTorch Conv/DeConv tensor shape validator |
| `skill_rag_faithfulness_check` | Heuristic hallucination detector for RAG pipelines |
| `skill_lint_commit_message` | Conventional Commits v1.0 linter |

## Prompts

| Prompt | Description |
|---|---|
| `prompt_code_review` | Deep LLM-guided Drama-Free code review |
| `prompt_unit_test_review` | Deep LLM-guided unit test quality review |
| `prompt_rag_faithfulness` | Claim-level RAG faithfulness audit |

## Resources

- `resource://guides/conventional-commits` — Conventional Commits quick reference
- `resource://guides/drama-free-review` — Code review principles
- `resource://guides/rag-quality` — RAG faithfulness standards

## Architecture

```
skills_server.py       # FastMCP entrypoint (tools + prompts + resources)
src/
  code_review.py       # Drama-Free review heuristics
  unit_testing.py      # Test quality rules
  nn_architecture.py   # PyTorch shape tracer
  rag_faithfulness.py  # RAG hallucination detector
  commit_linter.py     # Conventional Commits linter
  prompts.py           # Reusable LLM prompt templates
  resources.py         # Static reference guides
tests/                 # pytest coverage for all src modules
.github/workflows/     # CI pipeline (uv + pytest)
```

## Setup

```bash
uv sync
uv run python skills_server.py
```

## Run Tests

```bash
uv run pytest tests/ -v
```

## MCP Config (Claude Desktop)

```json
{
  "mcpServers": {
    "heimcp": {
      "command": "uv",
      "args": ["run", "python", "skills_server.py"]
    }
  }
}
```
