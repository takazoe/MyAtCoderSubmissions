#入力
n = int(input())
lst_a = list(map(int, input().split()))

#カウント
i = -1
c = True
while c:
  i += 1
  for j in range(n):
    a = lst_a[j]
    #2で割れた場合
    if a%2 == 0:
      lst_a[j] = a/2
    #2で割れない場合
    else:
      c = False
      break
  
#出力
print(i)