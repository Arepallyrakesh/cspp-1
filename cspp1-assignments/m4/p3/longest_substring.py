'''
@author : Arepallyrakesh
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in
which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart
If you've spent more than a few hours on this problem, we
suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've
had a break and cleared your head.'''

def main():

    # the input string is in s
    # remove pass and start your code here
    '''
    program to print longest sequence in a string
    '''
    s_1 = input()
    s_2 = ""
    for i in range(len(s_1)-1):
        s_s = s_1[i]
        while i+1 < len(s_1) and s_1[i] <= s_1[i+1]:
            i = i + 1
            s_s = s_s + s_1[i]
        if len(s_s) > len(s_2):
            s_2 = s_s
    print(s_2)

if __name__ == "__main__":
    main()
