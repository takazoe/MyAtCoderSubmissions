import collections

# in
N = int(input())
A = list(map(int, input().split()))
 
# calc
ans = 0
dict_A = collections.Counter(A)
cnt_dict_A = [0]
for i, v in enumerate(dict_A.values()):
  cnt_dict_A.append(cnt_dict_A[-1] + v)
l = len(cnt_dict_A)
for j in range(2, l-1):
  left_cnt = cnt_dict_A[j-1]
  center_cnt = cnt_dict_A[j] - left_cnt
  right_cnt = cnt_dict_A[-1] - cnt_dict_A[j]
  ans += left_cnt * center_cnt * right_cnt
  
# out
print(ans)