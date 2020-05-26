n, l = map(int, input().split())
s = [input() for i in range(n)]
result = ''
s.sort()

for j in s:
    result = result + j

print(result)