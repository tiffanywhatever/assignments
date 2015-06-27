# play hangman
import random

words = [
	"nice",
	"flute",
	"guitar",
	"game",
	"tommy",
	"water",
	"coffee",
	"food",
	"dessert",
	"burger"
]

word = words[random.randint(0, len(words)-1)] # pick a random word from the list of words
word_len = len(word) # Get the length of the word picked
max_wrong_guesses = 6 # total number of wrong guesses allowed

print("This word has %d characters." % word_len)

correct_guesses = 0 # total number of correct guesses made
wrong_guesses = 0   # total number of wrong guesses made

# loop until they either guess the correct number of letter or
# they have guessed wrong too many times.
while correct_guesses < word_len and wrong_guesses < max_wrong_guesses:
	guess = raw_input("Guess a letter: ")
	if len(guess) > 1:  # if they enter more than one letter,
		print("You can only guess one letter at a time.")
	elif guess in word: # if the letter is in the word
		print("Yes! That letter is in the word.")
		correct_guesses = correct_guesses + 1
	else: # else, they guessed wrong
		print("No! That letter is not in the word.")
		wrong_guesses = wrong_guesses + 1

	print("You have %d letters left to guess." % (word_len - correct_guesses))
	print("You have %d wrong guesses left." % (max_wrong_guesses - wrong_guesses))


# if they guessed wrong too many times
if wrong_guesses >= max_wrong_guesses:
	print("Your man was hanged! You lose.")
else:
	print("You win! The word was: %s" % word)





