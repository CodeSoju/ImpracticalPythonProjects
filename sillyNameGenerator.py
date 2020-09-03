'''
Project#1: GENERATING PSEUDONYMS
-------------------------------
OBJECTIVE:
	Randomly generate funny sidekick names using Python code that conforms to established style guidlines. 

A successful manager once said that his secret is to ASK LOTS OF QUESTIONS:
	- wHAT ARE YOU TRYING TO DO?
	- Why are you doing it? 
	- Why are you doing it this way?
	- How much time do you have?
	- How much money?

Two types of software development:
	1. Prototype and Patch: you start with a simple program and then use patches, or edited code, to handle problems
			encountered in testing. good for when you are working through a complex probelm you don't understand well. 
			But it can also produce complicated and unreadable code. 

	2. Designed Development: If you have aclear view on how to solve the problem use DD b/c it avoids future issues and their 
			subsequent patches. Makes coding easier and more efficient, and it typical leads to stronger and more relaible code. 

PSEUDOCODE:
---------
Load a list of first names
Load a list of last names
Choose a first name at random
Assign the name to a variable 
Choose a surname at random 
Assign the name to a variable 
Print names to the screen in order and in red font
Ask the user to quit or play again 
If user plays again: repeat
If user quits: end and exit
'''
import sys,random 

def main():
	
	print("Welcome to the Psych 'Sidekick Name Picker.\n")
	print("A name just like Sean would pick for Gus: \n\n")

	first = ('Baby Oil', 'Bad News', "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'", "Butterbean", 
			'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat')

	middle = ('Jappy', 'Strongman', 'Mr.Robot', 'Zen-zen', 'Wildy', 'Bugs', 'Random Ram', 'Styles', 'Cry Me a River', 'Lovehart',
				'Zanny', 'Crazy', 'Speedy', 'Moneybags', 'Java', 'Samurai')

	last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breddslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 
		'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooderapple', 'Goodsmith', 'Goodpasture', 'Guster', 'Henderson')

	while True:
		firstName = random.choice(first)

		middleName = random.choice(middle)

		surName = random.choice(last)

		print("\n\n")
		print("{} {} {}".format(firstName, middleName, surName), file = sys.stderr)
		print('\n\n')

		try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
		if try_again.lower() == 'n':
			break

	input("\nPress Enter to exit.")
if __name__ == "__main__":
	main()

'''
Import sys and random. You'll use sys to access the system-specific error message functionaloty, so you can color your output
an eye-catching red in the IDLE window. 

Python Enhancements Proposals, whichc are coding conventions for the Python code comprising the standard  library in the main Python
distribution. The most important of these is PEP8, a style guide for Python programming. PEP 8 evolves over time as new conventions
are identified andpast ones are rendered obsolete by changes in the language. 

PEP8's goal is to impraove readability of code and make it consistent across a wide spectrum of Python programs. 

Pylint:
-----
It's a source code, bug, and quality checker for the Python programming language. 


The __name__ variable is a special built-in variable that you can use to evaluate whether a proram is being run in stand-alone
mode or as an imported module. 

A module is just a Python program used inside another Python program. 
If you run the program directly, __name__ is set to __main__. 

__name__ is used to ensure that, when the program is imported, the main() function isn't run until you intentionally call it, but 
when you run the program directly, the condition in the if statement is met and main() is automatically called. 

You don't always need this convention. For example, your code just defines a function, you can load it as a module
and call it w/o need for __name__

Configuring Pylint:
-==-=-=-=-=-=-=-=--=
Run the option -rn ( short for -reports=n) to surpress the large volume of extraneous statistics that Pylint returns. 
'''