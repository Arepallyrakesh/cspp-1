'''
    Document Distance - A detailed description is given in the PDF
'''
import re
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF

    '''
    # List = []
    # List2 = []
    # dict1.lower()
    # dict2.lower()
    clearstring1 = re.sub('\W+'," ", dict1 )
    clearstring2 = re.sub('\W+', " ",dict2 )
    clearstring1.lower()
    clearstring2.lower()
    x = clearstring1.split()
    y = clearstring2.split()
    
    print(x)
    print(y)
    # List1 = List1.append(list(dict1))
    # List2 = List2.append(list(dict2))

    stopwords_doc = load_stopwords("stopwords.txt")
    
    

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
