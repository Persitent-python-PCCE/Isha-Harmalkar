#problem 3

def villanTerritoryOverlap(v1, v2, v3):
    v1, v2, v3 = set(v1), set(v2), set(v3)
    allThree = v1.intersection(v2)
    allThree = allThree.intersection(v3)
    print("Contested by all three: ", allThree)

    #exactlyOne =  v1.difference(v2)
    #exactlyOne = exactlyOne.difference(v3)
    union = v1.union(v2).union(v3)
    exactlyOne = set()
    for teritory in union:
        if teritory in v1 and teritory not in v2 and teritory not in v3:
            exactlyOne.add(teritory)
        elif teritory in v2 and teritory not in v1 and teritory not in v3:
            exactlyOne.add(teritory)
        elif teritory in v3 and teritory not in v1 and teritory not in v2:
            exactlyOne.add(teritory)

    print("Controlled by exactly one: ", exactlyOne)

    #disitinct = v1.union(v2).union(v3)
    print("Distinct neighborhoods: ", len(union))




goblin  = ["Queens", "Manhattan",
"Brooklyn", "Bronx"]
octopus = ["Manhattan", "Brooklyn",
"Harlem"]
vulture = ["Manhattan", "Bronx",
"Harlem"]

villanTerritoryOverlap(goblin, octopus, vulture)

v1 = ["A", "B", "C"]
v2 = ["A", "B"]
v3 = ["D", "E", "A", "B"]
villanTerritoryOverlap(v1, v2, v3)
