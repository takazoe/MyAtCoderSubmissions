# in
n = int(input())

# calc
DP = [[-1]*5 for _ in range(n+1)]
DP[0][0] = 0

t_b = 0
for i in range(n):
  t,x,a = map(int,input().split())
  length = t - t_b
  for j in range(5):
    s = max(0,j-length)
    e = min(5,j+length+1)
    DP[i+1][j] = max(DP[i][s:e]) # 行動できる範囲内のMAXで更新
  if DP[i+1][x] >= 0:
    DP[i+1][x] += a # アクセス可能な場所ならば点数を取得
  t_b = t   
  
# out 
print(max(DP[-1]))