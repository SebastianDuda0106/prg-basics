def f(n1,n2,n3):
    result=0
    if n1>n2 and n1>n3:
        if n2>n3:
            result = n1-n3
        else:
            result = n1-n2
    elif n2>n1 and n2>n3:
        if n1>n3:
            result = n2-n3
        else:
            result = n2-n1
    elif n3>n1 and n3>n2:
        if n1>n2:
            result = n3-n2
        else:
            result = n3-n1
    return result

print(f(7,4,9))
print(f(2,12,8))
