import numpy as np
import sys

def count_neighbors(grid, x, y):
    """
    Conta os vizinhos vivos ao redor da célula (x, y).
    """
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
            count += grid[nx, ny]
    return count

def next_generation(grid):
    """
    Gera o próximo estado da grade do Jogo da Vida.
    """
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)

    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_neighbors(grid, x, y)

            if grid[x, y] == 1:  # Célula viva
                if live_neighbors in (2, 3):
                    new_grid[x, y] = 1
            else:  # Célula morta
                if live_neighbors == 3:
                    new_grid[x, y] = 1

    return new_grid

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 script.py <arquivo_entrada.in>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Erro: arquivo '{input_file}' não encontrado.")
        sys.exit(1)

    # Lê os valores de n e m
    n, m = map(int, lines[0].split())

    # Lê o restante do tabuleiro
    grid = np.array([list(map(int, line.split())) for line in lines[1:]])

    if grid.shape != (n, m):
        print("Erro: Dimensões do tabuleiro não correspondem aos valores de n e m fornecidos.")
        sys.exit(1)

    print("Estado inicial:")
    print(grid)

    next_grid = next_generation(grid)

    print("\nPróxima geração:")
    for row in next_grid:
        print(" ".join(map(str, row)))
