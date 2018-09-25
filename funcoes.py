#AQUI VÃO TODAS AS FUNÇÕES DO PROJETO
def geraAleatorios():
  import random
  listaAlfa = []

  for i in range(9):
    listaAlfa.append(random.randint(-9, 9))

  return listaAlfa


def calibrar(lista,epoca,contador):
  #se contador e epoca for 0 significa que ele esta na primeira execução da linha
  lista_Alfa = geraAleatorios()
  if contador == 0 and epoca == 0:
      IA = (lista_Alfa[0]*int(lista['idade'])) + (lista_Alfa[1]*int(lista['sexo'])) + (lista_Alfa[2]*int(lista['emprego'])) + (lista_Alfa[3]*int(lista['habitacao'])) + (lista_Alfa[4]*int(lista['poupanca'])) + (lista_Alfa[5]*int(lista['corrente'])) + (lista_Alfa[6]*int(lista['credito'])) + (lista_Alfa[7]*int(lista['duracao'])) + (lista_Alfa[8]*int(lista['proposito']))
      return IA
  else:
      IA = (lista_Alfa[0]*int(lista['idade'])) + (lista_Alfa[1]*int(lista['sexo'])) + (lista_Alfa[2]*int(lista['emprego'])) + (lista_Alfa[3]*int(lista['habitacao'])) + (lista_Alfa[4]*int(lista['poupanca'])) + (lista_Alfa[5]*int(lista['corrente'])) + (lista_Alfa[6]*int(lista['credito'])) + (lista_Alfa[7]*int(lista['duracao'])) + (lista_Alfa[8]*int(lista['proposito']))
      return IA