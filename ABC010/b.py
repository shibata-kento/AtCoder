petal = [1, 3, 7, 9]
n = int(input())
a = list(map(int, input().split()))
result = []
for i in range(n):
    tmp = 10
    for j in range(4):
        if a[i] >= petal[j]:
            tmp = min(abs(a[i] - petal[j]), tmp)
    result.append(tmp)
print(sum(result))