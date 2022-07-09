# in
n,m,x,t,d = map(int,input().split())

# calc
ans = 0
s = 0
if n >= x:
  s = t - x*d
else:
  s = t - x*n
if m >= x:
  ans = s + x*d
else:
  ans = s + m*d
  
# out
print(ans)