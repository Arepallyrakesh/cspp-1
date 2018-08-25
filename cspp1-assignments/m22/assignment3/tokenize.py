'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

import re
def tokenize(string, input1):
    regex = re.compile('[^a-z0-9]+')
    string = regex.sub("", string).split()
    counts = {}
    words = string
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
def main():
    input1 = int(input())
    input_str = input()
    text = ''.join(input_str)
    text.split()
    print(tokenize(text, input1))
if __name__ == '__main__':
    main()



# from collections import defaultdict
# fq= defaultdict( int )
# for w in words:
#     fq[w] += 1