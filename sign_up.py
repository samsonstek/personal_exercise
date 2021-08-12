email = input("please insert your email address")
password = input("please insert your password")
if len(password) > 8:
    print("Thank you")
while len(password) <= 8:
    password = input("your password is too short, It has to be morethan 8 characters,/n Try again: ")
print(email)
print(password)