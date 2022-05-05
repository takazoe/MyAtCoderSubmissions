# in
n = int(input()) # 使わない
lst_A = list(map(int, input().split()))

# calc
m = 200000
ans = 0

idx = [0] * (m+1)  # 0～200000 のリストを作成
for i, A in enumerate(lst_A): # A番目にAの個数を追加
  idx[A] += 1

for aj in range(1, m+1):
  if idx[aj] == 0: # Aj が見つからない場合
    continue
  for ak in range(1, m//aj+1):
    ai = ak * aj
    ans += idx[ai] * idx[aj] * idx[ak]

# out
print(ans)