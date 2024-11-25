import csv
genre=[]
counter=5
countc=1
with open('08-FileHandling/books.csv',"r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #for i in range(0,len(spamreader)):
    #    if spamreader[i,2] not in genre:
    #        genre+=[spamreader[i,2]]
    #        with open(f"08-FileHandling/programs/books_{spamreader[i,2]}.txt","w") as file:
    #            file.write(f"{spamreader[i,0:2]+spamreader[i,2:]}\n")
    #    else:
    #        with open(f"08-FileHandling/programs/books_{spamreader[i,2]}.txt","a") as file:
    #            file.write(f"{spamreader[i,0:2]+spamreader[i,2:]}\n")
        

    for row in spamreader:
        for column in row:
            if counter==2 and column not in genre:
                genre+=[column]
                with open(f"08-FileHandling/programs/books_{column}.txt","w") as file:
                    file.write(f"{row}\n")
            elif counter==2:
                with open(f"08-FileHandling/programs/books_{column}.txt","a") as file:
                    file.write(f"{row}\n")
            counter+=1
        counter=0
print(genre)
            