# Berna TJGO DIACDE Lib

Biblioteca desenvolvida pelo **TJGO (Diretoria de Inteligência Artificial, Ciência de Dados e Estatística)**. Este pacote oferece ferramentas robustas para pré-processamento de texto e cálculo de similaridade textual, essenciais para processamento de linguagem natural (NLP) e preparação de dados para LLMs.

O núcleo das operações de texto é fornecido pela classe `TextUtils`, acessível através de duas interfaces:

1. **Interface Fluente (`ProcessLinked`):** Para aplicações diretas e encadeadas.
2. **Processador Baseado em Pipeline (`ProcessPipeline`):** Para workflows configuráveis e reprodutíveis.

Para cálculo de similaridade textual, a biblioteca disponibiliza a classe `Berna`.

> **Nota:** Este repositório público contém uma seleção de ferramentas usadas internamente pelo TJGO.

---


## Instalação
* **PyPI:** [berna-tjgo-diacde-lib](https://pypi.org/project/berna-tjgo-diacde-lib/)

Para instalar a biblioteca, utilize o gerenciador de pacotes `pip`:

```bash
pip install berna-tjgo-diacde-lib

```

### Dependências

O projeto utiliza as seguintes bibliotecas:

* `spacy`
* `nltk`
* `beautifulsoup4`
* `snowballstemmer`

*Nota: Alguns modelos do spaCy (como `pt_core_news_sm`) podem precisar ser baixados separadamente.*

---

## Módulo de Pré-Processamento

### 1. Interface Fluente com `ProcessLinked`

Ideal para transformações rápidas de forma legível.

```python
from berna_tjgo_diacde_lib import ProcessLinked

text = "  Olá, mundo! Este é um teste com números 123. E e-mail: test@example.com.  "

processed_text = (
    ProcessLinked(text)
    .filter_email()              # Remove e-mails
    .filter_spaces()             # Remove múltiplos espaços
    .filter_special_characters() # Remove pontuações
    .filter_numbers()            # Remove números
    .stemming()                  # Reduz palavras à raiz (ex: 'correndo' -> 'corr')
    .as_str()                    # Obtém a string final
)

print(processed_text)
# Saída: Olá mund Este é um test com númer E email

```

### 2. Pipeline Declarativo com `ProcessPipeline`

Ideal para definir fluxos complexos via configuração de lista, reutilizando pipelines.

```python
from berna_tjgo_diacde_lib import ProcessPipeline

text = "  Olá, mundo! Este é um teste com números 123. E e-mail: test@example.com.  "

pipeline_config = [
    {"name": "filter_email"},
    {"name": "filter_spaces"},
    {"name": "filter_special_characters"},
    {"name": "filter_numbers"},
    {"name": "remove_stopwords", "language": "portuguese"},
    {"name": "stemming"}
]

processor = ProcessPipeline(pipeline_config)
processed_text = processor.process(text)

print(processed_text)

```

---

### Métodos Disponíveis (via `TextUtils`)

| Método | Descrição |
| --- | --- |
| `filter_special_characters` | Remove pontuação e caracteres especiais. |
| `filter_spaces` | Padroniza múltiplos espaços para um único espaço. |
| `filter_numbers` | Remove caracteres numéricos. |
| `filter_links` | Remove URLs e links. |
| `filter_email` | Remove endereços de e-mail. |
| `filter_cnpj`/`cpf`/`rg` | Filtros específicos para documentos brasileiros. |
| `filter_cep`/`oab` | Filtros para códigos postais e registros da OAB. |
| `remove_stopwords` | Remove palavras comuns (ex: "e", "de", "o"). |
| `remove_html` | Remove tags HTML via BeautifulSoup. |
| `lemmatize` | Reduz palavras à forma base (lema) usando spaCy. |
| `stemming` | Reduz palavras à raiz usando snowballstemmer. |


---

## Licença

Este projeto está licenciado sob a **MIT License**. Você é livre para usar, modificar e distribuir o software, desde que mantenha os avisos de copyright.

---

## Créditos e Desenvolvedores

Desenvolvido pelo **Tribunal de Justiça do Estado de Goiás** - [Diretoria de Inteligência Artificial, Ciência de Dados e Estatística](https://github.com/TJGO-DIACDE).

**Time de Desenvolvimento:**

* [Antônio Pires](https://github.com/apcastrojr) - `<apcastro@tjgo.jus.br>`
* [Milton Ávila](https://github.com/Milton-Avila) - `<miltonavila.dev@gmail.com>`
* [João Gabriel](https://github.com/joaograndotto) - `<grandottojoao@gmail.com>`
* [Wesley Oliveira](https://github.com/waejl) - `<wesley@woliveira.me>`

---

*Contato oficial: [estatistica@tjgo.jus.br*]()