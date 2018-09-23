#AQUI VÃO TODAS AS FUNÇÕES DO PROJETO
def geraAleatorios():
  import random
  listaAlfa = []

  for i in range(9):
    listaAlfa.append(random.randint(-9, 9))

  return listaAlfa


def filtroLinha(linhaAtual):
  if (len(linhaAtual) == 10):
    return linhaAtual
  elif (len(linhaAtual) == 11) or (len(linhaAtual) == 12):
    linhaNova = []
    coluna = 0
    while coluna < len(linhaAtual):
      if ((linhaAtual[coluna] == 'quite') or (linhaAtual[coluna] == 'rich') or (linhaAtual[coluna] == 'domestic') or (
        linhaAtual[coluna] == 'appliances')):

        if ((linhaAtual[coluna] == 'quite') and (linhaAtual[coluna + 1] == 'rich')):
          linhaNova.append('quiteRich')

        if ((linhaAtual[coluna] == 'domestic') and (linhaAtual[coluna + 1] == 'appliances')):
          linhaNova.append('domesticAppliances')
      else:
        linhaNova.append(linhaAtual[coluna])

      coluna += 1

    return linhaNova
