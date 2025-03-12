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
from ._methods import *
from .packages import Packages

def clear(
    txt: str | list[str],
    preset: list[str] = [],
    no_ponctuation: bool = False,
    no_multiple_spaces: bool = False,
    no_loose_letters: bool = False,
    only_latin: bool = False,
    no_email: bool = False,
    no_numbers: bool = False,
    no_stopwords: bool = False,
    no_html: bool = False,
    lemmatize: bool = False,
    stemming: bool = False,
    replace_synonym_by_dict: bool = False
) -> str | list:
    """
    Função para processar o texto de várias formas, removendo ou alterando caracteres,
    espaços, pontuação, entre outros, conforme os parâmetros fornecidos.

    Args:
        txt (str or list[str]): Texto ou lista de textos a serem processados.
        preset (list[str], opcional): Lista de métodos pré-definidos para aplicar.
        no_ponctuation (bool, opcional): Se True, remove pontuação.
        no_multiple_spaces (bool, opcional): Se True, remove espaços múltiplos.
        no_loose_letters (bool, opcional): Se True, remove letras soltas.
        only_latin (bool, opcional): Se True, limita o texto ao alfabeto latino.
        no_email (bool, opcional): Se True, remove endereços de e-mail.
        no_numbers (bool, opcional): Se True, remove números.
        no_stopwords (bool, opcional): Se True, remove palavras de parada.
        no_html (bool, opcional): Se True, remove tags HTML.
        lemmatize (bool, opcional): Se True, realiza lematização no texto.
        stemming (bool, opcional): Se True, realiza stemming no texto.
        replace_synonym_by_dict (bool, opcional): Se True, substitui sinônimos por um dicionário.

    Returns:
        str or list[str]: Texto processado ou lista de textos processados.
    """# Se o input for uma lista de strings, iteramos sobre ela
    if isinstance(txt, list):
        return [clear_single(t, preset, no_ponctuation, no_multiple_spaces, no_loose_letters, 
                             only_latin, no_email, no_numbers, no_stopwords, no_html, 
                             lemmatize, stemming, replace_synonym_by_dict) for t in txt]
    
    # Caso contrário, tratamos o texto como uma string
    return clear_single(txt, preset, no_ponctuation, no_multiple_spaces, no_loose_letters, 
                         only_latin, no_email, no_numbers, no_stopwords, no_html, 
                         lemmatize, stemming, replace_synonym_by_dict)
    
def clear_single(
    txt: str,
    preset: list[str],
    no_ponctuation: bool,
    no_multiple_spaces: bool,
    no_loose_letters: bool,
    only_latin: bool,
    no_email: bool,
    no_numbers: bool,
    no_stopwords: bool,
    no_html: bool,
    lemmatize: bool,
    stemming: bool,
    replace_synonym_by_dict: bool
) -> str:
    
    if preset:
        for method in preset:
            txt = Packages.METHODS[method](txt)
            
        return txt
    
    else:
        txt = txt.lower()

        if no_email:
            txt = remove_email(txt)
    
        if no_html:
            txt = remove_html(txt)

        if replace_synonym_by_dict:
            txt = get_synonym_by_dict(txt)

        if no_ponctuation:
            txt = remove_ponctuation(txt)

        if no_multiple_spaces:
            txt = remove_multiple_espaces(txt)

        if no_loose_letters:
            txt = remove_loose_letters(txt)

        if only_latin:
            txt = set_only_latin(txt)
            
        if no_numbers:
            txt = remove_numbers(txt)

        if no_stopwords:
            txt = remove_stopwords(txt)

        if lemmatize:
            txt = lemmatize_txt(txt)

        if stemming:
            txt = stem_txt(txt)

        return txt

if __name__=="__main__":
    # Teste func 1
    print(clear(["<span>Eu sou o primeiro texto de antonio! pires, incluindo leis, resoluções, normas legais.</span>", "Essa é uma frase que não contém um email, joao@gmail.com."], no_html=True, no_email=True, no_ponctuation=True, only_latin=True))

    # Teste func 2
    print(lemmatize_txt("Esse é um exemplo de um texto lematizado, com palavras reduzidas a sua raíz."))

    # Teste func 3
    print(stem_txt("Esse é um exemplo de um texto lematizado, com palavras reduzidas a sua raíz."))

    # Teste func 4
    print(remove_ponctuation("Esse é um teste! e não devem haver pontuações nessa frase..."))
    
    # Teste func 5
    print(remove_html("<script>Essa é uma frase sem palavras de css, </script>"))
    
    # Teste func 6
    print(remove_stopwords("Esse é um exemplo de um texto sem stopwors, sem palavras de conjunção."))

    # # Teste func 7
    # print(get_synonym("Método de sinonimos: Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))

    # Teste func 8
    print(get_synonym_by_dict("Método de sinonimos por dicionário: Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais."))
    
    # Teste func 9
    print(remove_multiple_espaces("  Esse   é um teste!   e não devem haver espaços extras   nessa frase..  ."))
    
    # Teste func 10
    print(remove_loose_letters("Esse é um exemplo de frase sem letras s soltas a i."))
    
    # Teste func 11
    print(set_only_latin("Essa é uma frase apenas com caracteres do alfabeto latin."))
    
    # Teste func 12
    print(remove_email("Essa é uma frase que não contém um email, joao@gmail.com."))
    
    # Teste func 13
    print(remove_numbers("Essa é um5a frase q2ue não contém números 123 4 22 3 135"))