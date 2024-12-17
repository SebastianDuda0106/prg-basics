array1=[(lambda x: x)(x) for x in range(1,21)]
POWER3=list(filter((lambda x:x%3==0 and x%2==0),array1))
print(POWER3)