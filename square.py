while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    start = int(a ** 0.5)
    if start * start < a:
        start += 1
    
    end = int(b ** 0.5)
    
    if start > end:
        print(0)
    else:
        print(end)
