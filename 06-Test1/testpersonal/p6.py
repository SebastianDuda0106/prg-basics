def f(student1,student2):
    sum1=0
    count=0
    sum2=0
    for i in student1:
        if i == "2":
            count+=1
            sum1+=2
        elif i =="3":
            sum1+=3
            count+=1
        elif i =="4":
            sum1+=4
            count+=1
        elif i =="5":
            sum1+=5
            count+=1
        else:
            continue
    sum1=sum1/count
    count=0
    for i in student2:
        if i == "2":
            count+=1
            sum2+=2
        elif i =="3":
            sum2+=3
            count+=1
        elif i =="4":
            sum2+=4
            count+=1
        elif i =="5":
            sum2+=5
            count+=1
        else:
            continue
    sum2=sum2/count
    if sum1>sum2:
        return 1
    elif sum2>sum1:
        return 2
    else:
        return 0

if __name__=="__main__":
    print(f("3,4,5","4,3"))
    print(f("3,4,5","5,5,3,5"))
    print(f("3,4,5,4","4,4"))
    print(f("3,4,5,4,5,2,3","4,4,4,5,3"))