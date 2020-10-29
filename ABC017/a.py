total = []
for i in range(3):
    s, e = map(int, input().split())
    total.append(s*e // 10)

print(sum(total))