import json
with open("data.txt") as file:
    data = file.read()

dict = {
    "uppercase":{},
    "lowercase":{},
    "digit":{},
    "specialchars":{}
}
for char in data:
    if(char.isupper()):
        category = "uppercase"
    elif(char.islower()):
        category = "lowercase"
    elif(char.isdigit()):
        category = "digit"
    else:
        category = "specialchars"
    
    dict[category][char] = dict[category].get(char,0) + 1

print(json.dumps({"Dictionary of Characters": dict}, indent=4))
