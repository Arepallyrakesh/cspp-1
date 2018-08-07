'''
@author : Arepallyrakesh
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def factorial_in(n_in):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_in == 0:
        return 1
    return n_in * factorial_in(n_in - 1)

def main():
    '''
    Write a Python function, factorial(n), that takes in
    one number and returns the factorial of given number
    '''
    a_in = input()
    print(factorial_in(int(a_in)))
if __name__ == "__main__":
    main()
