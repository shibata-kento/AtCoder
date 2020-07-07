n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
alice = []
bob = []
for i in range(n):
    if i % 2 == 0:
        alice.append(a[i])
    else:
        bob.append(a[i])

print(sum(alice) - sum(bob))