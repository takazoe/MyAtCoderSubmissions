# in
n,p,q,r = map(int, input().split())
A = list(map(int, input().split()))

# calc
Asum = [0]
for i in range(n):
  Asum.append(Asum[i] + A[i])
S = set(Asum)

for sx in Asum[:-2]:
  sy = sx + p
  if not sy in S:
    continue
  sz = sy + q
  if not sz in S:
    continue
  sw = sz + r
  if not sw in S:
    continue
  print("Yes")
  exit()
        
print("No")