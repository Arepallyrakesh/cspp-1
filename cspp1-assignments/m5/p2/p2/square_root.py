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
    step = 0.1
    # your code starts here
    g_s = 0.0
    while g_s <= s_i:
        if abs(g_s**2-s_i) < epsilon:
            break
        else:
            g_s = g_s + step
    print(str(g_s))
if __name__ == "__main__":
    main()
