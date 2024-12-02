def f(dict):
    sum=0
    counter=0
    avg=0
    subj=''
    for key,value in dict.items():
        for grade in value:
            counter+=1
            sum+=grade
        if avg<(sum/counter):
            avg=sum/counter
            subj=key
    return subj
        

if __name__=='__main__':
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
    print(f({"math":[5,4],"geo":[3,4,4],"comp":[5,4,4,4]}))