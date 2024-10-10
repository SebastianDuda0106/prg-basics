import random
computer=random.randint(1,6)
you=int(input('Guess the number the dice rolled!\n'))
print(f'You won: {computer==you}')
if computer!=you:
    print(f'Computer rolled: {computer}')