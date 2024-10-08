# students = []
# course_to_search = None
# while True:
#     line = input()
#     if ":" not in line:
#         course_to_search = line
#         break
#
#     name, id, course = line.split(":")
#     students.append({"name": name, "id": id, "course": course})
#
# for student in students:
#     if course_to_search.startswith(student['course'][0:3]):        #ако първите 3 букви от курса на студента съвпадат с
#         print(f"{student['name']} - {student['id']}")              # търсения студент влез в проверката и принтирай


students_info = {}
course_to_search = None

while True:
    line = input()
    if ":" not in line:
        course_to_search = line
        break

    name, id, course = line.split(":")
    students_info[name] = {"id": id, "course": course}

for name, info in students_info.items():
    for id, course in info.items():
        if course_to_search.startswith(course[0:3]):
            print(f"{name} - {info['id']}")


