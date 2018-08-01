'''
@author :Arepallyrakesh
print the message
'''
VARA = input()
VARB = input()
if type(VARA) == str or type(VARB) == str:
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA < VARB:
    print("smaller")
else:
    print("equal")
