n = int(input())
yen = 0
for i in range(1, n+1):
    yen += 10000 * i * 1/n

print(int(yen))