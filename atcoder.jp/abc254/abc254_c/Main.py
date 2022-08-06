# in
n,k = map(int, input().split())
A = list(map(int, input().split()))

# calc
for i in range(k):
    A[i::k]=sorted(A[i::k])
    
# out
if A == sorted(A):
  print("Yes")
else:
  print("No")