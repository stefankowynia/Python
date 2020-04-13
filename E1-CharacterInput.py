#Practice Python - Exercise 1 : Character Input
#Date: 04 12 2020
#This program takes a user's input to calculate the year they will turn 100 years old

import datetime

name = input("Enter your name here: ")
age = input("Enter your age here: ")
number = int(input("Enter a number to repeat the message here: "))
date = datetime.datetime.now()
yearCurrent = date.year
year100 = int(yearCurrent) - int(age) + 100

message = name + ", you will turn 100 in the year " + str(year100) + "\n"

print(message * number)


