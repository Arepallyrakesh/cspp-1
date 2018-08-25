'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string, input1):
    '''
    tokenize the string
    '''
    # regex = re.compile('[^a-z0-9]+')
    # string = regex.sub("", string)
    words = string.split()
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary
def main():
    '''
    main function
    '''
    input1 = int(input())
    input_str = input()
    text = ''.join(input_str)
    text.split()
    print(tokenize(text, input1))
if __name__ == '__main__':
    main()
