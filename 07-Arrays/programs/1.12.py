categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
bigexp = 0
expnum = 0
for i in range(0,len(expenses)):
    if bigexp<expenses[i]:
        bigexp=expenses[i]
        expnum=i
print("The most expensive expense category was:",categories[expnum],"and it cost:",expenses[expnum])
