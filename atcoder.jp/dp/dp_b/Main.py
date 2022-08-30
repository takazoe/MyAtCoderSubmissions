# in
n,k = map(int, input().split())
H = list(map(int, input().split()))

# calc
DP = [0]*n
for i in range(min(n,k)):
  DP[i] = abs(H[i]-H[0])
if n <= k:
  print(DP[-1])
  exit()
  
for i in range(k,n):
  W = []
  for j in range(-k,0):
    W.append(DP[i+j]+abs(H[i]-H[i+j]))
  DP[i] = min(W)
  
# out
print(DP[-1])