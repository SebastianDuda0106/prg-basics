number1 = int(input('enter number 1: ')) 
number2 = int(input('enter number 2: ')) 
operator = input('enter operator: ') 

if operator == '+':
    result = number1+number2
elif operator == '-':
    result = number1-number2
elif operator == '*':
    result = number1*number2
elif operator == '/':
    if number2==0:
        result = "cannot divide by 0"
    else:
        result = number1/number2


# print result
print(f'{number1} {operator} {number2} = {result}')