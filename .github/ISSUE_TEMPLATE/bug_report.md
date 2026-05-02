---
name: Bug Report
about: A tool returns wrong output or crashes
title: "fix(<module>): <short description>"
labels: bug
---

## Tool or module affected

<!-- e.g. skill_evaluate_unit_tests / src/unit_testing.py -->

## Input that caused the bug

```
<paste the exact input string or JSON here>
```

## Actual output

```
<paste the actual output>
```

## Expected output

```
<describe what you expected>
```

## Steps to reproduce

```bash
uv run python -c "from src.<module> import <function>; print(<function>('<input>'))"
```
