guitars = ({'ES335': 'Xtra Large'}, 
	      {'Les Paul': 'Large'}, 
	      {'SG': 'Medium-Large'},
	      {'Stratocaster': 'Medium'},
	      {'Telecaster': 'Medium-Small'},
	      {'Baby Taylor': 'Small'})

aline = None  # holds next input from user
g_tars = []   # creates a list from what guitars are enter
while aline != 'done':
	aline = raw_input('Enter guitar name: ')  
	if aline != 'done':
		g_tars.append(aline)  #.append means that what guitars you entered is added to the value g_tars 


for i in guitars:  #i is the value in the map (loops through map for size of guitar name entered)
	for g in g_tars:  #g is the key to i in map (loops through map for name of the guitar entered)
		if g in i:
			print ("%s = %s" % (g, i[g])) #guitar = size, ()