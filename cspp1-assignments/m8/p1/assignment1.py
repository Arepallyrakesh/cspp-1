'''
@author : Arepallyrakesh
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def factorial_in(n):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n == 0:
        return 1
    else:
        return n * factorial_in(n - 1)

def main():
    '''
    Write a Python function, factorial(n), that takes in
    one number and returns the factorial of given number
    '''
    a = input()
    print(factorial_in(int(a)))    
if __name__ == "__main__":
    main()
