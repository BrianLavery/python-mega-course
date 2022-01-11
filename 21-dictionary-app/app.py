import json

data = json.load(open("data/data.json"))

def define(word):
    if word in data:
        return data[word]
    else:
        return "This word does not exist"
    

word = input("Enter word: ")

print(define(word))