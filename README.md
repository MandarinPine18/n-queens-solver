# N-Queens Puzzle Solver

## Overview
This is a solver for the n-queens puzzle. It can work with any number of queens (https://en.wikipedia.org/wiki/Eight_queens_puzzle)

## Installation
Please install **Python 3.7** and **pip**. Use pip to install **numpy**. Use git to clone this repository.

## Usage
Once in the directory, use the following command to start the guesser.
```sh
  python3.7 guesser.py
```

Included are two solvers: an early brute force solver and a more optimized systematic solver. The brute force solver is not recommended as it only prints one solution and it is very slow with a large number of queens. The systematic colver is far faster and outputs all solutions(press Ctrl+C to exit with large values of n, where there are thousands of solutions output).

## License
This is licensed under GNU GPL v3, included in the file named LICENSE.
