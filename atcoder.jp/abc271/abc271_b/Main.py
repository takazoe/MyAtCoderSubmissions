import math

def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()

# in
n,q = MII()
A = []
for _ in range(n):
  A.append(LMII()[1:])

for _ in range(q):
  s,t = MII()
  print(A[s-1][t-1])