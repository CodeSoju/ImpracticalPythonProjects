'''
Load dictionary files from the internet and use Python to discover first palindromes and then the more complex palindromes in those files. 

FINDING AND OPENING A DICTIONARY
--------------------------------


Handling Exceptions When Opening Files:
--------------------------------------
Whenevr you load an external file, your program should automatically check for I/O issues, like missing files or incorrect filenames, 
and let you know if there is a problem. 

try:
	with open(file) as in _file:
		do something
except IOError as e:
	print("{}\nError opening {}. Terminating program,", format(e, file), file=sys.stderr)
	sys.exit(1)


The try clasies is executed first. The with statement will automatically close the file after the nested block of code, regardless of 
how the blockexits. Closing files prior to terminating a process is a good practice. If you don't close those files, you could run out
of file descriptors(mainly a problem with large scripts that run for a long time), lock the file from further access in Windows, corrupt
files, or lose data if you are writing to the file. 

If something goes wrong and if the type of error matches the exception named after the except keyword, the rest of the try clause
is skipped, and the except clause is executed. If nothing goes wrong, the try clause is executed, and the except clause is skpped. 

The sys.exit(1) statement is used to terminate the program. The 1 in sys.exit(1) indicates that the program experienced an error and did not
close succesfully. 



LOADING THE DICTIONARY FILE:
0--------------------------
You can import this file into other programs as a module and run it with a one-line statement. Remember, a module is simply a Python
program that can be used in another Python program. 
Modules represents a form of ABSTRACTION. Meaning you don't have to worry about all the coding details. A principle of abstraction is encapsulation, the act of hiding the details. 
We encapsulate the file-loading code in a module so you don't have to see or worry about the detailed code in another program. 

SEE load_dictionary.py


Finding single word palindromes in a dictionary and then move on to the more difficult palindromic phrases. 

THE STRATEGY AND PSEUDOCODE:
----------------------------
Identifying a palindrom eis simple: simply compare a word to itself and slice backward
Ex:
	word = 'NURSES'
	word[:] ---> 'NURSES'
	word[::-1]  --> 'SESRUN'

If you don't provide values when slicing a string (or any sliceable type), the default is to use the start of the string, the end of
the string, and a positive step equal to 1. 

Negative slicing doesn't behave exactly the same way as forward slicing, and the positive and negative position values and 
endpoints are asymmetrical. this can lead to oncfusion, so let's restrict our negative slicing to the simple [::-1] frmat

Pseudocode:
-	Load digital dictionary file as a list of words
- 	Create an empty list to hold palindromes
-	Loop through each word in the word list:
		If word sliced is the same as word sliced backward:
			Append word to palindrome list
	Print palindrome list

'''
#Find palindromes (letter palingrams) in a dictionary file. 
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

for word in word_list:
	if len(word) > 1 and word == word[::-1]:
		pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')

'''
Line 80:
	Printing the aplindromes in an attractive way--stacked and with no quotation marks or commas. You can accomplish this by looping
	through every word in the list, but there is a more effecient way to do it. You can use the 'splat' operator (designated by the *), 
	which takes a list as input and expands it into positional args in the function call. The last arg is the separator is a space (sep=' ')
	, but instead, print each item on a new line ('\n')

'''

