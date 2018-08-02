'''
@author : Arepallyrakesh
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels
contained in the string s Valid vowels are: 'a', 'e', 'i', 'o', and 'u'
For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
'''
def main():
    '''
     Write a program that counts up the number of vowels
contained in the string s Valid vowels are: 'a', 'e', 'i', 'o', and 'u'
    '''
    s_i = input()
    # the input string is in s
    # remove pass and start your code here
    co_ov = 0
    for var in s_i:
        if var in "aeiou":
            co_ov += 1
    print(co_ov)
 