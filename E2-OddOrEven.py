#Practice Python - Exercise 2 : Odd or Even
#Date: 04 13 2020
#The first part of the program takes user input and checks if the integer is odd or even.
#The seccond part of the program checks if one integer devides into a seccond integer evenly.

#Part 1
number = int(input("Pick a number: "))

if number % 2 == 0:
	if number % 4 == 0:
		print(number, ' is an even number that is divisable by 4!')
	else:
		print(number, ' is an even number.')
else:
	print(number, ' is an odd number.')

print('\n' + ('- ')*20 + '\n')


#part 2
num = int(input('Pick another number: '))
check = int(input('Pick ANOTHER number: '))

def even(num1, num2):
	if num1 % num2 == 0:
		return str(num2) + ' divides into ' + str(num1) + ' evenly!'
	else:
		return str(num2) + ' does not divide into ' + str(num1) + ' evenly!'

answerCheck = even(num, check)

print(answerCheck)


