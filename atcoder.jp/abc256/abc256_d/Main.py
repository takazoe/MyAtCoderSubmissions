# in
n = int(input())

#calc
LR_key,LR_item = [],[]
for _ in range(n):
  l,r = map(int, input().split())
  LR_key.append(l)
  LR_item.append(1)
  LR_key.append(r)
  LR_item.append(-1)
ZIP_sort = sorted(zip(LR_key,LR_item)) # 小さい順に並び替え

ANS = [[ZIP_sort[0][0]]]
c = 1
for i in range(1,len(ZIP_sort)-1):
  c += ZIP_sort[i][1]
  if ZIP_sort[i][0] == ZIP_sort[i+1][0]: # LRが次と同じ値
    continue
  elif len(ANS[-1])==2: # 区間はじまり
    s = ZIP_sort[i][0]
    ANS.append([s])
  elif c == 0: # 区間終わり
    e = ZIP_sort[i][0]
    ANS[-1].append(ZIP_sort[i][0])
e = ZIP_sort[-1][0]
ANS[-1].append(e)

# out  
for ans in ANS:
    print(*ans)