from funcoes import *

def tratarDados():

    ref_arquivo = open('./german_credit.txt','r')
    #arquivo_pronto = open('./arquivoPronto.txt','w')

    #criando uma lista de cliente
    lista_clientes = []

    

    #linhas = ref_arquivo.readlines()


    for linha in ref_arquivo:
        linha_info = linha.split('\t')
        #linha_info = filtroLinha(linha_info)
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
        #print(linha_info)
        for coluna_contador in range(len(linha_info)):
          # aqui vou fazer a analise de todos os dados e inserir de maneira correta no 'arquivoPronto.txt' para ser usado no 'projetoCredito.py'

                if coluna_contador == 0: # IDADE
                    cliente["idade"] = linha_info[coluna_contador]
                elif coluna_contador == 1: # SEXO

                    if linha_info[coluna_contador] == 'female':
                        cliente["sexo"] = 0
                    else:
                        cliente["sexo"] = 1

                elif coluna_contador == 2: # EMPREGO
                    cliente["emprego"] = linha_info[coluna_contador]
                elif coluna_contador == 3: # HABITACAO

                    if linha_info[coluna_contador] == 'own':
                        cliente["habitacao"] = 0
                    elif linha_info[coluna_contador] == 'rent':
                        cliente["habitacao"] = 1
                    elif linha_info[coluna_contador] == 'free':
                        cliente["habitacao"] = 2

                elif coluna_contador == 4: # POUPANCA

                    if linha_info[coluna_contador] == 'no':
                        cliente["poupanca"] = 0
                    elif linha_info[coluna_contador] == 'little':
                        cliente["poupanca"] = 1
                    elif linha_info[coluna_contador] == 'moderate':
                        cliente["poupanca"] = 2
                    elif linha_info[coluna_contador] == 'rich':
                        cliente["poupanca"] = 3
                    elif linha_info[coluna_contador] == 'quite rich':
                        cliente["poupanca"] = 4
                    else:
                        print('Entrou em erro: ',linha_info[coluna_contador])
                        cliente["poupanca"] =  'ERRO'

                elif coluna_contador == 5: # CORRENTE

                    if linha_info[coluna_contador] == 'no':
                        cliente["corrente"] = 0
                    elif linha_info[coluna_contador] == 'little':
                        cliente["corrente"] = 1
                    elif linha_info[coluna_contador] == 'moderate':
                        cliente["corrente"] = 2
                    elif linha_info[coluna_contador] == 'rich':
                        cliente["corrente"] = 3
                    elif linha_info[coluna_contador] == 'quit reich':
                        cliente["corrente"] = 4
                    else:
                        print('Entrou em erro: ',linha_info[coluna_contador])
                        cliente["corrente"] =  'ERRO'

                elif coluna_contador == 6: # CRÉDITO
                    cliente["credito"] = linha_info[coluna_contador]
                elif coluna_contador == 7: # DURAÇÃO
                    cliente["duracao"] = linha_info[coluna_contador]
                elif coluna_contador == 8: # PROPOSITO
                    
                    if linha_info[coluna_contador] == 'radio/TV':
                        cliente["proposito"] =1
                    elif linha_info[coluna_contador] == 'vacation/others':
                        cliente["proposito"] =2
                    elif linha_info[coluna_contador] == 'furniture/equipment':
                        cliente["proposito"] =3
                    elif linha_info[coluna_contador] == 'car':
                        cliente["proposito"] =4
                    elif linha_info[coluna_contador] == 'business':
                        cliente["proposito"] =5
                    elif linha_info[coluna_contador] == 'domestic appliances':
                        cliente["proposito"] =6
                    elif linha_info[coluna_contador] == 'education':
                        cliente["proposito"] =7
                    elif linha_info[coluna_contador] == 'repairs':
                        cliente["proposito"] =8
                    else:
                        #aqui se puxa
                        print('Entrou em erro: ',linha_info[coluna_contador])
                        cliente["proposito"] =  'ERRO'
                else: # INDICE_APROVACAO
                    #print('linha len: ',int(linha_info[coluna_contador]))
                    #print('linha: ',linha_info[coluna_contador])
                    if int(linha_info[coluna_contador]) == -1:
                        cliente["indice"] = -1
                        #linha_info[coluna_contador]
                        #print('cliente: ',cliente["indice"])
                    else:
                        cliente["indice"] = 1
                        #print('cliente: ', cliente["indice"])
                #print(coluna_contador);



        lista_clientes.append(cliente)
        #print(cliente)





    return lista_clientes
    ref_arquivo.close()
    #arquivo_pronto.close()

#tratarDados()