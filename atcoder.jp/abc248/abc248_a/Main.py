#input
lst_s = list(map(int, input()))

#calc
lst_n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in lst_n:
  if not (n in lst_s):
    print(n)
    exit()