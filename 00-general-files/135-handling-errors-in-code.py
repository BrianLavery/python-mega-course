def divide(a, b):
    try:
        return a/ b
    except: # This is error handling for any type of error
        return "Zero division is meaningless"

print(divide(1,0))
print(divide("a","b"))

def divide2(a, b):
    try:
        return a/ b
    except ZeroDivisionError: # This is more specific/ better
        return "Zero division is again meaningless"

print(divide2(2,0))
print(divide2("a","b"))