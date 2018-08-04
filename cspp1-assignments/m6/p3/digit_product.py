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
        s_a = 1
        for i in str(n_i):
            s_a = s_a * int(i)
        print(s_a)
    else:
        n_i = -(n_i)
        s_a = 1
        for i in str(n_i):
            s_a = s_a * int(i)
        print(-s_a)
if __name__ == "__main__":
    main()
