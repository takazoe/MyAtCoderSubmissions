# in
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))

# calc
a_max = max(A)
for i, a in enumerate(A):
  if (a == a_max) and (i+1 in B):
    print("Yes")
    exit()

# out
print("No")