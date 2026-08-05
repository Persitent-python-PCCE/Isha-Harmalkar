
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