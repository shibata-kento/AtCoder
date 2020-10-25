k = int(input())
s = input()
if k < len(s):
    print(f'{s[:k]}...')
else:
    print(s)