import re


text = "John Doe: 28, Alice Smith: 34, Bob: 19, Charlie Brown: 45"

nameExp = r"[a-zA-z]+[\s]?[a-zA-Z]*:"  

ageExp = r"[\s][1-9]+[0-9]*"

nameMatches = re.findall(nameExp, text)

nameMatches = [s.replace(":", "") for s in nameMatches]
ageMatches = re.findall(ageExp, text)

#print("Name Matches: ", nameMatches)
#print("Age Matches: ", ageMatches)

for i in range(len(nameMatches)):
    print(f"{nameMatches[i]} - {ageMatches[i]}")
