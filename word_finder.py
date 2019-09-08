# Project 4: Word Search
# Author: Ben Clark

import funcs

print("\n", end='')
puzzle, words = funcs.get_puzzle()
puzzle = funcs.puzzle_to_list(puzzle)

forwards = funcs.check_forward(puzzle, words)
backs = funcs.check_backward(puzzle, words)
downs = funcs.check_down(puzzle, words)
ups = funcs.check_up(puzzle, words)
diagonals = funcs.check_diagonal(puzzle, words)

funcs.display_solution(puzzle, words, forwards, backs, downs, ups, diagonals)
print("\n", end='')



