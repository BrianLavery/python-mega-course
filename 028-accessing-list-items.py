monday_temperatues = [9.1, 8.8, 7.5]

# These two approaches are the same
# Python calls the top method in background when you write lower syntax
print(monday_temperatues.__getitem__(0))
print(monday_temperatues[0])