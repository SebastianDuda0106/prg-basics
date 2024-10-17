time=input("Enter time (24-hour format): ")
if len(time)<3:
    time="25:69"
if len(time)==3:
    time=f"{time[0]}:0{time[2]}"
if time[2]==":":
    if int(time[3:])>59:
        time="25:69"
if time[1]==":":
    print(f"Time in 12-hour format: {time}am")
elif time[2]==":"and int(time[0:2])<12:
    print(f"Time in 12-hour format: {time}am")
elif time[2]==":"and int(time[0:2])==12:
    print(f'Time in 12-hour format: {time}pm')
elif time[2]==":"and 24>int(time[0:2])>12:
    print(f'Time in 12-hour format: {int(time[0:2])-12}{time[2:]}pm')
else:
    print("invalid")