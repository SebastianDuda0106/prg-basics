import math
cm=int(input('Your height in cm: '))
feet=math.floor(cm / 30.48)
inches=round((cm/2.54)%12,2)
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')