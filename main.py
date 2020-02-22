from AtomFile import Atom, Coordinate
import os
from time import sleep

n = int(input("Please enter the number of lines for the grid: "))
m = int(input("Please enter the number of columns for the grid: "))

n += 1
m += 1
grid = []
grid.append([])
for i in range(n):
    for j in range(m):
        coordinate = Coordinate(i, j)
        print("{{ Added molecule x: {}; y: {} }}".format(i, j))
        atom = Atom(coordinate)
        grid[i].append(atom)
    grid.append([])

grid[1][2].revive()
grid[0][2].revive()
grid[1][1].revive()
grid[2][1].revive()

def print_grid():
    for line in grid:
        for atom in line:
            if atom.is_alive:
                print("#", end='')
            else:
                print("0", end='')
        print()
    return None


def simulate():
    deaths = []
    
    for line in grid:
        for molecule in line:
            if molecule.is_alive and not molecule.is_surviving(grid):
                deaths.append(molecule)
            elif not molecule.is_alive:
                molecule.reproduce(grid)

    for dead_molecule in deaths:
        dead_molecule.is_alive = False

    print_grid()


for i in range(1, 10000000):
    simulate()
    sleep(1)
    os.system('clear')
