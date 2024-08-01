'''
Created on Sun Jul 21 09:54:07 2024

@authors:
    Antonio Pires
    Milton Ávila
    Wesley Oliveira

@license:
Este projeto está licenciado sob a Licença Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Você pode compartilhar, adaptar e construir sobre o material, desde que atribua crédito apropriado, não use o material para fins comerciais e distribua suas contribuições sob a mesma licença.
Para mais informações, consulte o arquivo [LICENSE](./LICENSE).
'''


# Re
import re

# Pandas
import pandas as pd

# Setup tools
import pkg_resources

# NLTK
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

# NLTK
nltk.download('stopwords', quiet=True)
nltk.download('rslp', quiet=True)
stop_words = set(stopwords.words('portuguese'))
nlp = spacy.load('pt_core_news_sm')

def clear(
    txt: str,
    no_ponctuation: bool = False,
    no_stopwords: bool = False,
    no_html: bool = False,
    lemmatize: bool = False,
    stemming: bool = False,
    replace_synonym: bool = False,
    replace_synonym_by_dict: bool = False
) -> str:
    
    txt = txt.lower()
    
    if no_html:
        txt = remove_html(txt)

    if no_ponctuation:
        txt = remove_ponctuation(txt)

    if replace_synonym:
        txt = get_synonym(txt)
    elif replace_synonym_by_dict:
        txt = get_synonym_by_dict(txt)

    if no_stopwords:
        txt = remove_stopwords(txt)

    if lemmatize:
        txt = lemmatize_txt(txt)

    if stemming:
        txt = stem_txt(txt)

    return txt

def tokenize(txt: str) -> list:
    tokens = [w for w in nltk.word_tokenize(' '.join(txt))]
    
    return set(tokens)

def remove_ponctuation(txt: str) -> str:
    txt = ''.join([l for l in txt if l.isalnum() or l==' '])

    return txt

def remove_stopwords(txt: str) -> str:
    tokens = txt.split()
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

def lemmatize_txt(txt: str) -> str:
    doc = nlp(txt)
    txt = ' '.join([token.lemma_.lower() for token in doc])

    return txt

def stem_txt(txt: str) -> str:
    stemmer = RSLPStemmer()

    tokens = txt.split()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(stemmed_tokens)

def remove_html(txt: str) -> str:
    # Remove HTML
    txt = re.sub(r'<style.?>.?</style>', '', txt, flags=re.DOTALL)
    # Remove JavaScript
    txt = re.sub(r'<script.?>.?</script>', '', txt, flags=re.DOTALL)
    # Remove links
    txt = re.sub(r'<a.?>.?</a>', '', txt, flags=re.DOTALL)
    # Remove HTML tags
    txt = re.sub(r'<.*?>', '', txt)
    # Remove HTML entities
    txt = re.sub(r'&\w+;', '', txt)

    txt = txt.lower().replace('style@page','').replace('style','').replace('px','').replace('\"span ','').replace('p&ampnbsp','').replace(' p ','').replace('\"lineheight"','').replace('textindent','').replace('justify','').replace('150%','').replace(' /p ','').replace('100px','').replace('\"fontsize','').replace('marginleft','').replace('70px','').replace('&ampnbsp','').replace('\"fontfamily','').replace('80px','').replace('30px','').replace('100%','').replace('marginright','').replace(' margin ','').replace('\"textalign','').replace('\"fontfamily','').replace('','').replace(' times ','').replace(' br ','').replace(' span ','').replace('lineheight','').replace('fontsize','').replace('fontfamily','').replace('textalign','').replace(' p ','').replace('2016p','').replace('3cm','').replace('4cm','').replace('p&ampnbsp','').replace(' new ','').replace('romanspan','').replace('&ampnbsp','')

    return txt

def get_synonym(txt: str) -> str:
    # synonym of law
    txt = txt.replace('leis','lei')
    txt = txt.replace('complementares','complementar')
    txt = txt.replace('estaduais','estadual')
    txt = txt.replace('federais','federal')
    txt = txt.replace('portarias','portaria')
    txt = txt.replace('decretos','decreto')
    txt = txt.replace('resoluções','resolucao')
    txt = txt.replace('resolucoes','resolucao')
    txt = txt.replace('resolução','resolucao')
    txt = txt.replace('normas','norma')
    txt = txt.replace('ec.','lei')
    txt = txt.replace('ec','lei')
    txt = txt.replace('lei complementar','lei')
    txt = txt.replace('lei estadual','lei')
    txt = txt.replace('lei federal','lei')
    txt = txt.replace('norma','lei')
    txt = txt.replace('lei nº','lei')
    txt = txt.replace('lei n','lei')
    txt = txt.replace('lei n.','lei')
    txt = txt.replace('atos normativos','lei')
    txt = txt.replace('emenda constitucional','lei')
    txt = txt.replace('ato normativo','lei')
    txt = txt.replace('alterada pela','lei')
    txt = txt.replace('decreto-lei','lei')
    txt = txt.replace('decreto','lei')
    txt = txt.replace('resolucao','lei')
    txt = txt.replace('portaria','lei')
    txt = txt.replace('lei lei','lei')
    txt = txt.replace('adi',' lei')

    return txt

def get_synonym_by_dict(txt: str) -> str:
    table_dict = _read_binary()

    for _, row in table_dict.iterrows():

        for token in str(row['DE_PARA']).split(','):
            token = token.lower()

            if token in txt:
                txt = txt.replace(token, row['PALAVRA'].strip(', ').lower())

    return txt


def _read_binary() -> object:
    file_local = pkg_resources.resource_filename(__name__, 'data/data.pkl')
    df_carregado = pd.read_pickle(file_local)

    return df_carregado


if __name__=='__main__':
    # Teste func 1
    print(clear('<span>Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.</span>', no_html=True, replace_synonym_by_dict=True))

    # Teste func 2
    print(lemmatize_txt('Esse é um exemplo de um texto lematizado, com palavras reduzidas a sua raíz.'))

    # Teste func 3
    print(stem_txt('Esse é um exemplo de um texto lematizado, com palavras reduzidas a sua raíz.'))

    # Teste func 4
    print(remove_ponctuation('Esse é um teste! e não devem haver pontuações nessa frase...'))
    
    # Teste func 5
    print(remove_html('<script>Essa é uma frase sem palavras de css, </script>'))
    
    # Teste func 6
    print(remove_stopwords('Esse é um exemplo de um texto sem stopwors, sem palavras de conjunção.'))

    # Teste func 7
    print(get_synonym('Método de sinonimos: Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.'))

    # Teste func 8
    print(get_synonym_by_dict('Método de sinonimos por dicionário: Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.'))