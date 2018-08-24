

def take_input():
    matrix = []
    for _ in range(3):
        matrix.append(input().strip().split())
    return matrix

def is_valid_character(matrix):
    for row in matrix:
        for element in row:
            if element not in ['x', 'o', '.']:
                return False
    return True

def is_valid_rules(matrix):
    for row in matrix:
        x_count += row.count('x') 
        o_count += row.count('o')
    if o_count > 5 or x_count > 5 or o_count == x_count:
        return False
    return True

def check_valid_rules(matrix):
    for index_row,row in enumerate(matrix):
        if len(set(row)) == 1 and row[0] == variable:
            return True
            for index_col, element in enumerate(row):


def decide_winner(matrix, variable):
    # for row in matrix:
    # return False

def main():
    matrix = take_input()
    chk = is_valid_character(matrix)
    if chk:
        if decide_winner(matrix, 'x')
    elif decide_winner(matrix, 'o')
    else:
        print("invalid input")

main()
    


