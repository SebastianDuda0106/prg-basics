temperature = int(input('Enter temperature: '))
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It is hot, for a temperature above 30 degrees")
elif temperature > 15:
    print("It is warm, for a temperature of at least 15 degrees")
elif temperature >= 0:
    print("It is cold, for a temperature of at least 0 degrees")
elif temperature < 0:
    print("Warning, frost, for a temperature below 0 degrees")