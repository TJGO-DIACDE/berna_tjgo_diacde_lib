"""
Created on Sun Jul 21 09:54:07 2024

@authors:
    Antonio Pires
    Milton Ávila
    Wesley Oliveira

@license:
Este projeto está licenciado sob a Licença Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Você pode compartilhar, adaptar e construir sobre o material, desde que atribua crédito apropriado, não use o material para fins comerciais e distribua suas contribuições sob a mesma licença.
Para mais informações, consulte o arquivo [LICENSE](./LICENSE).
"""
import re
import regex
import pandas as pd
# Setup tools
import pkg_resources
# NLTK
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

# NLTK start
nltk.download("stopwords", quiet=True)
nltk.download("rslp", quiet=True)
stop_words = set(stopwords.words("portuguese"))
nlp = spacy.load("pt_core_news_sm")

def remove_html(txt: str) -> str:
    # Remove HTML
    txt = re.sub(r"<style.?>.?</style>", "", txt, flags=re.DOTALL)
    # Remove JavaScript
    txt = re.sub(r"<script.?>.?</script>", "", txt, flags=re.DOTALL)
    # Remove links
    txt = re.sub(r"<a.?>.?</a>", "", txt, flags=re.DOTALL)
    # Remove HTML tags
    txt = re.sub(r"<.*?>", "", txt)
    # Remove HTML entities
    txt = re.sub(r"&\w+;", "", txt)

    return txt.lower().replace("style@page","").replace("style","").replace("px","").replace("\"span ","").replace("p&ampnbsp","").replace(" p ","").replace('\"lineheight"',"").replace("textindent","").replace("justify","").replace("150%","").replace(" /p ","").replace("100px","").replace("\"fontsize","").replace("marginleft","").replace("70px","").replace("&ampnbsp","").replace("\"fontfamily","").replace("80px","").replace("30px","").replace("100%","").replace("marginright","").replace(" margin ","").replace("\"textalign","").replace("\"fontfamily","").replace("","").replace(" times ","").replace(" br ","").replace(" span ","").replace("lineheight","").replace("fontsize","").replace("fontfamily","").replace("textalign","").replace(" p ","").replace("2016p","").replace("3cm","").replace("4cm","").replace("p&ampnbsp","").replace(" new ","").replace("romanspan","").replace("&ampnbsp","")

## Discarted ##
# def get_synonym(txt: str) -> str:
#     # synonym of law
#     return txt.replace("leis","lei").replace("complementares","complementar").replace("estaduais","estadual").replace("federais","federal").replace("portarias","portaria").replace("decretos","decreto").replace("resoluções","resolucao").replace("resolucoes","resolucao").replace("resolução","resolucao").replace("normas","norma").replace("ec.","lei").replace("ec","lei").replace("lei complementar","lei").replace("lei estadual","lei").replace("lei federal","lei").replace("norma","lei").replace("lei nº","lei").replace("lei n","lei").replace("lei n.","lei").replace("atos normativos","lei").replace("emenda constitucional","lei").replace("ato normativo","lei").replace("alterada pela","lei").replace("decreto-lei","lei").replace("decreto","lei").replace("resolucao","lei").replace("portaria","lei").replace("lei lei","lei").replace("adi"," lei")

def get_synonym_by_dict(txt: str) -> str:
    table_dict = _read_binary()

    for _, row in table_dict.iterrows():

        for token in str(row["DE_PARA"]).split(","):
            token = token.lower()

            if token in txt:
                txt = txt.replace(token, row["PALAVRA"].strip(", ").lower())

    return txt
# ##

def remove_ponctuation(txt: str) -> str:
    return re.sub(r"[^\w\s]", "", txt)

def remove_stopwords(txt: str) -> str:
    tokens = txt.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def lemmatize_txt(txt: str) -> str:
    return " ".join([token.lemma_.lower() for token in nlp(txt)])

def stem_txt(txt: str) -> str:
    stemmer = RSLPStemmer()

    tokens = txt.split()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return " ".join(stemmed_tokens)

def tokenize(txt: str) -> list:
    return set([w for w in nltk.word_tokenize(" ".join(txt))])

def set_only_latin(txt: str) -> str:
    return regex.sub(r"[^\p{IsLatin}\s\d\p{P}]", "", txt)

def remove_numbers(txt: str) -> str:
    return re.sub(r"\d", "", txt)

def remove_multiple_espaces(txt: str) -> str:
    return re.sub(r"\s+", " ", txt).strip()

def remove_loose_letters(txt: str) -> str:
    return re.sub(r"\b(?:[a-zA-Z] ){2,}[a-zA-Z]\b", "", txt)

def remove_email(txt: str) -> str:
    regex_emails_urls = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|https?://\S+|www\.\S+"
    return re.sub(regex_emails_urls, "", txt).strip()

def _read_binary() -> object:
    file_local = pkg_resources.resource_filename(__name__, "data/sinonimos.pkl")
    df_carregado = pd.read_pickle(file_local)

    return df_carregado