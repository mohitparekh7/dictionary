import json
from difflib import get_close_matches

loadData = json.load(open("data.json"))
# note the data.json should be in the same folder as that of the dictionary.py else you can provide the entire path of the data.json file


def findMeaning(word):
    word = word.lower()
    if word in loadData:
        return loadData[word]
    elif word.title() in loadData:
        return loadData[word.title()]
    elif word.upper() in loadData:
        return loadData[word.upper()]
    elif len(get_close_matches(word , loadData.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, loadData.keys())[0])
        decide = input("press y for yes or n for no")
        decide = decide.lower()
        if decide == "y":
            return loadData[get_close_matches(word , loadData.keys())[0]]
        elif decide == "n":
            return("please re enter your word correctly")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("please re enter your word correctly")


word = input("Enter the word you want to search: ")
output = findMeaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

