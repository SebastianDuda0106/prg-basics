hours_parked=int(input('Enter hours parked: '))
result=0
if hours_parked>=1 and hours_parked<=2:
    result=5
elif hours_parked>3 and hours_parked<=6:
    result=15
elif hours_parked>6:
    result=20
print(f"You will have to pay: {result}")