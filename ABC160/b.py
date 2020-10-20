x = int(input())
yen500 = (x // 500) * 1000
yen5 = x % 500 // 5 * 5
print(yen500 + yen5)
