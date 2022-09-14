#getting input
user_input = int(input())

#dividing

hund = (user_input//100)
a = (hund*100)

tens = ((user_input-a)//10)
b = (hund*100)+(tens*10)

ones = ((user_input-b)//1)

#printing the statment
print(hund, "hundreds", tens, "tens", ones, "units")