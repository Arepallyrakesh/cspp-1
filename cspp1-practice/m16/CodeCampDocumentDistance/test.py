# List1 = []
# List2 = []
# dict1.lower()
# dict2.lower()
# List1 = List1.append(list(dict1))
# List2 = List2.append(list(dict2))
# print(List1)
import re
mystring = "Special $#! characters,?   spaces 888323"
# ''.join(e for e in string if e.isalnum())
# re.sub('[^A-Za-z0-9]+', '', mystring)
cleanString = re.sub('\W+','', mystring )
print(cleanString)