'''
@author: Arepallyrakesh
'''
def mult_matrix(m_1 , m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''

    # result2 = []

    # result = [[0 for row in range(len(m_1 ))] for col in range(len(m_2[0]))]
    # for i in range(len(m_1    )):
    #     for j in range(len(m_2[0])):
    #         for k in range(len(m_2)):
    #             result[i][j] += m_1   [i][k] * m_2[k][j]
    #         # result1.append(result)
    #     # result1.append(result1)
    # return result
    add_ = re_mat(len(m_1), len(m_2[0]))
    if len(m_1  [0]) == len(m_2):
        for i in range(len(m_1)):
            for j in range(len(m_2[0])):
                for k in range(len(m_2)):
                    add_[i][j] += m_1   [i][k] * m_2[k][j]
        return add_
    else:
        print("Error: Matrix shapes invalid for mult")
        return None






def re_mat(rows, colums):
    '''
    empty matrix
    '''
    add_matrix = [[0 for i in range(colums)] for j in range(rows)]
    return add_matrix



def add_matrix(m_1  , m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    # if len(m_1    ) == len(m_2) and len(m_1   [0]) == len(m_2[0]):
    #     result1 = []
    #     for i in range(len(m_1    )):
    #         result = []
    #         for j in range(len(m_1    [0])):
    #             result.append(m_1 [i][j] + m_2[i][j])
    #             # result1.append(list(map(int,  )))
    #         result1.append(result)
    #     return result1
    # # except ValueError:
    # #     print("Matrix shapes invalid for add")
    # if len(m_1    ) == len(m_2) and len(m_1   [0]) == len(m_2[0]):
    # print(m_1 , m_2)
    # add_ = []
    # print(m_1 , m_2)
    add_ = re_mat(len(m_1   ), len(m_1  [0]))
    if len(m_1  ) == len(m_2) and len(m_1   [0]) == len(m_2[0]):
        for i in range(len(m_1  )):
            for j in range(len(m_1  [0])):
                # add_1 = add_
                add_[i][j] += (m_1  [i][j] + m_2[i][j])
        return add_
    else:
        print("Error: Matrix shapes invalid for addition")
        return None





def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    # mat = input().split(",")
    # row_size = int(mat[0])
    # column_size = int(mat[1])
    # matrix = []
    # for i in range(row_size):
    #     matrix.append(list(map(int, input().rstrip().split(" "))))

    # return matrix
    matrix = []
    list_input = input().split(",")
    rows, columns = int(list_input[0]), int(list_input[1])
    for _ in range(rows):
        list_mat_row = input().split()
        if columns == len(list_mat_row):
            matrix.append([int(i) for i in list_mat_row])
            # print(matrix)
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix
def main():
    # read matrix 1
    m_1  = read_matrix()
    if m_1   is None:
        exit()

    # read matrix 2
    m_2 = read_matrix()
    if m_2 is None:
        exit()
    # add matrix 1 and matrix 2
    print(add_matrix(m_1, m_2))

    # multiply matrix 1 and matrix 2
    print(mult_matrix(m_1, m_2))

if __name__ == '__main__':
    main()
