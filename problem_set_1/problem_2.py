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