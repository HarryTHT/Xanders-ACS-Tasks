#Boolean Value
notfound = False

#the loop
while not(notfound):

    number = int(input("Number between 1 and 3"))

    if number >= 1 and number <= 3:
        notfound = True
    else:
        int(input())
        
exit
        
#out of the for loop
print("you chose option ", number)

