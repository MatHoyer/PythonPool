import sys

args = sys.argv

if len(args) > 2:
	print('AssertionError: more than one argument is provided')
else:
	if len(args) == 2:
		try:
			arg = int(args[1])
			if arg % 2 == 0:
				print('I\'m Even.')
			else:
				print('I\'m Odd.')
		except ValueError:
			print('AssertionError: argument is not an integer')