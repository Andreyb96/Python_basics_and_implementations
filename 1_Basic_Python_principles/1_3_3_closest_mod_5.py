def closest_mod_5(x):
    if x%5 == 0:
        return(x)
    else:
        return((x//5+1)*5)