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
m1 = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
# count = 0
# for i in m1:
#     count += i.count('1')
# print(count)
for i in m1:
    for j in i:
        if j not  in 'xo.':
           print("invalid game")
        
print(m1)
# if (count_mat(m1, 'x') >= 5) or (count_mat(m1, 'o') >= 5) or count_mat(m1, 'x') == count_mat(m1, 'o'):
#         print("invalid game")
# else:
#     return m1
            
