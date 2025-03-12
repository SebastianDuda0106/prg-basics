cars=[["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
cars2=[]
for car in cars:
    if (car[1]=='in'):
        cars2.append(car[0])
    if (car[1]=='out'):
        cars2.remove(car[0])
print(sorted(cars2))