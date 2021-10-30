monday_temperatues = [9.1, 8.8, 7.5, 6.6, 9.9]

print(monday_temperatues[1:4]) # Upper limit is not included
print(monday_temperatues[3:]) # Leave second blank to go to end
print(monday_temperatues[:3]) # Leave first blank to start from index 0

# Can use negative indexing
print(monday_temperatues[-1]) # Last in list

# Can use negative index in slices
print(monday_temperatues[-2:])