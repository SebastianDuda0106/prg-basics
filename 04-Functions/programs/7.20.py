def f(n):
    num=0
    i=0
    count=2
    truth=True
    while i<n:
        for j in range(2,count):
            if count%j==0:
                truth=False
                break
        if truth==True:
            num=count
            i+=1
        else:
            truth=True
        count+=1
    return num

print(f(1))
print(f(5))
    