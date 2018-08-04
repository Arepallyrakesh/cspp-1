'''
@author : Areapallyrakesh
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
'''

def main():
    '''
    Write a python program to find if the given number is a perfect cube or not
    '''
    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here
    c_b = int(input())
    g_s = 1
    while (g_s**3) < c_b:
        g_s += 1
    if int(g_s**3) == c_b:
        print(c_b, "is a perfect cube")
    else:
        print(c_b, "is not a perfect cube")
if __name__ == "__main__":
    main()
