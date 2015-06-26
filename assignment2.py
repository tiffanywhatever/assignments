 # Assignment 2

operators = {'+': 'plus',
			'-': 'minus',
			'/': 'divide by',
			'*': 'times'}

a_number = raw_input('Enter a number: ')
operator = raw_input('Enter an operator: ')
another_number = raw_input('Enter another number: ')

# +, -, *, /
a = int(a_number)
b = int(another_number)

if operator == '+':
	print("%d %s %d equals %d" % (a, operators[operator], b, a + b))
elif operator == '*':
	print("%d %s %d equals %d" % (a, operators[operator], b, a * b)) 
elif operator == '-':
	print("%d %s %d equals %d" % (a, operators[operator], b, a - b))
elif operator == '/':
	print("%d %s %d equals %d" % (a,operators[operator], b, a / b))
else:
	print('operator not supported')


