import itertools
def read_input():
    list1 = []
    matrix = []
    for i in range(3):
        list_input = input()
        matrix.append(list(itertools.chain(*list_input)))
    return matrix 

# list1=[[1, 2], [2], [2, 3]]
# print(list(itertools.chain(*list1)))


def main():
    m1 = read_input()
    print(m1)

main()