n = int(input())
a = list(map(int, input().split()))
flg = True
cnt = 0
while flg == True:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
        else:
            flg = False
            print(cnt)
            exit()

    cnt += 1

print(cnt)

