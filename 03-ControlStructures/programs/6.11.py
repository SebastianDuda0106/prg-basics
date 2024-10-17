current_price=int(input("Enter current price: "))
previous_price=int(input('Enter previous price: '))
discount=round((1-current_price/previous_price)*100)
if discount>=10:
    print('Buy the product!')
    print(f'Product price reduced by {discount}%!')
elif discount>0:
    print(f'Product price reduced by {discount}%')
elif discount==0:
    print('Product price is the same as before!')
else:
    print(f'Product price increased by {-discount}%!')