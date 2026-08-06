def create_hero(name, *powers, **stats):
    print("Hero: ", name)
    print("Powers: ", end=" ")
    for p in powers:
        print(p, end=" ")
    print()
    print("Stats: ")
    overallRating = 0
    for stat, val in stats.items():
        print(" ",stat, ":", val)
        overallRating += val
    overallRating = round((overallRating / len(stats)), 2)    
    print("Overall rating: ", overallRating, end="")
    if overallRating >= 90:
        print("-> S-Tier *")






create_hero("Spider-Man", "wall-crawl",
"spider-sense",
strength=85, agility=95,
intelligence=92)

