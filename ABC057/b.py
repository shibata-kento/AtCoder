#??

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    d = (10**8)*4
    result = 0
    for j in range(m):
        if abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1]) < d:
            d = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
            result = j+1
    print(result)
