ref_arquivo = open('./german_credit.txt','r')
arquivo_pronto = open('./arquivoPronto.txt','w')

#criando uma lista de clientes
lista_clientes = []

cliente = {
  "idade": None,
  "sexo": None,
  "emprego": None,
  "habitacao": None,
  "poupanca": None,
  "corrente": None,
  "credito": None,
  "duracao": None,
  "proposito": None,
  "indice": None
}

linhas = ref_arquivo.readlines()

for linha in linhas:
  linha_info = linha.split()

  for coluna_contador in range(len(linha_info)):
      # aqui vou fazer a analise de todos os dados e inserir de maneira correta no 'arquivoPronto.txt' para ser usado no 'projetoCredito.py'
        clientes = cliente
        if len(linha_info) == 10:

            if coluna_contador == 0: # IDADE
                clientes["idade"] = linha_info[coluna_contador]
            elif coluna_contador == 1: # SEXO

                if linha_info[coluna_contador] == 'Female':
                    clientes["sexo"] = 0
                else:
                    clientes["sexo"] = 1

            elif coluna_contador == 2: # EMPREGO
                clientes["emprego"] = linha_info[coluna_contador]
            elif coluna_contador == 3: # HABITACAO

                if linha_info[coluna_contador] == 'own':
                    clientes["emprego"] = 0
                elif linha_info[coluna_contador] == 'rent':
                    clientes["emprego"] = 1
                else:
                    clientes["emprego"] = 2

            elif coluna_contador == 4: # POUPANCA

                if linha_info[coluna_contador] == 'no':
                    clientes["poupanca"] = 0
                elif linha_info[coluna_contador] == 'little':
                    clientes["poupanca"] = 1
                elif linha_info[coluna_contador] == 'moderate':
                    clientes["poupanca"] = 2
                elif linha_info[coluna_contador] == 'rich':
                    clientes["poupanca"] = 3
                elif linha_info[coluna_contador] == 'quite rich':
                    clientes["poupanca"] = 4

            elif coluna_contador == 5: # CORRENTE

                if linha_info[coluna_contador] == 'no':
                    clientes["corrente"] = 0
                elif linha_info[coluna_contador] == 'little':
                    clientes["corrente"] = 1
                elif linha_info[coluna_contador] == 'moderate':
                    clientes["corrente"] = 2
                elif linha_info[coluna_contador] == 'rich':
                    clientes["corrente"] = 3
                elif linha_info[coluna_contador] == 'quite rich':
                    clientes["corrente"] = 4

            elif coluna_contador == 6: # CRÉDITO
                clientes["credito"] = linha_info[coluna_contador]
            elif coluna_contador == 7: # DURAÇÃO
                clientes["duracao"] = linha_info[coluna_contador]
            elif coluna_contador == 8: # PROPOSITO
                if linha_info[coluna_contador] == 'radio/TV':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'vacation/others':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'furniture/equipment':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'car':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'business':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'domestic appliances':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'education':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'repairs':
                    clientes["corrente"] =
            else: # INDICE_APROVACAO
                clientes["indice"] = linha_info[coluna_contador]

        #tratando o erro no caso de linha_info possuir 11 linhas
        elif len(linha_info) == 11:

            if coluna_contador == 0:  # IDADE
                clientes["idade"] = linha_info[coluna_contador]
            elif coluna_contador == 1:  # SEXO

                if linha_info[coluna_contador] == 'Female':
                    clientes["sexo"] = 0
                else:
                    clientes["sexo"] = 1

            elif coluna_contador == 2:  # EMPREGO
                clientes["emprego"] = linha_info[coluna_contador]
            elif coluna_contador == 3:  # HABITACAO

                if linha_info[coluna_contador] == 'own':
                    clientes["emprego"] = 0
                elif linha_info[coluna_contador] == 'rent':
                    clientes["emprego"] = 1
                else:
                    clientes["emprego"] = 2

            elif coluna_contador == 4:  # POUPANCA

                if linha_info[coluna_contador] == 'no':
                    clientes["poupanca"] = 0
                elif linha_info[coluna_contador] == 'little':
                    clientes["poupanca"] = 1
                elif linha_info[coluna_contador] == 'moderate':
                    clientes["poupanca"] = 2
                elif linha_info[coluna_contador] == 'rich':
                    clientes["poupanca"] = 3
                elif linha_info[coluna_contador] == 'quite rich':
                    clientes["poupanca"] = 4

            elif coluna_contador == 5:  # CORRENTE

                if linha_info[coluna_contador] == 'no':
                    clientes["corrente"] = 0
                elif linha_info[coluna_contador] == 'little':
                    clientes["corrente"] = 1
                elif linha_info[coluna_contador] == 'moderate':
                    clientes["corrente"] = 2
                elif linha_info[coluna_contador] == 'rich':
                    clientes["corrente"] = 3
                elif linha_info[coluna_contador] == 'quite rich':
                    clientes["corrente"] = 4

            elif coluna_contador == 6:  # CRÉDITO
                clientes["credito"] = linha_info[coluna_contador]
            elif coluna_contador == 7:  # DURAÇÃO
                clientes["duracao"] = linha_info[coluna_contador]
            elif coluna_contador == 8:  # PROPOSITO
                if linha_info[coluna_contador] == 'radio/TV':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'vacation/others':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'furniture/equipment':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'car':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'business':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'domestic appliances':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'education':
                    clientes["corrente"] =
                elif linha_info[coluna_contador] == 'repairs':
                    clientes["corrente"] =
            else:  # INDICE_APROVACAO
                clientes["indice"] = linha_info[coluna_contador]

  lista_clientes.append(clientes)

  #agora que ja temos todos os arquivos tratados em lista_clientes, vamos coloca-los no arquivo_pronto


ref_arquivo.close()
arquivo_pronto.close()