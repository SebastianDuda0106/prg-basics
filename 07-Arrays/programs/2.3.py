# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
sum=[0,0,0,0,0,0,0,0]
week=0
for row in monthly_expenses:
    for i in range(0,len(row)):
        sum[0]+=row[i]
        if i==0:
            sum[1]+=row[i]
        if i==1:
            sum[2]+=row[i]
        if i==2:
            sum[3]+=row[i]
        sum[4+week]+=row[i]
    week+=1
    
        
        
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',sum[1])
print('Transport:',sum[2])
print('Utilities:',sum[3])
print('Week 1:',sum[4])
print('Week 2:',sum[5])
print('Week 3:',sum[6])
print('Week 4:',sum[7])
print('---------------')
print('TOTAL:',sum[0])