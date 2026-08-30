"""
students = ["Hermoine", "Harry", "Ron"]

print(students[0])
"""

"""
for i in [0,1,2]:
    print("meow")
"""
"""
for i in range(3):
    print("meow")

"""
"""
students = ["Hermoni", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])

"""
"""
students = ["Hermoni", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slyherin"]
"""
"""
students ={
    "Hermioni" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
    }

for student in students:
    print(student, students[student], sep=",")

"""

students = [

    {"name" : "Hermoni", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry" , "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron" , "house" : "Gryffindor" , "patronus" : "Jack Russel Terrier"},
    {"name" : "Draco" , "house" : "Slytherin" , "patronus" : None}
]
for student in students:
    print(student["name"],student["house"],student["patronus"],sep=", ")