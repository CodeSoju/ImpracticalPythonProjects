'''
Load a text file as a list. 

Arguments:
	- text file name (and a dictionary path, if needed)

Exceptions:
	- IOError if filename not found

Returns:
	-A list of all words in a text file in lower case

Requires:
	- import sys

'''
import sys

def load(file):
	'''
	Open a text file & return a list of lowercase strings.

	The strip method returns a copy of the string in which all chars have been stripped from the beginning and the end of the string
	(default whitespace chars)
	'''
	try:
		with open(file) as in_file:
			loaded_txt = in_file.read().strip().split('\n')
			loaded_txt = [x.lower() for x in loaded_txt]
			return loaded_txt
	except IOError as e:
		print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
		sys.exit(1)

'''
Function based on the previous file-opening discussion. The function takes a filename as an arg. 
If no exceptions are raised, the text file's whitespace is removed, and it's items are split into separate lines and added to a list. 
We want each word to be separate item in the list, before the list is returned. And since case matters to Python, the words in the list
are converted to lowercase via list comprehension. 

List Comprehension: a shorthand way to convert a list, or other iterabel, into another list. In this case it replaces a for-loop

Generally, you wouldn't call sys.exit() from a module, as you may want your program to do something_like write a log file- prior to 
terminating. In later chapters, we'll move both the try-except blocks and sys.exit() into a main() function for clarity and control. 
'''

