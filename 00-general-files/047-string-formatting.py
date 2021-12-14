user_input = input("Enter your name: ")
message = "Hello %s!" % user_input.title() # This method works for Python 2 and 3
print(message)

# New method for Python 3.6 onwards
message = f"Hello {user_input.upper()}"
print(message)