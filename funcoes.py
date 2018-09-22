#AQUI VÃO TODAS AS FUNÇÕES DO PROJETO
def geraAleatorios():
  import random
  listaAlfa = []

  for i in range(9):
    listaAlfa.append(random.randint(-9, 9))

  return listaAlfa

