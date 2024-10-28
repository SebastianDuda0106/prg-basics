def f(expression):
    charbefore=""
    charnow=""
    sum=int(expression[0])
    for i in range(1,len(expression)):
        charbefore=expression[i-1]
        if charbefore=="+":
            sum+=int(expression[i])
        elif charbefore == "-":
            sum-=int(expression[i])
    return sum

print(f("2+3"))
print(f("3+8+1") )
print(f("2+3-4+5-0"))