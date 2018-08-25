'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string, input1):
    counts = {}
    string.split()
    for word in string:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
            
def main():
    input1 = int(input())
    input_str = input()
    text = ''.join(input_str)
    print(text)
    print(tokenize(text, input1))
if __name__ == '__main__':
    main()



# from collections import defaultdict
# fq= defaultdict( int )
# for w in words:
#     fq[w] += 1