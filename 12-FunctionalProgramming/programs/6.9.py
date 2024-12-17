temps={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
positive=list(map(lambda x:x[0], list(filter(lambda temp:temp[1]>0,temps.items()))))
print(positive)