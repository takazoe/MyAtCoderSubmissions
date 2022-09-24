def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()

x,y,z = MII()

if 0<x<y or y<x<0:
  print(abs(x))
elif (x<0 and 0<y) or (y<0 and 0<x):
  print(abs(x))
elif 0<z<y or y<z<0:
  print(abs(x))
elif (z<0 and 0<y) or (y<0 and 0<z):
  print(abs(x)+abs(z)*2)
else:
  print(-1)