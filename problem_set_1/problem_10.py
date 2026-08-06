
def inventory_report(inventory, gst=0.05, **filters):
    #uniqueCat = map(inventory[1], inventory)
    uniqueCat = set(map(lambda x: x[1], inventory)) #remove duplicate
    uniqueCat = list(uniqueCat) # inorder to sort turn to list
    uniqueCat.sort()
    print("Categories: ", list(uniqueCat))

    lowStock = (filter(lambda x : ( x[2] < 10), inventory))
    lowStock = list(map(lambda x: x[0], lowStock))


    print("[!] Reorder soon (stock < 10):", lowStock)

    def getGstPrice(p):
    
        return (p[0], p[1], p[2], p[3] + p[3] * gst)
        

    inventoryList = list(inventory)

    gstPrices = list(map(getGstPrice, inventoryList))
    print("Price incl. GST: { ")
    for items in gstPrices:
       
        print("'", str(items[0]), ":", str(items[3]), "',", end=" ")

    print("'")

    filterMap = {}
    for filterType, val in filters.items():
        filterMap[filterType] = val

    print("Matching filters", filterMap)
    filterItems = []

    if "category" in filterMap and "max_price" in filterMap:
        cat = list(filter(lambda x : ( x[1] == filterMap["category"]), inventory))
        items = list(filter(lambda x : ( x[3] <= filterMap["max_price"]), inventory))
       
        cat = set(cat)
        items = set(items)
        
        uniqueCat = []
        for item in cat:
            if item in items:
                uniqueCat.append(item[0])
        print(uniqueCat)
    

    elif "category" in filterMap:
        cat = list(filter(lambda x : ( x[1] == filterMap["category"]), inventory))
        print(cat)
    elif "max_price" in filterMap:
        items = list(filter(lambda x : ( x[3] <= filterMap["max_price"]), inventory))
        print(items)
        
            



inv = [
("Masala Chai", "Tea", 5, 20),
("Green Tea", "Tea", 15, 30),
("Samosa", "Snack", 8, 15),
("Biscuit", "Snack", 25, 10),
]
inventory_report(inv, category="Snack",
max_price=15)