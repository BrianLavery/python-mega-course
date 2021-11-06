len("hello") # takes exactly 1 argument
isinstance("hello", str) # takes exactly 2 arguments
print("hello") # takes indefinite number of arguments

def example(*args):
    return args

print(example(1, 2, 3, 'a', 4)) # prints a tuple

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 2, 3, 4))

# Cannot have keyword arguments as *args seems to take all the args

print(mean(1, 2, 3, a=4))