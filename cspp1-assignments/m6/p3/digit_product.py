'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = (input())
    st = str(int_input)
    l = len(int_input)
    s=0  
    for i in range(l):
    	while i <= l:
    		s = s *st[i]
    		print(s)

    


if __name__ == "__main__":
    main()
