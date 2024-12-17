stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

value = round(sum(list(map(lambda position:position[0]*position[1],stock))),2)
print(value)