# Easter eggs
import re

string = input()

pattern = r"(?<=\@\#)*\b([a-z]+)([\W]*)[\/]+([0-9]+)[\/]+"

matches = re.findall(pattern, string)

eggs = {}
for match in matches:
    colour = match[0]
    amount = int(match[2])
    print(f"You found {amount} {colour} eggs!")
