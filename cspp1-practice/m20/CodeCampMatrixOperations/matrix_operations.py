def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
     
    # result2 = []
    for i in range(len(m1)):
        result1 = []
        for j in range(len(m2[0])):
            result = []
            for k in range(len(m2)):
                result.append(m1[i][k] * m2[k][j])
            result1.append(result)
        result1.append(result1)
    return result1
  



def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    
    
    result1 = []
    for i in range(len(m1)):
        result = []
        for j in range(len(m1[0])):
            result.append(m1[i][j] + m2[i][j])
            # result1.append(list(map(int,  )))
        result1.append(result)
            
    return result1
    # except ValueError:
    #     print("Matrix shapes invalid for add")


def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    mat = input().split(",")
    row_size = int(mat[0])
    column_size = int(mat[1])
    matrix = []
    for i in range(row_size):
        matrix.append(list(map(int, input().rstrip().split(" "))))
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
