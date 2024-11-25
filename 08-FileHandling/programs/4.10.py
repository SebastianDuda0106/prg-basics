import csv

counter=0
printr1=False
printr2=False
with open('08-FileHandling/clothing.csv',"r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        for column in row:
            counter+=1
            if counter==6:
                try:
                    if float(column)<60:
                        printr1=True
                except:
                    continue
            elif counter==7:
                try:
                    if int(column)<40:
                        printr2=True
                except:
                    continue
            if printr1==True and printr2==True:
                print(row)
        printr1=False
        printr2=False
        counter=0
