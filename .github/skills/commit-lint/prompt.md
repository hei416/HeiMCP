You are linting a git commit message using the HeiMCP toolkit.

You have access to:
- `skill_lint_commit_message` — Conventional Commits v1.0 linter

### Step 1 — Lint
Call `skill_lint_commit_message` with:
- `commit_message`: {{commit_message}}

### Step 2 — Explain Results

If the message passes: confirm it's compliant and explain why it's good.

If the message fails: for each violation, show:
1. What the rule is
2. What was wrong
3. A corrected example

Always end with a corrected version of the full commit message if any changes are needed.
