###
# Reads a non-existent file
#

# there is no file with this name on the disk
file_name = '08-FileHandling/it_company.csv'

with open(file_name,'r') as file:
    counter=0
    for line in file:
        print(line)
        counter+=1
        if counter%5==0:
            input("Press Enter key...")
