firstnum=0
secondnum=1
nextnumber=firstnum
for i in range(0,20):
    if i==1:
        print(1,end=' ')
    else:
        print(nextnumber, end=" ")
        nextnumber=firstnum+secondnum
        firstnum=secondnum
        secondnum=nextnumber
print()


