from AtomFile import Atom, Coordinate
import os
from time import sleep
import random

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


def print_grid():
    for line in grid:
        for atom in line:
            if atom.is_alive:
                print("1", end='')
            else:
                print("0", end='')
        print()
    print()
    return None


def build_initial_celular_automata():
    number_of_live_molecules = int(input("Please enter the number of live cells you wish to start with: "))
    print_grid()
    
    for _ in range(number_of_live_molecules):
        x = random.randrange(0, len(grid) - 1)
        y = random.randrange(0, len(grid[0]) - 1)
        try:
            grid[x][y].revive()
        except:
            print(x)
            raise IndexError

    print_grid()


def simulate():
    deaths = []
    revives = []
    
    for line in grid:
        for molecule in line:
            if molecule.is_alive and not molecule.is_surviving(grid):
                deaths.append(molecule)
            elif not molecule.is_alive:
                if len(molecule.get_neighbours(grid)) == 3:
                    revives.append(molecule)
    
    for revived_molecule in revives:
        revived_molecule.revive()
    
    for dead_molecule in deaths:
        dead_molecule.is_alive = False

    if len(revives) == 0 and len(deaths) == 0:
        return -1
    
    print_grid()
    return 0


build_initial_celular_automata()
for i in range(1, 10000000):
    if simulate() == -1:
        print("Reached a final state.")
        break
    sleep(0.5)
    os.system('cls')