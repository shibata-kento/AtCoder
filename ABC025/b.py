n, a, b = map(int, input().split())
news = [0, 0]
for i in range(n):
    s, d = input().split()
    if a >= int(d):
        d = a
    if int(d) >= b:
        d = b
    if s == 'East':
        news[0] += int(d)
    elif s == 'West':
        news[1] += int(d)
if news[0] > news[1]:
    print('East', abs(news[0] - news[1]))
elif news[0] < news[1]:
    print('West', abs(news[0] - news[1]))
else:
    print(0)
