def f(word):
    count=0
    count1=0
    string=''
    for i in range(len(word)):
        for char in word:
            if count==count1:
                string+=char.capitalize()
            else:
                string+=char
            count1+=1
        count+=1
        count1=0
        if count!=len(word):
            string+='-'
    return string

print(f('book'))
print(f('water'))
print(f('ok'))
print(f('a'))
print(f(''))