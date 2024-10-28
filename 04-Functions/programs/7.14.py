def f(n1,n2,op1):
    result=0
    if(op1=="+"):
        result=n1+n2
    elif(op1=="-"):
        result=n1-n2
    elif(op1=="%"):
        result=n1%n2
    elif(op1=="*"):
        result=n1*n2
    elif(op1=="**"):
        result=n1**n2
    return result

print(f(2,3,"+"))
print(f(2,3,"%"))
print(f(2,3,"**"))
print(f(2,3,"*"))
print(f(2,3,"-"))