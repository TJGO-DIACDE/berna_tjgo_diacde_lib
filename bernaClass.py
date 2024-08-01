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


# Módulo Integrado
import preProcessamento as prep         # Retire o ponto para rodar localmente

# NLTK
from nltk.cluster.util import cosine_distance

class Berna:
    def __init__(self, doc1: str, doc2: str, pre_process: bool = False) -> None:
        if len(doc1) == 0 or len(doc2) == 0:
            raise ValueError("Erro! As sentenças não podem ser vazias.") 

        self.pre_process = pre_process
        self.vec_terms1 = self.texto_para_vetor(doc1)
        self.vec_terms2 = self.texto_para_vetor(doc2)

        self.calcula_similaridade_cosseno()
        self.calcula_similaridade_jaccard()

    def get_similaridade_jaccard(self) -> float | None:
        return self.similaridade_jaccard

    def get_similaridade_cosseno(self) -> float:
        return self.similaridade_cosseno

    def calcula_similaridade_jaccard(self) -> None:
        words1 = prep.tokenize(self.vec_terms1)
        words2 = prep.tokenize(self.vec_terms2)
        
        union_terms =           len(words1 | words2)
        intersection_terms =    len(words1 & words2)
        
        self.similaridade_jaccard = round( (intersection_terms / union_terms) * 100, 4 )

    def calcula_similaridade_cosseno(self) -> None:
        words1 = prep.tokenize(self.vec_terms1)
        words2 = prep.tokenize(self.vec_terms2)

        union_terms = list(words1 | words2)
        l1 = [0] * len(union_terms)
        l2 = [0] * len(union_terms)

        for w in words1:
            l1[union_terms.index(w)] += 1
        for w in words2:
            l2[union_terms.index(w)] += 1

        self.similaridade_cosseno = round( (1 - cosine_distance(l1, l2)) * 100, 4 )

    def texto_para_vetor(self, txt: str, pre_process: bool = False) -> list:
        if self != None:
            pre_process = self.pre_process

        if pre_process:
            txt = prep.clear(
                txt, 
                no_ponctuation=True, 
                stemming=True, 
                lemmatize=True,
                no_stopwords=True,
                replace_synonym_by_dict=True
            )

        vetor = [w for w in txt.split()]

        return ' '.join(vetor).split()


def teste() -> None:
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
    # se Preprocess True: 77.7778 e 87.5
    # se Preprocess False: 45.4545 e 62.5

    # Teste métodos módulo Pré Processamento
    print('\nFrase sem pontuações: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))
    print('Frase com sinonimos filtrados: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", replace_synonym=True))
    print('Frase com sinonimos filtrados por dicionário: ' + prep.clear("Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", replace_synonym_by_dict=True))

    # Teste método estático
    print(f'\nUtilizando text_para_vetor estaticamente: {Berna.texto_para_vetor(None, "Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.", True)}\n')
    
if __name__ == '__main__':
    teste()