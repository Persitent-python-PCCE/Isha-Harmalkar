#problem 7

ledgerMap = {}
def award_points(house, points = 10, reason='general excellence', ledger = None):
    global ledgerMap
    if house not in ledgerMap:
        ledgerMap[house] = 0

    ledgerMap[house] += points
    print(house, " +" ,str(points), "(", reason, ") → total", ledgerMap[house])



 
led = award_points("Gryffindor")
led = award_points("Gryffindor", 50,
"defeating a troll", led)
led = award_points("Slytherin", 30,
ledger=led) 


print("Final ledger: ", end=" ")
for house, pts in ledgerMap.items():
    print(house, ": ", pts," ,", end=" ")
