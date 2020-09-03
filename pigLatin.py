'''
Take an English word that begines with a consonant, move that consonant to the end, and then add "ay" to the end of the 
word. If the word begins with a vowel, you simply add "way" to the end of the word. 
'''
import sys

def main():
	print("Welcome to the Pig Latin Word Generator")
	VOWELS = 'aeiouy'
	while True:
		word = input("Enter a word: \n")
		if word[0] in VOWELS:
			pig_Latin = word + "way"
		else:
			pig_Latin = word[1:] + word[0] + "ay"
		print()
		print("{}".format(pig_Latin))

		try_again = input("\n\nTry again? (Press Enter else n to stop)\n")
		if try_again.lower() == "n":
			sys.exit()

if __name__ == "__main__":
	main()
