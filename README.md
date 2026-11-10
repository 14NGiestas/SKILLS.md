# SKILLS.md — AI Skills for Humanities & Academic Research

A collection of Markdown **skills**: structured prompts for academic research, qualitative methodology (Bardin's Content Analysis), and literature review in the Humanities and Social Sciences.

**Languages:** [English](./README.md) | [Português (pt-br)](./pt-br/README.md)

---

## What is a skill?

A skill is a Markdown file with a small YAML header:

```markdown
---
name: bardin-coding
description: "When the assistant should use this skill."
---

# Title

...instructions...
```

The `name` and `description` tell an AI assistant **when** to load the skill; the body tells it **what to do**. Because a skill is plain text, it works in ChatGPT, Claude, Gemini, and CLI agents without any installation.

## Start here in 30 seconds

1. Pick a skill from the tables below.
2. Open the `.md` file and copy its full contents.
3. Paste it into your assistant:
   - **ChatGPT:** create a Custom GPT, then paste it under *Instructions*.
   - **Claude:** open a Project, then paste it under *Project knowledge*.
   - **CLI agents (opencode, etc.):** add the file to your skills directory, or paste it into the system prompt.
4. Send your material with a clear request, for example:
   > Using the `bardin-pre-analysis` skill, build the corpus protocol for the attached documents.

New to Bardin? Read the short [Pre-Analysis example](./examples/en/bardin-pre-analysis.md) first.

## Which skill do I need?

| If you have... | Use... |
| :--- | :--- |
| A paper, chapter, or thesis to summarize with quotes and page numbers | [Annotated Bibliography](./en/literature-review/annotated-bibliography.md) |
| A pile of documents and no plan yet | [Bardin 01 — Pre-Analysis](./en/content-analysis-bardin/01-pre-analysis.md) |
| An approved corpus and need to cut/count text units | [Bardin 02 — Coding](./en/content-analysis-bardin/02-coding.md) |
| Coded units and need meaningful groups | [Bardin 03 — Categorization](./en/content-analysis-bardin/03-categorization.md) |
| Final categories and need to write/defend the discussion | [Bardin 04 — Interpretation](./en/content-analysis-bardin/04-interpretation.md) |

## Repository structure

```text
SKILLS.md/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
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
│   │   └── annotated-bibliography.md
│   └── content-analysis-bardin/
│       ├── 01-pre-analysis.md
│       ├── 02-coding.md
│       ├── 03-categorization.md
│       └── 04-interpretation.md
└── pt-br/
    ├── README.md
    ├── revisao-bibliografica/
    │   └── fichamento-academico.md
    └── analise-de-conteudo-bardin/
        ├── 01-pre-analise.md
        ├── 02-codificacao.md
        ├── 03-categorizacao.md
        └── 04-interpretacao.md
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
