import redaction_config as config


linesRead = []
with open("report.txt", "r") as file:
    reader = file.readlines()
    redactedReport = []
    count = {}
    for s in config.SENSITIVE:
        count[s] = 0

    for line in reader:
        words =  line.split()
        newLine = []
        for w in words:
            if w in config.SENSITIVE:
                newLine.append("[REDACTED]")
                count[w] += 1
            else:
                newLine.append(w)

        redactedReport.append(' '.join(newLine) + "\n")

    with open("report_redacted.txt", "w") as file:
        file.writelines(redactedReport)

   


    for corp, c in count.items():
        print(corp, "->", c, "occurences redacted")

    

        
