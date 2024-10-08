student_records = {
    "Ivan": {"Math": 5, "Science": 6, "English": 5},
    "Nikolay": {"Math": 4, "Science": 6, "English": 5},
    "Maria": {"Math": 6, "Science": 6, "English": 3}
}

for name, info in student_records.items():

    print(name)

    for subject, grade in info.items():
        if subject == "Math":
            print(grade)