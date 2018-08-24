# def is_validation(m1):
def count(m1):
    sum1 = []
    for word in m1:
        sum1.append(word.count(word))
    return sum1

def is_validation(m1):
    for i in m1:
        for j in i:
              if j in 'xo.':
                print("Invalid input") 
    

def read_input():
    matrix = []
    # list_input = input().split(" ")
    # rows, columns = list_input[0], list_input[1]
    # print(list_input[1])
    # for _ in range(rows):
    #     if columns == rows:
    #         matrix.append([int(i) for i in list_mat_row])
    #         # print(matrix)
    #     else:
    #         print("Error: Invalid input")
    #         return None
    # return matrix
    for i in range(3):
        list_input = input().split(" ")
        matrix.append(list_input)
    return matrix 


def main():
    m1 = read_input()
    print(m1)

main()