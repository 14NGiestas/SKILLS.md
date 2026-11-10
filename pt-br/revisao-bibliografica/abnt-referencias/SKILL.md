---
name: abnt-referencias
description: "Use quando for montar, revisar ou conferir referências de trabalhos acadêmicos segundo a ABNT NBR 6023:2025: livros, capítulos, artigos, teses, eventos, documentos jurídicos, mídias e fontes online. Cobre autoria, ordem dos elementos, pontuação, DOI, URL e data de acesso."
metadata:
  category:
    en: "ABNT References"
    pt: "Referências ABNT"
  group: abnt-referencias
  order: 2
---

# Referências ABNT NBR 6023:2025

Skill para elaborar, revisar e auditar listas de referências conforme a **ABNT NBR 6023:2025** (3. ed., publicada em 21.05.2025, que cancela e substitui a NBR 6023:2018).

Esta skill trata da **lista de referências**. Citações no corpo do texto seguem a ABNT NBR 10520 e não são o foco aqui.

## Quando usar

- Para transformar dados bibliográficos soltos em referências ABNT completas.
- Para conferir referências já escritas antes de entregar TCC, monografia, dissertação, tese ou artigo.
- Para padronizar uma lista inteira (pontuação, destaque do título, ordem alfabética, presença de DOI/URL e data de acesso).
- Para decidir quais elementos são essenciais em cada tipo de fonte.

## Fluxo de trabalho

1. **Classifique a fonte.** Livro, capítulo, artigo de periódico, tese, trabalho de evento, documento jurídico, mídia, página web etc.
2. **Colete os dados na própria fonte.** Autor, título, subtítulo, edição, local, editora, ano, páginas, volume, número, DOI, URL e data de acesso.
3. **Abra o arquivo de referência do tipo.** Use a árvore de decisão abaixo; leia apenas o arquivo necessário.
4. **Monte a referência na ordem dos elementos.** Use um dos modelos e adapte sem inventar dados.
5. **Audite a lista inteira.** Verifique se o destaque do título e a pontuação são uniformes e se as referências estão em ordem alfabética.

## Regras essenciais

### Ordem dos elementos

- A referência segue uma sequência padronizada: **autor → título → subtítulo → edição → local → editora → data → descrição física → notas → disponibilidade/acesso**.
- A ordem exata varia conforme o tipo de documento. Não acrescente elementos de um tipo em outro.
- Elementos essenciais identificam o documento. Elementos complementares (páginas, ISBN, DOI, séries, notas) melhoram a identificação e, se usados, devem aparecer em todas as referências do mesmo tipo.

### Autoria

- Pessoa física: **SOBRENOME, Nome**, com o último sobrenome em maiúsculas.
- Até três autores: indicar todos, separados por ponto e vírgula.
- Quatro ou mais autores: recomenda-se indicar todos; é permitido indicar o primeiro seguido de `et al.`
- Organizador, compilador, editor e coordenador: `(org.)`, `(comp.)`, `(ed.)`, `(coord.)`, em minúsculas e no singular, após o último nome.
- Pessoa jurídica: entrada pelo nome conhecido, em maiúsculas, por extenso ou abreviado.
- Evento: nome do evento em maiúsculas, seguido de número, ano e local.
- Autoria desconhecida: entrada pelo título. Nunca use `Anônimo` ou `Autor desconhecido`.

### Título e subtítulo

- Reproduza o título como aparece no documento.
- Separe título e subtítulo por **dois pontos**.
- Use sempre o mesmo recurso de destaque para o título em toda a lista (itálico, negrito ou sublinhado). Os modelos desta skill usam itálico.
- Títulos longos podem ser encurtados com `[...]`, desde que o sentido não mude.

### Edição, local, editora e data

- Edição: numeral ordinal + `ed.` no idioma do documento (`2. ed.`, `5th ed.`). Acrescente `rev. e aum.` quando constar.
- Local: cidade como consta. Se não houver cidade, use o estado ou o país. Cidades homônimas recebem a sigla do estado ou o país.
- Local não identificado: `[S. l.]`; editora não identificada: `[s. n.]`; ambos: `[S. l.: s. n.]`.
- Editora: nome como aparece, sem a natureza jurídica ou comercial (`Editora Atlas`, não `Editora Atlas S.A.`).
- Data: ano em algarismos arábicos. Sem ano, use `[20--]`, `[197-?]`, `[ca. 1960]` etc. conforme a certeza disponível.
- Mês: abreviado no idioma original e antes do ano (`mar. 2024`). Vários meses: `maio/dez.`

### Documentos online

