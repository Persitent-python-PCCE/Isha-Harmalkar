import grading

import csv


with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    studentRes = []
    topAvg = 0
    topper = ""
    passed, failed = 0, 0


    for row in reader:
        roll_no, name, maths, physics, chemistry = row["roll_no"], row["name"], int(row["maths"]),int(row["physics"]), int(row["chemistry"])
        total = maths + physics + chemistry
        average = round(total / 3, 2)
        grade = grading.grade(average)
        if grade != "F":
            passed += 1
        else:
            failed += 1

        cur = {"roll_no": roll_no, "name":name, "maths":maths, "physics":physics, "chemistry":chemistry, "total":total, "average":average, "grade":grade}
        studentRes.append(cur)
        if average > topAvg:
            topAvg = average
            topper = name
            

  

    with open("student_result.csv", "w", newline='') as file:
        fieldNames = ["roll_no", "name", "maths", "physics", "chemistry", "total", "average", "grade"]
        writer = csv.DictWriter(file, fieldnames=fieldNames)

        writer.writeheader()
        writer.writerows(studentRes)

    print("Proccessed", len(studentRes), "students -> students_result.csv")

    print("Class Topper : ", topper, "(avg", topAvg, ")")
    print("Passed : ", passed, "| Failed : ", failed)


    

    



