# Contributing

Thanks for helping improve these skills.

## Add or edit a skill

1. Pick a language folder (`en/` or `pt-br/`) and the matching topic folder.
2. Copy an existing `.md` file and rename it.
3. Keep the YAML frontmatter and fill in both keys:

```yaml
---
name: my-skill-name
description: "One or two sentences describing when the skill should be used."
---
```

### Rules

- `name`: kebab-case and unique across the repo (e.g. `bardin-coding`).
- `description`: **always wrap it in double quotes** if it contains `: ` (colon followed by a space). An unquoted colon is the most common cause of `mapping values are not allowed in this context`.
- Keep `description` under 1024 characters. It is what agents use to decide when to load the skill.
- Write the body in Markdown with a single H1 and clear `##` sections.
- Keep the `en/` and `pt-br/` versions in sync when methodology changes.
- Add the language switcher line under the H1, linking to the translated file:

```markdown
> **English** | [Português](../../pt-br/<topic>/<file>.md)
```

## Run the linter

```bash
pip install pyyaml
python3 scripts/lint_skills.py
```

CI runs the same command on every push and pull request.

## Pull requests

- Keep one topic per PR.
- Explain what changed and why.
- Make sure the linter passes.
