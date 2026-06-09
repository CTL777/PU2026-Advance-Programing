def is_balance(s):
  stack = []
  match = {')':'(', ']':'[', '}':'{'}
  for ch in s:
    if ch in '([{':
      stack.append(ch)
    elif ch in ')]}':
      if not stack or stack[-1] != match [ch]:
        return False
      stack.pop()
  return len(stack) == 0
n = int(input().strip())
for _ in range(n):
  line = input().strip()
  if is_balance(line):
    print("Yes")
  else:
    print("No")
