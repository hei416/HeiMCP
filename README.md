# HeiMCP — Staff Engineer Skills as MCP Tools

A FastMCP toolkit that encodes opinionated engineering quality rules as
LLM-callable **Tools**, **Prompts**, and **Resources**.

Unlike generic MCP integrations (GitHub, Slack, Notion), HeiMCP provides
an **opinionated engineering quality layer** — each tool embeds a specific,
named framework rather than wrapping a raw API.

[![CI](https://github.com/hei416/HeiMCP/actions/workflows/ci.yml/badge.svg)](https://github.com/hei416/HeiMCP/actions/workflows/ci.yml)

---

## 🚀 Quick Start

### VS Code + GitHub Copilot (Recommended — Zero Config)

1. Clone the repo and open in VS Code:
   ```bash
   git clone https://github.com/hei416/HeiMCP.git
   cd HeiMCP
   ```
2. Install `uv` if you don’t have it:
   ```bash
   pip install uv
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```
4. Open the folder in VS Code — **that’s it.**

VS Code reads `.vscode/mcp.json` automatically and starts the HeiMCP server
when GitHub Copilot agent mode is active. You’ll see `heimcp` appear in the
Copilot tools list (🔧 icon in the chat input).

> **Tip:** Enable agent mode in Copilot Chat with `Ctrl+Shift+P` →
> `GitHub Copilot: Open Agent Mode`.

---

### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "heimcp": {
      "command": "uv",
      "args": ["run", "python", "skills_server.py"],
      "cwd": "/absolute/path/to/HeiMCP"
    }
  }
}
```

**Config file locations:**
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

---

### Cursor

Add to `.cursor/mcp.json` in your project, or to `~/.cursor/mcp.json` globally:

```json
{
  "mcpServers": {
    "heimcp": {
      "command": "uv",
      "args": ["run", "python", "skills_server.py"],
      "cwd": "/absolute/path/to/HeiMCP"
    }
  }
}
```

---

## 🛠 Tools

| Tool | Description |
|---|---|
| `skill_code_review_logic` | Drama-Free code review: checks PR intent vs. diff |
| `skill_evaluate_unit_tests` | Behavioural unit test quality checker |
| `skill_nn_architecture_check` | PyTorch Conv/DeConv tensor shape validator |
| `skill_rag_faithfulness_check` | Heuristic hallucination detector for RAG pipelines |
| `skill_lint_commit_message` | Conventional Commits v1.0 linter |

## 💬 Prompts

| Prompt | Description |
|---|---|
| `prompt_code_review` | Deep LLM-guided Drama-Free code review |
| `prompt_unit_test_review` | Deep LLM-guided unit test quality review |
| `prompt_rag_faithfulness` | Claim-level RAG faithfulness audit |

## 📚 Resources

| URI | Description |
|---|---|
| `resource://guides/conventional-commits` | Conventional Commits quick reference |
| `resource://guides/drama-free-review` | Code review principles |
| `resource://guides/rag-quality` | RAG faithfulness standards |

---

## 📁 Architecture

```
skills_server.py          # FastMCP entrypoint (tools + prompts + resources)
src/
  code_review.py          # Drama-Free review heuristics
  unit_testing.py         # Test quality rules
  nn_architecture.py      # PyTorch shape tracer
  rag_faithfulness.py     # RAG hallucination detector
  commit_linter.py        # Conventional Commits linter
  prompts.py              # Loads prompts/*.md templates
  resources.py            # Loads resources/*.md guides
  loader.py               # Markdown loader with {{placeholder}} injection
prompts/                  # LLM prompt templates (.md)
resources/                # Reference guides (.md)
tests/                    # pytest test suite
.vscode/mcp.json          # Auto-start config for VS Code + Copilot
.github/workflows/ci.yml  # CI: lint → security scan → tests
CLAUDE.md                 # AI coding rules (Claude Code, Cursor)
AGENTS.md                 # Agent reasoning patterns
```

---

## ⚙️ Development

```bash
# Install all dependencies (including dev tools)
uv sync --group dev

# Run tests
uv run pytest

# Lint + complexity check
uv run ruff check src/ skills_server.py

# Security scan
uv run bandit -r src/ skills_server.py -ll --skip B101,B603

# Auto-fix style issues
uv run ruff check src/ skills_server.py --fix
uv run ruff format src/ skills_server.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide on adding new tools.

---

## 🤖 AI Coding Rules

This repo ships with `CLAUDE.md` and `AGENTS.md` — these are auto-loaded by
Claude Code and Cursor respectively, encoding the architecture rules and
coding standards directly into the AI agent’s context.
