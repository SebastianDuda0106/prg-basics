def negeven(rangestart,rangeend):
    count=0
    for i in range(rangestart,rangeend):
        if i<0 and i%2==0:
            count+=1
    return count

num1=int(input("start: "))
num2=int(input("end: "))

print(negeven(num1,num2))