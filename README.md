# Berna TJGO DIACDE lib

Biblioteca da Berna desenvolvida pelo TJGO, Diretoria de Inteligência Artificial, Ciência de Dados e Estatística. <br>
Pacote referente a classe Berna para cálculo de similaridade entre textos e um Módulo de Pré-processamento de texto.

Para a instalação, utilize o comando:
```bash
pip install berna-tjgo-diacde-lib
```

## Classe Berna
Para o uso, apenas importe a biblioteca da seguinte forma:
```python
import berna_tjgo_diacde_lib as brn
```

* Instância:
A classe é definida com duas strings obrigatórias e um valor booleano opcional indicando a utilização do pré-processamento, é considerado falso por padrão caso omitido.
```python
calc1 = brn.Berna('Teste de string similaridade 1', 'teste de texto similaridade 2', True)
```

* Método de Similaridade Jaccard: 
obtém o coeficiente de similaridade Jaccard relativo às duas strings de entrada utilizando o método:
```python
calc1.get_similaridade_jaccard()        # retornaria 50.0
```

* Método de Similaridade por Cosseno: 
também é possivel obter o valor de similaridade por Cosseno utilizando o método:
```python
calc1.get_similaridade_cosseno()        # retornaria 66.6667
```

* Transformação de texto para vetor: 
é usado pela própria classe ao instânciar um objeto, porém tambem pode ser utilizado de maneira estática. Ele recebe como parâmetros, um valor vazio, o texto a ser separado e um valor booleano opcional de acordo com a necessidade de pré-processamento. utilize a seguinte estrutura:
```python
brn.Berna.texto_para_vetor(None, "*Texto de Exemplo*", True)    # retornaria ['texto', 'exemplo']
```

## Pré-Processamento
Modulo que conta com três funções de pré-processamento.

Para o uso, importe o módulo dessa forma:
```python
from berna_tjgo_diacde_lib import Prep
```

* clear: 
remove todos os caracteres que não sejam alfanuméricos ou espaços. Também remove algumas palavras relacionadas a html e css, como 'span', 'style', '70px', entre outras. Utilize da seguinte forma:
```python
Prep.clear('*Texto de Exemplo*')                                # Retornaria 'texto de exemplo'
```

* get_synonym: 
substitui certas palavras do meio jurídico por suas contrapartes.
Por exemplo: 'norma', 'decreto' e 'resolucao' são substituidas pela palavra 'lei'. Utilize da seguinte forma
```python
Prep.get_synonym('*Texto de Exemplo contendo leis e normas*')   # Retornaria '*texto de exemplo contendo lei e lei*'
```

* get_synonym_by_dict:
semelhante ao método anterior, substitúi certas palavras do meio jurídico por termos padronizados, mas dessa vez utilizando outro método de substituição e um grande dicionário que inclui mais termos e termos em latin. Utilize da seguinte forma:
```python
Prep.get_synonym_by_dict('*Texto de Exemplo contendo leis e normas*') # Retornaria '*texto de exemplo contendo leis e Leis*'
```

# Exemplos Práticos:

```python
# Import da classe Berna
import berna_tjgo_diacde_lib as brn
# Import do módulo de Pré-processamento
from berna_tjgo_diacde_lib import Prep as prep

# Instância
calc1 = brn.Berna('Eu sou o primeiro texto de Antonio Pires', 'Eu sou o segundo texto de antonio pires', False)

# Teste valores de entrada
print(f'\nFrase 1: {calc1.vec_terms1}')
print(f'Frase 2: {calc1.vec_terms2}')
print(f'Preprocessamento: {calc1.pre_process}')

# Teste cálculos Similaridades 
print('\nCálculo de Similaridade')
print(f'Jaccard: {calc1.get_similaridade_jaccard()}')
print(f'Cosseno: {calc1.get_similaridade_cosseno()}')
# Resultados esperados:
# se Preprocess True: 66.6667 e 80.0
# se Preprocess False: 45.4545 e 62.5

# Teste métodos módulo Pré Processamento
print('\nFrase sem pontuações: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))
print('Frase com sinonimos filtrados: ' + prep.get_synonym("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))
print('Frase com sinonimos filtrados por dicionário: ' + prep.get_synonym_by_dict("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))

# Teste método estático
print(f'\nUtilizando text_para_vetor estaticamente: {brn.Berna.texto_para_vetor(None, "Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.")}\n')
```

## Out:
```
Frase 1: ['sou', 'primeiro', 'texto', 'antonio', 'pires']
Frase 2: ['sou', 'segundo', 'texto', 'antonio', 'pires']
Preprocessamento: True

Cálculo de Similaridade
Jaccard: 66.6667
Cosseno: 80.0

Frase sem pontuações: sou primeiro texto antonio pires incluindo leis resoluções normas legais
Frase com sinonimos filtrados: eu sou o primeiro texto de antonio pires, incluindo lei, lei, lei legais.
Frase com sinonimos filtrados por dicionário: eu sou o primeiro texto de antonio pires, incluindo leis, Leis, Leis legais.

Utilizando text_para_vetor estaticamente: ['sou', 'primeiro', 'texto', 'antonio', 'pires', 'incluindo', 'lei', 'lei', 'legais']
```
