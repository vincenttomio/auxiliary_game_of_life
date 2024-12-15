def contar_zeros_e_uns_arquivo(nome_arquivo):
  """Conta a quantidade de 0s e 1s em uma matriz a partir de um arquivo.

  Args:
    nome_arquivo: O nome do arquivo contendo a matriz.

  Returns:
    Uma tupla com a quantidade de 0s, a quantidade de 1s e a porcentagem de 1s.
  """

  with open(nome_arquivo, 'r') as arquivo:
    # Ler as dimensões da matriz
    n, m = map(int, arquivo.readline().split())

    # Ler os valores da matriz
    matriz = []
    for _ in range(n):
      linha = list(map(int, arquivo.readline().split()))
      matriz.append(linha)

  # Achatar a matriz em uma lista
  lista_numeros = [num for linha in matriz for num in linha]

  # Contar os zeros e uns
  quantidade_zeros = lista_numeros.count(0)
  quantidade_uns = lista_numeros.count(1)

  # Calcular a porcentagem de uns
  total_elementos = len(lista_numeros)
  porcentagem_uns = (quantidade_uns / total_elementos) * 100

  return quantidade_zeros, quantidade_uns, porcentagem_uns

import sys


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Uso: python script.py nome_do_arquivo")
    sys.exit(1)

  nome_arquivo = sys.argv[1]
  resultado = contar_zeros_e_uns_arquivo(nome_arquivo)

  print("Quantidade de 0s:", resultado[0])
  print("Quantidade de 1s:", resultado[1])
  print("Porcentagem de 1s:", resultado[2], "%")
