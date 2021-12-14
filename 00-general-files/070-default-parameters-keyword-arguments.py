def area(a, b):
    return a * b

# non-keyword arguments/ positional arguments - communicate argument based on position
print(area(4, 5)) 

# keyword arguments where position or order does not matter
print(area(b=5, a=4)) 

# Default parameters - cannot come before non-default parameters
def area2(a, b=6):
    return a * b

print(area2(a=5))
print(area2(a=5, b=7))
print(area2(5, 7))