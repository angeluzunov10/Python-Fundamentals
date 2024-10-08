courses = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)

for course, names in courses.items():
    students_count = len(names)
    print(f"{course}: {students_count}")
    for name in names:
        print(f"-- {name}")

