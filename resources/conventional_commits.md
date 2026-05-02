# Conventional Commits v1.0 Quick Reference

## Format

```
<type>(<scope>): <short description>

[optional body]

[optional footer(s)]
```

## Types

| Type | Purpose |
|---|---|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code change that is not a fix or feature |
| `perf` | Performance improvement |
| `test` | Adding or fixing tests |
| `chore` | Build process or tooling |
| `ci` | CI/CD configuration |
| `revert` | Reverting a previous commit |

## Rules

- Subject line max **72 characters**
- Use **imperative mood**: "add" not "added"
- No period at end of subject
- Blank line between subject and body
- Breaking changes: add `!` after type, or `BREAKING CHANGE:` in footer

## Examples

```
feat(auth): add OAuth2 login support
fix(api): handle null response from payment gateway
docs(readme): update installation steps
feat!: remove deprecated /v1 endpoints
```

## Reference

https://www.conventionalcommits.org
