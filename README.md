# Berna TJGO DIACDE lib

Biblioteca da Berna desenvolvida pelo TJGO, Diretoria de Inteligência Artificial, Ciência de Dados e Estatística.

## Classe Berna
A classe é definida com duas strings obrigatórias e um operador booleano opcional indicando a utilização do pré-processamento declarado falso de forma padrão.

Para o uso, apenas importe a biblioteca da seguinte forma:
```python
from berna_tjgo_diacde_lib import Berna
```

* Método de Similaridade Jaccard: 
obtém o coeficiente de similaridade Jaccard relativo às duas strings de entrada utilizando o método:
```python
get_similaridade_jaccard()
```

* Método de Similaridade por Cosseno: 
também é possivel obter o valor de similaridade por Cosseno utilizando o método:
```python
get_similaridade_cosseno()
```

* Transformação de texto para vetor: 
é usado pela própria classe ao instânciar um objeto, porém tambem pode ser utilizado de maneira estática utilizando a seguinte estrutura:
```python
Berna.texto_para_vetor(None, "*Texto de Exemplo*")
```

## Pré-Processamento
Modulo que conta com duas funções de pré-processamento.

Para o uso, importe o módulo dessa forma:
```python
from berna_tjgo_diacde_lib import Prep
```

* clear: 
remove todos os caracteres que não sejam alfanuméricos ou espaços. Também remove algumas palavras relacionadas a html e css, como 'span', 'style', '70px', entre outras. Utilize da seguinte forma:
```python
Prep.clear('*Texto de Exemplo*')
```

* get_synonym: 
substitui certas palavras do meio jurídico por suas contrapartes.
Por exemplo: 'norma', 'decreto' e 'resolucao' são substituidas pela palavra 'lei'. Utilize da seguinte forma
```python
Prep.get_synonym('*Texto de Exemplo*')
```

# Exemplos Práticos:

```python
# Import da classe Berna
from berna_tjgo_diacde_lib import Berna
# Import do módulo de Pré-processamento
from berna_tjgo_diacde_lib import Prep as prep

# Instância
berna = Berna('Eu sou o primeiro texto de Antonio Pires', 'Eu sou o segundo texto de antonio pires', False)

# Teste valores de entrada
print(f'\nFrase 1: {berna.vec_terms1}')
print(f'Frase 2: {berna.vec_terms2}')
print(f'Preprocessamento: {berna.pre_process}')

# Teste cálculos Similaridades 
print('\nCálculo de Similaridade')
print(f'Jaccard: {berna.get_similaridade_jaccard()}')
print(f'Cosseno: {berna.get_similaridade_cosseno()}')
# Resultados esperados:
# se Preprocess True: 66.6_ e 80.0
# se Preprocess False: 45.45_ e 62.5

# Teste métodos módulo Pré Processamento
print('\nFrase sem pontuações: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))
print('Frase com sinonimos filtrados: ' + prep.get_synonym("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))

# Teste método estático
print(f'\nUtilizando text_para_vetor estaticamente: {Berna.texto_para_vetor(None, "Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.")}\n')
```

## Out:
```
Frase 1: ['Eu', 'sou', 'o', 'primeiro', 'texto', 'de', 'Antonio', 'Pires']
Frase 2: ['Eu', 'sou', 'o', 'segundo', 'texto', 'de', 'antonio', 'pires']
Preprocessamento: False

Cálculo de Similaridade
Jaccard: 45.4545
Cosseno: 62.5

Frase sem pontuações: eu sou o primeiro texto de antonio pires incluindo leis resoluções normas legais
Frase com sinonimos filtrados: eu sou o primeiro texto de antonio pires, incluindo lei, lei, lei legais.

Utilizando text_para_vetor estaticamente: ['Eu', 'sou', 'o', 'primeiro', 'texto', 'de', 'antonio', 'pires,', 'incluindo', 'leis,', 'resoluções,', 'normas', 'legais.']
```
