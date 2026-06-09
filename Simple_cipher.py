word1 = input().strip()
word2 = input().strip()

freq1 = [0] * 26
freq2 = [0] * 26

for ch in word1:
    freq1[ord(ch) - ord('A')] += 1

for ch in word2:
    freq2[ord(ch) - ord('A')] += 1

freq1.sort()
freq2.sort()

if freq1 == freq2:
    print("YES")
else:
    print("NO")
