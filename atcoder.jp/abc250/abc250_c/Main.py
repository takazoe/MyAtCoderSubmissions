# in
n,q = map(int, input().split())

# calc
B,IDX = [],[]
for i in range(n): # [0,1,2, .. n-1]
  B.append(i+1)
  IDX.append(i)
  
for _ in range(q):
  x = int(input())-1
  idx = IDX[x]
  if idx == n-1: # ボールが右端にある場合
    IDX[x],IDX[B[idx-1]-1] = IDX[B[idx-1]-1],IDX[x]
    B[idx],B[idx-1] = B[idx-1],B[idx]
  else: # ボールが右端でない場合
    IDX[x],IDX[B[idx+1]-1] = IDX[B[idx+1]-1],IDX[x]
    B[idx],B[idx+1] = B[idx+1],B[idx]
    
# ans
print(*B)