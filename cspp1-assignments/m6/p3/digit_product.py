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
    n_i = int((input()))
    if n_i >= 0:
        la = list(str(n_i))
        s = 1
        for i in str(n_i):
            s = s * int(i)
        print(s)
    else:
        n_i = -(n_i)
        la = list(str(n_i))
        s = 1
        for i in str(n_i):
            s = s * int(i)
        print(-s)
if __name__ == "__main__":
    main()
