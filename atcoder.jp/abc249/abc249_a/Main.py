#input
a,b,c,d,e,f,x = map(int, input().split())

#calc
i,j = 0,0
if (x % (a + c)) // a == 0:
  i = (x % (a + c))
else:
  i = a
if (x % (d + f)) // d == 0:
  j = (x % (d + f))
else:
  j = d
time_t_walking = a * (x // (a + c)) + i
time_a_walking = d * (x // (d + f)) + j
distance_t = time_t_walking*b
distance_a = time_a_walking*e

if distance_t > distance_a:
  print("Takahashi")
elif distance_t < distance_a:
  print("Aoki")
else:
  print("Draw")