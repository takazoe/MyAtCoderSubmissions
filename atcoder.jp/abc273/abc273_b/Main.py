from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
n,k = map(int, input().split())
l = len(str(n))
for i in range(1,k+1):
  n = int(Decimal(n).quantize(Decimal('1E'+str(i)), rounding=ROUND_HALF_UP))
print(n)