def weather_condition(temp):
    if temp > 7:
        return 'Warm'
    else:
        return 'Cold'

# Use input to get user input
user_input = float(input('Enter temperature: ')) # Always returns a string unless we parse
print(weather_condition(user_input))