# დაწერეთ კოდი სადაც გამოვიძახებთ რენდომად მოსწავლეს, დავუსვამთ კითხვას და დავუწერთ შესაბამის ქულას

import random
students = ["anri", "bacho", "miro", "soso"]
points = [5, 10]
#answer = input("please say yes: ")
for i in range(len(students)):
    student = random.choice(students)
    print(student)
    answer = input("please say yes: ")
    students.remove(student)
    if answer == "yes":
        print(student, "your point is", points[1])
    else:
        print(student, "your point is", points[0])
