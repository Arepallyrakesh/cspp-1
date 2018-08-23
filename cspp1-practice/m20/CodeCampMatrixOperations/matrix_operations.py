def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
     
    # result2 = []
    
    # result = [[0 for row in range(len(m1))] for col in range(len(m2[0]))]
    # for i in range(len(m1)):
    #     for j in range(len(m2[0])):
    #         for k in range(len(m2)):
    #             result[i][j] += m1[i][k] * m2[k][j]
    #         # result1.append(result)
    #     # result1.append(result1)
    # return result
def re_mat(rows, colums):
    add_matrix = [[0 for i in range(colums)] for j in range(rows)]
    
    return add_matrix



def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
    # if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    #     result1 = []
    #     for i in range(len(m1)):
    #         result = []
    #         for j in range(len(m1[0])):
    #             result.append(m1[i][j] + m2[i][j])
    #             # result1.append(list(map(int,  )))
    #         result1.append(result)
                
    #     return result1
    # # except ValueError:
    # #     print("Matrix shapes invalid for add")
    # if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    # print(m1, m2)
    # add_ = []
 
    # print(m1, m2)
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        add_ = re_mat(len(m1), len(m1[0])) 
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                # add_1 = add_           
                add_[i][j] += (m1[i][j] + m2[i][j])
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
            print("error: invalid input")
            return None
    return matrix
def main():
    # read matrix 1
    m1 = read_matrix()
    # read matrix 2
    m2 = read_matrix()
    
    # add matrix 1 and matrix 2
    print(add_matrix(m1, m2))

    # multiply matrix 1 and matrix 2
    print(mult_matrix(m1, m2))
    

if __name__ == '__main__':
    main()
