k = int(input())
a, b = map(int, input().split())
for i in range(0, b+1, k):
    if a <= i <= b:
        print('OK')
        exit()
print('NG')