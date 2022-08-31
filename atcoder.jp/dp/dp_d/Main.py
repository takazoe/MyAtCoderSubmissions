# in
N,W = map(int, input().split())

# calc
DP = [[0]*(W+1) for _ in range(N+1)]
for i in range(N):
  w,v = map(int, input().split())
  for j in range(W+1):
    if j < w:
      DP[i+1][j] = DP[i][j]
    else:
      DP[i+1][j] = max(DP[i][j], DP[i][j-w]+v)
      
# out
print(max(DP[-1]))