n = int(input())
a = list(map(int, input().split()))
ans, bst = 0, 0
for i in range(2, max(a)+1):
    tmp = 0
    for j in range(len(a)):
        if a[j] % i == 0:
            tmp += 1
    if tmp > bst:
        ans = i
        bst = tmp
print(ans)