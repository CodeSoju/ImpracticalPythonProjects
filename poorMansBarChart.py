'''
Map letters from string into dictionary & print bar chart of frequency

class collections.defaultdict([default_factory[,...]])
	Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. 
	It overrides one method and adds one writable instance variable. The remaining functionality is the name as
	for the dict class and is not documented here. 

defaultdict Examples:
Using list as the default_factory, it is easy to group a sequence of key-value pairs intoa dictionary of lists:
	s = [('yellow', l), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
	d = defaultdict(list)
	for k, v in s:
		d[k].append(v)

	list(d.items())
	[('blue', [2,4]), ('red', [1]), ]
'''
import sys
import pprint
from collections import defaultdict

#Note: text should be a short phrase for bars to fit in IDLE window
text = 'Like the castle in its corner in a medieval game, I forsee terrible trouble and I stay here just the same.'

ALPHA = 'abcdefghijklmnopqrstuvwxyz'

#defaultdict module lets you build dictionary keys on the fly!
mapped = defaultdict(list)
for character in text:
	character = character.lower()
	if character in ALPHA:
		mapped[character].append(character)

#pprint lets you print stacker output
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')

'''
Python print end keyword:
The end key of print function will set the string that needs to be appended when printing is done. 
By default the end key is a set by newline character. So after finishing all the variables, a newline char is appended

pprint.pprint(object, stream=Nonem indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)
	Prints the formatted representaion of object on stream, followed by a newline. If stream is None, sys.stdout is used. 
'''
print("{}\n".format(text), file=sys.stderr)
pprint.pprint(mapped, width = 110)

