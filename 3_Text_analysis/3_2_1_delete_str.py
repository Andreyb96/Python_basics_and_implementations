s = input()
a = input()
b = input()
c = ''
k = 0
while True:
    if a in s and a in b:
        print('Impossible')
        break
    c = s.replace(a, b)
    if c != s:
        k += 1
        s = c
    else:
        print(k)
        break