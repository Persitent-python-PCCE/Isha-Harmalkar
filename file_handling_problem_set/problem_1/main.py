
import collections

import log_utils


import csv



lines = log_utils.read_logs("app.log")


data  = []


for line in lines:    
        
    data.append(log_utils.parse_line(line))
  

filteredData = []
errors = set()

for level, msg in data:
    filteredData.append(level)
    errors.add(msg)



summary = dict(collections.Counter(filteredData))

f1 =  open("log_summary.txt", "w")
f1.write("=== Log Summary ===")
f1.write("\n")



print("=== Log Summary ===")
for level, count in summary.items():
    print(level, ":", count)
    cur = level + " :" + str(count)
    f1.write(cur)
    f1.write("\n")

print("Errors found:")
f1.writelines("Errors found")
f1.write("\n")

for e in errors:
    print("-", e)
    cur = "-" + e

    f1.write(cur)
    f1.write("\n")


f1.close()




