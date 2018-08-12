'''
@author : Arepallyrakesh
# Assignment-3
At this point, we have written code to generate
a random hand and display that hand to the user.
We can also ask the user for a word (Python's input)
and score the word (using your getWordScore).
However, at this point we have not written any code to verify that a word
given by a player obeys the rules of the game. A valid word is in the
word list; and it is composed entirely of letters from the current hand.
Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition,
you will want to test your implementation by calling it multiple
times on the same hand - what should the correct behavior be? Additionally,
the empty string ('') is not a valid word - if you code this function correctly,
you shouldn't need an additional check for this condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed the
appropriate tests in test_ps4a.py before pasting your function definition here.
'''

def is_valid_word(w_ord, h_and, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    count = 0
    if w_ord in word_list:
        for i in word_list:
            if i in h_and and h_and[i] > 0:
                count += 1
    return count == len(w_ord) 


def main():
    ''' 
    main function
    '''
    w_ord = input()
    n_input = int(input())
    a_dict = {}
    for data in range(n_input):
        data = input()
        l_ist = data.split()
        a_dict[l_ist[0]] = int(l_ist[1])
    l2_list = input().split()
    print(is_valid_word(w_ord, a_dict, l2_list))



if __name__ == "__main__":
    main()
