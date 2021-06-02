class Coordinate:
    #Built this structure only to make the code more readable
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Atom:
    #This structure represents a molecule
    def __init__(self, start_coordinate):
        self.coordinate = start_coordinate
        self.is_alive = False

    '''
        Function used the determine if a molecule will survive or not
        @param: self is the molecule that is being tested
        @param: grid is the collections of molecules that compose the grid(both dead and alive)
        @return: returns True if the molecule will survive the iteration or if it dies
        The rules are easy to deduce from the code or they can be found on the internet
    '''
    def is_surviving(self, grid):
        return self.get_neighbours(grid) in [2, 3]


    '''
        Function determines if a set of coordinates belong to the grid
        @param: x is the first coordinate(x-axis)
        @param: y is the second coordinate(y-axis)
        @param: grid is the collection of molecules that compose the grid(both dead and alive)
        @return: <type: bool> True if the coordinates belong to the grid, False otherwise
    '''
    def test_coordinates(self, x, y, grid):
        if x >= len(grid) - 1 or x < 0:
            return False
        elif y >= len(grid[0]) - 1 or y < 0:
            return False
        return True

    
    '''
        Function used to revive a dead molecule
        @param: self is the molecule that will be removed
        @return: void
    '''
    def revive(self):
        self.is_alive = True
    
    '''
        Function returns the living molecules that surround the molecule sent as parameter
        @param: self is the molecule in question
        @param: grid is the collection of molecules that compose the grid(both dead and aive)
        @return: <type: list> a list of all the living molecules surrounding the molecule referenced
    '''
    def get_neighbours(self, grid):
        ret = []

        initial_x = self.coordinate.x
        initial_y = self.coordinate.y

        tx = [0, 0, -1, 1, -1, -1, 1, 1]
        ty = [-1, 1, 0, 0, -1, 1, -1, 1]
        for i in range(len(tx)):
            new_x = initial_x + tx[i]
            new_y = initial_y + ty[i]

            if not self.test_coordinates(new_x, new_y, grid):
                continue
            try:
                if grid[new_x][new_y].is_alive:
                    ret.append(grid[new_x][new_y])
            except IndexError:
                print("{{ Checking molecule x: {}; y: {}; }}".format(new_x, new_y))

        return ret

    '''
        Function that determines if a molecule will be revived
        @param: self is the molecule in question
        @param: grid is the collection of molecules that compose the grid(both dead and alive)
        @return: void
    '''
    def reproduce(self, grid):
        initial_x = self.coordinate.x
        initial_y = self.coordinate.y
        
        tx = [0, 0, -1, 1, -1, -1, 1, 1]
        ty = [-1, 1, 0, 0, -1, 1, -1, 1]

        for i in range(len(tx)):
            new_x = initial_x + tx[i]
            new_y = initial_y + ty[i]

            if not self.test_coordinates(new_x, new_y, grid):
                continue

            number_of_neighbours = len(grid[new_x][new_y].get_neighbours(grid))
            
            if number_of_neighbours == 3:
                self.revive()
