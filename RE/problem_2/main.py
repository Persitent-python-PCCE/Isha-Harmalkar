#valid product code


#start with 2 or 3 uppcase
#followed by hyphen
#followed by exactly 4 digts
#optionally ends with an uppercase letter


import re


words = ["AB-1234",
"XYZ-9876A",
"A-1234",
"ABCD-1234",
"XY-12A",
"PQ-4567B"
]

exp = r"[A-Z]{2,3}\-[0-9]{4,5}[A-Z]*"

for word in words:
    if re.match(exp, word):
        print("Valid")
    else:
        print("Invalid")
