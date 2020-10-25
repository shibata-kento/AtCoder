import collections
n = int(input())
s = [input() for i in range(n)]
S = collections.Counter(s)
print(S.most_common()[0][0])