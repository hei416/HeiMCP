# HeiMCP Usage Guide

This guide covers all three ways to use HeiMCP with GitHub Copilot in VS Code.

---

## Setup (One Time)

```bash
git clone https://github.com/hei416/HeiMCP.git
cd HeiMCP
uv sync
code .
```

VS Code will detect `.vscode/mcp.json` and show a prompt:
> *"Allow MCP server 'heimcp' to run?"*

Click **Allow**. This is a one-time step — VS Code remembers it.

Then open Copilot Chat (`Ctrl+Shift+I`) and switch to **Agent mode** using
the mode dropdown in the chat input bar.

---

## Method 1 — Slash Commands (Easiest)

Type `/` in Copilot Chat agent mode to see all available skills.

### `/full-pr-review` — End-to-end PR review

Runs Drama-Free code review + commit lint + unit test quality in one shot:

```
/full-pr-review

pr_description: Add JWT refresh token support to the auth module

code_diff:
diff --git a/src/auth.py b/src/auth.py
+def refresh_token(token: str) -> str:
+    payload = jwt.decode(token, SECRET)
+    return jwt.encode({...}, SECRET)

commit_message: feat(auth): add JWT refresh token

test_code:
def test_refresh_token():
    token = create_token(user_id=1)
    new_token = refresh_token(token)
    assert new_token is not None
    assert new_token != token
```

`commit_message` and `test_code` are optional — omit them if not available.

**Output:** Unified report with 🔍 Code Quality, 📝 Commit Message,
✅ Test Quality, and 📊 Overall Verdict.

---

### `/rag-audit` — Hallucination check for RAG outputs

```
/rag-audit

query: What is the capital of France?

retrieved_context: France is a country in Western Europe. Paris is its
capital and largest city, with a population of over 2 million.

generated_answer: The capital of France is Paris, which has a population
of over 2 million people.
```

**Output:** Claim-level grounding report with hallucination risk flags
and a recommendation on whether to show, revise, or regenerate the answer.

---

### `/commit-lint` — Validate a commit message

```
/commit-lint

commit_message: feat(api): add rate limiting middleware
```

**Output:** Pass/fail with specific rule violations, explanations,
and a corrected version of the message.

---

## Method 2 — Conversational Tool Calls

Mention what you want in plain language — Copilot picks the right tool:

> "Check if this commit message follows Conventional Commits: `fix: resolved the bug`"

> "Is this RAG answer faithful to the context? [paste context and answer]"

> "Review this PR using Drama-Free principles: [paste description and diff]"

For the PyTorch shape validator (no slash command), use:

> "Check my neural network architecture with `skill_nn_architecture_check`:"
> ```json
> {
>   "input_shape": [3, 64, 64],
>   "layers": [
>     {"name": "conv1", "type": "Conv2d", "out_channels": 32,
>      "kernel_size": 3, "stride": 1, "padding": 1}
>   ]
> }
> ```

---

## Method 3 — Tools Panel (🔧 Icon)

1. In Copilot Chat agent mode, click the **🔧 tools icon** in the input bar
2. Expand **heimcp** to see all 5 tools
3. Click a tool name to view its input schema
4. Fill in the inputs and run

Best for first-time exploration of what each tool expects.

---

## All Tools & Slash Commands

| Tool | Slash Command | Description |
|---|---|---|
| `skill_code_review_logic` | `/full-pr-review` (step 1) | Drama-Free PR review |
| `skill_evaluate_unit_tests` | `/full-pr-review` (step 3) | Test quality checker |
| `skill_lint_commit_message` | `/commit-lint` | Conventional Commits linter |
| `skill_rag_faithfulness_check` | `/rag-audit` | RAG hallucination detector |
| `skill_nn_architecture_check` | Conversational only | PyTorch shape validator |

---

## Using with Claude Desktop or Cursor

Slash commands are VS Code-only. On Claude Desktop or Cursor, use
conversational tool calls (Method 2) — the agent will call the right
tool automatically based on what you describe.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `/full-pr-review` doesn't appear | Ensure you're in **Agent mode**, not Ask or Edit |
| `heimcp` not in 🔧 tools list | `View → Output → MCP: heimcp` to see error log |
| `uv: command not found` | `pip install uv` then restart VS Code |
| Server starts but tools return errors | Run `uv run pytest` to verify `src/` is healthy |
| Allow prompt never appeared | `Ctrl+Shift+P` → `MCP: List Servers` → start manually |
