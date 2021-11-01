monday_temperatures = [9.1, 8.8, 7.5]
student_grades = { "Marry": 9.1, "Jim": 8.8, "John": 7.5 }

# Lists
for temperature in monday_temperatures:
    print(round(temperature))

for letter in 'hello':
    print(letter)

print()

# Dictionaries
for grade in student_grades.items():
    print(grade) # output is a tuple

for grade in student_grades.keys():
    print(grade)

for grade in student_grades.values():
    print(grade)

# Iterating with key/ value pairs and formatting
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

for key, value in phone_numbers.items():
    print("%s has as phone number %s" % (key, value))