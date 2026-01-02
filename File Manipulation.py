from collections import Counter

with open("sample.txt", "r") as file:
    words = file.read().lower().split()

count = Counter(words)

for word in sorted(count):
    print(word, ":", count[word])
