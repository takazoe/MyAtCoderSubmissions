# in
S = input()
T = input()
 
# calc
S2,T2 = [["start",1]],[["start",1]]
for s in S:
  if s == S2[-1][0]:
    S2[-1][1] += 1
  else:
    S2.append([s,1])
for t in T:
  if t == T2[-1][0]:
    T2[-1][1] += 1
  else:
    T2.append([t,1])
    
if len(S2) != len(T2):
  print("No")
  exit()
  
for s,t in zip(S2,T2):
  if not(s[0] == t[0] and ((s[1] > 1 and t[1] > 1 and s[1] <= t[1]) or (s[1] == 1 and t[1] == 1))):
    print("No")
    exit()
    
# out
print("Yes")