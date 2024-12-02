import json
def f(years,course,average_grade):
    avg=0
    sum=0
    counter=0
    counter2=0
    with open('09-DictionariesStacksAndQueues/mocktest/data.json','r') as file:
        data=json.load(file)
    for person in data:
        if person['age']>=years:
            for studies in person['studies']['courses']:
                if studies['name']==course:
                    for grades in studies['grades']:
                        sum+=grades
                        counter+=1
                    avg=sum/counter
                    sum=0
                    counter=0
                    if avg>=average_grade:
                        counter2+=1
    #print(data[0]['studies']['courses'])
    
    return counter2


if __name__=='__main__':
    print(f(21,'statistics',4))