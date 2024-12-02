import csv
def f(value):
    counter=0
    with open('09-DictionariesStacksAndQueues/mocktest/data.csv','r') as file:
        data=csv.reader(file)
        for lines in data:
            try:
                if int(lines[9])>=value:
                    counter+=1
            except:
                continue
    return counter

if __name__=='__main__':
    print(f(9200))
    print(f(11640))