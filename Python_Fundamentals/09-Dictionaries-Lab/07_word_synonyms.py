words_count = int(input())

synonyms = {}

for _ in range(words_count):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)


for word, synonyms in synonyms.items():
    synonyms = ", ".join(synonyms)
    print(f"{word} - {synonyms}")

