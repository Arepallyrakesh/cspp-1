# https://www.geeksforgeeks.org/enumerate-in-python/
import re
my_list = ['Computers makes as many mistakes in one second as three men working for thirty years straight.', 'Talk is cheap. Show me the code.', "That's the thing about people who think they hate computers. What they really hate is lousy programmer.", "I'm not a great programmer; I'm just a good programmer with great habits.", 'Any fool can write code that computers can understand. Good programmers write code that humans can understand.', "At forty, I was too old to work as a programmer myself anymore; writing code is a young person's job."]
removetable = str.maketrans('', '', '@#%123456789')
x = [s.translate(removetable) for s in my_list]
stri = ''.join(x)
print(stri)
exam = stri.lower().strip()
regex = re.compile('[^a-z]')
words = regex.sub(" ", exam).split(" ")
print(words)
dictionary = {}
stopwords = load_stopwords("stopwords.txt")
for word in words_list:
word = word.strip()
if word not in stopwords and len(word) > 0:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
    print(dictionary)
# given_words = word_input.lower().strip().replace('\'', '')
#     regex = re.compile('[^a-z]')
#     words = regex.sub(" ", given_words).split(" ")
#     return words

    # def combine_dict(word_one, word_two):
    '''returns dictionary
    # '''
    # dictionary = {}
    # for word in word_one:
    #     if word in word_two:
    #         dictionary[word] = [word_one[word], word_two[word]]

    # for word in word_one:
    #     if word not in dictionary:
    #         dictionary[word] = [word_one[word], 0]
    # for word in word_two:
    #     if word not in dictionary:
    #         dictionary[word] = [0, word_two[word]]
    # return dictionary

    # def create_dict_of_values(words_list):
    # '''
    # removing the spaces
    # '''
    # dictionary = {}
    # stopwords = load_stopwords("stopwords.txt")
    # for word in words_list:
    #     word = word.strip()
    #     if word not in stopwords and len(word) > 0:
    #         if word not in dictionary:
    #             dictionary[word] = 1
    #         else:
    #             dictionary[word] += 1
    # return dictionary