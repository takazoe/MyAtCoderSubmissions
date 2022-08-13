# in
r,c = map(int, input().split())
x,y = 8,8

# calc
r,c = abs(r-x),abs(c-y)
if max(r,c)%2 == 1:print("black")
else:print("white")