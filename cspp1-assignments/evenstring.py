'''
@author : Arepallyrakesh
multiple of the number
'''
S = "rakesh"
L = len(S)
M = ""
N = ""
for i in range(L):
    if i%2 == 0:
        M += S[i]
    if i%2 != 0:
        N += S[i]
print(M, N)
