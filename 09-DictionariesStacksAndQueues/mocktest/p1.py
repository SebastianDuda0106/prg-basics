def f(player1,player2):
    value1=value2=0
    numbers=['1','2','3','4','5','6','7','8','9']
    for char in f'{player1}':
        if char == 'A' or char =='K' or char =='Q' or char =='J' or char =='T':
            value1+=10
        elif char in numbers:
            if int(char)<10 and int(char)>0:
                value1+=int(char)
    for char in f'{player2}':
        if char == 'A' or char =='K' or char =='Q' or char =='J' or char =='T':
            value2+=10
        elif char in numbers:
            if int(char)<10 and int(char)>0:
                value2+=int(char)
    if value1>=value2:
        return True
    else:
        return False
        
if __name__=="__main__":
    print('yes')
    print(f('AJ972','AQT72'))
    print(f('9532','K8'))