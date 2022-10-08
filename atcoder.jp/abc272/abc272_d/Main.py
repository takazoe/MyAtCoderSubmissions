def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
  
import math
from collections import deque

def is_integer(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False
  
# input
n,m = MII()
ANS = [[-1]*n for _ in range(n)]
ANS[0][0] = 0

D = set()
for i in range(m+1):
  if m-i**2<0:break
  j = math.sqrt(m-i**2)
  if is_integer(j):
    j = int(j)
    D.add((i,j))
    D.add((-i,j))
    D.add((i,-j))
    D.add((-i,-j))

que = deque()
que.append([0, 0])
# bfs
while que:
    x,y = que.popleft() # キューから取り出し
    # 現在位置から上下左右に探索
    for i, j in D:
        if x+i<0 or y+j<0:continue
        if x+i>n-1 or y+j>n-1:continue
        if ANS[x+i][y+j] != -1:continue           
        ANS[x+i][y+j] = ANS[x][y] + 1
        que.append([x+i, y+j]) # 次のマスをキューに格納       

#out
for ans in ANS:
  print(*ans)