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