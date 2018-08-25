'''
@author: Arepallyrakesh
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	'''
	frequency graph
	'''

    keys_dic = sorted(dictionary.keys())
    for values in keys_dic:
        print(values, '-', dictionary[values]*('#'))

def main():
	'''
	main fuction
	'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()

