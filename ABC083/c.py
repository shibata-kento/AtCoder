x, y = map(int, input().split())
cnt = 1
while True:
    if 2*x <= y:
        x *= 2
        cnt += 1
    else:
        break
print(cnt)