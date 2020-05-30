n = int(input())
num = 1
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
       num = i

ans = len(str(max(num, n // num)))
print(ans)