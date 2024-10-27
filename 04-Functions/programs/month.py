def months(n):
    monthnames=["January","February","March","April","May","June","July","August","September","October","November","December"]
    if n>0 and n<13:
        print(f"The name of month {n} is {monthnames[n-1]}")
    else:
        print("invalid month number")

def main():
    for i in range(1,13):
        months(i)

if __name__ == "__main__":
    main()