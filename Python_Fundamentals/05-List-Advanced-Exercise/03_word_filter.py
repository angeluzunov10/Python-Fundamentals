# text = input().split()
# words = [word for word in text if len(word) % 2 == 0]
# for word in words:
#     print(word, end="\n")

text = [word for word in input().split() if len(word) % 2 == 0]
for word in text:
    print(word, end="\n")
