import funcoes
from ajustarDados import *

#listaAlfa = funcoes.geraAleatorios()


ref_arquivo = open("german_credit.txt", "r")
linhas = (ref_arquivo.readline()).split('\t')

for linha in ref_arquivo:
  linhaAtual = linha.split()
  #Tamanho menos um são as linhas com parametros corretos pelo fato de existir um parametro excedente que é real_Aprovação
  #9 - com todos os atributos certos

indiceAprovacao = 0
#linhas = ref_arquivo.readlines()
#arquivo = tratarDados(ref_arquivo)
#print(arquivo)
#for linha in arquivo:
    #linha_info = linha.split()
    #print(len(linha_info))
   # print(linha,'\n')
  #para cada linha, antes de entrar no laço for que ira percorrer cada trecho da linha, a variavel lista_aleatorio ira criar 9 numeros
 # lista_aleatorio = funcoes.geraAleatorios()
  #for coluna_contador in range(len(linha_info) - 1):
"""
    usando 'range(len(linha_info) - 1)' pois eu vou incrementar apenas os 9 valores para a variavel indiceAprovacao
    # agora que eu ja tenho os numeros aleatorios devo inicar a variavel IA
      #indiceAprovacao *= (linha_info[coluna_contador] + lista_aleatorio[coluna_contador])
      #print(indiceAprovacao)
    """
