import random

def geraAleatorios():
  listaAlfa = []

  for i in range(9):
    listaAlfa.append(random.randint(-9, 9))

  print(listaAlfa)

geraAleatorios()

cliente = {
  "idade": None,
  "sexo": None,
  "emprego": None,
  "habitacao": None,
  "poupanca": None,
  "corrente": None,
  "credito": None,
  "duracao": None,
  "proposito": None
}

ref_arquivo = open("german_credit.txt", "r")
linhas = (ref_arquivo.readline()).split('\t')

for linha in ref_arquivo:
  print((linha.split()))