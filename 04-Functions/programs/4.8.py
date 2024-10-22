def time_string(hours, minutes, time_format):
    if minutes>=0 and minutes<10:
        minutes=f"0{minutes}"
    if time_format==24:
        if hours>=0 and hours<=24:
            if hours>=0 and hours<10:
                hours=f"0{hours}"
            result=f"{hours}:{minutes}"
        else:
            result="Wrong hour"
    elif time_format==12:
        if hours>12 and hours<24:
            result=f"{hours-12}:{minutes}pm"
        elif hours==12:
            result=f"{hours}:{minutes}pm"
        elif hours>0 and hours<12:
            result=f"{hours}:{minutes}am"
        elif hours==0:
            result=f"{hours+12}:{minutes}am"
        else:
            result="Wrong hour"
    else:
        result="wrong time format"
    return result
h=0
while h != 25:
    h=int(input('Enter hour: '))
    if h==25:
        break
    m=int(input('Enter minute/s: '))
    tf=int(input('Enter time format(12/24): '))
    print(time_string(h,m,tf))