age=int(input('Enter dog\'s age in human years: '))
dog_age=0
for i in range(age):
    if (i+1)<=2:
        dog_age+=10.5
    else:
        dog_age+=4
dog_age=int(dog_age)
print(f"The dog's age in dog's years is {dog_age} years")