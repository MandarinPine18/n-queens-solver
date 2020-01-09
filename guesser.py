#!/usr/bin/env python3.7

import numpy as np
import random
from support.diagonals import *

# number of queens
n = 20

# first letter of solver (options: 's', 'b') (recommended: 's')
solver = 's'

def brute(n):
    """
    *** IMPORTANT ***
    *** This function is not used by default as it is inefficient. Instead, 'systematic()' is used by default as it is a
    much more efficient method. To change this, edit the value for 'solver' in line 11 ***

    This is a simple brute force solver which generates random guesses and checks for validity. It uses another file
    in the folder titled support to verify diagonals efficiently. It, however, only generates one solution and takes
    time. In a problem with 20 queens, there are 2.78 E 33 possible combinations. The amount of time this strategy would
    take is unreasonable. This was optimized in a more methodical solver below. This solver is primarily based on the
    generation and analysis of arrays with binary values. The 0 entries are empty and the 1 entries have a queen. This
    can be used interchangeably with the next solver.
    """
    checkList = np.ones((1, n))[0]
    attempts = 0
    while True:
        # log data
        attempts += 1

        # initializing array
        a = np.zeros((n, n))

        # generating a randomized plot of n queens. Axis 1 does not need checking
        for i in range(n):
            row = i
            col = random.randint(0, n - 1)
            a[row, col] = 1

        if any(a.sum(axis=0) != checkList):
            continue
        elif not diagVer(a):
            continue
        elif not diagVer(np.flip(a, axis=1)):
            continue
        else:
            break

    print(a)

    return {
        'solution': a,
        'attempts': attempts,
    }


class systematic:
    """
    This is another type of solver. It uses above rows to decide where on a row to place a queen. It is far faster than
    the previous solver and outputs many more possible solutions. This solver is based on the generation of a model with
    a list. It is easier to analyze within a program than an array, but requires a renderer to allow human
    comprehension.
    """
    def __init__(self, n):
        """
        This class is designed to work like a method to maintain interchangeability. When this is instantiated, it
        accepts the same parameter as the previous function. A counter is created and run is started
        """
        self.size = n
        self.counter = 0
        self.run()

    def checker(self, board, testrow, column):
        """
        Checks for if a certain position on a row is free from danger by systematically checking each queen in relation
        to the position input.
        """
        for row in range(testrow):
            if column in (board[row], board[row] - row + testrow, board[row] + row - testrow):
                return False
        return True

    def place(self, board, row):
        """
        Main solving method in this class. If it hits a situation where a queen cannot be placed on a row without being
        in danger, it fizzles out. However, if all queens are placed, it forwards the board to the renderer for display
        and searches for another solution.
        """
        if row == self.size:
            self.counter += 1
            self.render(board)
        else:
            for column in range(self.size):
                if self.checker(board, row, column):
                    newBoard = board
                    newBoard[row] = column
                    self.place(newBoard, row + 1)

    def render(self, positions):
        """
        This renders a board from the list format used in this program. It converts the list to an array. The "-" spots
        are empty while the "Q" spots have a queen on them.
        """
        board = np.full((self.size, self.size), '-')
        for row in range(self.size):
            board[row][positions[row]] = 'Q'
        print("Solution number "+str(self.counter))
        print(board)
        print("\n")

    def run(self):
        """
        This begins the placer. It uses a different type of board than brute(). For example, brute would use
        [[0, 0, 1], [0, 1, 0], [1, 0, 0]
        while systematic() would use
        [2, 1, 0]
        This si easier to compute with math, but harder to visualize. It is also not practical for other chessboard
        programs as is only supports one piece per row.
        """
        board = [-1] * self.size
        self.place(board, 0)


if __name__ == '__main__':
    try:
        if solver == 's':
            np.set_printoptions(linewidth=4 * (n + 1))
            systematic(n)
        elif solver == 'b':
            brute(n)
        else:
            print("Invalid solver. Valid options for solver value are:\n's', 'b'")
    except KeyboardInterrupt:
        print("System inturrupted, terminating.")
    except ImportError:
        print("Import error, make sure the dependencies in the README were installed.")
