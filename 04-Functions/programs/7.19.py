def f(number):
    numbers=[]
    count=[0,0,0,0,0,0,0,0,0,0]
    counter=0
    fnumbers=f"{number}"
    for i in range(0,len(fnumbers)):
        if fnumbers[i] in numbers:
            if count[int(fnumbers[i])]==0:
                count[int(fnumbers[i])]+=1
                counter+=int(fnumbers[i])*2
            elif count[int(fnumbers[i])]>0:
                count[int(fnumbers[i])]+=1
                counter+=int(fnumbers[i])
        else:
            numbers.append(fnumbers[i])
    return counter

print(f(1027))
print(f(230335))
print(f(513553007))