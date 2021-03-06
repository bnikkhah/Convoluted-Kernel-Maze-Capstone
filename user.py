from random import randint

class User:

    def __init__(self):
        pass

    def intro(self):
        print("\nWelcome to the Convoluted Kernel Maze Builder and Pathfinder")
        print("This is a capstone project on Codecademy for the course Computer Science Basics: Algorithms")
        print("Author: Behnam Nikkhah\n")
        print("Terms:")
        print("\t'S' represents the start of the maze")
        print("\t'E' represents the end of the maze")
        print("\tRows: The amount of rows for the maze")
        print("\tColumns: The amount of columns for the maze")
        print("\tMow rate: Higher rate = more walls; Lower rate = less walls (Recommended: 2)")
        print("\tSwag List: Props to be laid out in the maze")
        print("\t\tNote: If custom, please use a swag item that does start with an 's' (reserved for 'start')")
        print("\tSwag Rate: How often should a swag item appear. Higher rate = less chance; Lower Rate = more chance\n")
        print("Pathfinding:")
        print("\tEach '.' represents a movement")
        print("\tIf the pathfinder finds the opportunity, it will go diagonally in order to attain the shortest path (greedy algorithm)")
        print("\tThe pathfinding algorithm is based upon the A* algorithm\n")

    def row_and_column(self):
        while True:
            maze_choice = input("Random maze or Custom?\n\t'r' for random\n\t'c' for Custom\n")
            if maze_choice == 'r':
                while True:
                    try:
                        maze_size = int(input("Max size: "))
                        row = randint(1, maze_size)
                        col = randint(1, maze_size)
                        return row, col
                    except ValueError:
                        print("That's not a number! Try again.")
            elif maze_choice == 'c':
                while True:
                    try:
                        row = int(input("Maze rows: "))
                        break
                    except ValueError:
                        print("That's not a number! Try again.")
                while True:
                    try:
                        col = int(input("Maze columns: "))
                        break
                    except ValueError:
                        print("That's not a number! Try again.")
                return row, col
            else:
                print("That's not a valid choice! Please try again.")

    def swag(self):
        print("\nDefine the type of swags you would like to appear in the maze. Default: ['candy corn', 'werewolf', 'pumpkin']")
        swag_list = ['candy corn', 'werewolf', 'pumpkin']
        swag_rate = 10
        use_swag_defaults = input("Use swag list defaults?\nType any key to confirm or 'c' for custom swag list: ")
        if use_swag_defaults == "c":
            print("Type 'f' or 'finished' when you're finished inserting your swags.")
            swag_list.clear()
            i = 0
            while True:
                swag_item = input("Swag Item {0}: ".format(i))
                if swag_item.lower() == "f" or swag_item.lower() == "finished":
                    break
                swag_list.append(swag_item)
                i += 1
        print("\nHow often should the swags appear? Default: 10%")
        use_swag_defaults = input("Use swag rate defaults?\nType any key to confirm or 'c' for custom swag rate: ")
        if use_swag_defaults == "c":
            while True:
                try:
                    swag_rate = int(input("Swag rate: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
        return swag_list, swag_rate

    def mow_rate(self):
        while True:
            try:
                mow_rate = int(input("Mow rate (Recommended: 2): "))
                break
            except ValueError:
                print("That's not a number! Try again.")
        return mow_rate