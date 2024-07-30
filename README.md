# Berna TJGO DIACDE Lib

Biblioteca desenvolvida pelo TJGO, Diretoria de Inteligência Artificial, Ciência de Dados e Estatística. Este pacote inclui a classe Berna para cálculo de similaridade entre textos e um módulo de pré-processamento de texto.

## Instalação

Para instalar a biblioteca, use o comando abaixo (ainda não publicada):
```bash
pip install berna-tjgo-diacde-lib
```

# Classe Berna
Para utilizar a classe, importe a biblioteca da seguinte forma:
```python
import berna_tjgo_diacde_lib as brn
```

## Instanciação:
A classe Berna é definida com duas strings obrigatórias e um valor booleano opcional indicando a utilização do pré-processamento, considerado falso por padrão.
```python
calc1 = brn.Berna('Texto de exemplo 1', 'Texto de exemplo 2', True)
```

## Métodos
### Similaridade Jaccard: 
Obtém o coeficiente de similaridade Jaccard entre as duas strings de entrada:
```python
similaridade_jaccard = calc1.get_similaridade_jaccard()  # Retorno: 50.0
```

### Similaridade por Cosseno: 
Obtém o valor de similaridade por cosseno entre as duas strings de entrada:
```python
similaridade_cosseno = calc1.get_similaridade_cosseno()  # Retorno: 66.6667
```

### Transformação de texto para vetor: 
Método estático para converter um texto em vetor. Pode ser usado diretamente ou pela instância da classe:
```python
vetor = brn.Berna.texto_para_vetor(None, "*Texto de Exemplo*", True)  # Retorno: ['texto', 'exemplo']
```

## Módulo de Pré-Processamento
Modulo que conta com uma função principal que engloba e executa funções.

### Importação
Para usar o módulo de pré-processamento, importe da seguinte maneira:
```python
from berna_tjgo_diacde_lib import Prep as prep
```

### clear: 
Método principal do módulo de pré-processamento que engloba e executa todas as funções. Recebe a string a ser processada e uma série de valores booleanos correspondentes às funções aplicadas durante o processamento.
```python
def clear(
    txt: str,
    no_punctuation: bool = False,  # Remove caracteres não-alfanuméricos
    no_css: bool = False,          # Remove palavras relacionadas a HTML e CSS
    no_stopwords: bool = False,    # Remove stopwords
    lemmatize: bool = False,       # Aplica lematização à string
    replace_synonym: bool = False, # Aplica o método get_synonym
    replace_synonym_by_dict: bool = False # Aplica o método get_synonym_by_dict
) -> str:
```

### Exemplo de uso:
```python
texto_limpo = prep.clear(
    "Seu texto aqui",
    no_punctuation=True,
    no_css=True,
    no_stopwords=True,
    lemmatize=True,
    replace_synonym=True,
    replace_synonym_by_dict=False
)
```

### get_synonym: 
Substitui certas palavras do meio jurídico por suas contrapartes. Por exemplo: 'norma', 'decreto' e 'resolução' são substituídas pela palavra 'lei':
```python
prep.get_synonym('*Texto de Exemplo contendo leis e normas*')           # Retornaria '*Texto de Exemplo contendo lei e lei*'
```

### get_synonym_by_dict:
Semelhante ao método anterior, substitui certas palavras do meio jurídico por termos padronizados, mas desta vez utilizando um grande dicionário que inclui mais termos e termos em latim:
```python
prep.get_synonym_by_dict('*Texto de Exemplo contendo leis e normas*')   # Retornaria '*Texto de Exemplo contendo leis e Leis*'
```

# Exemplos Práticos:
```python
# Import da classe Berna
import berna_tjgo_diacde_lib as brn

# Import do módulo de Pré-processamento
from berna_tjgo_diacde_lib import Prep as prep

# Instância
berna = brn.Berna('Eu sou o primeiro texto de Antonio Pires', 'Eu sou o segundo texto de antonio pires', True)

# Teste init
print(f'\nFrase 1: {berna.vec_terms1}')
print(f'Frase 2: {berna.vec_terms2}')
print(f'Preprocessamento: {berna.pre_process}')

# Teste cálculos Similaridades 
print('\nCálculo de Similaridade')
print(f'Jaccard: {berna.get_similaridade_jaccard()}')
print(f'Cosseno: {berna.get_similaridade_cosseno()}')
# Resultados esperados:
# se Preprocess True: 77.7778 e 87.5
# se Preprocess False: 45.4545 e 62.5

# Teste métodos módulo Pré Processamento
print('\nFrase sem pontuações: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))
print('Frase com sinonimos filtrados e sem pontuações: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", replace_synonym=True))
print('Frase com sinonimos filtrados por dicionário: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", False, replace_synonym_by_dict=True))

# Teste método estático
print(f'\nUtilizando text_para_vetor estaticamente: {brn.Berna.texto_para_vetor(None, "Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", True)}\n')
```

## Saída Esperada:
```
Frase 1: ['eu', 'ser', 'o', 'primeiro', 'texto', 'de', 'antonio', 'pir']
Frase 2: ['eu', 'ser', 'o', 'segundo', 'texto', 'de', 'antonio', 'pir']
Preprocessamento: True

Cálculo de Similaridade
Jaccard: 77.7778
Cosseno: 87.5

Frase sem pontuações: eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.
Frase com sinonimos filtrados: eu sou o primeiro texto de antonio pires, incluindo lei, lei, lei legais.
Frase com sinonimos filtrados por dicionário: eu sou o primeiro texto de antonio pires, incluindo leis, leis, leis legais.

Utilizando text_para_vetor estaticamente: ['eu', 'ser', 'o', 'primeiro', 'texto', 'de', 'antonio', 'pires', 'incluir', 'lei', 'lei', 'legal']
```

# Licença

Este projeto está licenciado sob a Licença Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). 

Você pode:
- Compartilhar — copiar e redistribuir o material em qualquer formato ou mídia
- Adaptar — remixar, transformar e construir sobre o material

Sob as seguintes condições:
- Atribuição — Você deve dar o crédito apropriado, prover um link para a licença, e indicar se mudanças foram feitas. Você pode fazê-lo de qualquer forma razoável, mas não de forma que sugira que o licenciador endossa você ou seu uso.
- Não Comercial — Você não pode usar o material para fins comerciais.
- Compartilhar Igual — Se você remixar, transformar ou criar a partir do material, deve distribuir suas contribuições sob a mesma licença que o original.

Para mais detalhes, consulte o texto completo da licença no arquivo [LICENSE](./LICENSE) ou visite [CC BY-NC-SA 4.0 Legal Code](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

# Créditos
A biblioteca Berna TJGO DIACDE foi desenvolvida pelo Tribunal de Justiça do Estado de Goiás, pela [Diretoria de Inteligência Artificial, Ciência de Dados e Estatística](https://github.com/TJGO-DIACDE) - <TJGOdiacde@tjgo.jus.br>.

## Desenvolvedor:
[Milton Ávila](https://github.com/Milton-Avila) - <milton.estudantil@gmail.com>.
