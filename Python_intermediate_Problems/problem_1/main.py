
import datetime
import json
import random


class StudentData:
    def __init__(self, n, year):
        self.n = int(n)
        self.year = datetime.datetime.strptime(year, "%Y").date()


    def generateData(self):
        uniqueIds = random.sample(range(1, self.n + 10), self.n)
        print("Uniques Ids: ", uniqueIds)

        names = ["Ariya", "Bina", "Ciya", "Dina", "Era", "Fiona", "Georgia", "Hina", "Ivy", "Jay", "Kia","Leo", "Mansi", "Nio", "Opia", "Pia", "Quince", "Ria", "Sitar", "Tiva", "Uni", "Viena", "Wutan", "Xian", "Yan", "Zian"]

        departments = ["Computer Science", "Information Technology", "Electronics", "Mechanical"]

        #AgeList = random.randrange(18, 25)

      
        #print("Age List: ", AgeList )

        pythonMarkList = [ random.uniform(0, 100) for i in range(self.n)]
        databaseMarkList = [ random.uniform(0, 100) for i in range(self.n)]
        computerNetworkMarkList = [ random.uniform(0, 100) for i in range(self.n)]

        students = {}

        #startDate, endDate = datetime.date(year=self.year, month=1, day=1), datetime.date(year=self.year, month=12, day=31)
        """  startDate, endDate = datetime.date(self.year, 1, 1), datetime.date(self.year, 12, 31)


        dates = [startDate]

        while (startDate != endDate) or len(dates) < self.n:
            startDate += datetime.datetime.timedelta(days=1)
            dates.append(startDate) """

        td = datetime.datetime(2025, 1, 1)
        dates  = [td + datetime.timedelta(days=idx) for idx in range(min(self.n, 364))]


        

        NewData = []

        passedCount = 0
        failedCount = 0
        highestAvg = float("-inf")
        lowestAvg = float("inf")
    


        for i in range(self.n):
            id = uniqueIds[i]
            name = random.choice(names)
            age = random.randrange(18, 25)
            department = random.choice(departments)
            #marks
            total = pythonMarkList[i] + databaseMarkList[i] + computerNetworkMarkList[i]
            average = round(total/3)

            highestAvg = max(highestAvg, average)
            lowestAvg = min(lowestAvg, average)
            result = ""
            if pythonMarkList[i] > 40 and databaseMarkList[i] > 40 and computerNetworkMarkList[i] > 40:
                result = "Pass"
                passedCount += 1
            else:
                result = "Fail"
                failedCount += 1


            examDate = str( random.choice(dates))

            cur = {"student_id":id, "name":name, "age":age, "department":department, "marks":{"python": pythonMarkList[i], "database":databaseMarkList[i], "networks":computerNetworkMarkList[i]},
                   "total":total, "average":average, "result": result, "exam_date": examDate}

            print(cur)


            NewData.append(cur)

        

        print("Student Performance Summary")
        print("---------------------------")
        print(f"{'Total Students':15}:{self.n:3}")
        print(f"{'Passed':15}:{passedCount:3}")
        print(f"{'Total Students':15}:{failedCount:3}")
        print()

        print(f"{'Highest Average':16}:{failedCount:3.2f}")
        print(f"{'Lowest Average':16}:{failedCount:3.2f}")
        print()

        self.generateFile(NewData)


    def generateFile( self, dict):
        with open('students.json', 'w') as file:
            json.dump(dict, file)

        print("Student data successfully written to students.json")






            


    
    


""" n = int(input("Enter number of students: "))
year = (input("Enter examination year")) """
s1 = StudentData("5", "2025")
s1.generateData()
