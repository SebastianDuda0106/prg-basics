def f(card_number):
    mask=""
    stringcard=f"{card_number}"
    for i in range(0,len(f"{card_number}")):
        if i>=0 and i<2:
            mask+=stringcard[i]
        elif i>=len(stringcard)-4 and i<len(stringcard):
            mask+=stringcard[i]
        else:
            mask+="*"
    return mask
            

if __name__ =="__main__":
    print(f("5290312400019022"))
    print(f("213513161236511126"))