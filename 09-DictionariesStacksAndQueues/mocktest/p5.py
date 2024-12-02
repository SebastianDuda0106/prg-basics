import re
def f(firstletter,lastletter):
    let1=f'{firstletter}'
    let2=f'{lastletter}'
    words=[]
    patern=f'\b[{let1.upper()}|{let1.lower()}]+\w[{let2.upper()}|{let2.lower()}]\b'
    patern=f'^[{let1.upper()}|{let1.lower()}]+\w+[{let2.upper()}|{let2.lower()}]'
    
    patern=r'\b['
    patern+=let1.upper()
    patern+=r'|'
    patern+=let1.lower()
    patern+=r']+\w+['
    patern+=let2.upper()
    patern+=r'|'
    patern+=let2.lower()
    patern+=r']\b'

    #(\b uppercase|lowercase \w+ uppercase|lowercase \b)
    with open('09-DictionariesStacksAndQueues/mocktest/data.txt','r',encoding="utf8") as file:
        content=file.read()

    for line in content.split():
        words+=re.findall(patern,line)
    return len(words)


if __name__=='__main__':
    print(f('c','r'))
    print(f('w','d'))