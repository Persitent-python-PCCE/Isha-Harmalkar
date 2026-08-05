
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


    
   
    for house, count in hashMap.items():
        print("House: ", house, "Key: ", count)

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



name = input("Name: ")
signals = input("Signals: ")
sortingHat(name, signals)

""" sortingHat("Neville", "ggghGhs")
sortingHat("Mariam", "dhfsdfdfssss")
sortingHat("Kia", "dsdfdfdhhhHhkkk")
sortingHat("John", "sdjjjjkkkrrrjjR") """