# in
h1,h2,h3,w1,w2,w3 = map(int, input().split())

#calc
if h1+h2+h3 != w1+w2+w3:
  print(0)
  exit()
  
ans = 0
m_max = 30
for m11 in range(1,m_max):
  for m12 in range(1,m_max-m11):
    for m21 in range(1,m_max-m11):
      for m22 in range(1,m_max-m12):
        m13 = h1 - m11 - m12
        m23 = h2 - m21 - m22
        m31 = w1 - m11 - m21
        m32 = w2 - m12 - m22
        m33 = h3 - m31 - m32
        if m13>0 and m23>0 and m31>0 and m32>0 and m33>0:
          ans += 1
          
# out      
print(ans)