n, k = map(int, input().split()) 
def elements(n,k): 
    if k>n: 
        return(0) 
    elif k == 0: 
        return(1) 
    else: 
        return(elements(n-1,k) + elements(n-1,k-1))
print(elements(n,k))