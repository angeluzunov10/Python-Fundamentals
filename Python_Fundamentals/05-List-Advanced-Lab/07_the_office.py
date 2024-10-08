list_of_employees_happiness = list(map(int, (input().split())))
happiness_improvement_factor = int(input())
total_happiness = 0
total_happiness_list = []
for employee_happiness in list_of_employees_happiness:
    happiness = employee_happiness * happiness_improvement_factor
    total_happiness += happiness
    total_happiness_list.append(happiness)

happy_employees_count = 0

for each in total_happiness_list:
    if each >= total_happiness / len(list_of_employees_happiness):
        happy_employees_count += 1
if happy_employees_count >= len(list_of_employees_happiness) / 2:
    print(f"Score: {happy_employees_count}/{len(list_of_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees_count}/{len(list_of_employees_happiness)}. Employees are not happy!")
