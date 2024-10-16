light_switch1 = False # False - switch off, True - switch on
light_switch2 = True
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on+=2
print(f'bulbs on: {bulbs_on}')