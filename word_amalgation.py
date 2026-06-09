import sys

dictionary = []
anagram_map = {}

# 1️⃣ Read dictionary
for line in sys.stdin:
    word = line.strip()
    if word == "XXXXXX":
        break
    dictionary.append(word)
    key = ''.join(sorted(word))
    anagram_map.setdefault(key, []).append(word)

# Sort dictionary words for correct output order
for key in anagram_map:
    anagram_map[key].sort()

# 2️⃣ Process scrambled words
for line in sys.stdin:
    scrambled = line.strip()
    if scrambled == "XXXXXX":
        break

    key = ''.join(sorted(scrambled))

    if key in anagram_map:
        for w in anagram_map[key]:
            print(w)
    else:
        print("NOT A VALID WORD")

    print("******")
