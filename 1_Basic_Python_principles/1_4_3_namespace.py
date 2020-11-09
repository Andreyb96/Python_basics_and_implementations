n = int(input())
slovar = {'global' : {'parent' : None, 'vars' : []}}
output = []
def create(ns,var):
    slovar[ns] = {'parent' : var, 'vars' : []}

def add(ns,var):
    slovar[ns]['vars'].append(var)

def gett(ns,var):
    if var not in slovar[ns]['vars'] and slovar[ns]['parent'] == None:
        output.append('None')
    elif var in slovar[ns]['vars']:
        output.append(ns)
    else:
        ns = slovar[ns]['parent']
        return(gett(ns,var))
    
for i in range(n):
    cmd, ns, var = input().split()
    if cmd == 'create':
        create(ns,var)
    elif cmd == 'add':
        add(ns,var)
    elif cmd == 'get':
        gett(ns,var)
for i in output:
    print(i)