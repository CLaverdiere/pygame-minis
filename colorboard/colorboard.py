from random import *
from node import *

class ColorBoard:
    def __init__(self, num_x, num_y):
        # Number of squares in x direction
        self.num_x = num_x

        # Number of squares in y direction
        self.num_y = num_y

        # Create empty container for nodes
        self.nodes = [[None for x in range(num_x)] for y in range(num_y)]

        # Create all nodes
        for y in range(num_y):
            for x in range(num_x):
                self.nodes[y][x] = Node((255, 255, 255))

    # Set the color of a single node
    def set_node_color(self, x, y, color):
        self.nodes[y][x].color = color


    # Set every node on the board a single color
    def set_board_color(self, color):
        for row in self.nodes:
            for node in row:
                node.color = color

    # Set a checkerboard color theme for the board
    def set_alt_colors(self, color1, color2):
        count = 0
        for row in self.nodes:
            for node in row:
                if count % 2 == 0:
                    node.color = color1
                else:
                    node.color = color2
                count += 1

    # Sets colors in board to a random shade
    def set_random_shade(self):
        for row in self.nodes:
            for node in row:
                seed = randint(1,10)
                node.color = (node.color[0] / seed, node.color[1] / seed, node.color[2] / seed)

    # Sets colors to be randomly tinted
    def set_random_tint(self):
        for row in self.nodes:
            for node in row:
                seed = randint(1,10)

                node.color = ( ((255 - node.color[0]) / seed + node.color[0]),
                               ((255 - node.color[1]) / seed + node.color[1]),
                               ((255 - node.color[2]) / seed + node.color[2]))

    # Set all node colors to different random colors
    def set_random_colors(self):
        for row in self.nodes:
            for node in row:
                node.color = (randint(0,255), randint(0,255), randint(0,255))

    # Shift all nodes in a given direction
    def shift_colors(self, direction):
        if direction == "up":
            self.nodes.append(self.nodes.pop(0))

        elif direction == "down":
            self.nodes.insert(0, self.nodes.pop())

        elif direction == "left":
            for row in self.nodes:
                row.append(row.pop(0))

        elif direction == "right":
            for row in self.nodes:
                row.insert(0, row.pop())

        elif direction == "upright":
            self.nodes.append(self.nodes.pop(0))
            for row in self.nodes:
                row.insert(0, row.pop())

        elif direction == "upleft":
            self.nodes.append(self.nodes.pop(0))
            for row in self.nodes:
                row.append(row.pop(0))

        elif direction == "downright":
            self.nodes.insert(0, self.nodes.pop())
            for row in self.nodes:
                row.insert(0, row.pop())

        elif direction == "downleft":
            self.nodes.insert(0, self.nodes.pop())
            for row in self.nodes:
                row.append(row.pop(0))

    def shift_colors_random(self):
        seed = randint(0, 7)
        if seed == 0:
            self.shift_colors("up")
        elif seed == 1:
            self.shift_colors("down")
        elif seed == 2:
            self.shift_colors("left")
        elif seed == 3:
            self.shift_colors("right")
        elif seed == 4:
            self.shift_colors("upright")
        elif seed == 5:
            self.shift_colors("upleft")
        elif seed == 6:
            self.shift_colors("downright")
        elif seed == 7:
            self.shift_colors("downleft")

