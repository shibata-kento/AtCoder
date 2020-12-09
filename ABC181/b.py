n = int(input())
c = 0
for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    c += (b * (b + 1) // 2) - (a * (a + 1) // 2)
print(c) 