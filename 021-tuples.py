monday_temperatures = (1, 4, 5)
tuesday_temperatures = [2, 3, 6]

print(monday_temperatures)
print(tuesday_temperatures)

tuesday_temperatures.append(10)
print(tuesday_temperatures)

monday_temperatures.append(10) # Tuples are immutable so cannot add more values to it
# Tuples are a bit faster than lists