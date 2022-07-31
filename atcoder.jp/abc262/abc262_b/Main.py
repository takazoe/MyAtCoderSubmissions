n,m = map(int,input().split())

if m<3:
  print(0)
  exit()

L = []
for _ in range(n):
  L.append(set())
for _ in range(m):
  s,e = map(int,input().split())
  L[s-1].add(e-1)

ans = 0
for a in range(n):
  for b in range(n):
    for c in range(n):
      if (b in L[a]) and (c in L[a]) and (c in L[b]):
        ans += 1

print(ans)