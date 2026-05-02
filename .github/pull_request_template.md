## What does this PR do?

<!-- One sentence. -->

## Which engineering principle does the new/changed tool encode?

<!-- e.g. 'Conventional Commits v1.0', 'Drama-Free Code Review', etc. -->

## Checklist

- [ ] `uv run pytest tests/ -v` passes
- [ ] New `src/` module has a corresponding `tests/test_<module>.py`
- [ ] All new tools follow the `try/except → ERROR: string` pattern
- [ ] Prompt templates have no dangling `{{placeholders}}`
- [ ] Commit messages follow Conventional Commits
- [ ] `README.md` tables updated
- [ ] No secrets or credentials in any file
