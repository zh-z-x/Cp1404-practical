MIN_LENGTH = 8

password = input("Enter your password: ")
while len(password) < MIN_LENGTH:
    print("Password too short")
    password = input("Enter your password: ")

print("*" * len(password))
