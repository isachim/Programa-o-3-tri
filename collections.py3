03/09

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1
     {'bem': 1,

     'cachorro': 2,

     'de': 2,

     'e': 2,

     'eu': 1,

     'gosto': 2,

     'guilherme': 1,

     'meu': 2,

     'muito': 2,

     'nome': 1,

     'nomes': 1,

     'o': 1,

     'tenho': 1,

     'vindo': 1,

     'é': 1})
aparicoes
class Conta:
  def __init__(self):
    print("Criando uma conta")
   texto1.split( )

Counter(text1.lower())
aparicoes = Counter(texto1.lower())
total_de_caracteres = sum(aparicoes.values())
for letra, frequencia in aparicoes.items():
    tupla=(letra, frequencia / total_de_caracteres)
    print(tupla)

aparicoes = Counter(texto1.lower())
total_de_caracteres = sum(aparicoes.values())

[(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))
analisa_frequencia_de_letras(texto1)

