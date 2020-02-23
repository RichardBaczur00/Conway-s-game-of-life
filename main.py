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


def print_grid():
    for line in grid:
        for atom in line:
            if atom.is_alive:
                print("1", end='')
            else:
                print("0", end='')
        print()
    return None


def build_initial_celular_automata():
    number_of_live_molecules = int(input("Please enter the number of live cells you wish to start with: "))
    
    for i in range(number_of_live_molecules):
        x_coordinate = int(input("{{ Please enter the x coordiante of the {}-(th) molecule: }}".format(i)))
        y_coordinate = int(input("{{ Please enter the y coordiante of the {}-(th) molecule: }}".format(i))) 

        grid[x_coordinate][y_coordinate].revive()

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
    
    print_grid()


build_initial_celular_automata()
for i in range(1, 10000000):
    simulate()
    sleep(0.5)
    os.system('clear')
