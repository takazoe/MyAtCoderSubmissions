#input
n = int(input())
lst_d = [int(input()) for i in range(n)]

#calc
lst_d_unique = list(set(lst_d))
l = len(lst_d_unique)

#out
print(l)