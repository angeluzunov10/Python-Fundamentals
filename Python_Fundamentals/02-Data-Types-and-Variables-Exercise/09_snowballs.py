snowballs_count = int(input())

max_snowball_value = 0

max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0

for balls in range(1, snowballs_count + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = int(snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_weight} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})")
