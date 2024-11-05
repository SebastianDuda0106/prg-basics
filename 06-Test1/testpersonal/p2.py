def f(x,y):
    cw=0
    if x>0 and y>0:
        cw=1
    elif x<0 and y>0:
        cw=2
    elif x<0 and y <0:
        cw=3
    elif x>0 and y<0:
        cw=4
    return cw

if __name__=="__main__":
    print(f(5,2))
    print(f(-5,2))
    print(f(-5,-2))
    print(f(5,-2))