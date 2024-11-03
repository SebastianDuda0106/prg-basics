def f(sentence):
    count=0
    chars=["a","e","i","o","u","y"]
    for i in range(0,len(sentence)):
        if sentence[i] in chars:
            count+=1
    return count

if __name__ =="__main__":
    print(f("water"))
    print(f("hello world"))
    print(f("cokolwiek tylko nie to"))