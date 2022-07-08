import json
from difflib import get_close_matches
data = json.load(open("076 data.json"))
def dic(val):
    val=val.lower()
    if val in data:
        result = data[val]
        return result
    elif val.title() in data:
        return data[val.title()]
    elif val.upper() in data:
        return data[val.upper()]
    elif len(get_close_matches(val,data.keys())) > 0:
        closest = get_close_matches(val,data.keys())[0]
        inpt="Did you mean: " + closest + ", Type Y if yes and N if No: "
        promt = input(str(inpt))
        if promt == "y".lower():
            return data[closest]
        elif promt == "n".lower():
            return "Please double check your word"
        else:
            return "Please Type Correctly"
    else:
        return "Ypu typed the wrong word"


while True:
    valu=input("Key: ")
    output= dic(valu)
    if type(output) == list:
        for out in output:
            print(out)
    else:
        print(output)
