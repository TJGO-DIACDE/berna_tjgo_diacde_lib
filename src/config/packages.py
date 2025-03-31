'''
Created on Sun Jul 21 09:54:07 2024

@authors:
    Antonio Pires
    Milton Ávila
    João Gabriel
    Wesley Oliveira

@License:
Este projeto está licenciado sob a Licença Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Você pode compartilhar, adaptar e construir sobre o material, desde que atribua crédito apropriado, não use o material para fins comerciais e distribua suas contribuições sob a mesma licença.
Para mais informações, consulte o arquivo [LICENSE](./LICENSE).
'''
from src.preprocessing import _methods

class Packages:
    METHODS: dict[str, any] = {
        "no_ponctuation": _methods.remove_ponctuation,
        "no_loose_letters":_methods.remove_loose_letters,
        "no_multiple_spaces": _methods.remove_multiple_espaces,
        "replace_synonym_by_dict": _methods.get_synonym_by_dict,
        "no_html": _methods.remove_html,
        "no_email": _methods.remove_email,
        "no_numbers": _methods.remove_numbers,
        "no_stopwords": _methods.remove_stopwords,
        "only_latin": _methods.set_only_latin,
        "lemmatize": _methods.lemmatize_txt,
        "stemming": _methods.stem_txt,
    }