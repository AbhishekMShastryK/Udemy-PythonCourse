import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()] #If user entered "delhi" this will 
                               #check for "Delhi" as well.
    elif w.upper() in data:
        return data[w.upper()] #In case user enters words like USA or NATO.
    elif len(get_close_matches(w, data.keys()))>0: #To get close matches 
                                                   #to the entered word.
        yn = input("Did you mean '%s' instead? Enter Y if yes, or N for no:" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your response."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the word:")

output = translate(word.lower()) #Since most of the words present 
                                #in dictionary are lower case.

if type(output) == list: #To display items present in the list.
    for item in output:
        print(item)
else:
    print(output) #To diplay string.