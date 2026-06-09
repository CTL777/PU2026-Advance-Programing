while True:
  a, b = map(int, input().split())
  c = a - b
  d = b - a
  e = 100 + c
  if a == -1:
    break
  if d < e:
    print(d)
  else:
    print(e)
