class Coordinate:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;


class Atom:
    def __init__(self, start_coordinate):
        self.coordinate = start_coordinate
        self.is_alive = False

    
    def is_surviving(self, grid):
        neighbours = self.get_neighbours(grid)
        if len(neighbours) < 2:
            return False
        elif len(neighbours) > 3:
            return False
        elif len(neighbours) == 3:
            this.reproduce(grid)
            return True
        else:
            return True
    

    def revive(new_x, new_y):
        grid[new_x][new_y].is_alive = True
    

    def get_neighbours(self, grid):
        ret = []

        initial_x = self.coordinate.x
        initial_y = self.coordinate.y

        tx = [0, 0, -1, 1, -1, -1, 1, 1]
        ty = [-1, 1, 0, 0, -1, 1, -1, 1]

        for i in range(len(tx)):
           new_x = initial_x + tx[i]
           new_y = initial_y + ty[i]

           if grid[new_x][new_y].is_alive:
                ret.append(grid[new_x][new_y])

        return ret

    
    def reproduce(self, grid):
        initial_x = self.coordinate.x
        initial_y = self.coordinate.y
        
        tx = [0, 0, -1, 1, -1, -1, 1, 1]
        ty = [-1, 1, 0, 0, -1, 1, -1, 1]

        for i in range(len(tx)):
            new_x = initial_x + tx[i]
            new_y = initial_y + ty[i]

            number_of_neighbours = len(grid[new_x][new_y].get_neighbours(grid))
            
            if number_of_neighbours == 3:
                revive(new_x, new_y)
