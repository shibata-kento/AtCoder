k, s = map(int, input().split())
 
result = 0
for i in range(k+1):
    x = min(s-i, k) - max(0, s-k-i)
    if x >= 0:
        result += x + 1

print(result)