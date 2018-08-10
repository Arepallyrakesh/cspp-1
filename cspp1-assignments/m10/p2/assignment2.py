'''
@author : Arepallyrakesh
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secret_word
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
WORDlist_in_FILENAME = "words.txt"
def load_words():
    """
    Returns a list_in of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list_in, this function may
    take a while to finish.
    """
    print("Loading word list_in from file...")
    # in_file: file
    in_file = open(WORDlist_in_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # word_list_in: list_in of strings
    word_list_in = line.split()
    print("  ", len(word_list_in), "words loaded.")
    return word_list_in
def choose_word(word_list_in):
    """
    word_list_in (list_in): list_in of words (strings)

    Returns a word from word_list_in at random
    """
    return random.choice(word_list_in)
# end of helper code
# -----------------------------------
# Load the list_in of words into the variable word_list_in
# so that it can be accessed from anywhere in the program
word_list_in = load_words()
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list_in, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secret_word:
        if i in letters_guessed:
            return True
    return False
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list_in, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    w_s = ""
    for i in secret_word:
        if i not in letters_guessed:
            w_s = w_s + "_"
        else:
            w_s = w_s + i
    return w_s
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list_in, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s_2 = ""
    strin = string.ascii_lowercase
    # string = "abcdefghijklmnopqrstuvwxyz"
    for i in strin:
        if i not in letters_guessed:
            s_2 = s_2 + i
    return s_2
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " +  str(len(secret_word)) +" letters long")
    wrong_guess = 8
    enter_character = ""
    list_in = []
    #wordguess = False
    while True:
        print("----------------")
        print("You have " + str(wrong_guess)  + " guesses left")
        print("Available letters :" + get_available_letters(enter_character))
        char_in = input("please guess a letter: ")
        enter_character = enter_character + " " + char_in
        if char_in not in list_in:
            if is_word_guessed(secret_word, char_in):
                print("Good guess: " + get_guessed_word(secret_word, enter_character.split()))
                list_in = list_in + enter_character.split()
            else:
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, enter_character.split()))
                wrong_guess -= 1
        else:
            print("Oops! You've already guessed that letter: " + get_guessed_word(secret_word, enter_character.split()))
        list_in = list_in + enter_character.split()
        if get_guessed_word(secret_word, enter_character.split()) == secret_word:
            print("Congratulations, you won!")
            break
        elif wrong_guess == 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word)
            break
def main():
    '''
    Main function for the given program
        When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secret_word while you're testing)
    '''
    secret_word = choose_word(word_list_in).lower()
    hangman(secret_word)
if __name__ == "__main__":
    main()
