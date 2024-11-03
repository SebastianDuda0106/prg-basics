def f(amount_to_pay):
    count=0
    while amount_to_pay>0:
        if amount_to_pay>=5:
            count+=1
            amount_to_pay-=5
        elif amount_to_pay>=2:
            count+=1
            amount_to_pay-=2
        elif amount_to_pay==1:
            count+=1
            amount_to_pay-=1
    return count

if __name__ =="__main__":
    print(f(23))
    print(f(8))
    print(f(int(input())))