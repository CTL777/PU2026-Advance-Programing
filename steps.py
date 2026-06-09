#this is a code for counting the least steps needed from one location to another
n = int(input())

for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())

    def f(x, y):
        t = x + y
        return (t * (t + 1)) // 2 + x

    steps = f(x2, y2) - f(x1, y1)

    print(f"Case {i}: {steps}")
