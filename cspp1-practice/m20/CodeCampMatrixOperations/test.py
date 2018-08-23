# m = int(input('number of rows, m = '))
# n = int(input('number of columns, n = '))
# matrix = []; columns = []
# # initialize the number of rows
# for i in range(0,m):
#   matrix += [0]
# # initialize the number of columns
# for j in range (0,n):
#   columns += [0]
# # initialize the matrix
# for i in range (0,m):
#   matrix[i] = columns
# for i in range (0,m):
#   for j in range (0,n):
#     print ('entry in row: ',i+1,' column: ',j+1)
#     matrix[i][j] = int(input())
# print (matrix)
# # mat = []
# mat_s = input().split(",")
# for i in range(len(mat_s) + 1):
# 	mat.append(input().split(" "))
# print(mat)
mat = input().split(",")
row_size = int(mat[0])
column_size = int(mat[1])
print(row_size, column_size)
matrix = []
for i in range(row_size):
	matrix.append(list(map(int, input().rstrip().split())))
	# for j in range(column_size):
	# 	matrix[i][j] = matrix.append(input().split(" "))
print(matrix)
		
# for i,j in range(row_size, column_size):
# 	matrix[i][j] = 
# print(matrix)

