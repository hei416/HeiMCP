# HeiMCP — Agent Behaviour Guide

This file is auto-loaded by Cursor and read by Claude Code agents.
It defines reasoning patterns and workflow rules for AI agents working in this repo.

---

## Understanding This Codebase

Before making any change, understand the three-layer architecture:

```
[MCP Layer]    skills_server.py         — registers tools/prompts/resources
[Logic Layer]  src/<module>.py          — pure Python logic, no MCP deps
[Content Layer] prompts/*.md            — prompt templates with {{placeholders}}
               resources/*.md           — static reference guides
```

Changes to logic → edit `src/`. Changes to prompt wording → edit `prompts/*.md`.
Changes to reference content → edit `resources/*.md`. The two should rarely mix.

---

## Reasoning Patterns

### Before Adding a Feature

1. **Check if it belongs in `src/`** — is this pure deterministic logic? If yes, `src/`.
2. **Check if it belongs in `prompts/`** — is this instructional text for an LLM? If yes, `prompts/*.md`.
3. **Check if it is already covered** — run `grep -r "<keyword>" src/` before creating a duplicate.
4. **Plan the test first** — write the test function signature before writing the implementation.

### When Editing Prompt Templates

- Read the existing `.md` file fully before editing
- Confirm every `{{placeholder}}` matches the Python caller in `src/prompts.py`
- After editing, mentally trace: `load_prompt("name", key=val)` → are all `{{key}}` replaced?
- Check: does the prompt have an explicit **Output Format** section? If not, add one.

### When Fixing a Bug

1. Write a failing test that reproduces the bug first
2. Fix the minimal code needed to make the test pass
3. Confirm no existing tests regressed: `uv run pytest tests/ -v`

---

## Self-Check Before Committing

- [ ] All new functions have type annotations and docstrings
- [ ] All new tools follow the `try/except → ERROR: string` pattern
- [ ] All new `.md` templates have no dangling `{{placeholders}}`
- [ ] `uv run pytest tests/ -v` passes with no failures
- [ ] Commit message follows Conventional Commits: `feat(scope): description`
- [ ] No secrets or credentials added to any file
- [ ] `README.md` tables updated if a new tool/prompt/resource was added
