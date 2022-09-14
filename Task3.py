
# getting number
number = int(input("Number between 1 and 3"))

# is it within the range?
for a in range(10000000): #how may times it would repeat,
    if number >= 1 and number <= 3:
        continue
    else:
        number = 0
        number = int(input("option not didn't work, choose a new number"))
        
#out of the for loop
print("you chose option ", number)

print("test")



