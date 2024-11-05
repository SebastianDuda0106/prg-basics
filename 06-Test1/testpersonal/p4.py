def f(n):
    results=""
    for i in range(1,n+1):
        results+=f"{i}"
    return results

if __name__=="__main__":
    print(f(11))
    print(f(4))
    print(f(0))