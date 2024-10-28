def f(code):
    sum=0
    #print(code[-1])
    for i in range(0,len(code)-1):
        sum+=int(code[i])
    #print(sum)
    #print(sum%7)
    if sum%7==int(code[-1]):
        return True
    return False

print(f("1082"))
print(f("2035"))
print(f("1114") )
print(f("7071") )