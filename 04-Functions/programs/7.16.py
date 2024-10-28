def f(n):
    count=1
    k=1
    l=1
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1: 
        for i in range(2,n-1):
            count+=k
            k=l
            l=count
            #print(count)
    return count
# 0 1 1 2 3
print(f(3))
print(f(5))
print(f(9))

