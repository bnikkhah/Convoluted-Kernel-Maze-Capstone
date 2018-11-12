from random import randint
from user import User

class Maze:

    def __init__(self, m, n, swag, swag_rate):
        self.m = m
        self.n = n
        self.swag = swag
        self.swag_rate = swag_rate

    def build_maze(self):
        grid = [["wall" for row in range(self.n)] for col in range(self.m)]
        start_i = randint(0, self.m-1)
        start_j = randint(0, self.n-1)
        grid[start_i][start_j] = "start"
        self.mow(grid, start_i, start_j)
        self.explore_maze(grid, start_i, start_j)
        return grid

    def explore_maze(self, grid, start_i, start_j):
        grid_copy = [row[:] for row in grid]
        bfs_queue = [[start_i, start_j]]
        directions = ["U", "D", "L", "R"]
        while bfs_queue:
            i, j = bfs_queue.pop(0)
            if grid[i][j] != "start" and randint(1, self.swag_rate) == 1:
                grid[i][j] = self.swag[randint(0, len(self.swag)-1)]
            grid_copy[i][j] = "visited"
            for direction in directions:
                explore_i = i
                explore_j = j
                if direction == "U":
                    explore_i = i-1
                elif direction == "D":
                    explore_i = i+1
                elif direction == "L":
                    explore_j = j-1
                elif direction == "R":
                    explore_j = j+1
                if explore_i < 0 or explore_j < 0 or explore_i >= len(grid) or explore_j >= len(grid[0]):
                    continue
                elif grid_copy[explore_i][explore_j] != "visited" and grid_copy[explore_i][explore_j] != "wall":
                    bfs_queue.append([explore_i, explore_j])
        grid[i][j] = "end"

    def print_maze(self, grid):
        for row in grid:
            printable_row = ""
            for cell in row:
                if cell == "wall":
                    char = "|"
                elif cell == "empty":
                    char = " "
                else:
                    char = cell[0]
                printable_row += char
            print(printable_row)

    def mow(self, grid, i, j):
        directions = ["U", "D", "L", "R"]
        while (len(directions) > 0):
            directions_index = randint(0, len(directions)-1)
            direction = directions.pop(directions_index)
            if direction == "U":
                if i-2 < 0:
                    continue
                else:
                    if grid[i-2][j] == "wall":
                        grid[i-1][j] = "empty"
                        grid[i-2][j] = "empty"
                        self.mow(grid, i-2, j)
            elif direction == "D":
                if i+2 >= len(grid):
                    continue
                else:
                    if grid[i+2][j] == "wall":
                        grid[i+1][j] = "empty"
                        grid[i+2][j] = "empty"
                        self.mow(grid, i+2, j)
            elif direction == "L":
                if j-2 < 0:
                    continue
                else:
                    if grid[i][j-2] == "wall":
                        grid[i][j-1] = "empty"
                        grid[i][j-2] = "empty"
                        self.mow(grid, i, j-2)
            elif direction == "R":
                if j+2 >= len(grid[0]):
                    continue
                else:
                    if grid[i][j+2] == "wall":
                        grid[i][j+1] = "empty"
                        grid[i][j+2] = "empty"
                        self.mow(grid, i, j+2)


user = User()
row, col = user.row_and_column()
swag_list, swag_rate = user.swag()
print("Defining a maze with parameters:\n\tRows: {0}\n\tColumns: {1}\n\tSwag List: {2}\n\tSwag Rate: {3}".format(row, col, swag_list, swag_rate))
maze = Maze(row, col, swag_list, swag_rate)
grid = maze.build_maze()
maze.print_maze(grid)

