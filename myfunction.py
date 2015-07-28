#for loop, if state, len, variable, list of string

my_list = ['dean', 'sam', 'crowley', 'kevin', 'impala', 'supernatural']

largest = ''
for x in my_list:
	if len(x) > len(largest):
		largest = x

print(largest)