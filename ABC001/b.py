m = int(input())
m = m / 1000
if m <= 5:
    m = int(m*10)
    if len(str(m)) < 2:
        print(f'0{m}')
    else:
        print(m)
elif 6 <= m <= 30:
    print(int(m) + 50)
elif 35 <= m <= 70:
    print((int(m)-30)//5 + 80)
elif 70 <= m:
    print(89)
