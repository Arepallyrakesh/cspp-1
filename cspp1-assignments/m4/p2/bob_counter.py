'''
@author : Arepallyrakesh
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''
    Write a program that prints the number of times the string 'bob' occurs in s.
    '''
    s_1 = input()
    # the input string is in s
    # remove pass and start your code here
    s_2 = "bob"
    c_h = 0
    for i in range(len(s_1)-2):
        count = 0
        j = 0
        k = i
        while (j < 3 and s_1[k] == s_2[j]):
            count = count + 1
            j = j + 1
            k = k + 1
        if count == 3:
            c_h = c_h + 1
    print(c_h)

if __name__ == "__main__":
    main()
