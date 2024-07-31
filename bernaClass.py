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


from . import preProcessamento as prep         # Retire o ponto para rodar localmente

class Berna:
    def __init__(self, doc1: str, doc2: str, pre_process: bool = False) -> None:
        self.pre_process = pre_process

        self.vec_terms1 = self.texto_para_vetor(doc1)
        self.vec_terms2 = self.texto_para_vetor(doc2)

        self.calcula_similaridade_cosseno()
        self.calcula_similaridade_jaccard()

    def get_similaridade_jaccard(self) -> float:
        return self.similaridade_jaccard

    def get_similaridade_cosseno(self) -> float:
        return self.similaridade_cosseno
            
    def calcula_similaridade_jaccard(self) -> None:
        intersection_terms =    set(self.vec_terms1) & set(self.vec_terms2)
        union_terms =           set(self.vec_terms1) | set(self.vec_terms2)

        if len(self.vec_terms1) == 0 or len(self.vec_terms2) == 0:
            self.similaridade_jaccard = None
        else:
            self.similaridade_jaccard = round( (len(intersection_terms) / len(union_terms)) * 100, 4)

    def calcula_similaridade_cosseno(self) -> None:
        union_terms = set(self.vec_terms1) | set(self.vec_terms2)
        l1, l2 = [], []
        c=0

        for w in union_terms:
            if w in list(set(self.vec_terms1)):
                l1.append(1)
            else: 
                l1.append(0)

            if w in list(set(self.vec_terms2)):
                l2.append(1)
            else:
                l2.append(0)

        for i in range(len(union_terms)):
            c+=l1[i]*l2[i]

        if len(self.vec_terms1) == 0 or len(self.vec_terms2) == 0:
            self.similaridade_cosseno = None
        else:
            cosine = c / (sum(l1)*sum(l2))**0.5
            self.similaridade_cosseno =  round(cosine*100, 4)

    def texto_para_vetor(self, txt: str, pre_process: bool = False) -> list:
        try:
            pre_process = self.pre_process
        except:
            pass

        if pre_process:
            txt = prep.clear(txt, lematize=True, no_ponctuation=True, replace_synonym=True)

        vetor = [token for token in txt.split()]

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