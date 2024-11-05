def f(product_code):
    sum=0
    fcode=f"{product_code}"
    for i in fcode:
        sum+=int(i)
    sum-=int(fcode[-1])
    sum=sum%7
    if sum==int(fcode[-1]):
        return True
    else:
        return False

if __name__=="__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))
    