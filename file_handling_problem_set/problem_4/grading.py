def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75 and avg <=89:
        return "B"
    elif avg >= 60 and avg <=74:
        return "C"
    elif avg >= 40 and avg <=50:
        return "D"    
    
    elif avg < 40:
        return "F"