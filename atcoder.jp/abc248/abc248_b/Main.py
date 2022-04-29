#input
A, B, K = map(int, input().split())

#calc
i = 0
while A < B:
  i += 1
  A *= K

#out
print(i)