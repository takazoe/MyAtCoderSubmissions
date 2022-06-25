# in
n = int(input())
S = input()
W = list(map(int, input().split()))

# calc
WS_sorted = zip_sort = sorted(zip(W,S)) # 小さい順に並び替え

S_sorted_sum = [0]
W_sorted = [0] 
for i,p in enumerate(WS_sorted):
  S_sorted_sum.append(S_sorted_sum[i] + int(p[1]))
  W_sorted.append(p[0])

ans = 0
for j,w in enumerate(W_sorted):
  if j < len(W_sorted)-1: # 最後のw以外
    if w == W_sorted[j+1]: # 次のwと同じ場合
      continue
  x = S_sorted_sum[j]
  t = j - x + S_sorted_sum[-1] - x
  if ans < t:
    ans = t
  
# out
print(ans)