arr1=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

arr2=list(map(lambda x:f'{x[0]}'.upper()+f', {x[1]}',arr1))

print(arr2)