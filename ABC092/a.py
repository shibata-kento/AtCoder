a = int(input())
b = int(input())
c = int(input())
d = int(input())
result = 0
if a <= b:
    result += a
else:
    result += b

if c <= d:
    result += c
else:
    result += d

print(result)