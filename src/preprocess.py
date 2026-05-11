"""
Created on Sun Jul 21 09:54:07 2024

@authors:
    Antonio Pires
    Milton Ávila
    João Gabriel
    Wesley Oliveira

@license:
Este projeto está licenciado sob a Licença Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Você pode compartilhar, adaptar e construir sobre o material, desde que atribua crédito apropriado, não use o material para fins comerciais e distribua suas contribuições sob a mesma licença.
Para mais informações, consulte o arquivo [LICENSE](./LICENSE).
"""
from typing import Self

from . import TextUtils, PROCESS_METHODS

# Linked Methods, Static
class ProcessLinked:
    def __init__(self, txt: str) -> Self:
        if not isinstance(txt, str):
            raise TypeError("Input must be a string")

        self.txt = txt

    def filter_special_characters(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_special_characters(self.txt, change_for)
        return self

    def filter_spaces(self, change_for = " ") -> Self:
        self.txt = TextUtils.filter_spaces(self.txt, change_for)
        return self

    def filter_numbers(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_numbers(self.txt, change_for)
        return self

    def filter_links(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_links(self.txt, change_for)
        return self

    def filter_email(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_email(self.txt, change_for)
        return self

    def filter_cnpj(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_cnpj(self.txt, change_for)
        return self

    def filter_cpf(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_cpf(self.txt, change_for)
        return self

    def filter_rg(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_rg(self.txt, change_for)
        return self

    def filter_cep(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_cep(self.txt, change_for)
        return self

    def filter_oab(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_oab(self.txt, change_for)
        return self

    def filter_telefone(self, change_for = "") -> Self:
        self.txt = TextUtils.filter_telefone(self.txt, change_for)
        return self

    def remove_stopwords(self, language = "portuguese") -> Self:
        self.txt = TextUtils.remove_stopwords(self.txt, language)
        return self

    def remove_html(self) -> Self:
        self.txt = TextUtils.remove_html(self.txt)
        return self

    def lemmatize(self, core = "pt_core_news_sm") -> Self:
        self.txt = TextUtils.lemmatize(self.txt, core)
        return self

    def stemming(self) -> Self:
        self.txt = TextUtils.stemming(self.txt)
        return self

    # Utils
    def as_str(self) -> str:
        return self.txt

    def __str__(self) -> str:
        return self.txt

# Pipeline Class
class ProcessPipeline:
    def __init__(self, pipeline: list[dict[str, str|dict]]) -> Self:
        self.pipeline = pipeline

    def process(self, txt: str) -> str:
        if not isinstance(txt, str):
            raise TypeError("Input must be a string")

        for proc in self.pipeline:
            if (proc_name := proc["name"]) not in PROCESS_METHODS:
                raise Exception(f"{proc_name} does not exist as a preprocessing method.")

        for proc in self.pipeline:
            if proc_meth := getattr(TextUtils, proc.get("name"), None):
                proc.pop("name")
                txt = proc_meth(txt, **proc)
            else:
                raise Exception("Bad pipeline format.")

        return txt