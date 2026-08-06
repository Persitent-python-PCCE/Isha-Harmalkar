import csv
import statistics


with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    total_revenue = 0
    topPrdt = ""
    maxRev = 0
    prices = []
    hashMap = {}

    
    for data in reader:
        curTotal = float(data["quantity"]) * float(data["unit_price"])
        total_revenue += (curTotal) 
        if curTotal > maxRev:
            topPrdt = data["product"]
            maxRev = curTotal
        prices.append(curTotal)
        if data["category"] not in hashMap:
            hashMap[data["category"]]= 0

        hashMap[data["category"]] += curTotal


    print("=== Sales Report ===")
    print("revenue by Category:")
    for cat, rev in hashMap.items():
        print(" ",cat, " :", rev)



    print()

    print("Top Product: ", topPrdt, "(", maxRev, ")")
    print("Total Revenue :", total_revenue)
    avg = statistics.mean(prices)
    print("Avg / Txn :", avg)