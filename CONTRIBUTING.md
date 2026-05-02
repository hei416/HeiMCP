# Contributing to HeiMCP

Thank you for contributing! HeiMCP is a FastMCP toolkit of opinionated
engineering quality tools. Every contribution should add a **named,
specific engineering principle** — not a generic capability.

---

## Quick Start

```bash
git clone https://github.com/hei416/HeiMCP.git
cd HeiMCP
uv sync
uv run pytest tests/ -v   # all tests should pass
```

---

## What Makes a Good Contribution

**Good** — Adds a tool that encodes a specific, named framework:
- "Checks if SQL queries follow the Repository Pattern"
- "Validates that API endpoints follow REST Level 2 (Richardson Maturity Model)"
- "Checks Python for SOLID principle violations"

**Not a good fit** — Generic wrappers around existing services:
- "Calls the GitHub API to list PRs" (use `@modelcontextprotocol/server-github`)
- "Reads files from disk" (use `@modelcontextprotocol/server-filesystem`)

---

## Adding a New Tool

Follow the checklist in `CLAUDE.md` → *Adding a New Tool*. The short version:

1. **Logic** → `src/<name>.py` (pure function, no FastMCP)
2. **Prompt template** → `prompts/<name>.md` (if applicable)
3. **Reference guide** → `resources/<name>.md` (if applicable)
4. **MCP wiring** → add `@mcp.tool()` / `@mcp.prompt()` / `@mcp.resource()` to `skills_server.py`
5. **Tests** → `tests/test_<name>.py` (happy path + error path + edge case)
6. **Docs** → update `README.md` tables

---

## Commit Messages

All commits must follow [Conventional Commits v1.0](https://www.conventionalcommits.org):

```
feat(auth): add JWT validation tool
fix(unit-testing): correct assertion counter per-function
docs(readme): update tool table
```

You can validate your own commit message with:
```bash
uv run python -c "from src.commit_linter import lint_commit_message; print(lint_commit_message('your message here'))"
```

---

## Pull Request Checklist

- [ ] `uv run pytest tests/ -v` passes locally
- [ ] New tool/prompt/resource documented in `README.md`
- [ ] Commit messages follow Conventional Commits
- [ ] No hardcoded secrets or API keys
- [ ] PR description explains *which engineering principle* the tool encodes
