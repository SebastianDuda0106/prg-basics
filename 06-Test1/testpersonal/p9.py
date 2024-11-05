def f(size1,size2):
    a=0
    b=0
    if size1==size2:
        return 0
    
    if size1=="L":
        a=3
    elif size1=="M":
        a=2
    elif size1=="S":
        a=1
    
    if size2=="L":
        b=3
    elif size2=="M":
        b=2
    elif size2=="S":
        b=1

    if a>b:
        return 1
    elif a<b:
        return 2
    return 4
    

if __name__=="__main__":
    print(f("L","S"))
    print(f("M","L"))
    print(f("S","S"))