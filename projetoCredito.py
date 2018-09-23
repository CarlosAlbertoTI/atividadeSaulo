import funcoes

listaAlfa = funcoes.geraAleatorios()

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
count = 0
for linha in ref_arquivo:
  linhaAtual = linha.split()
  linhaNova = []
  #Tamanho menos um são as linhas com parametros corretos pelo fato de existir um parametro excedente que é real_Aprovação
  #9 - com todos os atributos certos
  #
  linhaAtual = funcoes.filtroLinha(linhaAtual)
  if(len(linhaAtual) == 9):
    count += 1
    print(linhaAtual)
    print(count)