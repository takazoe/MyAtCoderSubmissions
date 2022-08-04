# in
n,x = map(int,input().split())

# calc
ans = 10**20
ab = 0
for i in range(n):
  a,b = map(int,input().split())
  if i>x:
    break
  ab += a+b
  ans = min(ans,ab+b*(x-i-1))
  
# out
print(ans)