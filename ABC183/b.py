x1, y1, x2, y2 = map(int, input().split())
sumy = y1+y2
sumx = x1*y2 + x2*y1
print(sumx/sumy)