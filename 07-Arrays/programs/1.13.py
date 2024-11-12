# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]
sum=0
for i in range(0,len(product_prices)):
    sum=round(sum+product_prices[i]*product_quantities[i],2)
    #print(round(product_prices[i]*product_quantities[i],2))
print("The value of all the goods available in the store is: ",round(sum,2))