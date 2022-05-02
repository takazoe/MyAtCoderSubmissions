from collections import deque

# in 
R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
maze = [list(input()) for h in range(R)]

# calc
sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1

dist = [[2500 for _ in range(C)] for _ in range(R)] # 各マスの手数を最大値で初期化
dist[sx][sy] = 0 # スタート位置の手数は0

que = deque()
que.append([sx, sy])
d = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 移動方向のリスト

# 幅優先探索
while que:
    x, y = que.popleft() # キューから取り出し

    # 現在位置から上下左右に探索
    for i, j in d:
        if maze[x+i][y+j] == '#': # 壁の場合
            continue
        if dist[x+i][y+j] != 2500: # 最小手数確定済みの場合
            continue           
        dist[x+i][y+j] = dist[x][y] + 1
        que.append([x+i, y+j]) # 次のマスをキューに格納
        
#out
print(dist[gx][gy])