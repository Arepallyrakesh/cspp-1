# def clean_given_text(text_input):
#     words = text_input.lower().strip().replace('\'', '')
#     regex = re.compile('[^a-z]')
#     words = regex.sub(" ", words).split(" ")
#     return words

# import re
# import string
# frequency = {}
# document_text = open('test.txt', 'r')
# text_string = document_text.read().lower()
# match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
# for word in match_pattern:
#     count = frequency.get(word,0)
#     frequency[word] = count + 1
     
# frequency_list = frequency.keys()
 
# for words in frequency_list:
#     print words, frequency[words]
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))