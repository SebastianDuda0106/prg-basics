import csv
with open('08-FileHandling/programs/powers.csv',"w",newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(1,101):
        spamwriter.writerow([i]+[i**2]+[i**3])