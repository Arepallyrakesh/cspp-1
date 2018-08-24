# def is_validation(m1):
def count_mat(m1, cnt):
    # sum1 = []
    # for word in m1:
    #     sum1.append(word.count(cnt))
    # print(sum(sum1))
    count1 = 0
    for word in m1:
        count1 += word.count(cnt)
    return count1


def is_validation(m1):         
    for i in m1:
        for j in i:
            if j not  in 'xo.':
                return "invalid game"
                exit()
            elif (count_mat(m1, 'x') >= 5) or (count_mat(m1, 'o') >= 5) or count_mat(m1, 'x') == count_mat(m1, 'o'):
                return "invalid game"
                exit()
            else:
                return m1
            
             
    
# def string1(m1):
#     print(list(itertools.chain(*m1)))
def result_int(m1):
    # for cnt in m1:
        if m1[0][0] == m1[1][1] == m1[0][1]:

            return m1[0][0]
            # exit()

        elif m1[0][0] == m1[0][1] == m1[0][2]:

            return m1[0][0]
            # exit()
        elif m1[1][0] == m1[1][1] == m1[2][1]:

            return m1[1][0]
            # exit()
        elif m1[2][0] == m1[2][1] == m1[2][2]:

            return m1[2][0]
            # exit()
        elif m1[0][0] == m1[1][0] == m1[2][0]:

            return m1[0][0]
            # exit()
        elif m1[0][1] == m1[1][1] == m1[2][1]:

            return m1[0][1]
            # exit()
        elif m1[0][2] == m1[1][2] == m1[2][2]:

            return m1[0][2]
            # exit()
        elif m1[2][0] == m1[1][1] == m1[0][2]:
            return m1[2][0]

    
            # exit()
def read_input():
    matrix = []
    
    for i in range(3):
        list_input = input().split(" ")
        matrix.append(list_input)
    return matrix


def main():
    m1 = read_input()
    print(result_int(is_validation(m1)))

main()