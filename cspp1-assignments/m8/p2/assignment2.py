# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n == 1:
    	return 1
    else:
    	return n + sumofdigits(n-1)


def main():
    a = input()
    print(sumofdigits(int(a)))  

if __name__== "__main__":
    main()

