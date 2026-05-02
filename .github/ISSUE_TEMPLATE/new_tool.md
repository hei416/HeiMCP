---
name: New Tool Proposal
about: Propose a new MCP tool, prompt, or resource for HeiMCP
title: "feat: add skill_<name>"
labels: enhancement
---

## What engineering principle does this tool encode?

<!-- e.g. "SOLID Single Responsibility Principle checker" -->

## What problem does it solve for an AI coding agent?

<!-- What would Claude/Cursor do better with this tool available? -->

## Proposed tool signature

```python
@mcp.tool()
async def skill_<name>(input: SomeInput) -> str:
    """One-line description."""
    ...
```

## Input / output example

**Input:**
```
...
```

**Expected output:**
```
...
```

## Is this already covered by an existing MCP server?

<!-- Check https://mcpservers.org first. If yes, explain why HeiMCP should still include it. -->
