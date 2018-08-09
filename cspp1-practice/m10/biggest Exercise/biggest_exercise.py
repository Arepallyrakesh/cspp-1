#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maximum = 0
    ans = 0
    for i in aDict:
        if type(aDict[i]) == list or type(aDict[i]) == tuple:
            if len(aDict[i]) > maximum:
                maximun = len(aDict[i])
                ans = i
    return ans,maximun


    

def main():
    # aDict={}
    # s=input()
    # l=s.split()
    # if l[0][0] not in aDict:
    #     aDict[l[0][0]]=[l[1]]
    # else:
    #     aDict[l[0][0]].append(l[1])
    aDict = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd' : ['donkey', 'dog', 'dingo']}
    print(biggest(aDict))

if __name__== "__main__":
    main()