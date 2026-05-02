# Drama-Free Code Review Principles

## The Core Rules

1. **READ FIRST** — Understand the PR intent before reading a single line of code
2. **DISCREPANCY CHECK** — Does the code match what the description says?
3. **GROWTH MINDSET** — Assume the author had good reasons for their choices
4. **ASK QUESTIONS** — "What happens if...?" not "Change this."
5. **CATEGORISE** — Every comment needs a label: `[Blocker]` / `[Suggestion]` / `[Nit]`
6. **LANGUAGE IDIOMS** — Flag anti-patterns specific to the language
7. **COMPLIMENT** — Explicitly acknowledge clever solutions

## Category Guide

| Category | Merge Impact | Examples |
|---|---|---|
| `[Blocker]` | Must fix before merge | Security bug, data loss, incorrect logic |
| `[Suggestion]` | Should fix, won't block | Performance, readability, missing test |
| `[Nit]` | Author's discretion | Naming preference, minor style |

## Anti-Pattern Examples

- Kotlin written like Java (using `!!` everywhere instead of safe calls)
- Python using `for i in range(len(x))` instead of `for item in x`
- Java using raw `String` concatenation in loops instead of `StringBuilder`
