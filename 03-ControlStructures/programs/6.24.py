y=1
h=34

for i in range(1,h):
    if i<(h/2):
        for j in range(0,y):
            print('*',end=' ')
        y+=1
        print()
    if i>=(h/2):
        for j in range(0,y):
            print('*',end=' ')
        y-=1
        print()