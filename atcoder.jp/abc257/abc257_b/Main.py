# in
n,k,q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

# calc
for i in range(q):
  if A[L[i]-1] != n and not A[L[i]-1] + 1 in A:
    A[L[i]-1] += 1
  
# out
print(*A)