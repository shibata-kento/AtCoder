n, a, b = map(int, input().split())
c = 0
kake = n // (a+b)
blue = kake * a
br = kake * (a+b)
num = n - br
if num < a:
    blue = blue + num
else:
    blue = blue + a
print(blue)