import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data/data.json"))

def define(word):
    close_match = get_close_matches(word, data.keys(), n=1, cutoff=0.8)
    if word in data:
        return data[word]
    elif word.title() in data: # For proper nouns (e.g. Delhi)
        return data[word.title()]
    elif word.upper() in data: # For acronums (e.g. NATO)
        return data[word.upper()]
    elif close_match:
        # return "This word does not exist. Did you mean {}".format(close_match[0])
        response = input("This word does not exist. Did you mean %s? Enter Y if yes, or N if no. " % close_match[0]).lower()
        if response == "y":
            return data[close_match[0]]
        elif response == "n":
            return "Word does not exist."
        else:
            return "We did not understand your entry."
    else:
        return "This word does not exist"
    

word = input("Enter word: ").lower()

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
