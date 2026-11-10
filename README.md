# SKILLS.md — AI Skills for Humanities & Academic Research

A collection of Markdown **skills**: structured prompts for academic research, qualitative methodology (Bardin's Content Analysis), and literature review in the Humanities and Social Sciences.

**Languages:** [English](./README.md) | [Português (pt-br)](./pt-br/README.md)

---

## What is a skill?

A skill is a folder containing a `SKILL.md` file with a small YAML header:

```text
bardin-coding/
└── SKILL.md
```

```markdown
---
name: bardin-coding
description: "Use when coding a corpus in Bardin's content analysis..."
---

# Title

...instructions...
```

The folder name **must** match `name`. The `name` and `description` tell an AI assistant **when** to load the skill; the body tells it **what to do**. Because a skill is plain text, it also works in ChatGPT, Claude, and Gemini when pasted manually.

## Start here in 30 seconds

1. Pick a skill from the tables below.
2. Open its `SKILL.md` and copy the full contents.
3. Paste it into your assistant:
   - **ChatGPT:** create a Custom GPT, then paste it under *Instructions*.
   - **Claude:** open a Project, then paste it under *Project knowledge*.
   - **opencode / CLI agents:** if the repo is your working directory, the skills load automatically (see below).
4. Send your material with a clear request, for example:
   > Using the `bardin-pre-analysis` skill, build the corpus protocol for the attached documents.

New to Bardin? Read the short [Pre-Analysis example](./examples/en/bardin-pre-analysis.md) first.

## Auto-discovery (opencode / Claude)

This repo follows the `<skill-name>/SKILL.md` convention. For opencode, [`opencode.json`](./opencode.json) registers both language folders:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": { "paths": ["./en", "./pt-br"] }
}
```

opencode scans those paths recursively for `**/SKILL.md`, so each skill is discovered without copying anything. Restart opencode after pulling changes. To expose only one language, remove the other path.

For Claude, copy or symlink the folders you want into `~/.claude/skills/`.

## Which skill do I need?

| If you have... | Use... |
| :--- | :--- |
| A paper, chapter, or thesis to summarize with quotes and page numbers | [Annotated Bibliography](./en/literature-review/annotated-bibliography/SKILL.md) |
| A pile of documents and no plan yet | [Bardin 01 — Pre-Analysis](./en/content-analysis-bardin/bardin-pre-analysis/SKILL.md) |
| An approved corpus and need to cut/count text units | [Bardin 02 — Coding](./en/content-analysis-bardin/bardin-coding/SKILL.md) |
| Coded units and need meaningful groups | [Bardin 03 — Categorization](./en/content-analysis-bardin/bardin-categorization/SKILL.md) |
| Final categories and need to write/defend the discussion | [Bardin 04 — Interpretation](./en/content-analysis-bardin/bardin-interpretation/SKILL.md) |

## Repository structure

```text
SKILLS.md/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── opencode.json
├── scripts/
│   └── lint_skills.py
├── .github/workflows/
│   └── lint.yml
├── examples/
│   ├── README.md
│   ├── en/bardin-pre-analysis.md
│   └── pt-br/bardin-pre-analise.md
├── en/
│   ├── README.md
│   ├── literature-review/
│   │   └── annotated-bibliography/
│   │       └── SKILL.md
│   └── content-analysis-bardin/
│       ├── bardin-pre-analysis/SKILL.md
│       ├── bardin-coding/SKILL.md
│       ├── bardin-categorization/SKILL.md
│       └── bardin-interpretation/SKILL.md
└── pt-br/
    ├── README.md
    ├── revisao-bibliografica/
    │   └── fichamento-academico/SKILL.md
    └── analise-de-conteudo-bardin/
        ├── bardin-pre-analise/SKILL.md
        ├── bardin-codificacao/SKILL.md
        ├── bardin-categorizacao/SKILL.md
        └── bardin-interpretacao/SKILL.md
```

## Catalogs

- [English catalog](./en/README.md)
- [Catálogo em português](./pt-br/README.md)

## Glossary

- **Corpus:** the delimited set of documents that will actually be analyzed.
- **Floating reading:** a first, unstructured contact with the material to surface impressions and hypotheses.
- **Recording Unit (RU):** the smallest segment that carries meaning for the analysis (word, theme, sentence, event).
- **Context Unit (CU):** the surrounding passage needed to understand an RU correctly.
- **Coding:** cutting the corpus into RUs and assigning them stable codes.
- **Categorization:** grouping RUs into homogeneous, mutually exclusive categories.
- **Manifest content:** what the text explicitly says.
- **Latent content:** underlying meanings, silences, values, and contradictions.
- **Inference:** reasoned interpretation that goes beyond paraphrasing the data.
- **Traceability matrix:** the table linking category, code, quote, and document/participant.

## Contributing

Read [`CONTRIBUTING.md`](./CONTRIBUTING.md). Before opening a PR, run:

```bash
pip install pyyaml
python3 scripts/lint_skills.py
```

## License

Released under [Creative Commons Attribution 4.0 (CC BY 4.0)](./LICENSE). Free to share and adapt with attribution.
