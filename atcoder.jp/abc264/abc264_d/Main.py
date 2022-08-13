# in
S = input()
S2 = "atcoder"

# calc
ans = 0
for i in range(7):
  idx = S2.find(S[i]) # "atcoder"の何番目か
  for j in range(i+1,7):
    if idx > S2.find(S[j]): # 自分より後ろにidxの小さい数があるか
      ans += 1

# out
print(ans)