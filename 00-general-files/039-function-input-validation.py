def mean(value):
    # This first line also works but is less preferred
    # if type(value) == dict:
    if isinstance(value, dict):
        return sum(value.values()) / len(value)
    else:
        return sum(value) / len(value)

print(mean([1, 4, 7]))
print(mean({ 'a': 1, 'b': 4, 'c': 7 }))