#in
n = int(input())
P = list(map(int,input().split()))

ans = 0
o = P[-1]
for i in range(len(P),0,-1):
  if o == i:
    ans += 1
    o = P[i-2]
    
print(ans)