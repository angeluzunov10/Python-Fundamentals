# Read employee efficiencies
employee_efficiencies = []
for _ in range(3):
    employee_efficiencies.append(int(input()))

# Read student count
student_count = int(input())

# Calculate total student questions
total_questions = student_count

# Calculate working hours
working_hours = 0
remaining_students = total_questions

while remaining_students > 0:
    # Calculate questions handled in current hour
    current_hour_questions = 0
    for efficiency in employee_efficiencies:
        current_hour_questions += efficiency

    # Handle questions until break
    remaining_students -= current_hour_questions
    working_hours += 1

    # Handle break
    if working_hours % 4 == 0:
        working_hours += 1

# Print time needed
print(f"Time needed: {working_hours}h.")