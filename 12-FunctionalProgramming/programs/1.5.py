dis=int(input('Enter distance in km: '))
hours=int(input('Enter number of travel hours: '))
minutes=int(input('Enter travel minutes: '))

def avg_speed(distance,hours,minutes):
    return round(distance/(hours+minutes/60),2)

print(f'Average speed: {avg_speed(dis,hours,minutes)} km/h')