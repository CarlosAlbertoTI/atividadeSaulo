import funcoes
from ajustarDados import *

lista_clientes = tratarDados()
lista_alfas = []

for epoca in range(50):
  contador = 0
  for cliente in lista_clientes:
    clientes = calibrar(cliente,epoca,contador)
    contador+=1
