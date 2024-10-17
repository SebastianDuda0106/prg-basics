car_speed=int(input("Enter car speed: "))
speed_limit_min=40
speed_limit_max=140
if car_speed>speed_limit_max:
    print("Speed limit exceeded!")
elif speed_limit_min<car_speed<speed_limit_max:
    print("Your speed is within limits")
else:
    print("invalid car speed!")