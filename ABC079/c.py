num = list(input())
num = [int(i) for i in num]
 
if sum(num) == 7:
    print(f'{num[0]}+{num[1]}+{num[2]}+{num[3]}=7')
elif num[0]+num[1]+num[2]-num[3] == 7:
    print(f'{num[0]}+{num[1]}+{num[2]}-{num[3]}=7')
elif num[0]+num[1]-num[2]+num[3] == 7:
    print(f'{num[0]}+{num[1]}-{num[2]}+{num[3]}=7')
elif num[0]-num[1]+num[2]+num[3] == 7:
    print(f'{num[0]}-{num[1]}+{num[2]}+{num[3]}=7')
elif num[0]+num[1]-num[2]-num[3] == 7:
    print(f'{num[0]}+{num[1]}-{num[2]}-{num[3]}=7')
elif num[0]-num[1]+num[2]-num[3] == 7:
    print(f'{num[0]}-{num[1]}+{num[2]}-{num[3]}=7')
elif num[0]-num[1]-num[2]+num[3] == 7:
    print(f'{num[0]}-{num[1]}-{num[2]}+{num[3]}=7')
else:
    print(f'{num[0]}-{num[1]}-{num[2]}-{num[3]}=7')