'''
@uthor : Arepallyrakesh
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    n = int((input()))
    if n >= 0:
        la = list(str(n))
        s = 1
        for i in str(n):
            s = s * int(i)
        print(s)
    else:
        n = -(n)
        la = list(str(n))
        s = 1
        for i in str(n):
            s = s * int(i)
        print(-s)
if __name__ == "__main__":
    main()
