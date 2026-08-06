import csv


def parse_line(line):
  
    s = line[0]
    res = s.split(" ")
    date, timestamp, level, msg = res[0], res[1], res[2], ' '.join(res[3:])

    return (level, msg)
   



def read_logs(path):
  

    with open("app.log", "r") as f:
        data = csv.reader(f)
        res = []
        for row in data:
            res.append(row)

        return res


        

       

        
       
       