# Contributing

Thanks for helping improve these skills.

## Add or edit a skill

Each skill is a folder containing a `SKILL.md` file. The folder name must match the frontmatter `name`.

```text
en/content-analysis-bardin/bardin-coding/
└── SKILL.md
```

```yaml
---
name: bardin-coding
description: "Use when coding a corpus in Bardin's content analysis: cut Recording Units..."
---
```

### Rules

- `name`: kebab-case, unique across the repo, and identical to the folder name (e.g. `bardin-coding`).
- `description`: **always wrap it in double quotes** if it contains `: ` (colon followed by a space). An unquoted colon is the most common cause of `mapping values are not allowed in this context`.
- Start the description with `Use when...` (English) or `Use quando...` (Portuguese) and front-load the keywords a user is likely to say.
- Keep `description` under 1024 characters. It is what agents use to decide when to load the skill.
- Write the body in Markdown with a single H1 and clear `##` sections.
- Keep the `en/` and `pt-br/` versions in sync when methodology changes.
- Keep the root `README.md` and `README.pt-br.md` in sync when the structure or instructions change.
- Add the language switcher line under the H1, linking to the translated `SKILL.md`:

```markdown
> **English** | [Português](../../../pt-br/<topic>/<skill-name>/SKILL.md)
```

## Run the linter

```bash
pip install pyyaml
python3 scripts/lint_skills.py
```

The linter checks the YAML, the folder/name match, duplicate names, and stray Markdown files. CI runs the same command on every push and pull request.

## Website

The GitHub Pages site is built automatically by the reusable [skills-site](https://github.com/14NGiestas/skills-site) action. Generated files are not committed, so there is nothing to rebuild locally.

## Pull requests

- Keep one topic per PR.
- Explain what changed and why.
- Make sure the linter passes.
