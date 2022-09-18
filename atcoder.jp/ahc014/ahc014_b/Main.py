import math

def II(): return int(input())
def MII(): return map(int, input().split())
def LMII(): return list(map(int, input().split()))
def LMIIS(n): return [LMII() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()

# in
n,m = MII()
Pts = []
for _ in range(m):
  x,y = MII()
  Pts.append((x,y))
L = set()

def sign(x):
  # 数値の符号に応じて1, -1, 0を返す
  return (x > 0) - (x < 0)
        
def get_Pt2(Pt1,Pts):
  # Pt1の座標からPt2のリストを返す
  x1,y1 = Pt1
  #D = [(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1)]
  D = [(1,-1),(1,0),(1,1),(0,1)]
  Pt2s = []
  for dx,dy in D:
    for i in range(1,n):
      x2 = x1+dx*i
      y2 = y1+dy*i
      if (x2,y2) in Pts:
        Pt2s.append((x2,y2))
        break
  return Pt2s
      
def get_Pt3(Pt1,Pt2,Pts):
  # Pt1,Pt2の座標からPt3を返す
  x1,y1 = Pt1
  x2,y2 = Pt2
  dx,dy = sign(x2-x1),sign(y2-y1)
  for i in range(1,n):
    x3 = x2-dy*i
    y3 = y2+dx*i
    if (x3,y3) in Pts:
      return (x3,y3)
      
def get_Pt4(Pt1,Pt2,Pt3):
  # Pt1,Pt2,Pt3からPt4の座標を計算
  x1,y1 = Pt1
  x2,y2 = Pt2
  x3,y3 = Pt3
  x4 = x1+x3-x2
  y4 = y1+y3-y2
  if not(0<=x1<n and 0<=y4<n): return # Pt4が枠外にある場合
  dx,dy = sign(x3-x2),sign(y3-y2)
  for i in range(1,n):
    a1 = x3-dy*i
    b1 = y3+dx*i
    if (a1,b1) in Pts: return
    if (a1,b1) == (x4,y4): break
  for i in range(1,n):
    a2 = x1+dx*i
    b2 = y1+dy*i
    if (a2,b2) in Pts: return
    if (a2,b2) == (x4,y4): break
  return (x4,y4)

def get_len(Pt1,Pt2):
  # Pt1,Pt2間の距離を計算
  x1,y1 = Pt1
  x2,y2 = Pt2
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def is_overlaped(Crv1,Crv2):
  # 2つの線分が重なっているかチェック
  Pt1,Pt2 = Crv1
  Pt3,Pt4 = Crv2
  d13 = get_len(Pt1,Pt3)
  d23 = get_len(Pt2,Pt3)
  d14 = get_len(Pt1,Pt4)
  d24 = get_len(Pt2,Pt4)
  d = get_len(Pt1,Pt2)
  if round(d13+d23,4) == round(d,4) and (round(d14+d24,4) == round(d,4) or round(d14,4) == round(d24+d,4) or round(d14 == d24-d,4)): return True
  elif round(d13,4) == round(d23-d,4) and (round(d14+d24,4) == round(d,4) or round(d14,4) == round(d24+d,4)): return True
  elif round(d13,4) == round(d23+d,4) and (round(d14+d24,4) == round(d,4) or round(d14,4) == round(d24-d,4)): return True
  return False

k = 0
ANS = set()
CRV = []

for Pt1 in Pts:
  Pt2s = get_Pt2(Pt1,Pts)
  for Pt2 in Pt2s:
    x1,y1 = Pt1
    x2,y2 = Pt2
    # 3点目を取得
    Pt3 = get_Pt3(Pt1,Pt2,Pts)
    if not Pt3: continue # 範囲内にPt3がない場合
    # 4点目を取得
    Pt4 = get_Pt4(Pt1,Pt2,Pt3)
    if not Pt4: continue # 範囲内にPt4がない場合
    # 解答を出力
    ans = (Pt4[0],Pt4[1],Pt1[0],Pt1[1],Pt2[0],Pt2[1],Pt3[0],Pt3[1])
    # 重なりをチェック
    for crv in CRV:
      for c in [(Pt1,Pt2),(Pt2,Pt3),(Pt3,Pt4),(Pt4,Pt1)]:
        if is_overlaped(crv,c): break
      else: continue
      break
    else:
      Pts.append(Pt4)
      CRV.append((Pt1,Pt2))
      CRV.append((Pt2,Pt3))
      CRV.append((Pt3,Pt4))
      CRV.append((Pt4,Pt1))
      ANS.add(ans)
      k += 1

print(k)
for ans in ANS: print(*ans)