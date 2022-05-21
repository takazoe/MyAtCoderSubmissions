# in
n = int(input())
S = [input() for _ in range(n)]

# calc
ans = 10000
for num in range(0, 10):
  t_max = 0
  dp = [0]*10
  num = str(num)
  for s in S:
    idx = s.index(num)
    t = idx + 10*dp[idx]
    t_max = max(t_max, t)
    dp[idx] += 1
  ans = min(ans, t_max)
  
# out
print(ans)