import re

text = input()
pattern = r"\b((www.)([A-Za-z0-9\-]+)\.([a-z\.]+)+)\b"
while text:
    searched_links = re.findall(pattern, text)
    for searched_link in searched_links:
        print(searched_link[0])
    text = input()
