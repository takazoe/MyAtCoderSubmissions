def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()

# input
n = II()
A = MII()

n1 = []
n2 = []
for a in A:
  if a % 2 == 0:n2.append(a)
  else:n1.append(a)
n1 = sorted(n1, reverse=True)
n2 = sorted(n2, reverse=True)

if len(n1)==1 and len(n2) <=1:
  print(-1)
  exit()
  
ANS = []
if len(n1)>1: ANS.append(n1[0]+n1[1])
if len(n2)>1: ANS.append(n2[0]+n2[1])

if len(ANS)==0:
  print(-1)
  exit()
print(max(ANS))