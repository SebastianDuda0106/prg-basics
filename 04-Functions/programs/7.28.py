def f(dice):
    eyes=[0,0,0,0,0,0]
    eye=0
    for i in range(0,len(dice)):
        #print(dice[i])
        eye=int(dice[i])-1
        eyes[eye]+=1
    if eyes[1]>eyes[2] and eyes[1]>eyes[3] and eyes[1]>eyes[4] and eyes[1]>eyes[5] and eyes[1]>eyes[0]:
        return 2
    elif eyes[2]>eyes[1] and eyes[2]>eyes[3] and eyes[2]>eyes[4] and eyes[2]>eyes[5] and eyes[2]>eyes[0]:
        return 3
    elif eyes[3]>eyes[1] and eyes[3]>eyes[2] and eyes[3]>eyes[4] and eyes[3]>eyes[5] and eyes[3]>eyes[0]:
        return 4
    elif eyes[4]>eyes[1] and eyes[4]>eyes[2] and eyes[4]>eyes[3] and eyes[4]>eyes[5] and eyes[4]>eyes[0]:
        return 5
    elif eyes[5]>eyes[1] and eyes[5]>eyes[2] and eyes[5]>eyes[3] and eyes[5]>eyes[4] and eyes[5]>eyes[0]:
        return 6
    elif eyes[0]>eyes[1] and eyes[0]>eyes[2] and eyes[0]>eyes[3] and eyes[0]>eyes[4] and eyes[0]>eyes[5]:
        return 1
    return 0
print(f("5233165554211"))
print(f("2133"))
print(f)
