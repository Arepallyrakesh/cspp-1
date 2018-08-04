'''
@author : Arepallyrakesh
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    s_1 = 0
    f_1 = 0
    for i in range(1, num+1, 1):
        if i%3 !=0 and i%5 !=0:
            print(i)
        if i%3 ==0:
            s_1 = 3*i
            print("Fizz")
        if i%5 == 0:
            f_1 = 5*i
            print("Buzz")

if __name__ == "__main__":
    main()
