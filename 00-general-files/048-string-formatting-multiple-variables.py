name = input("Enter your name: ")
surname = input("Enter your surname: ")

message = "Hello %s %s!" % (name, surname)
print(message)

message = f"Hello {name} {surname}!"
print(message)