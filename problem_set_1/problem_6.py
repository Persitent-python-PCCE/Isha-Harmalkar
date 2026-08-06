#problem 6




groupData1 = [("Brazil", 3, 0, 0), ("Japan", 1, 2,
0), ("Spain", 2, 0, 1), ("Ghana", 0, 1,
2)]



pts = list(filter((lambda x: (x[1] * 3 + x[2]) >= 6 and x[3] <= 1), groupData1))

print("Advancing to knockouts: ")
for team, wins, draws, losses in pts:
    print(team, " -", wins * 3, "pts")