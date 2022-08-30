# in
n = int(input())
H = list(map(int, input().split()))

# calc
DP = [0, abs(H[1]-H[0])]
for i in range(n-2):
  w1 = DP[i]+abs(H[i+2]-H[i])
  w2 = DP[i+1]+abs(H[i+2]-H[i+1])
  DP.append(min(w1,w2))
  
# out
print(DP[-1])