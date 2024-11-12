def bubbleSort(arr):
   arrtemp=0
   n = len(arr)
   for i in range(0,n):
      for j in range(0,n-i-1):
         if arr[j] > arr[j+1]:
               arrtemp=arr[j+1]
               arr[j+1]=arr[j]
               arr[j]=arrtemp
   return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]

print(car_fuel_consumption)
sorted_car_fuel_consumption = bubbleSort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubbleSort(bank_transactions) 
print(sorted_bank_transactions)