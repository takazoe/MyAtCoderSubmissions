def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes

# in
n = int(input())

# calc
ans = 0
P = sieve_of_eratosthenes(793700)
for i in range(len(P)-1):
  for j in range(i+1,len(P)):
    if P[i]*P[j]**3 > n:
      break
    ans += 1
      
# out
print(ans)