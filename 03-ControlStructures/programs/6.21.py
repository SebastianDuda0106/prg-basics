zloty=int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {zloty} in coins: ")
coin5=0
coin2=0
coin1=0
while zloty>=5:
    coin5+=1
    zloty-=5
while zloty>=2:
    coin2+=1
    zloty-=2
coin1=zloty
print(f'5 PLN coins: {coin5}')
print(f'2 PLN coins: {coin2}')
print(f'1 PLN coins: {coin1}')