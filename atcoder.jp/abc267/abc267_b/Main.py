# in
S = input()
C = [3,2,4,1,3,5,0,2,4,6]

# calc
if S[0] == "1":
  print("No")
  exit()
  
R = [0]*7
for i,s in enumerate(S):
  if s == "1":
    R[C[i]] += 1

for i in range(5):
  for j in range(i+1,6):
    for k in range(j+1,7):
      if R[i] >= 1 and R[j] == 0 and R[k] >= 1:
        print("Yes")
        exit()
      
print("No")