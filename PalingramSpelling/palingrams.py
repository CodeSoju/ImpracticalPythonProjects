'''
Finding palingrams requires a bit more effort than finding one-word palindromes. 

THE OBJECTIVE:
	Use Python to search an Enligsh language dictionary for two-word palingrams. Analyze and optimize the palingram code using
	the cProfile tool. 

The Strategy:
	The program will examine the coreword. :
		1. It can have either even or odd number of letters:
		2. One contiguous part of the word spells a real word when read backwards. 
		3. This contiguous part can occupy part or all of the core word. 
		4. The other contiguous part contains a palindromic sequences of letters. 
		5. The palindromic sequence can occupy part or all of the core word. 
		6. The aplindromic sequence does not have to be a real word (unless it occupies the whole word)
		7. The two parts can't overlap or share letters.
		8. The sequence is reversible. 

Note:
	If the reversed word occupies the whole core word and is not  a palindrome, it's called a semordnilap. A semordnilap is 
	similar to a palindrome except for one key difference: rather than spelling the same word when read backward, it speels a different 
	word. 


Here is the pseudocode for a palingram-finding algorithm:
- Load digital dictionary as a list of words
-Start an empty list to hold palingrams
- For word in wordList:
	Get length of word
	If length > 1:
		Loop through the letters in the word:
			If reversed word fragment at front of word is in word list and letters after form a palindromic sequence:
				Append the word and reversed word to palingram list
			If reversed word fragment at end of word is in word list and letters before form a palindromic sequence:
				Append reversed word and word to palingram list
 Sort palingram list alphabetically
 Print word-pair palingrams from list

'''
import time
import load_dictionary

start_time = time.time()

word_list = load_dictionary.load('2of4brif.txt')

#find word-pair palingrams
def find_palingrams():
	'''Find dictionary palingrams'''
	pali_list = []
	for word in word_list:
		end = len(word)
		rev_word = word[::-1]  # alternative choice: ''.join(reversed(word))
		if end > 1:
			for i in range(end):
				if word[i:] == rev_word[:end - i] and rev_word[end - i:] in word_list:
					pali_list.append((word, rev_word[end-i:]))
				if word[:i] == rev_word[end - i:] and rev_word[:end - 1] in word_list:
					pali_list.append((rev_word[:end-i], word))
	return pali_list

palingrams = find_palingrams()

#sort plaingrams on first word
palingrams_sorted = sorted(palingrams)

#display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first,second in palingrams_sorted:
	print("{} {}".format(first, second))

end_time = time.time()
print("Runtime for this program was {} seconds".format(end_time-start_time))

'''
Since you are looking for word-pair palingrams, exclude single letter words. Then nest another for statement to loop through the letters
in the current word. 

Now, run a conditional requiring the back end of the word to be palindromic and the frount end to be a reverse word in the word list. 
If a word passes the test, it is appended to the list, immediately followed by the reversed word. 

We now have to repeat the conditiona;, but change the slicing direction and word order to reverse the output. I.e, you must capture
palindromic sequences at the start of the word rather than the end. Return the list of palingrams to complete the function. 

PALINGRAM PROFILING:
--------------------
Profiling is an analytical process that gathers statistics on a program's behavior-ex:, the number and duration of function calls-
as the program executes. 

Profiling is important for optimization process. It tells you exacctly what parts of a program are taking the mosty time memory. 

Profiling using cProfile:
-------------------------
A profile is a measurment output- a record of how long and how often parts of a program are executed. The Python standard lib provides 
a profiling inteface, cProfile, which is a C extension suitable for profiling long-running programs. 





Palingram Optimization:
-----------------------
Using an alternate data structure to lists_like tuples, sets, or dictionaries- might reduce time. 
'''

