'''
@author : Arepallyrakesh
#Exercise: Assignment-4
#We are now ready to begin writing the code
that interacts with the player. We'll be implementing
the playHand function. This function allows the user to
play out a single hand. First, though, you'll need to
implement the helper calculateHandlen function,
which can be done in under five lines of code.
''' 

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    count = 0
    for i in hand:
        count += hand[i]
    return count

def main():
    ''' 
    main function
    ''' 
    n_input=input()
    a_dict={}
    for data in range(int(n_input)):
        data=input()
        l_list=data.split()
        a_dict[l_list[0]]=int(l_list[1])
    print(calculate_handlen(a_dict))



if __name__ == "__main__":
    main()
