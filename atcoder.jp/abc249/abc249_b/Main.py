#input
s = input()

#cals
l = len(s)
if len(''.join(set(s))) < l or s.isupper() or s.islower():
  print("No")
else:
  print("Yes")