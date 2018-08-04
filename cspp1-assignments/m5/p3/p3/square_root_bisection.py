'''
@author : Arepallyrakesh
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    '''
   Write a python program to find the square root of the given number
    '''
    s_i = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    # your code starts here
    low = 0.0
    h_v = s_i
    bi_v = (h_v + low)/2.0
    while abs(bi_v**2 - s_i) > epsilon:
        if bi_v**2 < s_i:
            low = bi_v
        else:
            h_v = bi_v
        bi_v = (h_v + low)/2.0
    print(bi_v)
if __name__ == "__main__":
    main()
