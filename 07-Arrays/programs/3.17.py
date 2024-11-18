tup1=(50,20,40,50,30,50)
val=50
count=0
for i in tup1:
    if val==i:
        count+=1
print(f"Tuple: {tup1}\nValue: {val}\nNumber of occurrences: {count}")