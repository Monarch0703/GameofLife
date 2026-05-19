import random
import time
import os
def make_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for i in grid:
        for j in i:
            print('#' if j else '.', end=' ')
        print()

def count_neighbours(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    dirs = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
            count += 1
    return count

def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)]for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            n_neighbours = count_neighbours(grid, i, j)
            if grid[i][j]:
                if n_neighbours<2:
                    new_grid[i][j] = 0 # Underpopulation
                elif n_neighbours in [2,3]:
                    new_grid[i][j] = 1 # Stable
                else:
                    new_grid[i][j] = 0 # Overpopulation
            else:
                if n_neighbours==3:
                    new_grid[i][j] = 1 # Reproduction

    return new_grid

def random_seed(grid, prob):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if random.random() <prob:
                grid[i][j] =1

grid = make_grid(20, 20)
random_seed(grid, 0.3)

for generation in range(100):
    os.system('cls')
    print_grid(grid)
    grid = next_generation(grid)
    time.sleep(0.2)