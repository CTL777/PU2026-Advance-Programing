import sys

for line in sys.stdin:
    a, b = line.strip().split()

    # stop condition
    if a == "0" and b == "0":
        break

    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    count = 0

    # add digit by digit from right to left
    while i >= 0 or j >= 0:
        da = int(a[i]) if i >= 0 else 0
        db = int(b[j]) if j >= 0 else 0

        if da + db + carry >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        i -= 1
        j -= 1

    # output formatting
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")
