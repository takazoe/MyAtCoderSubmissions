def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()

# input
n,m = MII()
L = [set() for _ in range(n)]
for _ in range(m):
  X = LMII()
  for x in X[1:]:
    for x2 in X[1:]:
      L[x-1].add(x2)

for l in L:
  if len(l) < n: NO()  
YES()