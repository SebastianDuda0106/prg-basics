number_of_prod=int(input("Number of products purchased: "))
product_price=int(input("Product price: "))
total=0
if number_of_prod>2:
    total=((product_price*2)+((number_of_prod-2)*3/4*product_price))
elif number_of_prod<=0:
    total=0
else:
    total=product_price*number_of_prod
print(f'Amount to pay: {total}')