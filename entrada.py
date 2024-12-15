import random

def criar_matriz(n, m):
    # Criar uma matriz n x m de zeros
    matriz = [[0 for _ in range(m)] for _ in range(n)]
    
    # Preencher a parte interior com 0 e 1, com maior probabilidade de zeros
    for i in range(1, n-1):
        for j in range(1, m-1):
            matriz[i][j] = random.choices([0, 1], weights=[0.6, 0.4])[0]
    
    return matriz

# Solicitar as entradas n e m do usuário
n = int(input("Digite o valor de n: "))
m = int(input("Digite o valor de m: "))

# Criar e imprimir a matriz
matriz = criar_matriz(n, m)
for linha in matriz:
    print(" ".join(map(str, linha)))
