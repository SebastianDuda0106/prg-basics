def f(fnc,prods):
    lista=list(map(fnc,prods))
    strona=''
    count=0
    for item in lista:
        strona+=f'{item}'
        if count!=len(lista)-1:
            count+=1
            strona+=','
    return strona
prods = ["water","cheese","tomato"]  
fnc1 = lambda x: "id:"+x[:2] 
fnc2 = lambda x: (x[0]+x[-1]).upper()
print(f(fnc1,prods))
print(f(fnc2,prods))