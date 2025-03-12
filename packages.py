from ._methods import *

class Packages:
    METHODS: dict[str, any] = {
        "no_ponctuation": remove_ponctuation,
        "no_multiple_spaces": remove_stopwords,
        "lemmatize": lemmatize_txt,
        "stemming": stem_txt,
        "tokenize": tokenize,
        "only_latin": set_only_latin,
        "no_numbers": remove_numbers,
        "no_multiple_spaces": remove_multiple_espaces,
        "no_loose_letters": remove_loose_letters,
        "no_email": remove_email,
        "no_html": remove_html,
        "replace_synonym_by_dict": get_synonym_by_dict
    }