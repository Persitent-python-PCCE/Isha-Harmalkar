import re

text = "Contact us at 9876543210 or 987-654-3210. You can also call (987) 654-3210 or 987 654 3210 for support."

exp = r"[0-9]{10}|[0-9]{3}-?\s?[0-9]{3}-?\s?[0-9]{4}|\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}"

""" matches = re.findall(exp, text)
print(matches)

for m in matches:
    n = len(m)
    newCopy = "*" * (n - 4) + m[-4:]
    print(newCopy) """

def modify(match):
    
    return "*" * 6 + match.group()[-4:]



result = re.sub(exp, modify, text)
print(result)