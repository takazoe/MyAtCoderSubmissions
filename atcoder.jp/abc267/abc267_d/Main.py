# in
n,m = map(int, input().split())
A = list(map(int, input().split()))

# calc
DP = [[0]*(n+1)] + [[-1*10**18]*(n+1) for _ in range(m)]
  
for i in range(m):
  for j in range(i,n):
    DP[i+1][j+1] = max(DP[i+1][j], DP[i][j]+A[j]*(i+1))
  
# out
print(DP[-1][-1])