'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def read_input():
	input1 = int(input())
	list1 = []
	for i in range(input1):
		input_str = input()
		list1.append(input_str)
		text = '\n'.join(list1)
	return text 


def main():
	print(read_input())
    

if __name__ == '__main__':
    main()


# matrix = []
#     list_input = input().split(",")
#     rows, columns = int(list_input[0]), int(list_input[1])
#     for _ in range(rows):
#         list_mat_row = input().split()
#         if columns == len(list_mat_row):
#             matrix.append([int(i) for i in list_mat_row])
#             # print(matrix)
#         else:
#             print("Error: Invalid input for the matrix")
#             return None
#     return matrix