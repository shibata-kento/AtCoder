a = int(input())
b = int(input())
c = int(input())
rank = [a, b, c]
rank = sorted(rank, reverse=True)
print(rank.index(a)+1)
print(rank.index(b)+1)
print(rank.index(c)+1)