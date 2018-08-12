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

def calculateHandlen(hand):
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
	adict={}
	for i in range(int(n_input)):
		data=input()
		l_list=data.split()
		adict[l_list[0]]=int(l_list[1])
	print(calculateHandlen(adict))
		


if __name__ == "__main__":
	main()
