import csv

graphic_designers=[]
printr=False
with open('08-FileHandling/it_company.csv',"r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        for column in row:
            if column=="Graphic Designer":
                printr=True
        if printr==True:
            graphic_designers+=[row]
            printr=False
counter=0
print("GRAPHIC DESIGNERS")
print("=================")
for i in range(len(graphic_designers)):
    for j in range(len(graphic_designers[i])):
        if counter==0:
            print(graphic_designers[i][j],end=" ")
        elif graphic_designers[i][j]!="Graphic Designer":
            print(graphic_designers[i][j],end=",")
        counter+=1
    print()
    counter=0