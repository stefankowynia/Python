#Practice Python - Exercise 3 : List Less Than Ten
#Date: 04 19 2020
#Program exercise shows basic list manipulation with a variety of syntax

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num = int(input('Type a damn number: '))

print([value for value in a if value <= 5], ' This is the first list')

for value in a:
		if value <= num:
			b.append(value)

print(b, ' This is the seccond list')