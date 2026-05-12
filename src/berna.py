'''
Created on Sun Jul 21 09:54:07 2024

@authors:
    Antonio Pires
    Milton Ávila
    João Gabriel
    Wesley Oliveira

@license:
Este projeto está licenciado sob a Licença Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Você pode compartilhar, adaptar e construir sobre o material, desde que atribua crédito apropriado, não use o material para fins comerciais e distribua suas contribuições sob a mesma licença.
Para mais informações, consulte o arquivo [LICENSE](./LICENSE).
'''
from nltk.cluster.util import cosine_distance
import nltk

from .preprocess import TextUtils

class Berna:
    def __init__(self, doc1: str, doc2: str) -> None:
        if not isinstance(doc1, str) or not isinstance(doc2, str):
            raise ValueError("Ambas as sentenças devem ser strings válidas.")
        if len(doc1) == 0 or len(doc2) == 0:
            raise ValueError("Erro! As sentenças não podem ser vazias.")

        nltk.download('punkt')

        self.vec_terms1 = TextUtils.tokenize(doc1)
        self.vec_terms2 = TextUtils.tokenize(doc2)
        vec_terms_tuple = (self.vec_terms1, self.vec_terms2)

        self.sim_cosseno = self.calcula_similaridade_cosseno(*vec_terms_tuple)
        self.sim_jaccard = self.calcula_similaridade_jaccard(*vec_terms_tuple)

    @staticmethod
    def calcula_similaridade_jaccard(vec_terms1: list[str], vec_terms2: list[str]) -> None:
        union_terms =           len(vec_terms1 | vec_terms2)
        intersection_terms =    len(vec_terms1 & vec_terms2)

        return round( (intersection_terms / union_terms) * 100, 4 )

    @staticmethod
    def calcula_similaridade_cosseno(vec_terms1: list[str], vec_terms2: list[str]) -> None:
        union_terms = list(vec_terms1 | vec_terms2)
        l1 = [0] * len(union_terms)
        l2 = [0] * len(union_terms)

        for w in vec_terms1:
            l1[union_terms.index(w)] += 1
        for w in vec_terms2:
            l2[union_terms.index(w)] += 1

        return round( (1 - cosine_distance(l1, l2)) * 100, 4 )
