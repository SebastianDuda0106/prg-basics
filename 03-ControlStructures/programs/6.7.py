age=int(input('Enter your age: '))
if age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teen")
elif age>=20 and age<=64:
    print("Adult")
elif age>65:
    print("Senior")