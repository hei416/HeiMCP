# HeiMCP — AI Coding Rules

This file governs how AI coding agents (Claude Code, Cursor, Copilot, etc.)
behave when contributing to this repository.

---

## Project Overview

HeiMCP is a FastMCP toolkit that encodes opinionated engineering quality rules
as LLM-callable **Tools**, **Prompts**, and **Resources**. It is designed to
run locally via stdio transport with Claude Desktop or any MCP-compatible client.

**Stack:** Python 3.11+, FastMCP, Pydantic v2, pytest, uv

---

## Architecture Rules

### The Three-Layer Separation

```
skills_server.py        ← MCP wiring ONLY (tools, prompts, resources)
src/<module>.py         ← Pure logic ONLY (no FastMCP imports)
prompts/<name>.md       ← Prompt content ONLY (no Python)
resources/<name>.md     ← Reference content ONLY (no Python)
tests/test_<module>.py  ← pytest unit tests for each src/ module
```

- **NEVER import FastMCP into `src/` modules.** Logic must be testable without starting an MCP server.
- **NEVER put prompt strings in Python files.** All prompt content lives in `prompts/*.md` with `{{placeholder}}` syntax.
- **NEVER put resource content in Python files.** All guides/references live in `resources/*.md`.
- **NEVER expose a tool that raises an unhandled exception.** Every `@mcp.tool()` must catch exceptions and return a descriptive `ERROR: ...` string.

---

## Code Quality Rules

### Python Style

- Use **type annotations** on all function signatures: `def foo(x: str) -> str:`
- Use **Pydantic BaseModel** for all multi-field tool inputs — never `**kwargs`
- Use **f-strings** for interpolation — not `.format()` or `%`
- Maximum function length: **30 lines** — extract helpers if longer
- Maximum file length: **150 lines** — split into modules if larger
- Every function must have a **docstring** (one line minimum)
- Use `pathlib.Path` for all file operations — never `os.path`

### Naming Conventions

| Element | Convention | Example |
|---|---|---|
| MCP tool functions | `skill_<verb>_<noun>` | `skill_lint_commit_message` |
| MCP prompt functions | `prompt_<noun>` | `prompt_code_review` |
| MCP resource URIs | `resource://guides/<name>` | `resource://guides/rag-quality` |
| src/ functions | `<verb>_<noun>` (snake_case) | `evaluate_faithfulness` |
| Pydantic models | PascalCase + `Input` suffix | `PRReviewInput` |
| Markdown placeholders | `{{snake_case}}` | `{{pr_description}}` |

### Input Validation Rules

- **Always guard against empty strings:** check `if not x or not x.strip()` before processing
- **Use Pydantic `Field(min_length=N)`** for minimum length constraints
- **Validate JSON inputs with `json.loads()` inside a try/except**
- **Return `ERROR: <explanation>` strings** — never raise exceptions to the LLM
- **Sanitise user input before template injection:** strip `{{` and `}}` from values passed to `load_prompt()`

### Error Handling Pattern (mandatory for all tools)

```python
@mcp.tool()
async def skill_example(input: SomeInput) -> str:
    """One-line description — this IS the LLM's tool description."""
    try:
        return some_logic(input.field)
    except Exception as e:
        return f"ERROR: Example failed — {type(e).__name__}: {e}"
```

---

## Adding a New Tool — Checklist

1. [ ] Create `src/<name>.py` with pure logic function(s)
2. [ ] Create `prompts/<name>.md` if the tool has an LLM-guided prompt variant
3. [ ] Create `resources/<name>.md` if the tool has a reference guide
4. [ ] Add `@mcp.tool()`, `@mcp.prompt()`, `@mcp.resource()` wrappers in `skills_server.py`
5. [ ] Add Pydantic `Input` model if the tool takes >1 parameter
6. [ ] Add `tests/test_<name>.py` with at least 3 test cases
7. [ ] Test locally: `uv run pytest tests/ -v`
8. [ ] Verify CI passes before opening a PR
9. [ ] Update `README.md` tables (Tools, Prompts, Resources)

---

## Testing Rules

- **Every `src/` module must have a corresponding `tests/test_<module>.py`**
- **Each test file must have at minimum:**
  - One test for the happy path (valid input → expected output)
  - One test for invalid/empty input (should return `ERROR: ...`)
  - One test for an edge case specific to the tool's domain
- **Tests must NOT import from `skills_server.py`** — only from `src/`
- **Use `assert "ERROR" in result`** to check error paths — never assert exact error messages (they may change)
- **No mocking of `src/` functions in unit tests** — they are pure functions and should be tested directly

---

## Markdown Template Rules

- Placeholders use `{{double_braces}}` syntax
- Placeholder names must exactly match the Python keyword argument names in `load_prompt()`
- Every placeholder in a `.md` file **must** be injected — dangling `{{variables}}` in output is a bug
- Use GitHub Flavored Markdown (GFM) — headings, tables, code fences
- Prompt files (`prompts/`) should include an explicit **Output Format** section
- Resource files (`resources/`) should use tables for structured reference data

---

## NEVER Do These

- **NEVER commit secrets** — no API keys, tokens, or credentials in any file
- **NEVER modify `uv.lock` manually** — run `uv add <package>` instead
- **NEVER use `print()` in `src/` modules** — use return values only
- **NEVER use mutable global state in tools** — tools must be stateless
- **NEVER add a `@mcp.tool()` that is incomplete** — remove or raise `NotImplementedError` with a clear message instead of returning a stub string
- **NEVER interpolate raw user input directly into prompts** without sanitising `{{` and `}}`
- **NEVER use `os.path`** — use `pathlib.Path`
- **NEVER hardcode file paths as strings** — use `Path(__file__).parent / "..."`
