array1=[(lambda x: x)(x) for x in range(1,21)]
POWER3=list(map(lambda x:x**3,array1))
print(POWER3)