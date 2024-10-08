string = input().split()
result = ""
for word in string:
    word = word * len(word)
    result += word

print(result)
