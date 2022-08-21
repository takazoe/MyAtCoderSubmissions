# in
n,m,t = map(int, input().split())
A = list(map(int, input().split()))

# calc
D = [0]*n
for _ in range(m):
  x,y = map(int, input().split())
  D[x-1] = y

for i,a in enumerate(A):
  t += D[i]
  t -= a
  if t <= 0:
    print("No")
    exit()
  
print("Yes")