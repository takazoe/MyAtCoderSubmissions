#input
n = int(input())

#calc
t_o, x_o, y_o = 0, 0, 0
for i in range(n):
  t, x, y = map(int, input().split())
  diff_x = abs(x - x_o)
  diff_y = abs(y - y_o)
  diff_t = t - t_o
  t_o, x_o, y_o = t, x, y
  if diff_x + diff_y > diff_t or (diff_t - diff_x + diff_y) % 2 == 1:
    print("No")
    exit()
    
#out
print("Yes")