#in 
A = list(map(int,input().split()))

for i in range(1,14):
  for j in range(1,14):
    if A.count(i) == 3 and A.count(j) == 2:
      print("Yes")
      exit()
print("No")