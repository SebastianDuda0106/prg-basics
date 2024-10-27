def sumevod(num,even):
    sum=0
    if f"{num}".isdigit():
        num=f"{num}"
        if even==True: 
            print(num)
            for i in range(0,len(num)):
                if int(num[i])%2==0:
                    sum+=int(num[i])
        elif even==False:
            for i in range(0,len(num)):
                if int(num[i])%2==1:
                    sum+=int(num[i])
    return sum

number=int(input("Enter number: "))
odd=input("Add (even) or (odd)?: ")
if odd=="even":
    odd=True
elif odd=="odd":
    odd=False
    
print(sumevod(number,odd))