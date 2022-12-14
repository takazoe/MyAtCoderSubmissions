import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

# in
H, W = map(int, input().split()) # Height, Width
maze = [list(input()) for _ in range(H)]

# calc
# スタート位置を取得 O(H*W)
for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w
            
# 深さ優先探索 O(x*y/2)
def dfs(x, y):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
        return

    # ゴールに辿り着ければ終了
    if maze[x][y] == 'g':
        print('Yes')
        exit()

    maze[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(sx, sy) # スタート位置から深さ優先探索
print('No')