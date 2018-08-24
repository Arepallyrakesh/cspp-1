'''
@author:Arepallyrakesh
'''
def count_mat(m_1, cnt_var):
    '''
    counting the values
    '''
    count1 = 0
    for word in m_1:
        count1 += word.count(cnt_var)
    return count1
def is_validation(m_1):
    '''
    validation of matrices
    '''
    for i in m_1:
        for j in i:
            if j not  in 'xo.':
                print("invalid input")
                return False
    if (count_mat(m_1, 'x') == 4 and count_mat(m_1, 'o') == 5)  or \
     (count_mat(m_1, 'x') == 5 and count_mat(m_1, 'o') == 4):
        print("draw")
        return False
    if (count_mat(m_1, 'x') > 5) or (count_mat(m_1, 'o') > 5) or\
     count_mat(m_1, 'x') == count_mat(m_1, 'o'):
        print("invalid game")
        return False
    return True
def result_int(m_1):
    '''
    result of input
    '''
    if m_1[0][0] == m_1[1][1] == m_1[2][2]:
        return m_1[0][0]
    elif m_1[0][0] == m_1[0][1] == m_1[0][2]:
        return m_1[0][1]
    elif m_1[1][0] == m_1[1][1] == m_1[1][2]:
        return m_1[1][0]
    elif m_1[2][0] == m_1[2][1] == m_1[2][2]:
        return m_1[2][0]
    elif m_1[0][0] == m_1[1][0] == m_1[2][0]:
        return m_1[0][0]
    elif m_1[0][1] == m_1[1][1] == m_1[2][1]:
        return m_1[0][1]
    elif m_1[0][2] == m_1[1][2] == m_1[2][2]:
        return m_1[0][2]
    elif m_1[2][0] == m_1[1][1] == m_1[0][2]:
        return m_1[2][0]
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
    m_1 = read_input()
    if is_validation(m_1):
        print(result_int(m_1))
main()
