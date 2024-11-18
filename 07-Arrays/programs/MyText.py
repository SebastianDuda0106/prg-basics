def numofwords(text):
    count=0
    for i in text:
        if i ==" ":
            count+=1
    return count

def wordslongtoshort(text):
    word=["" for x in range(0,numofwords(text)+1)]
    words=[0 for x in range(0,numofwords(text)+1)]
    count=0
    for i in text:
        word[count]+=i
        words[count]+=1
        if i ==" ":
            count+=1
    word2="word"

    for j in range(0,len(word)-2):
        for t in range(0,len(word)-1):  
            if len(word[t])<len(word[t+1]):
                word2=word[t]
                word[t]=word[t+1]
                word[t+1]=word2
    return word

def textalphab(text):
    word=["" for x in range(0,numofwords(text)+1)]
    count=0
    for i in text:
        word[count]+=i
        if i ==" ":
            count+=1
    word.sort()
    return word