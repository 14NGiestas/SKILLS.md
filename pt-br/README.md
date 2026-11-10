# Catálogo de Skills (Português — PT-BR)

Guia de prompts operacionais e metodológicos estruturados para apoiar pesquisas em Ciências Humanas, Sociais Aplicadas e Educação.

**Idiomas:** [English](../en/README.md) | [Português](./README.md)

---

## Comece aqui em 30 segundos

1. Escolha uma skill nas tabelas abaixo.
2. Abra o `SKILL.md` e copie o conteúdo inteiro.
3. Cole no seu assistente:
   - **ChatGPT:** crie um Custom GPT e cole em *Instructions*.
   - **Claude:** abra um Project e cole em *Project knowledge*.
   - **Agentes de CLI (opencode etc.):** se o repositório for seu diretório de trabalho, as skills carregam automaticamente via [`opencode.json`](../opencode.json).
4. Envie seu material com um pedido claro, por exemplo:
   > Usando a skill `bardin-pre-analise`, monte o protocolo do corpus para os documentos anexados.

Primeira vez com Bardin? Leia o [exemplo de Pré-Análise](../examples/pt-br/bardin-pre-analise.md).

## Qual skill eu preciso?

| Se você tem... | Use... |
| :--- | :--- |
| Um artigo, capítulo ou tese para resumir com citações e páginas | [Fichamento Acadêmico](./revisao-bibliografica/fichamento-academico/SKILL.md) |
| Um monte de documentos e nenhum plano ainda | [Bardin 01 — Pré-Análise](./analise-de-conteudo-bardin/bardin-pre-analise/SKILL.md) |
| Um corpus aprovado e precisa recortar/contar unidades | [Bardin 02 — Codificação](./analise-de-conteudo-bardin/bardin-codificacao/SKILL.md) |
| Unidades codificadas e precisa de grupos com sentido | [Bardin 03 — Categorização](./analise-de-conteudo-bardin/bardin-categorizacao/SKILL.md) |
| Categorias finais e precisa redigir/defender a discussão | [Bardin 04 — Interpretação](./analise-de-conteudo-bardin/bardin-interpretacao/SKILL.md) |

## Índice de Skills

### Revisão de Literatura & Fichamento
| Skill | Metodologia / Norma | Descrição | Link |
| :--- | :--- | :--- | :--- |
| **Fichamento Acadêmico** | ABNT / APA | Estrutura tese central, resumo temático, transcrição de citações paginadas e crítica analítica. | [`revisao-bibliografica/fichamento-academico/SKILL.md`](./revisao-bibliografica/fichamento-academico/SKILL.md) |

### Análise de Conteúdo (Laurence Bardin)
| Etapa / Ficha | Fase de Bardin | Descrição | Link |
| :--- | :--- | :--- | :--- |
| **01. Pré-Análise** | Fase 1 | Leitura flutuante, auditoria das 4 regras do corpus e formalização de hipóteses/índices. | [`analise-de-conteudo-bardin/bardin-pre-analise/SKILL.md`](./analise-de-conteudo-bardin/bardin-pre-analise/SKILL.md) |
| **02. Codificação** | Fase 2a | Recorte de Unidades de Registro (UR) e Contexto (UC), regras de enumeração e evidências textuais. | [`analise-de-conteudo-bardin/bardin-codificacao/SKILL.md`](./analise-de-conteudo-bardin/bardin-codificacao/SKILL.md) |
| **03. Categorização** | Fase 2b | Agrupamento analógico, auditoria dos 5 critérios formais, dicionário categorial e matriz de rastreabilidade. | [`analise-de-conteudo-bardin/bardin-categorizacao/SKILL.md`](./analise-de-conteudo-bardin/bardin-categorizacao/SKILL.md) |
| **04. Interpretação** | Fase 3 | Análise de conteúdo latente, triangulação teórica, redação metodológica e simulação de banca. | [`analise-de-conteudo-bardin/bardin-interpretacao/SKILL.md`](./analise-de-conteudo-bardin/bardin-interpretacao/SKILL.md) |

---

## Diretrizes de Execução

- **Rastreabilidade Teórica:** todas as skills exigem fundamentação com os autores originais (ex.: Bardin, Freire, Minayo, Paro).
- **Separação de Vozes:** mantém-se distinção rigorosa entre a síntese fiel do autor analisado e a apreciação crítica do pesquisador.

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

Leia [`CONTRIBUTING.md`](../CONTRIBUTING.md). Antes de abrir um PR, rode:

```bash
pip install pyyaml
python3 scripts/lint_skills.py
```

## Licença

Distribuído sob [Creative Commons Attribution 4.0 (CC BY 4.0)](../LICENSE). Livre para compartilhar e adaptar com atribuição.
