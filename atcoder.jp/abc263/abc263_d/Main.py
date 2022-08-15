# in
n,l,r = map(int,input().split())
A = list(map(int,input().split()))

# calc
left = 0
ans = r*n
for i, a in enumerate(A):
    left = min(left + a, l*(i+1))
    ans = min(ans, left + r*(n-i-1))

# out
print(ans)