#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the same column for any queen
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal for any queen
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper right diagonal for any queen
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N, row, board, solutions):
    """Recursively soolve the N Queens problem."""
    if row == N:
        # Found a solution, add it to the list
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col  # Place queen
                solve_nqueens(N, row + 1, board, solutions)  # Recurse
                board[row] = -1  # Backtrack


def nqueens(N):
    """Solve the N Queens problem and print each solution."""
    board = [-1] * N  # Represent the position of queens on the board
    solutions = []  # List to store solutions
    solve_nqueens(N, 0, board, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Argument handling
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print the solution
    nqueens(N)
