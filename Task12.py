#Write a program which takes an integer from the user and outputs all the factors or the number. 
# E.g. user enters 48 output is 2, 3, 4, 6, 8, 12, 18, 24.

#Getting input
number = int(input())

#setting divider
x = 2

#how many times it will run
for a in range(number):
    if (number/x) == (number//x):
        print(x)
    elif (number/x) == number:
        break

#increasing the divider
    x = x+1