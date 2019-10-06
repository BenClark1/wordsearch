# Project 4: Word Search
# Author: Ben Clark

def get_puzzle():
    puzzle = input("")
    words = input("")
    return (puzzle, words.split())

def puzzle_to_list(puzzle):
    # converts input string to a list of strings of length 10
    listOut = []
    for i in range(10):
        new_str = ""
        for j in range(10*i, 10*(i+1)):
            new_str += puzzle[j]
        listOut.append(new_str)
    return listOut

def check_forward(puzzle, words):
    # takes a puzzle in list format and a list of words 
    # searches for forward-oriented words
    words_found = {}
    for row in puzzle:
        for word in words:
            if row.find(word) >= 0:
                col_result = row.find(word)
                row_result = puzzle.index(row)
                words_found[word] = (row_result, col_result)
    return words_found 

def check_backward(puzzle, words):
    # searches for backward oriented words
    backward_puz = [i[::-1] for i in puzzle]
    words_found = check_forward(backward_puz, words) #indecies not yet corrected
    for word in words_found:
        words_found[word] = backward_index_converter(words_found[word])
    return words_found

def backward_index_converter(location):
    # the argument location is a tuple of two indecies, row and col
    # converts indecies from a backward puzzle to the correct indecies
    backward = "9876543210"
    row_result = location[0] # here, the row doesn't change
    col_result = int(backward[location[1]])
    return (row_result, col_result)

def check_down(puzzle, words):
    downward_puz = [] 
    # this converts downward columns to forward rows
    for i in range(len(puzzle[0])): # iterate through each column index
        column_list = [str(row[i]) for row in puzzle]
        downward_puz.append("".join(column_list))

    words_found = check_forward(downward_puz, words)
    for word in words_found: # correct the indecies
        words_found[word] = downward_index_converter(words_found[word])
    return words_found

def downward_index_converter(location):
    # the argument location is a tuple of two indecies, row and col
    # this function switches the two indecies
    row_result = location[1]
    col_result = location[0]
    return (row_result, col_result)

def check_up(puzzle, words):
    # convert to downward puzzle first
    downward_puz = []
    for i in range(len(puzzle[0])):
        column_list = [str(row[i]) for row in puzzle]
        downward_puz.append("".join(column_list))
    # then reverse that to get an upward puzzle
    upward_puz = [i[::-1] for i in downward_puz]

    words_found = check_forward(upward_puz, words)
    for word in words_found: #correct the indecies 
        words_found[word] = backward_index_converter(words_found[word])
        words_found[word] = downward_index_converter(words_found[word])
    return words_found

def check_diagonal(puzzle, words):
    shifted_puzzle = []
    for i in range(10):
        shifted_string = puzzle[i][i:] + puzzle[i][:i]
        shifted_puzzle.append(shifted_string)

    row_col_switched = []
    for i in range(len(shifted_puzzle[0])):
        column_list = [str(row[i]) for row in shifted_puzzle]
        row_col_switched.append("".join(column_list))

    words_found = check_forward(row_col_switched, words)
    for word in words_found:
        words_found[word] = diagonal_index_converter(words_found[word])
    
    return words_found
        
def diagonal_index_converter(location):
    new_location = downward_index_converter(location)
    row_result = new_location[0]
    col_result = new_location[1] + row_result
    if col_result > 9:
        col_result -= 10
    return (row_result, col_result)

def display_solution(puzzle, words, forwards, backs, downs, ups, diagonals):
    print("Puzzle:\n")
    for row in puzzle:
        print(row)
    print("\n", end='')
    
    for key in forwards:
        row_string = str(forwards[key][0])
        col_string = str(forwards[key][1])
        print(key+": (FORWARD) row: "+row_string+" column: "+col_string)
    
    for key in backs:
        row_string = str(backs[key][0])
        col_string = str(backs[key][1])
        print(key+": (BACKWARD) row: "+row_string+" column: "+col_string)

    for key in downs:
        row_string = str(downs[key][0])
        col_string = str(downs[key][1])
        print(key+": (DOWN) row: "+row_string+" column: "+col_string)

    for key in ups:
        row_string = str(ups[key][0])
        col_string = str(ups[key][1])
        print(key+": (UP) row: "+row_string+" column: "+col_string)

    for key in diagonals:
        row_string = str(diagonals[key][0])
        col_string = str(diagonals[key][1])
        print(key+": (DIAGONAL) row: "+row_string+" column: "+col_string)

    for word in words:
        not_in1 = word not in forwards
        not_in2 = word not in backs
        not_in3 = word not in downs
        not_in4 = word not in ups
        not_in5 = word not in diagonals
        if not_in1 and not_in2 and not_in3 and not_in4 and not_in5:
            print(word+": word not found")



