number = int(input('Enter number: '))
if number==0:
    result="Number is 0"
elif number>0:
    result=f"Number {number} is positive"
elif number<0:
    result=f"Number {number} is negative"
print(result)