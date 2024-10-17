x=int(input("x = "))
y=int(input("y = "))
text = "Wrong"
if x==y==0:
    text="in the center of tge coordinate system"
elif x>=0:
    if y>=0:
        text="in the first quadrant of the coordinate system"
    if y<0:
        text="in the forth quadrant of the coordinate system"
elif x<0:
    if y>=0:
        text="in the second quadrant of the coordinate system"
    if y<0:
        text="in the third quadrant of the coordinate system"
print(f'P({x},{y}) is {text}')