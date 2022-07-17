import sys
sys.setrecursionlimit(10**9) # 再帰の上限を解放
 
def dist2(x1, y1, x2, y2):
  d2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
  return d2
 
def IsIntersect(c1, c2):
  x1, y1, r1 = c1
  x2, y2, r2 = c2
  dist = dist2(x1,y1,x2,y2)
  if dist > (r1 + r2) ** 2 or dist < (r1 - r2) ** 2:
    return False
  return True
 
def dfs(idx, visited):
  # ゴールに辿り着ければ終了
  if idx == goal_id:
    print('Yes')
    exit()
  # 確認した円は消しておく
  visited[idx] = True
  # 接する円で再起していく
  for i,c in enumerate(C):
    if visited[i]:
      continue
    if IsIntersect(c, C[idx]):
      dfs(i, visited)
  # ゴールに辿り着けない場合は戻る
  return
  
# in
n = int(input())
sx,sy,tx,ty = map(int, input().split())
 
# スタート・ゴールの円のインデックスを調べる
C = []
start_id,goal_id = -1,-1
for id in range(n):
  x,y,r = map(int, input().split())
  if start_id == -1 and dist2(x,y,sx,sy) == r**2:
    start_id = id
  if goal_id == -1 and dist2(x,y,tx,ty) == r**2:
    goal_id = id
  C.append([x,y,r])
 
# スタート位置から深さ優先探索
dfs(start_id, [False]*n) 
    
# out
print("No")