def amount_to_pay(amount):
    total=0
    while amount>0:
        if amount>=5:
            amount-=5
            total+=1
        elif amount>=2:
            amount-=2
            total+=1
        elif amount>=1:
            amount-=1
            total+=1
    return total

num=int(input("Enter amount: "))
print(amount_to_pay(num))