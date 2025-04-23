

# Berna TJGO DIACDE Lib
[![PyPI version](https://img.shields.io/pypi/v/berna-tjgo-diacde-lib)](https://pypi.org/project/berna-tjgo-diacde-lib/)
[![License](https://img.shields.io/pypi/l/mkdocs-badges)](LICENSE.md)
![Python versions](https://img.shields.io/pypi/pyversions/mkdocs-badges)

## Documentation
Biblioteca desenvolvida pelo TJGO, Diretoria de Inteligência Artificial, Ciência de Dados e Estatística. Este pacote inclui o módulo de pré-processamento de texto e a classe Berna para cálculo de similaridade entre textos.

Esse repositório público contém algumas das ferramentas usadas internamente. Por enquanto, ele conta apenas com um módulo para pré-processamento de texto e um módulo secundário para cálculo de similaridade entre textos.

Esse repositório representa apenas uma parte do processo de padronização textual utilizado internamente e não contém nenhuma parte do código da BERNA.

## Github
https://github.com/TJGO-DIACDE/berna_tjgo_diacde_lib

## Instalação
Para instalar a biblioteca, use o comando abaixo:
```bash
pip install berna-tjgo-diacde-lib
```

## Dependências
Este projeto depende das seguintes bibliotecas:

- `pandas>=2.2.2`
- `spacy>=3.7.5`
- `nltk>=3.8.1`

# Módulo de Pré-Processamento
Módulo que conta com uma função principal que engloba e executa funções auxiliares.

## Importação
Para usar o módulo de pré-processamento, importe da seguinte maneira:
```python
from berna_tjgo_diacde_lib import preProcessamento as prep
```

### clear:
Método principal do módulo de pré-processamento que engloba e executa todas as funções. Recebe a string a ser processada e uma série de valores booleanos correspondentes às funções aplicadas durante o processamento.
```python
def clear(
    txt: str | list[str],
    preset: list[str] = [],
    no_ponctuation: bool = False,
    no_loose_letters: bool = False,
    no_multiple_spaces: bool = False,
    replace_synonym_by_dict: bool = False,
    no_html: bool = False,
    no_email: bool = False,
    no_numbers: bool = False,
    no_stopwords: bool = False,
    only_latin: bool = False,
    lemmatize: bool = False,
    stemming: bool = False
) -> str | list[str]:
```

### Argumento preset
O argumento preset permite configurar previamente um conjunto de métodos de pré-processamento de texto, evitando que o usuário precise especificá-los manualmente em cada chamada da função.

#### Como usar
Ao definir um preset, a função será configurada para sempre utilizar os métodos especificados, aplicando-os na ordem definida. Isso garante consistência no processamento sem a necessidade de repetir os argumentos a cada uso.

#### Exemplo de preset
```python
from berna_tjgo_diacde_lib import preProcessamento as prep

preset = ["no_ponctuation", "no_multiple_spaces", "only_latin"]
text = "Hello!!   This is an   example."

clean_text = prep.clear(text, preset)  
print(clean_text)  # Saída esperada: "Hello This is an example"
```
Os métodos são aplicados na sequência em que são passados no preset. Isso significa que a ordem irá impactar o resultado final.

#### Por exemplo:
```python
preset1 = ["tokenize", "stemming"]
preset2 = ["stemming", "tokenize"]
```
No primeiro caso, o texto será primeiro tokenizado (dividido em palavras) e depois passado pelo stemming (reduzido à raiz da palavra). No segundo caso, o stemming será aplicado antes da tokenização, o que pode alterar significativamente o resultado.

Ao definir um preset, certifique-se de que a ordem dos métodos faz sentido para o processamento desejado.

### Exemplo de Uso sem Presets:
```python
texto_limpo = prep.clear(
    "Seu texto aqui",
    no_punctuation=True,
    no_stopwords=True,
    lemmatize=True,
    replace_synonym_by_dict=True,
)
```

### Funções Isoladas:
Também é possível utilizar cada uma das funções separadamente pelos seguintes métodos:

#### `remove_email(txt: str) -> str`
Remove endereços de e-mail do texto.
```python
prep.remove_email("Essa é uma frase com email: exemplo@email.com")
```

#### `remove_html(txt: str) -> str`
Remove tags HTML do texto.
```python
prep.remove_html("<p>Texto com HTML</p>")
```

#### `remove_ponctuation(txt: str) -> str`
Remove pontuação do texto.
```python
prep.remove_ponctuation("Texto com pontuação!")
```

#### `remove_multiple_espaces(txt: str) -> str`
Remove espaços excessivos no texto.
```python
prep.remove_multiple_espaces("Texto   com   espaços  extras.")
```

#### `remove_loose_letters(txt: str) -> str`
Remove letras soltas no texto.
```python
prep.remove_loose_letters("E s s e  é  u m  t e x t o")
```

#### `set_only_latin(txt: str) -> str`
Mantém apenas caracteres do alfabeto latino.
```python
prep.set_only_latin("Texto com caracteres especiais: đ, ć, ł")
```

#### `remove_numbers(txt: str) -> str`
Remove números do texto.
```python
prep.remove_numbers("Texto com números 12345")
```

#### `remove_stopwords(txt: str) -> str`
Remove palavras de parada (stopwords) do texto.
```python
prep.remove_stopwords("Esse é um exemplo de um texto com stopwords.")
```

#### `lemmatize_txt(txt: str) -> str`
Aplica lematização ao texto.
```python
prep.lemmatize_txt("Os carros estão correndo.")
```

#### `stem_txt(txt: str) -> str`
Aplica stemming ao texto.
```python
prep.stem_txt("Correndo, correram, correria.")
```

#### `get_synonym_by_dict(txt: str) -> str`
Substitui certas palavras por sinônimos definidos em um dicionário pré-definido.
```python
prep.get_synonym_by_dict("Incluindo leis, resoluções, normas legais.")
```

# Módulo de Similaridade
Para utilizar a classe Berna de similaridade, importe a biblioteca da seguinte forma:
```python
import berna_tjgo_diacde_lib as brn
```

## Instanciação:
A classe Berna é definida com duas strings obrigatórias e um valor booleano opcional indicando a utilização do pré-processamento, considerado falso por padrão. Lança um Erro caso alguma das duas sentenças for falsa.
```python
calc1 = brn.Berna('Texto de exemplo 1', 'Texto de exemplo 2', True)
```

## Métodos
### Similaridade Jaccard:
Obtém o coeficiente de similaridade Jaccard, em porcentagem, entre as duas strings de entrada:
```python
similaridade_jaccard = calc1.get_similaridade_jaccard()     # Retorno: 50.0
```

### Similaridade por Cosseno:
Obtém o valor de similaridade por cosseno, em porcentagem, entre as duas strings de entrada:
```python
similaridade_cosseno = calc1.get_similaridade_cosseno()     # Retorno: 66.6667
```

### Transformação de texto para vetor:
Método estático para converter um texto em vetor. Pode ser usado diretamente ou pela instância da classe:
```python
vetor = brn.Berna.texto_para_vetor(None, "*Texto de Exemplo*", True)     # Retorno: ['texto', 'exemplo']
```

# Exemplos Práticos:
```python
# Import da classe Berna
import berna_tjgo_diacde_lib as brn

# Import do módulo de Pré-processamento
from berna_tjgo_diacde_lib import preProcessamento as prep

# Instância
berna = Berna('Eu sou o primeiro texto de Antonio Pires', 'Eu sou o segundo texto de antonio pires', True)

# Teste init
print(f'\nFrase 1: {berna.vec_terms1}')
print(f'Frase 2: {berna.vec_terms2}')
print(f'Preprocessamento: {berna.pre_process}')

# Teste cálculos Similaridades 
print('\nCálculo de Similaridade')
print(f'Jaccard: {berna.get_similaridade_jaccard()}')
print(f'Cosseno: {berna.get_similaridade_cosseno()}')
# Resultados esperados:
# se Preprocess True: 60.0 e 75.0
# se Preprocess False: 45.4545 e 62.5

# Teste métodos módulo Pré Processamento
print('\nFrase sem pontuações: ', prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))
print('Frase com sinonimos filtrados e lematização: ', prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", lemmatize=True, only_latin=True))
print('Frase com sinonimos filtrados por dicionário e stemming: ', prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", stemming=True, replace_synonym_by_dict=True))
```

## Saída Esperada:
```
Frase 1: ['prim', 'text', 'antoni', 'pir']
Frase 2: ['segund', 'text', 'antoni', 'pir']
Preprocessamento: True

Cálculo de Similaridade
Jaccard: 60.0
Cosseno: 75.0

Frase sem pontuações: eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.
Frase com sinonimos filtrados e lematização: eu ser o primeiro texto de antonio pires , incluir lei , lei , lei legal .
Frase com sinonimos filtrados por dicionário e stemming: eu sou o prim text de antoni pires, inclu leis, leis, lei legais.

Utilizando text_para_vetor estaticamente: ['prim', 'text', 'antoni', 'pir', 'inclu', 'lei', 'lel', 'lel', 'legal']
```

# Licença
Este projeto está licenciado sob a Licença Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). 

Domingo, 21 de Julho de 2024, às 09:54:07

### Você pode:
- Compartilhar — copiar e redistribuir o material em qualquer formato ou mídia.
- Adaptar — remixar, transformar e construir sobre o material.

### Sob as seguintes condições:
- Atribuição — Você deve dar o crédito apropriado, prover um link para a licença, e indicar se mudanças foram feitas. Você pode fazê-lo de qualquer forma razoável, mas não de forma que sugira que o licenciador endossa você ou seu uso.
- Não Comercial — Você não pode usar o material para fins comerciais.
- Compartilhar Igual — Se você remixar, transformar ou criar a partir do material, deve distribuir suas contribuições sob a mesma licença que o original.

Para mais detalhes, consulte o texto completo da licença no arquivo [LICENSE](./LICENSE.md) ou visite [CC BY-NC-SA 4.0 Legal Code](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

# Créditos
A biblioteca Berna TJGO DIACDE foi desenvolvida pelo Tribunal de Justiça do Estado de Goiás, pela [Diretoria de Inteligência Artificial, Ciência de Dados e Estatística](https://github.com/TJGO-DIACDE) - <TJGOdiacde@tjgo.jus.br>.

# Desenvolvedores:
[Antônio Pires](https://github.com/apcastrojr) - <apcastro@tjgo.jus.br> <br>
[Milton Ávila](https://github.com/Milton-Avila) - <milton.estudantil@gmail.com> <br>
[João Gabriel](https://github.com/joaograndotto) - <grandottojoao@gmail.com> <br>
[Wesley Oliveira](https://github.com/waejl) - <wesley@woliveira.me>
