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

for linha in ref_arquivo:
  linhaAtual = linha.split()
  #Tamanho menos um são as linhas com parametros corretos pelo fato de existir um parametro excedente que é real_Aprovação
  #9 - com todos os atributos certos
  if(len(linhaAtual)-1) == 10:
    print(linhaAtual[4] + " " + linhaAtual[5])
  