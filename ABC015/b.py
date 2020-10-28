import math
n = int(input())
a = list(map(int, input().split()))
A = [i for i in a if i > 0]
print(math.ceil(sum(A) / len(A)))