def depth(child, slovar):
    global mas
    mas += slovar[child]
    for element_of_child in slovar[child]:
        depth(element_of_child,slovar)
    return(mas)


n = int(input())
slovar = {}
s=[]
for i in range(n):
    s.append(input().split())
    if s[i][0] not in slovar:
        slovar[s[i][0]] = []
        for j in range(2,len(s[i])):
            slovar[s[i][0]].append(s[i][j])
    else:
        for j in range(2,len(s[i])):
            slovar[s[i][0]].append(s[i][j])

m = int(input())
a =[]
b =[]
for i in range(m):
    f = input()
    a.append(f)
    mas = []
    depth(a[i],slovar)
    for j in range(len(a)-1):
        if a[j] in mas:
            b.append(a[i])
            break
for i in range(len(b)):
    print(b[i])