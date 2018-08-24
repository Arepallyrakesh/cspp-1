# def is_validation(m1):
def count_mat(m1, cnt):
    sum1 = []
    for word in m1:
        sum1.append(word.count(cnt))
    return sum(sum1)

def is_validation(m1):
    for i in m1:
        for j in i:
            if j in 'xo.':
              return ("Invalid input") 
    if (count_mat(m1,x) > 5) or (count_mat(m1,o) >= 5) or count_mat(m1,x) = count_mat(m1,o):
       return ("Invalid input")
    


def read_input():
    matrix = []
    for i in range(3):
        list_input = input().split(" ")
        matrix.append(list_input)
    return matrix 


def main():
    m1 = read_input()
    print(m1)

main()