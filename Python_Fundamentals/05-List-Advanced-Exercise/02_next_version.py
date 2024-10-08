software_version = list(map(int, input().split(".")))
new_software_version = software_version.copy()
new_software_version[2] += 1

if new_software_version[2] > 9:
    new_software_version[2] = 0
    new_software_version[1] += 1
if new_software_version[1] > 9:
    new_software_version[1] = 0
    new_software_version[0] += 1

new_software_version = list(map(str, new_software_version))

print(".".join(new_software_version))
