'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def combine_dictonary(dictionary_one, dictionary_two):
    dictionary = {}
    for word in dictionary_one:
        if word in dictionary_two:
            dictionary[word] = [dictionary_one[word], dictionary_two[word]]
    for word in dictionary_one:
        if word not in dictionary:
            dictionary[word] = [dictionary_one[word], 0]
    for word in dictionary_two:
        if word not in dictionary:
            dictionary[word] = [0, dictionary_two[word]]
    return dictionary

def clean_given_text(text_input):
    words = text_input.lower().strip().replace('\'','')
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words

def create_dictionary(word_list):
    '''
    returnns str and returns list.
    '''
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in words_list:
        word = word.strip()
        if word not in stopwords and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary



def calculate_similarity(dictionary):
    numerator = sum([k[0] *  k[1] for k in dictionary.values()])
    d1 = math.sqrt(sum([k[0] ** 2 for k in dictionary.values()]))
    d2 = math.sqrt(sum([k[1] ** 2 for k in dictionary.values()]))
    return numerator/(d1*d2)

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF

    '''
    # dict_1 = {}
    # dict_2 = {}
    # dict_3 = {}
    # # List = []
    # # List2 = []
    # # dict1.lower()
    # # dict2.lower()
    # clearstring1 = re.sub('\W+'," ", dict1 )
    # clearstring2 = re.sub('\W+', " ",dict2 )
    # clearstring1.lower()
    # clearstring2.lower()
    # x = clearstring1.split()
    # y = clearstring2.split()
    
    # print(x)
    # print(y)
    # List1 = List1.append(list(dict1))
    # List2 = List2.append(list(dict2))

    # stopwords_doc = load_stopwords("stopwords.txt")

    # for i in x:
    #     if i not in stopwords_doc:
    #         if i not in dict_1:
    #             dict_1[i] = 1
    #         else:
    #             dict_1[i] += 1
    # print(dict_1)
    
    # for i in y:
    #     if i not in stopwords_doc:
    #         if i not in dict_2:
    words_list_one = clean_given_text(dict1)
    words_list_one = clean_given_text(dict2)
    dictionary = combine_dictonary(dictionary_one, dictionary_two)
    return (sorted(dictionary_two), sorted(dictionary_one))
    

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
