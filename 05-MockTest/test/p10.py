def f(sentence):
    sum=0
    for i in range(0,len(sentence)):
        sum+=ord(sentence[i])
    return sum%2==0

if __name__ =="__main__":
    print(f("hello world"))
    print(f("university"))
    print(f("student"))
    print(f("Sebastian"))
    print(f("Duda"))
    print(f("Sebastian Duda"))