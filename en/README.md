# Skills Catalog (English — EN)

Structured operational prompts to support research in the Humanities, Applied Social Sciences, and Education.

**Languages:** [English](./README.md) | [Português (pt-br)](../pt-br/README.md)

---

## Start here in 30 seconds

1. Pick a skill from the tables below.
2. Open its `.md` file and copy the whole file.
3. Paste it into your assistant:
   - **ChatGPT:** create a Custom GPT and paste it under *Instructions*.
   - **Claude:** open a Project and paste it under *Project knowledge*.
   - **CLI agents (opencode, etc.):** add the file to your skills directory, or paste it into the system prompt.
4. Send your material with a clear request, for example:
   > "Using the `bardin-pre-analysis` skill, build the corpus protocol for the three documents below."

## Which skill do I need?

| If you have... | Use... |
| :--- | :--- |
| A paper, chapter, or thesis to summarize with quotes and page numbers | [Annotated Bibliography](./literature-review/annotated-bibliography.md) |
| A pile of documents and no plan yet | [Bardin 01 — Pre-Analysis](./content-analysis-bardin/01-pre-analysis.md) |
| An approved corpus and need to cut/count text units | [Bardin 02 — Coding](./content-analysis-bardin/02-coding.md) |
| Coded units and need meaningful groups | [Bardin 03 — Categorization](./content-analysis-bardin/03-categorization.md) |
| Final categories and need to write/defend the discussion | [Bardin 04 — Interpretation](./content-analysis-bardin/04-interpretation.md) |

## Skill index

### Literature Review & Reading Notes
| Skill | Standard | Description | Link |
| :--- | :--- | :--- | :--- |
| **Annotated Bibliography** | APA / Chicago | Central thesis, thematic summary, paginated verbatim quotes, and critical appraisal. | [`literature-review/annotated-bibliography.md`](./literature-review/annotated-bibliography.md) |

### Content Analysis (Laurence Bardin)
| Step | Bardin phase | Description | Link |
| :--- | :--- | :--- | :--- |
| **01. Pre-Analysis** | Phase 1 | Floating reading, audit of the 4 corpus rules, and formalization of hypotheses/indices. | [`content-analysis-bardin/01-pre-analysis.md`](./content-analysis-bardin/01-pre-analysis.md) |
| **02. Coding** | Phase 2a | Cutting Recording Units (RU) and Context Units (CU), enumeration rules, and textual evidence. | [`content-analysis-bardin/02-coding.md`](./content-analysis-bardin/02-coding.md) |
| **03. Categorization** | Phase 2b | Analogical grouping, audit of the 5 formal criteria, category dictionary, and traceability matrix. | [`content-analysis-bardin/03-categorization.md`](./content-analysis-bardin/03-categorization.md) |
| **04. Interpretation** | Phase 3 | Latent content analysis, theoretical triangulation, methodological drafting, and board simulation. | [`content-analysis-bardin/04-interpretation.md`](./content-analysis-bardin/04-interpretation.md) |

---

## Worked examples

See [`examples/`](../examples/README.md) for a short end-to-end walkthrough of the Pre-Analysis skill.

## Execution guidelines

- **Theoretical traceability:** every skill requires grounding in the original authors (e.g. Bardin, Freire, Minayo, Paro).
- **Separation of voices:** keep a strict distinction between the faithful summary of the analyzed author and the researcher's critical appraisal.

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

Read [`CONTRIBUTING.md`](../CONTRIBUTING.md). Run `python3 scripts/lint_skills.py` before opening a PR.

## License

Released under [CC BY 4.0](../LICENSE).
