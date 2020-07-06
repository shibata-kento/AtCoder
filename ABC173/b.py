n = int(input())
result = [0]*4
for i in range(n):
    r = input()
    if r == 'AC':
        result[0] += 1
    elif r == 'WA':
        result[1] += 1
    elif r == 'TLE':
        result[2] += 1
    elif r == 'RE':
        result[3] += 1

print(f'AC x {result[0]}')
print(f'WA x {result[1]}')
print(f'TLE x {result[2]}')
print(f'RE x {result[3]}')
