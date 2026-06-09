def count_syllables(line):
  vowel = set("aeiouy")
  count = 0
  in_vowel = False
  for ch in line:
    if ch in vowel:
      if not in_vowel:
        count += 1
        in_vowel = True
    else:
      in_vowel = False
  return count
  
lines = [input().strip(" ")for _ in range(3)]
required = [5,7,5]
correct = True
for i in range(3):
  if count_syllables(lines[i]) != required[i]:
    print(i+1)
    correct = False
    break
if correct:
    print ("Y")
