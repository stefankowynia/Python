#Guess The number
#Date: 2020 04 05

from random import randint

x = randint(1,10)
a = int(input('Pick a number between One and Ten: '))

#print(x)

while a != x:
	if a > x:
		if a > 10:
			print('the number is between 1 and 10')
		else:
			print('lower')
	elif a < x:
		if a <= 0:
			print('the number is between 1 and 10')
		else:
			print('higher')

	a = int(input('Guess again: '))

print('Correct! ' + str(a) + ' ' + 'is my number')
