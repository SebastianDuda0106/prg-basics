def occurs(number,array):
    if number in array:
        return True
    return False

if __name__=="__main__":
    num=int(input('Number:'))
    print("Array: 15 38 7 23 14")
    arr=[15,38,7,23,14]
    print("Result: ",end="")
    if occurs(num,arr)==True:
        print(f"number {num} appears in the array")
    else:
        print(f"number {num} does not appears in the array")
        