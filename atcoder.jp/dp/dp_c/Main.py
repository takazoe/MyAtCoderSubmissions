# in
n = int(input())

# calc
DP = [[0]*3 for _ in range(n+1)]
for i in range(n):
  abc = list(map(int, input().split()))
  abc += abc
  for j in range(3):
    s1 = DP[i][(j+1)%3]
    s2 = DP[i][(j+2)%3]
    DP[i+1][j] = max(s1,s2) + abc[j]
  
# out
print(max(DP[-1]))