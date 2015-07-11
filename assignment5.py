import random

words = ['funny', 'potato', 'pickle', 'anya',
		'foot', 'tired', 'hello', 'toe']

word = words[random.randint(0, len(words)-1)]
word_length = len(word)
total_hints = 4


print("This word has %d letters." % word_length)

your_total_hints = 1 

def give_hint(hints):
	if hints > total_hints:	
		print ("You have no more hints left.")
	else:
		print word[:hints]
	return hints + 1	

guess = ''
while guess != word:
	guess = raw_input("Guess the word (? for a hint): ")
	
	if guess == "?":
		your_total_hints = give_hint(your_total_hints)
	elif word != guess:
		print ("Incorrect, try again.")
	else:
		print("Yes that is correct!")

