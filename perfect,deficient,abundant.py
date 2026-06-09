num = int(input())
x = 0
total = 0
for i in range (1,1000):
  if i >= num:
      break
  if num % i == 0:
    total = total + i
if total == num:
  print("perfect")
elif total > num:
  print("abundant")
else:
  print("deficient")
