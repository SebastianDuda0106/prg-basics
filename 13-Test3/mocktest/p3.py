def f(uid):
    try:
        if (len(set(uid))==len(uid)):
            return True
        else:
            return False
    except:
        return False
print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
print(f(["abc123","ann","abc123","a10"]))
print(f(["bob2",'bob2']))
print(f(["bob2",'BOB2']))

    