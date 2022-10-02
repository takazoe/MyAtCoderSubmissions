def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()

n = II()
A = LMII()

S = set(A)
c = 0
for i in range(10**9):
  if i+1 in S: c += 1
  else: c += 2
  if c>n:
    print(i)
    exit()