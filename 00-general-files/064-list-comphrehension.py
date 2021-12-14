temps = [221, 234, 340, 230] # commonly data stored without decimlas to save space

# Means when reading in data need to perform some operations to stored data

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# Above works but there is a simpler way to do it using list comprehensions in Python

second_temps = [temp + 1 for temp in new_temps]
print(second_temps)