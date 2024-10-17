total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')
if program=="j"or program=="jacket":
    total_washing_time+=40
elif program=="u" or program=="underwear":
    total_washing_time+=70
elif program=="s" or program=="shoes":
    total_washing_time+=20

if extra_rinse=="y":
    total_washing_time+=15
if extra_spin=="y":
    total_washing_time+=9

print(f'Total washing time: {total_washing_time} minutes')