# in
N, K = map(int, input().split())
A = list(map(int, input().split()))

# calc
P0, P1 = [],[]
for i in range(N):
  xy = list(map(int, input().split()))
  if i+1 in A:
    P1.append(xy)
  else:
    P0.append(xy)

ans = []
for xy0 in P0:
  dis = []
  for xy1 in P1:
    dis.append( ( (xy1[0]-xy0[0])**2 + (xy1[1]-xy0[1])**2 ) ** (0.5))
  ans.append(min(dis))

# out
print(max(ans))