'''
@author:Arepallyrakesh
'''
def count_mat(m1, cnt):
    '''
    counting the values
    '''
    count1 = 0
    for word in m1:
        count1 += word.count(cnt)
    return count1
def is_validation(m1):
    '''
    validation of matrices
    '''
    for i in m1:
        for j in i:
            if j not  in 'xo.':
                print("invalid input")
                return False
    if (count_mat(m1, 'x') == 4 and count_mat(m1, 'o') ==5)  or \
     (count_mat(m1, 'x') == 5 and count_mat(m1, 'o') == 4):
        print("draw")
        return False
    if (count_mat(m1, 'x') > 5) or (count_mat(m1, 'o') > 5) or\
     count_mat(m1, 'x') == count_mat(m1, 'o'):
        print("invalid game")
        return False
    return True
def result_int(m1):
    '''
    result of input
    '''
    if m1[0][0] == m1[1][1] == m1[2][2]:
        return m1[0][0]
    elif m1[0][0] == m1[0][1] == m1[0][2]:
        return m1[0][1]
    elif m1[1][0] == m1[1][1] == m1[1][2]:
        return m1[1][0]
    elif m1[2][0] == m1[2][1] == m1[2][2]:
        return m1[2][0]
    elif m1[0][0] == m1[1][0] == m1[2][0]:
        return m1[0][0]
    elif m1[0][1] == m1[1][1] == m1[2][1]:
        return m1[0][1]
    elif m1[0][2] == m1[1][2] == m1[2][2]:
        return m1[0][2]
    elif m1[2][0] == m1[1][1] == m1[0][2]:
        return m1[2][0]
    else:
        return ("invalid input")
def read_input():
    '''
    read the input
    '''
    matrix = []
        for i in range(3):
        list_input = input().split(" ")
        matrix.append(list_input)
    return matrix
def main():
    '''
    main function
    '''
    m1 = read_input()
    if is_validation(m1):
        print(result_int(m1))
main()
