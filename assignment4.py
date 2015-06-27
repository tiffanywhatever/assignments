#Assignment 4

#gives you a random number from 0 to 100. 

import random
ran_num = random.randint(0, 100) 
number = None

while number != ran_num:
	number = int(raw_input('Guess a number between 0 and 100: '))
	if number > ran_num:
		print ('Too high! Choose a lower number!')
	elif number < ran_num:
		print ('Too low! Choose a higher number.!')

print("You guessed the number: %d" % ran_num)
