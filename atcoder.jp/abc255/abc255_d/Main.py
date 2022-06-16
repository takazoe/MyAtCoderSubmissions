from bisect import bisect_left

# in
n,q = map(int, input().split())
A = list(map(int, input().split()))

# calc
A_sort = sorted(A) # 小さい順に並び替え
A_sort_sum = [0] # 合計値を計算
for i,a in enumerate(A_sort):
  A_sort_sum.append(A_sort_sum[i] + a)

for _ in range(q):
  x = int(input())
  idx = bisect_left(A_sort, x)
  left = idx*x - A_sort_sum[idx] # Ai<X の範囲を計算
  right = A_sort_sum[-1] - A_sort_sum[idx] - (n-idx)*x # Ai>=X の範囲を計算
  print(left + right)