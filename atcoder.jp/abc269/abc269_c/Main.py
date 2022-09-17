n = int(input())
A = [n]
while A[-1]>0: A.append((A[-1]-1)&n)
print(*A[::-1])