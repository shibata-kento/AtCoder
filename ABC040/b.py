n = int(input())
num = int(n**0.5)
lst = [0]*num
for i in range(1, num+1):
    tmp = n // i
    lst[i-1] += n-tmp*i + tmp-i
print(min(lst))