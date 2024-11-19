try:
    filename=input("Enter file name: ")
    nrl=0
    nrc=0
    nrw=0
    with open(filename,'r') as file:
        content=file.read()
    for line in content.splitlines():
        for word in line.split():
            nrw+=1
        for word in line:
            nrc+=1
        nrl+=1
    print("Number of lines",nrl)
    print("Number of characters",nrc)
    print("Number of words",nrw)
except FileExistsError:
    print("File not existo")
except:
    print("EXCEPTION!")
finally:
    print("Goodbye")

