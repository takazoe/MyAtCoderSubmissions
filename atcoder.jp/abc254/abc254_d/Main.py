import math

# in
n = int(input())

# calc
ans = 0
m = 1
while m**2 <= n:
  m += 1

for i in range(1,m):
  for j in range(i+1,m):
    if math.gcd(i, j) <= 1: # i と j が互いに素の場合
      ans += n//(j*j)
    
# out
print(ans*2+n)