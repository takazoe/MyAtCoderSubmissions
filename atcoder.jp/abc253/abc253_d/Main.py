import math

# in
n,a,b = map(int, input().split())
 
# calc
def f(n):
  return n*(n+1)//2

def f2(a,n):
  return f(n//a)*a  

def lcm(x,y): # 最小公倍数
  return (x * y) // math.gcd(x, y)
  
ans = f(n) - f2(a,n) - f2(b,n) + f2(lcm(a,b),n)

# out
print(ans)