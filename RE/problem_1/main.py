import re


text = "John Doe: 28, Alice Smith: 34, Bob: 19, Charlie Brown: 45"

#Name : Age
#name  -> alpha + spaces
#age = number

#exp = '^[A-Za-z]:\d+$'
#res = re.findall(r"[A-Za-z+:\d+", text)

#names = re.findall(r"[A-Za-z\s+?]\s*", text)

names = re.findall(r"([A-Za-z\s]+?):\s*\d+", text)
names = [name.strip() for name in names]

print(names)