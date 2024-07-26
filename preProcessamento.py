import pandas as pd
import pkg_resources

def clear(txt: str) -> str:
    out_txt = txt.lower().replace('style@page','').replace('style','').replace('70px','').replace('\"span ','').replace('p&ampnbsp','').replace(' p ','').replace('\"lineheight"','').replace('textindent','').replace('justify','').replace('150%','').replace(' /p ','').replace('100px','').replace('\"fontsize','').replace('marginleft','').replace('70px','').replace('&ampnbsp','').replace('\"fontfamily','').replace('80px','').replace('30px','').replace('100%','').replace('marginright','').replace(' margin ','').replace('\"textalign','').replace('\"fontfamily','').replace('','').replace(' times ','').replace(' br ','').replace(' span ','').replace('lineheight','').replace('fontsize','').replace('fontfamily','').replace('textalign','').replace(' p ','').replace('2016p','').replace('3cm','').replace('4cm','').replace('p&ampnbsp','').replace(' new ','').replace('romanspan','').replace('&ampnbsp','')
    out_txt = ''.join([l for l in out_txt if l.isalnum() or l==' '])
    out_txt = ' '.join([w for w in out_txt.split() if len(w) > 2])

    return out_txt

def get_synonym(txt: str) -> str:
    txt = txt.lower()

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
    txt = txt.lower()

    for _, row in table_dict.iterrows():

        for token in str(row['DE_PARA']).split(','):
            token = token.lower()

            if token in txt:
                txt = txt.replace(token, row['PALAVRA'].strip(', '))

    return txt
            

def _read_binary() -> object:
    file_local = pkg_resources.resource_filename(__name__, 'data/data.pkl')
    df_carregado = pd.read_pickle(file_local)

    return df_carregado


if __name__=='__main__':
    # Teste func 1
    print(clear('Esse é um teste! e não devem haver pontuações nessa frase... :# style@page'))

    # Teste func 2
    print(get_synonym('Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.'))

    # Teste func 3
    print(get_synonym_by_dict('Eu sou o primeiro texto de antonio pires, incluindo leis, resoluções, normas legais.'))
