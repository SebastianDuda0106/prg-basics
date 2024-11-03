def f(number,even):
    numberf=f"{number}"
    sum=0
    if even==True:
        for i in range(0,len(f"{number}")):
            if int(numberf[i])%2==0:
                sum+=int(numberf[i])
    elif even==False:
        for i in range(0,len(f"{number}")):
            if int(numberf[i])%2==1:
                sum+=int(numberf[i])
    return sum

if __name__ =="__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))
    print(f(13165,True))