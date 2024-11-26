arr=[
    {
        'name':'Poland',
        'population':'38000000'
        },
    {
        'name':'United States',
        'population':'345426571'
        },
    {
        'name':'Indonesia',
        'population':'283487931'
        },
    {
        'name':'Nigeria',
        'population':'232679478'
        },
    {
        'name':'Brazil',
        'population':'211998573'
        },
]
print("COUNTRY  POPULATION")
for dict in arr:
    for key,value in dict.items():
        print(f'{value}',end="  ")
    print()

