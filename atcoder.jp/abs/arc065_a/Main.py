#input
s = input()

#calc
while len(s)>0:
    if s.endswith("dreamer"):
        s = s[:-7]
    elif s.endswith("dream"):
        s = s[:-5]
    elif s.endswith("eraser"):
        s = s[:-6]
    elif s.endswith("erase"):
        s = s[:-5]
    else:
        print("NO")
        exit()

#out
print("YES")