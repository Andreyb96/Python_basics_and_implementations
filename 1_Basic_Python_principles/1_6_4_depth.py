def depth(parent, child, slovar):
    global mas
    mas += slovar[child]
    for element_of_child in slovar[child]:
        depth(parent, element_of_child,slovar)
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

q = int(input())            
for i in range(q):
    parent, child = input().split()
    mas = []
    depth(parent,child,slovar)
    if (parent in mas) | (parent == child):
        print('Yes')
    else:
        print('No')
    q += 1