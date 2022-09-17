a,b,c,d = 0,10,0,10

for i in range(10):
  S = input()
  if a == 0 and S != "..........":
    a = i+1
    for j,s in enumerate(S):
      if c == 0 and s != ".":
        c = j+1
      elif c != 0 and d == 10 and s == ".":
        d = j
  elif a != 0 and b == 10 and S == "..........":
    b = i
  
print(a,b)
print(c,d)