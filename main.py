from AtomFile import Atom, Coordinate

n = int(input("Please enter the number of lines for the grid: "))
m = int(input("Please enter the number of columns for the grid: "))

grid = []
grid.append([])
for i in range(n):
    for j in range(m):
        coordinate = Coordinate(i, j)
        atom = Atom(coordinate)
        grid[i].append(atom)
    grid.append([])

for line in grid:
    for atom in line:
        print(atom, end = ' ')
    print()

