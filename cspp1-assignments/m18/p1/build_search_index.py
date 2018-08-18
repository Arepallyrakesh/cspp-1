'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

# helper function to load the stop words from a file
import re

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    remove = str.maketrans('', '', '@#%123456789')
    x_lis = [s.translate(remove) for s in text]
    string = ''.join(x_lis)
    string1 = string.lower().strip()
    regex = re.compile('[^a-z]')
    list1 = regex.sub(" ", string1).strip().split(" ")
    return list1

    
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    
    document_1 = word_list(docs)
    # print(document_1)
    search_index = {}
    
    # print(document_1)
    for ind, word in enumerate(docs):
        list1 = remove_swords(word_list(word))
        for i in set(list1):
            if i in search_index:
                search_index[i].append((ind, list1.count(i)))
            else:
                search_index[i] = [(ind, list1.count(i))]
    return search_index

def remove_swords(word1):
    list2 = word1
    stop_words = load_stopwords("stopwords.txt")
    for i in word1:
        if i in stop_words:
            list2.remove(i)
    return list2
    # for word in document_1:
    #     word = word.strip()
        
    #     if word not in stopwords and len(word) > 0:
    #         if word not in  search_index:
    #             search_index[word]  = 1
    #         else:
    #             search_index[word] += 1
    
    # return search_index



# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    list2=[]
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
