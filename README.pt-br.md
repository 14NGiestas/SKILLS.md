# SKILLS.md — Skills de IA para Humanidades e Pesquisa Acadêmica

Uma coleção de **skills** em Markdown: prompts estruturados para pesquisa acadêmica, metodologia qualitativa (Análise de Conteúdo de Bardin) e revisão de literatura em Ciências Humanas e Sociais.

**Idiomas:** [English](./README.md) | [Português](./README.pt-br.md)

---

## O que é uma skill?

Uma skill é uma pasta contendo um arquivo `SKILL.md` com um pequeno cabeçalho YAML:

```text
bardin-codificacao/
└── SKILL.md
```

```markdown
---
name: bardin-codificacao
description: "Use quando for codificar o corpus na Análise de Conteúdo de Bardin..."
---

# Título

...instruções...
```

O nome da pasta **precisa** ser igual ao `name`. O `name` e a `description` dizem ao assistente **quando** carregar a skill; o corpo diz **o que fazer**. Como é texto puro, também funciona no ChatGPT, Claude e Gemini quando colado manualmente.

## Comece aqui em 30 segundos

1. Escolha uma skill nas tabelas abaixo.
2. Abra o `SKILL.md` e copie o conteúdo inteiro.
3. Cole no seu assistente:
   - **ChatGPT:** crie um Custom GPT e cole em *Instructions*.
   - **Claude:** abra um Project e cole em *Project knowledge*.
   - **opencode / agentes de CLI:** se o repositório for seu diretório de trabalho, as skills carregam automaticamente (veja abaixo).
4. Envie seu material com um pedido claro, por exemplo:
   > Usando a skill `bardin-pre-analise`, monte o protocolo do corpus para os documentos anexados.

Primeira vez com Bardin? Leia o [exemplo de Pré-Análise](./examples/pt-br/bardin-pre-analise.md).

## Auto-descoberta (opencode / Claude)

Este repositório segue a convenção `<nome-da-skill>/SKILL.md`. Para o opencode, o [`opencode.json`](./opencode.json) registra as duas pastas de idioma:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["./en", "./pt-br"]
}
```

O opencode varre esses caminhos recursivamente por `**/SKILL.md`, então cada skill é descoberta sem copiar nada. Reinicie o opencode depois de puxar mudanças. Para expor só um idioma, remova o outro caminho.

Para o Claude, copie ou crie links simbólicos das pastas desejadas em `~/.claude/skills/`.

## Para agentes: descobrir e instalar

Dê um único link ao agente e ele encontra tudo:

- **Manifesto:** https://raw.githubusercontent.com/14NGiestas/SKILLS.md/main/llms.txt
- **Árvore de arquivos:** https://api.github.com/repos/14NGiestas/SKILLS.md/git/trees/main?recursive=1

Instale globalmente no opencode com:

```bash
git clone --depth 1 https://github.com/14NGiestas/SKILLS.md ~/.config/opencode/skills/SKILLS.md
```

Reinicie o opencode depois; todo `SKILL.md` dentro dessa pasta é descoberto (os dois idiomas). Para o Gemini web ou agentes de chat, cole este prompt:

```text
Acesse https://raw.githubusercontent.com/14NGiestas/SKILLS.md/main/llms.txt
Liste as skills disponíveis e, para cada uma que eu escolher:
1. Baixe o SKILL.md indicado.
2. Use o `name` do frontmatter como nome da habilidade e o `description` como gatilho.
3. Use o corpo após o segundo `---` como instruções, sem o YAML.
4. Mostre os três campos prontos para eu colar na tela de Habilidades do Gemini.
```

## Site

Um catálogo estático é publicado com GitHub Pages:

**https://14ngiestas.github.io/SKILLS.md/**

O site é construído pela action reutilizável [14NGiestas/skills-site](https://github.com/14NGiestas/skills-site) a partir dos mesmos arquivos `SKILL.md`; nenhum arquivo gerado é versionado. O `.github/workflows/pages.yml` reconstrói e publica a cada push na `main`.

Ative o Pages uma vez em **Settings → Pages → Source: GitHub Actions**.

## Qual skill eu preciso?

| Se você tem... | Use... |
| :--- | :--- |
| Um artigo, capítulo ou tese para resumir com citações e páginas | [Fichamento Acadêmico](./pt-br/revisao-bibliografica/fichamento-academico/SKILL.md) |
| Um monte de documentos e nenhum plano ainda | [Bardin 01 — Pré-Análise](./pt-br/analise-de-conteudo-bardin/bardin-pre-analise/SKILL.md) |
| Um corpus aprovado e precisa recortar/contar unidades | [Bardin 02 — Codificação](./pt-br/analise-de-conteudo-bardin/bardin-codificacao/SKILL.md) |
| Unidades codificadas e precisa de grupos com sentido | [Bardin 03 — Categorização](./pt-br/analise-de-conteudo-bardin/bardin-categorizacao/SKILL.md) |
| Categorias finais e precisa redigir/defender a discussão | [Bardin 04 — Interpretação](./pt-br/analise-de-conteudo-bardin/bardin-interpretacao/SKILL.md) |

## Estrutura do repositório

```text
SKILLS.md/
├── README.md
├── README.pt-br.md
├── CONTRIBUTING.md
├── LICENSE
├── llms.txt
├── opencode.json
├── scripts/
│   └── lint_skills.py
├── .github/workflows/
│   ├── lint.yml
│   └── pages.yml
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

## Catálogos

- [English catalog](./en/README.md)
- [Catálogo em português](./pt-br/README.md)

## Glossário

- **Corpus:** conjunto delimitado de documentos que será efetivamente analisado.
- **Leitura flutuante:** primeiro contato, não estruturado, com o material, para levantar impressões e hipóteses.
- **Unidade de Registro (UR):** menor segmento que carrega sentido para a análise (palavra, tema, frase, acontecimento).
- **Unidade de Contexto (UC):** trecho ao redor necessário para compreender corretamente uma UR.
- **Codificação:** recorte do corpus em URs e atribuição de códigos estáveis.
- **Categorização:** agrupamento de URs em categorias homogêneas e mutuamente exclusivas.
- **Conteúdo manifesto:** o que o texto diz explicitamente.
- **Conteúdo latente:** significados subjacentes, silêncios, valores e contradições.
- **Inferência:** interpretação fundamentada que vai além de parafrasear os dados.
- **Matriz de rastreabilidade:** tabela que liga categoria, código, citação e documento/participante.

## Contribuindo

Leia [`CONTRIBUTING.md`](./CONTRIBUTING.md). Antes de abrir um PR, rode:

```bash
pip install pyyaml
python3 scripts/lint_skills.py
```

## Licença

Distribuído sob [Creative Commons Attribution 4.0 (CC BY 4.0)](./LICENSE). Livre para compartilhar e adaptar com atribuição.
