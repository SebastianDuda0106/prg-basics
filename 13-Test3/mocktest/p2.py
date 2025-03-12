def f(x,y,digit):
    count=0
    for a in range(x,y+1):
        for num in (f'{a}'):
            if num==(f'{digit}'):
                count+=1
    return count

print(f(10,15,1))
print(f(28,32,2))
print(f(100,105,6))
print(f(100,101,0))