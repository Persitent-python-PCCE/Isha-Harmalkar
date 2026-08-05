
#1. Sorting Hat


def sortingHat(name, signals):
    print(name, signals)
    hashMap = {}
    #add house
    hashMap["G"] = 0
    hashMap["H"] = 0
    hashMap["R"] = 0
    hashMap["S"] = 0

    
    for c in signals:     
        if c.upper() in hashMap:
            hashMap[c.upper()] += 1
    
   


    maxCount = max(hashMap.values())
    res = []


    for house, count in hashMap.items():
        if count == maxCount:
            if house == "S":
                res.append("Slytherin")
            elif house == "R":
                res.append("Ravenclaw")
            elif house == "H":
                res.append("Hufflepuff")
            else:
                res.append("Gryffindor")

    res.sort()
    print(name, ", you belong in... ", res[0], "! (", maxCount, "signals)" )



""" name = input("Name: ")
signals = input("Signals: ")
sortingHat(name, signals) """

sortingHat("Neville", "ggghGhs")
sortingHat("Mariam", "dhfsdfdfssss")





print("---------------------------------------------------------")


def rushHourReport(cups):
    sum, avg, rushHours = 0, 0, []

    for  c in cups:
        sum += c

    avg = round(sum / len(cups), 1)
    print("Total: ", sum, "cups | Average: ", avg, "/hr")
    for i, c in enumerate(cups):
        if c > avg:
            rushHours.append(i + 8)

    print("Rush hours (above average): ", end=" ")
  
    for h in rushHours:
        if h > 12:
            print(str(h - 12)+"PM", end=" ")
        else:
            print(str(h)+"AM", end=" ")

    print()
    


   


rushHourReport([12, 5, 8, 20, 3, 15, 22])
rushHourReport([76, 23, 46, 88, 12, 34, 12])


print("----------------------------------------------------")\
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


print("---------------------------------------------------------")
#problem 4
def coordinateIntegrityCheck(records):
    #invalid records
    print("INVALID: ", end=" ")
    validRecords = []
    for codeName, lat, lon in records:
        if lat < -90 or lat > 90 or lon < -180 or lon > 180:
            print(codeName, "(", lat, lon, ")")
        else:
            validRecords.append((codeName, lat, lon))

    print("Briefing (N -> )")
    sortedValid = sorted(validRecords, key=lambda x : x[1], reverse=True)
    for codeName, lat, lon in sortedValid:
        print(codeName.upper(), " → Lat: ", lat, "Lon: ", lon)

record1 = [("Falcon", 34.05, -118.24), ("Ghost",
99.9, 12.0), ("Condor", 40.71, -74.00)]

coordinateIntegrityCheck(record1)

print("----------------------------------------------------")
#problem 5

def smartBillingEngine(orders):



    def calLinetotal(order):
        q, p = order[1], order[2]
        gstHiked = p + (p * 0.05)

        return round(q * gstHiked, 2)





    lineTotal = map(calLinetotal, orders)
    lineList = list(lineTotal)
    print("Line totals (incl. GST): ",lineList)
    print("Grand total: Rs", sum(lineList))



    




orders = [("Masala Chai", 3, 20), ("Samosa", 2,
15), ("Green Tea", 1, 30)]

smartBillingEngine(orders)

print("---------------------------------------------------------")
#problem 6




groupData1 = [("Brazil", 3, 0, 0), ("Japan", 1, 2,
0), ("Spain", 2, 0, 1), ("Ghana", 0, 1,
2)]



pts = list(filter((lambda x: (x[1] * 3 + x[2]) >= 6 and x[3] <= 1), groupData1))

print("Advancing to knockouts: ")
for team, wins, draws, losses in pts:
    print(team, " -", wins * 3, "pts")
 
