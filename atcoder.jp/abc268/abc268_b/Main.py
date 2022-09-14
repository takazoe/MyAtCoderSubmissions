S = input()
T = input()

l = len(S)
if S == T[:l]:
  print("Yes")
else:
  print("No")