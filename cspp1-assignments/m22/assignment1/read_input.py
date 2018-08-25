'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def read_input():
    '''
    read input
    '''
    input1 = int(input())
    list1 = []
    for _ in range(input1):
        input_str = input()
        list1.append(input_str)
        text = '\n'.join(list1)
    return text 
def main():
    print(read_input())
if __name__ == '__main__':
    main()
