from bisect import *

# in
n,k = map(int,input().split())
P = list(map(int,input().split()))

# calc
TOP,YAMA = [0],[[]] # 各山の最小値, 山
ANS = [-1]*n
 
for i,p in enumerate(P):
    idx = bisect(TOP,p) # 何番目の山に置くか

    if len(TOP) == idx: # 置ける山がない場合、新しい山をつくる
        TOP.append(p)
        YAMA.append([p])
    else: # 山の上に置く
        TOP[idx] = p
        YAMA[idx].append(p)

    if len(YAMA[idx]) == k: # 山がK以上の場合、山の各カードを記録して山を消す
        for number in YAMA[idx]: 
            ANS[number-1] = i+1
        TOP.pop(idx)
        YAMA.pop(idx)
    
# out
print(*ANS, sep='\n')