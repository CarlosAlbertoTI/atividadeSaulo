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
      #agora eu tenho que chamar os valores de lista_random e lista para junta-los numa variavel IA
      print('lista: ',int(lista["idade"]),' : ',lista_Alfa[0])
      IA = (lista_Alfa[0]*lista["idade"])#+(lista_Alfa[1]*lista["sexo"])+(lista_Alfa[2]*lista["emprego"])+(lista_Alfa[3]*lista["habitacao"])+(lista_Alfa[4]*lista["poucanca"])+(lista_Alfa[5]*lista["corrente"])+(lista_Alfa[6]*lista["credito"])+(lista_Alfa[7]*lista["duracao"])+(lista_Alfa[8]*lista["proposito"])
      maior_aleatorio = max(lista_Alfa)
      return IA,maior_aleatorio
      #print(IA)
  else:
      #print('lista: ', int(lista["idade"]), ' : ', lista_Alfa[0])
      #print('soma: ', int(lista["sexo"])+1,' : ',lista_Alfa[0])
      IA = (lista_Alfa[0] * int(lista["idade"])) + (lista_Alfa[1] * int(lista["sexo"])) + (lista_Alfa[2] * int(lista["emprego"])) + (lista_Alfa[3] * int(lista["habitacao"])) + (lista_Alfa[4] * lista["poucanca"]) + (lista_Alfa[5] * lista["corrente"]) + (lista_Alfa[6] * lista["credito"]) + (lista_Alfa[7] * lista["duracao"]) + (lista_Alfa[8] * lista["proposito"])
      maior_aleatorio = max(lista_Alfa)
      return IA,maior_aleatorio
      #print(IA)