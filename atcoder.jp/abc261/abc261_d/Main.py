n,m = map(int, input().split())
X = list(map(int, input().split()))
BONUS = [0]*(n+1)
for _ in range(m):
  c,y = map(int, input().split())
  BONUS[c] = y

# dp[i][c] := i 回コインをトスした後、カウンタの値が c の時に最も多くもらえるお金。
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
  for c in range(i+1):
    # 表が出た時の処理
    dp[i+1][c+1] = max(dp[i+1][c+1], dp[i][c]+X[i]+BONUS[c+1])
    # 裏が出た時の処理
    dp[i+1][0] = max(dp[i+1][0], dp[i][c])

print(max(dp[-1]))