- Todo documento consultado online recebe, ao final:
  `Disponível em: <URL>. Acesso em: <dia> <mês abreviado> <ano>.`
- Se houver DOI, informe-o como elemento complementar: `DOI: 10.xxxx/...`.
- A data de acesso é obrigatória para documentos online. Não invente a data: use a data real da consulta.
- Mensagens e documentos eletrônicos sem endereço disponível são exceção à regra de URL.

### Apresentação e ordenação

- Espaço simples, alinhamento à esquerda e uma linha em branco entre as referências.
- Pontuação uniforme em toda a lista.
- Sistema alfabético: lista única em ordem alfabética; numerais em ordem crescente.
- Sistema numérico: numere na ordem da primeira citação no texto.
- O destaque do título deve ser uniforme; a exceção são obras sem autoria, cuja entrada é o próprio título (a primeira palavra, incluindo artigo, fica em maiúsculas).

## Árvore de decisão

| Se a fonte for... | Leia |
| :--- | :--- |
| Livro, folheto, e-book, capítulo, tese, dissertação, TCC ou correspondência | [`references/livros-capitulos-teses.md`](references/livros-capitulos-teses.md) |
| Artigo de revista/jornal, coleção de periódico, anais de evento, patente, legislação, jurisprudência ou ato administrativo | [`references/periodicos-eventos-juridico.md`](references/periodicos-eventos-juridico.md) |
| Filme, vídeo, áudio, partitura, imagem, mapa, objeto 3D, site, blog, rede social, podcast ou software | [`references/midias-e-online.md`](references/midias-e-online.md) |
| Dúvida sobre autoria, pontuação, local, editora, data, descrição física, notas ou ordenação | [`references/regras-gerais-e-autoria.md`](references/regras-gerais-e-autoria.md) |
| Modelos prontos, abreviaturas e checklist final | [`references/modelos-rapidos.md`](references/modelos-rapidos.md) |

## Modelos mínimos

Nos modelos, os asteriscos indicam o trecho que deve receber o destaque do título; remova-os ao aplicar itálico, negrito ou sublinhado.

**Livro**
`SOBRENOME, Nome. *Título: subtítulo*. 2. ed. Local: Editora, 2024.`

**Capítulo de livro**
`SOBRENOME, Nome. Título do capítulo. In: SOBRENOME, Nome (org.). *Título do livro*. Local: Editora, 2024. p. 10-25.`

**Artigo de periódico**
`SOBRENOME, Nome. Título do artigo. *Título da Revista*, Local, v. 10, n. 2, p. 1-15, 2024.`

**Artigo de periódico online**
`SOBRENOME, Nome. Título do artigo. *Título da Revista*, Local, v. 10, n. 2, p. 1-15, 2024. DOI: 10.xxxx/xxxx. Disponível em: <URL>. Acesso em: 10 nov. 2026.`

**Tese ou dissertação**
`SOBRENOME, Nome. *Título*. 2024. Tese (Doutorado em Área) – Faculdade, Universidade, Local, 2024.`

**Trabalho em evento**
`SOBRENOME, Nome. Título do trabalho. In: NOME DO EVENTO, 10., 2024, Local. *Anais [...].* Local: Editora, 2024. p. 1-10.`

**Página web**
`SOBRENOME, Nome. *Título da página*. Local: Editora, 2024. Disponível em: <URL>. Acesso em: 10 nov. 2026.`

## Checklist de auditoria

- [ ] Todos os autores foram localizados e o sobrenome está em maiúsculas.
- [ ] Título e subtítulo estão separados por dois pontos.
- [ ] Edição, local, editora e ano estão na ordem correta.
- [ ] A descrição física (páginas, volumes, duração) foi incluída quando pertinente.
- [ ] Documentos online têm `Disponível em:` e `Acesso em:` com data real.
- [ ] DOI foi incluído quando disponível.
- [ ] O destaque do título é o mesmo em todas as referências.
- [ ] A lista está em ordem alfabética (ou numérica, se o trabalho usar citação numérica).
- [ ] Não há dados inventados, abreviações inconsistentes ou pontuação dupla.

## Limites

- Não use esta skill para formatar citações no texto; consulte a ABNT NBR 10520.
- Não invente DOI, URL, página, volume ou data de acesso. Quando o dado não existir, use as convenções de omissão (`[S. l.]`, `[s. n.]`, `[20--]`).
- A ABNT NBR 6023:2025 é uma norma técnica; em caso de dúvida não coberta aqui, consulte o texto oficial ou o orientador.
- Esta skill é um guia prático independente, baseado na ABNT NBR 6023:2025. A norma é protegida por direitos autorais; adquira o texto oficial da ABNT.
