import math
import sys
sys.setrecursionlimit(10**8) # 再起回数の設定

def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()

# in
n,x,y = MII()
S = [[] for _ in range(n+1)] # [set(), {2, 3}, {1}..]
for _ in range(n-1):
  u,v = MII()
  S[u].append(v)
  S[v].append(u)

def dfs(fu,u):
  if u == y:
    # yが見つかった場合
    ANS.append(u)
    return True
  for v in S[u]:
    if v == fu:
      # 来た方向には戻らない
      continue
    if dfs(u,v):
      # この先にyがあった場合
      ANS.append(u)
      return True
  return False # この先にyが無い場合

# main
ANS = []
dfs(0,x)
print(*ANS[::-1])