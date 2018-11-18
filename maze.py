from random import randint
from user import User
from collections import defaultdict, deque
from heapq import heappush, heappop

class Maze:

    def __init__(self, m, n, swag_items, swag_rate):
        self.m = m
        self.n = n
        self.swag_items = swag_items
        self.swag_rate = swag_rate

    def build_maze(self, mow_rate):
        grid = [["wall" for row in range(self.n)] for col in range(self.m)]
        start_i = randint(0, self.m-1)
        start_j = randint(0, self.n-1)
        grid[start_i][start_j] = "start"
        self.mow(grid, start_i, start_j, mow_rate)
        end_i, end_j = self.explore_maze(grid, start_i, start_j)
        self.astar(grid, (start_i, start_j), (end_i, end_j))
        return grid

    def heuristic(self, a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

    def astar(self, grid, start, end):
        neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        close_set = set()
        came_from = {}
        gscore = {start:0}
        fscore = {start:self.heuristic(start, end)}
        oheap = []
        heappush(oheap, (fscore[start], start))
        swag_collection = defaultdict(int)
        while oheap:
            current = heappop(oheap)[1]
            if current == end:
                data = []
                while current in came_from:
                    i, j = current
                    if grid[i][j] != "end" and grid[i][j] not in self.swag_items:
                        grid[i][j] = "."
                    elif grid[i][j] in self.swag_items:
                        swag_collection[grid[i][j]] += 1
                    data.insert(0, current)
                    current = came_from[current]
                print("Collected swags:")
                for key, value in swag_collection.items() :
                    print("\t{0}: {1}".format(key, value))
                return data
            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < len(grid[0]):
                    if 0 <= neighbor[1] < len(grid[1]):
                        if grid[neighbor[0]][neighbor[1]] == "wall":
                            continue
                    else:
                        continue
                else:
                    continue
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, end)
                    heappush(oheap, (fscore[neighbor], neighbor))
        return "no endpoint found"

    def explore_maze(self, grid, start_i, start_j):
        grid_copy = [row[:] for row in grid]
        bfs_queue = [[start_i, start_j]]
        directions = ["U", "D", "L", "R"]
        while bfs_queue:
            i, j = bfs_queue.pop(0)
            if grid[i][j] != "start" and randint(1, self.swag_rate) == 1:
                grid[i][j] = self.swag_items[randint(0, len(self.swag_items)-1)]
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
        return i, j

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

    def mow(self, grid, i, j, mow_rate):
        directions = ["U", "D", "L", "R"]
        while (len(directions) > 0):
            directions_index = randint(0, len(directions)-1)
            direction = directions.pop(directions_index)
            if direction == "U":
                if i-mow_rate < 0:
                    continue
                else:
                    if grid[i-mow_rate][j] == "wall":
                        counter = 1
                        while counter < mow_rate:
                            grid[i-counter][j] = "empty"
                            counter += 1
                        self.mow(grid, i-mow_rate, j, mow_rate)
            elif direction == "D":
                if i+mow_rate >= len(grid):
                    continue
                else:
                    if grid[i+mow_rate][j] == "wall":
                        counter = 1
                        while counter <= mow_rate:
                            grid[i+counter][j] = "empty"
                            counter += 1
                        self.mow(grid, i+mow_rate, j, mow_rate)
            elif direction == "L":
                if j-mow_rate < 0:
                    continue
                else:
                    if grid[i][j-mow_rate] == "wall":
                        counter = 1
                        while counter <= mow_rate:
                            grid[i][j-counter] = "empty"
                            counter += 1
                        self.mow(grid, i, j-mow_rate, mow_rate)
            elif direction == "R":
                if j+mow_rate >= len(grid[0]):
                    continue
                else:
                    if grid[i][j+mow_rate] == "wall":
                        counter = 1
                        while counter <= mow_rate:
                            grid[i][j+counter] = "empty"
                            counter += 1
                        self.mow(grid, i, j+mow_rate, mow_rate)


user = User()
row, col = user.row_and_column()
mow_rate = user.mow_rate()
swag_list, swag_rate = user.swag()
print("Defining a maze with parameters:\n\tRows: {0}\n\tColumns: {1}\n\tMow rate: {2}\n\tSwag List: {3}\n\tSwag Rate: 1/{4}".format(row, col, mow_rate, swag_list, swag_rate))
maze = Maze(row, col, swag_list, swag_rate)
grid = maze.build_maze(mow_rate)
maze.print_maze(grid)