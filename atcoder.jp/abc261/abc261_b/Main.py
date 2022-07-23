# in
n = int(input())
A = []
for _ in range(n):
  A.append(input())
  
for i in range(n):
  for j in range(n):
    if not((A[i][j] =="W" and A[j][i] == "L") or (A[i][j] =="L" and A[j][i] == "W") or (A[i][j] =="D" and A[j][i] == "D") or (A[i][j] =="-" and A[j][i] == "-")):
      print("incorrect")
      exit()
      
print("correct")