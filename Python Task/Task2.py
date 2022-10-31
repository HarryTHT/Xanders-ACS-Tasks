#getting user input
password = str(input(print("Enter a Password")))

if len(password)>6: #validating wether it is too long or short
    print("Password is valid")
else:
    print("password is too short")