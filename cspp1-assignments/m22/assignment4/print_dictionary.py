'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    keys_dic = sorted(dictionary.keys())
    for values in keys_dic:
        return (values, ':', dictionary[values])

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()

# for keys,values in cars.items():
#     print(keys)
#     print(values)

# for x in cars:
#     print (x)
#     for y in cars[x]:
#         print (y,':',cars[x][y])