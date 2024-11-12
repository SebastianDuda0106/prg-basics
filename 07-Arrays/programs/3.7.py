arr=['Genowefa', 'Onufry', "Celestyna", "Alojzy", "Pankracy"]
text=""
for i in arr:
    if len(text)<len(i):
        text=i
print("the longest name is:",text)