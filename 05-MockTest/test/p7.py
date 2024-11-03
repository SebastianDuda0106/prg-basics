def f(n):
    #0 1 1 2 3 5
    a=1
    b=1
    c=1
    if n<=1:
        return 0
    elif n==2:
        return 1
    else:
        for i in range(2,n-1):
            a=c+b
            c=b
            b=a
    return a
    
if __name__ =="__main__":
    for i in range(1,10):
        print(f"{i}. {f(i)}")
    print(f(5))
    print(f(9))