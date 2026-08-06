def launch(*argv, abort_threshold=5000):
    stage = 1
    curSum = 0
    for arg in argv:
        curSum += arg
        print("Stage ", stage, "→ cumulative ",curSum, "kg")

        if curSum >  abort_threshold:
            print("[ABORT] at stage", stage, ": threshold", abort_threshold, "kg exceeded.")
            break       

        stage += 1


launch(1200, 1800, 2500, 900)