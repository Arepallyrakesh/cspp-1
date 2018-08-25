'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def row_sudoku(sudoku):
    for value in sudoku:
        if len(set(value)) != 9:
            return False
    return True
def col_sudoku(sudoku):
    """checks for valid coloumn"""
    list1 = []
    for value in range(len(sudoku)):
        row = []
        for j in range(len(sudoku[0])):
            row.append(sudoku[i][j])
        list1.append(row)
        value += 1
    return rows(list1)

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # list1 = []
    # for i in sudoku:
    #     if len(set(i)) == 9:
    #     for i in range(len(sudoku)):
    #         row = []
    #         for j in range(len(sudoku[0])):
    #             row.append(sudoku[j][i])
    #             list1.append(row)
    #             i += 1
    # return list1
    return row_sudoku(sudoku) and col_sudoku(sudoku)



def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()


