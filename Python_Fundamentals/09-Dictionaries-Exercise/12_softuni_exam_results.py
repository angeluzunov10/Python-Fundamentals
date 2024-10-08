submissions = {}
results = {}

while True:
    command = input()

    if command == "exam finished":
        break

    if "banned" in command:
        command = command.split("-")
        banned_user = command[0]
        del results[banned_user]
        continue

    username, language, points = command.split("-")
    points = int(points)

    if username not in results:
        results[username] = points
    else:
        if points > results[username]:
            results[username] = points
    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1

print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, submission in submissions.items():
    print(f"{language} - {submission}")
