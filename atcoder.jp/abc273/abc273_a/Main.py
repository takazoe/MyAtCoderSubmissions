n = int(input())
if n == 0:print(1)
else:
  ans = 1
  for k in range(2, n+1):
    ans *= k
  print(ans)