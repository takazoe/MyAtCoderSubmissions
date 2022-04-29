from math import comb
 
#input
N, M, K = map(int, input().split())
 
#calc
i, c = 0, 0
while i*M <= K-N:
    c += ((-1)**i) * comb(N, i) * comb(K-i*M, N)
    i += 1
    
#out
out = c % 998244353
print(out)