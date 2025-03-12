import re

def f(vname):
    expres=r'\b[^\d\W]\w{1,4}\b'
    if re.match(expres,vname):
        return True
    else:
        return False
    
print(f("abc"))
print(f("Abc"))
print(f("aBC"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8abc"))
print(f("_aB8_"))
print(f("_4x"))