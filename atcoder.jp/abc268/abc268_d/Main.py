import itertools
 
n,m = map(int, input().split())
S = [input() for _ in range(n)]
T = set([input() for _ in range(m)])
 
l = 16-(n-1) # "_"に使用できる文字数
for s in S:
  l -= len(s)

for Sc in itertools.permutations(S, n):
  for Bc in itertools.product(range(l+1), repeat=n-1):
    # 解をつくる
    ans = ""
    for i in range(n-1):
      ans += Sc[i] + '_'*(Bc[i]+1)
    ans += Sc[-1]
    # 解を見つけたらたら終了する
    if 3<=len(ans)<=16 and not(ans in T):
      print(ans)
      exit()
      
print(-1)