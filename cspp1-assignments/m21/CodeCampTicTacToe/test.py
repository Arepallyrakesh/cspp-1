# import itertools
# def read_input():
#     list1 = []
#     matrix = []
#     for i in range(3):
#         list_input = input()
#         matrix.append(list(itertools.chain(*list_input)))
#     return matrix 

# # list1=[[1, 2], [2], [2, 3]]
# # print(list(itertools.chain(*list1)))


# def main():
#     m1 = read_input()
#     print(m1)

# main()
m1 = [['1', '1', '2'], ['1', '2', '3'], ['5', '1', '2']]
count = 0
for i in m1:
    count += i.count('1')
print(count)

