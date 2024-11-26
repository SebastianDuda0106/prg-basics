price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

def dys_dict(dict):
    for key,value in dict.items():
        print(f'{key}:{value}')
def dys_dict_total(dict):
    total=0
    for key,value in dict.items():
        total+=value
    total=round(total,2)
    print(total)
    return total

def dys_discount(dict,discount):
    for key,value in dict.items():
        dict[key]=round(float(value)*(1-(discount/100)),2)
    return dict

dys_dict(price_list)
dys_dict_total(price_list)
dys_discount(price_list,10)
dys_dict(price_list)
dys_dict_total(price_list)
