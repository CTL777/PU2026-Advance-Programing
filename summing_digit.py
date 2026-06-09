import sys

for line in sys.stdin:
    n = line.strip()
    if n == "0":
        break
    try:
        n = int(n)
    except ValueError:
        continue  # ignore non-integer lines
    if n == 0:
        break
    print(1 + ((n - 1) % 9))
